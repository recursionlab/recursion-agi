---
nexus: nexus-ai-chat-importer
plugin_version: "1.3.0"
provider: claude
artifact_id: aider_monitor
version_uuid: 08aeeede-d301-486c-90cf-39465a81899a
version_number: 1
command: create
conversation_id: fa968e89-4b1f-4488-b7ca-dad8e3bdd1a8
create_time: 2025-08-11T23:09:32.000Z
format: markdown
aliases: [Aider File Change Pattern Monitor, aider_monitor_v1]
---

# Aider File Change Pattern Monitor (Version 1)

**Conversation:** [[Nexus/Conversations/claude/2025/08/Aider-Notion Meta-AI Integration|Aider-Notion Meta-AI Integration]]

## Content

import asyncio
import os
import json
import hashlib
from pathlib import Path
from typing import Dict, List, Set, Optional, Tuple
from dataclasses import dataclass, asdict
from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import git
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

@dataclass
class FileChangeEvent:
    """Represents a single file change with semantic context"""
    filepath: str
    change_type: str  # 'created', 'modified', 'deleted', 'moved'
    timestamp: datetime
    file_hash: Optional[str]
    size_bytes: int
    git_status: Optional[str]
    aider_context: Optional[Dict]
    diff_summary: Optional[str]
    
    def to_dict(self):
        return asdict(self)

@dataclass
class AiderSession:
    """Tracks an active Aider session"""
    session_id: str
    start_time: datetime
    working_directory: str
    git_branch: str
    files_modified: Set[str]
    conversation_log: List[str]
    
class AiderFileMonitor(FileSystemEventHandler):
    """Monitors file changes in Aider working directory"""
    
    def __init__(self, working_dir: str, callback=None):
        self.working_dir = Path(working_dir)
        self.callback = callback
        self.file_states: Dict[str, Dict] = {}
        self.ignored_patterns = {'.git', '__pycache__', '.aider*', '*.pyc', '.DS_Store'}
        self.change_buffer: List[FileChangeEvent] = []
        self.git_repo = None
        
        # Initialize git repo if available
        try:
            self.git_repo = git.Repo(working_dir)
        except git.InvalidGitRepositoryError:
            logger.warning(f"No git repository found in {working_dir}")
    
    def should_ignore(self, filepath: str) -> bool:
        """Check if file should be ignored based on patterns"""
        path_obj = Path(filepath)
        
        for pattern in self.ignored_patterns:
            if pattern.startswith('*'):
                if path_obj.suffix == pattern[1:]:
                    return True
            elif pattern in path_obj.parts:
                return True
        
        return False
    
    def get_file_hash(self, filepath: str) -> Optional[str]:
        """Generate SHA256 hash of file content"""
        try:
            with open(filepath, 'rb') as f:
                return hashlib.sha256(f.read()).hexdigest()
        except (IOError, OSError):
            return None
    
    def get_git_status(self, filepath: str) -> Optional[str]:
        """Get git status for specific file"""
        if not self.git_repo:
            return None
        
        try:
            # Get relative path from repo root
            rel_path = Path(filepath).relative_to(self.git_repo.working_dir)
            
            # Check if file is tracked, modified, staged, etc.
            if str(rel_path) in self.git_repo.untracked_files:
                return 'untracked'
            
            # Check staged changes
            staged_files = [item.a_path for item in self.git_repo.index.diff("HEAD")]
            if str(rel_path) in staged_files:
                return 'staged'
            
            # Check unstaged changes
            unstaged_files = [item.a_path for item in self.git_repo.index.diff(None)]
            if str(rel_path) in unstaged_files:
                return 'modified'
            
            return 'tracked'
            
        except Exception as e:
            logger.debug(f"Git status check failed for {filepath}: {e}")
            return None
    
    def detect_aider_context(self, filepath: str) -> Optional[Dict]:
        """Detect if change is related to Aider session"""
        # Check for .aider.chat.history.md in working directory
        aider_history = self.working_dir / '.aider.chat.history.md'
        
        if not aider_history.exists():
            return None
        
        try:
            # Read recent entries from Aider history
            with open(aider_history, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                
            # Look for recent mentions of this file
            rel_filepath = str(Path(filepath).relative_to(self.working_dir))
            recent_context = []
            
            for line in reversed(lines[-100:]):  # Last 100 lines
                if rel_filepath in line:
                    recent_context.append(line.strip())
                if len(recent_context) >= 5:  # Limit context
                    break
            
            if recent_context:
                return {
                    'mentioned_in_history': True,
                    'context_lines': recent_context,
                    'history_file': str(aider_history)
                }
                
        except Exception as e:
            logger.debug(f"Aider context detection failed: {e}")
        
        return None
    
    def generate_diff_summary(self, filepath: str, old_hash: str, new_hash: str) -> str:
        """Generate a summary of what changed in the file"""
        if not old_hash or not new_hash:
            return "File content changed (hash comparison unavailable)"
        
        if old_hash == new_hash:
            return "No content changes detected"
        
        # TODO: Implement actual diff analysis
        # For now, return basic change indication
        try:
            file_size = os.path.getsize(filepath)
            return f"Content modified (new hash: {new_hash[:8]}..., size: {file_size} bytes)"
        except OSError:
            return "File modified (size unavailable)"
    
    def on_modified(self, event):
        if event.is_directory:
            return
        
        filepath = event.src_path
        if self.should_ignore(filepath):
            return
        
        self.process_file_change(filepath, 'modified')
    
    def on_created(self, event):
        if event.is_directory:
            return
        
        filepath = event.src_path
        if self.should_ignore(filepath):
            return
        
        self.process_file_change(filepath, 'created')
    
    def on_deleted(self, event):
        if event.is_directory:
            return
        
        filepath = event.src_path
        if self.should_ignore(filepath):
            return
        
        self.process_file_change(filepath, 'deleted')
    
    def on_moved(self, event):
        if event.is_directory:
            return
        
        # Handle as delete + create
        if not self.should_ignore(event.src_path):
            self.process_file_change(event.src_path, 'deleted')
        
        if not self.should_ignore(event.dest_path):
            self.process_file_change(event.dest_path, 'created')
    
    def process_file_change(self, filepath: str, change_type: str):
        """Process a file change event"""
        try:
            # Get current file state
            current_hash = self.get_file_hash(filepath) if change_type != 'deleted' else None
            file_size = os.path.getsize(filepath) if change_type != 'deleted' else 0
            
            # Get previous state
            previous_state = self.file_states.get(filepath, {})
            previous_hash = previous_state.get('hash')
            
            # Generate diff summary
            diff_summary = None
            if change_type == 'modified' and previous_hash:
                diff_summary = self.generate_diff_summary(filepath, previous_hash, current_hash)
            
            # Create change event
            change_event = FileChangeEvent(
                filepath=filepath,
                change_type=change_type,
                timestamp=datetime.now(),
                file_hash=current_hash,
                size_bytes=file_size,
                git_status=self.get_git_status(filepath),
                aider_context=self.detect_aider_context(filepath),
                diff_summary=diff_summary
            )
            
            # Update file state tracking
            if change_type != 'deleted':
                self.file_states[filepath] = {
                    'hash': current_hash,
                    'size': file_size,
                    'last_modified': datetime.now()
                }
            else:
                self.file_states.pop(filepath, None)
            
            # Add to buffer
            self.change_buffer.append(change_event)
            
            # Log the event
            logger.info(f"File {change_type}: {filepath} (git: {change_event.git_status})")
            
            # Call callback if provided
            if self.callback:
                asyncio.create_task(self.callback(change_event))
                
        except Exception as e:
            logger.error(f"Error processing file change for {filepath}: {e}")
    
    def get_recent_changes(self, minutes: int = 5) -> List[FileChangeEvent]:
        """Get changes from the last N minutes"""
        cutoff = datetime.now().timestamp() - (minutes * 60)
        return [
            change for change in self.change_buffer 
            if change.timestamp.timestamp() > cutoff
        ]
    
    def flush_change_buffer(self) -> List[FileChangeEvent]:
        """Return and clear the change buffer"""
        changes = self.change_buffer.copy()
        self.change_buffer.clear()
        return changes

class AiderSessionTracker:
    """Tracks active Aider sessions and correlates file changes"""
    
    def __init__(self, working_dir: str):
        self.working_dir = working_dir
        self.monitor = AiderFileMonitor(working_dir, self.on_file_change)
        self.observer = Observer()
        self.current_session: Optional[AiderSession] = None
        self.change_log: List[FileChangeEvent] = []
    
    async def on_file_change(self, change_event: FileChangeEvent):
        """Handle file change events"""
        self.change_log.append(change_event)
        
        # Check if this indicates an active Aider session
        if change_event.aider_context:
            await self.update_session_context(change_event)
    
    async def update_session_context(self, change_event: FileChangeEvent):
        """Update current session with new change context"""
        if not self.current_session:
            # Create new session
            self.current_session = AiderSession(
                session_id=hashlib.md5(f"{datetime.now().isoformat()}".encode()).hexdigest()[:8],
                start_time=datetime.now(),
                working_directory=self.working_dir,
                git_branch=self.get_current_branch(),
                files_modified=set(),
                conversation_log=[]
            )
        
        # Update session with change
        self.current_session.files_modified.add(change_event.filepath)
    
    def get_current_branch(self) -> str:
        """Get current git branch"""
        try:
            repo = git.Repo(self.working_dir)
            return repo.active_branch.name
        except:
            return "unknown"
    
    def start_monitoring(self):
        """Start file system monitoring"""
        self.observer.schedule(self.monitor, self.working_dir, recursive=True)
        self.observer.start()
        logger.info(f"Started monitoring {self.working_dir}")
    
    def stop_monitoring(self):
        """Stop file system monitoring"""
        self.observer.stop()
        self.observer.join()
        logger.info("Stopped monitoring")
    
    def export_session_data(self) -> Dict:
        """Export current session data for external integration"""
        return {
            'session': asdict(self.current_session) if self.current_session else None,
            'recent_changes': [change.to_dict() for change in self.change_log[-50:]],
            'file_states': dict(self.monitor.file_states),
            'export_timestamp': datetime.now().isoformat()
        }

# Usage example and test harness
async def main():
    """Example usage of the Aider file monitor"""
    working_dir = "/path/to/your/aider/project"  # Replace with actual path
    
    tracker = AiderSessionTracker(working_dir)
    
    try:
        tracker.start_monitoring()
        
        # Run for a specified duration or until interrupted
        while True:
            await asyncio.sleep(10)
            
            # Export session data every 10 seconds (for demo)
            session_data = tracker.export_session_data()
            print(f"Session data: {json.dumps(session_data, indent=2, default=str)}")
            
    except KeyboardInterrupt:
        logger.info("Shutting down monitor...")
    finally:
        tracker.stop_monitoring()

if __name__ == "__main__":
    asyncio.run(main())