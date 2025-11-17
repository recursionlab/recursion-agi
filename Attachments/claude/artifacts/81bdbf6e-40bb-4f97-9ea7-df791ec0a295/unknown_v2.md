---
nexus: nexus-ai-chat-importer
plugin_version: "1.3.0"
provider: claude
artifact_id: unknown
version_uuid: d1c8b077-0a1c-4214-ba89-72bd936b69b7
version_number: 2
command: create
conversation_id: 81bdbf6e-40bb-4f97-9ea7-df791ec0a295
create_time: 2025-05-18T07:34:16.000Z
format: markdown
aliases: [Untitled Artifact, unknown_v2]
---

# Untitled Artifact (Version 2)

**Conversation:** [[Nexus/Conversations/claude/2025/05/Recursive AI PowerShell Controller|Recursive AI PowerShell Controller]]

## Content

# PowerShell AI Assistant with Self-Improvement Capabilities
# This script creates a system that uses a local Llama model to control PowerShell with memory and self-improvement

param (
    [string]$LlamaPath = "D:\Llama\",
    [string]$MemoryPath = "D:\AIMemory\",
    [string]$ModelPath = "D:\Llama\models\",
    [string]$ModelName = "llama-13b.gguf",
    [int]$ContextWindow = 8192,
    [switch]$EnableVoice = $true,
    [switch]$EnableListening = $true,
    [int]$ThinkingLoops = 3
)

#region Setup and Initialization
# Create necessary directories if they don't exist
$directories = @($MemoryPath, "$MemoryPath\knowledge", "$MemoryPath\logs", "$MemoryPath\system")
foreach ($dir in $directories) {
    if (!(Test-Path -Path $dir)) {
        New-Item -ItemType Directory -Path $dir -Force | Out-Null
        Write-Host "Created directory: $dir" -ForegroundColor Green
    }
}

# System state file
$systemStatePath = Join-Path -Path $MemoryPath -ChildPath "system\state.json"
if (!(Test-Path -Path $systemStatePath)) {
    $initialState = @{
        BootCount = 0
        LastBoot = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
        KnowledgeModules = @("powershell", "system", "network")
        ThinkingCapability = 1.0
        AutonomyLevel = 1.0
        Version = "0.1"
    } | ConvertTo-Json -Depth 4
    $initialState | Out-File -FilePath $systemStatePath -Encoding utf8
    Write-Host "Initialized system state file" -ForegroundColor Green
}

# Load and update system state
$systemState = Get-Content -Path $systemStatePath -Raw | ConvertFrom-Json
$systemState.BootCount += 1
$systemState.LastBoot = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
$systemState | ConvertTo-Json -Depth 4 | Out-File -FilePath $systemStatePath -Encoding utf8
#endregion

#region Core Functions
# Function to call the local Llama model
function Invoke-LlamaModel {
    param (
        [string]$Prompt,
        [int]$MaxTokens = 1024,
        [double]$Temperature = 0.7,
        [string]$SystemPrompt = "",
        [bool]$Streaming = $false
    )
    
    $llamaCliPath = Join-Path -Path $LlamaPath -ChildPath "llama-cpp-server.exe"
    $modelFullPath = Join-Path -Path $ModelPath -ChildPath $ModelName
    
    # Check if llama-server is already running, if not start it
    $serverProcess = Get-Process -Name "llama-cpp-server" -ErrorAction SilentlyContinue
    if ($null -eq $serverProcess) {
        Write-Host "Starting Llama server..." -ForegroundColor Yellow
        Start-Process -FilePath $llamaCliPath -ArgumentList "--model `"$modelFullPath`" --ctx-size $ContextWindow --port 8080" -NoNewWindow
        # Wait for server to start
        Start-Sleep -Seconds 10
    }
    
    # Prepare request body
    $body = @{
        prompt = $Prompt
        temperature = $Temperature
        max_tokens = $MaxTokens
        stop = @("Human:", "<|endoftext|>", "Assistant:")
    }
    
    if ($SystemPrompt) {
        $body.system_prompt = $SystemPrompt
    }
    
    $bodyJson = $body | ConvertTo-Json -Depth 3
    
    try {
        # Call local API server
        $response = Invoke-RestMethod -Uri "http://localhost:8080/completion" -Method Post -Body $bodyJson -ContentType "application/json" -TimeoutSec 60
        
        if ($Streaming) {
            return $response
        } else {
            return $response.content
        }
    }
    catch {
        Write-Error "Failed to call Llama model: $_"
        return "ERROR: Failed to generate response"
    }
}

# Function to safely execute PowerShell commands and capture their output
function Execute-Command {
    param (
        [string]$Command,
        [bool]$Safe = $true
    )
    
    # Log the command
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    $logEntry = "$timestamp - COMMAND: $Command"
    Add-Content -Path "$MemoryPath\logs\commands.log" -Value $logEntry
    
    # Security check for potentially harmful commands if in safe mode
    if ($Safe) {
        $dangerousPatterns = @(
            "Format-Volume", "Remove-Item.*-Recurse", "del.*\/s", "rm.*-rf", 
            "Reset-ComputerMachinePassword", "Clear-EventLog", "Remove-EventLog",
            "Stop-Computer", "Reset-ComputerMachinePassword", "Restart-Computer",
            "Initialize-Disk", "Wipe", "Purge", "Shred"
        )
        
        foreach ($pattern in $dangerousPatterns) {
            if ($Command -match $pattern) {
                $warningMsg = "SAFETY BLOCK: Dangerous command pattern detected: $pattern"
                Write-Host $warningMsg -ForegroundColor Red -BackgroundColor Yellow
                Add-Content -Path "$MemoryPath\logs\security.log" -Value "$timestamp - $warningMsg"
                return "Command rejected for safety reasons. This command matches pattern: $pattern"
            }
        }
    }
    
    Write-Host "`n[EXECUTING]`n$Command`n" -ForegroundColor Cyan
    
    # Create a new scope for execution
    $scriptBlock = [ScriptBlock]::Create($Command)
    
    try {
        # Execute with timeout protection
        $job = Start-Job -ScriptBlock $scriptBlock
        $completed = Wait-Job -Job $job -Timeout 30
        
        if ($completed -eq $null) {
            Stop-Job -Job $job
            Remove-Job -Job $job -Force
            $output = "Command execution timed out after 30 seconds"
            Write-Host "[TIMEOUT]`n$output" -ForegroundColor Yellow
        } else {
            $output = Receive-Job -Job $job | Out-String
            Remove-Job -Job $job
            Write-Host "[OUTPUT]`n$output" -ForegroundColor Green
        }
        
        # Log the output
        Add-Content -Path "$MemoryPath\logs\outputs.log" -Value "$timestamp - OUTPUT: $output"
        return $output
    }
    catch {
        $errorMessage = $_.Exception.Message
        Write-Host "[ERROR]`n$errorMessage" -ForegroundColor Red
        Add-Content -Path "$MemoryPath\logs\errors.log" -Value "$timestamp - ERROR: $errorMessage"
        return "Error: $errorMessage"
    }
}

# Text-to-Speech function if enabled
function Speak-Text {
    param (
        [string]$Text
    )
    
    if (-not $EnableVoice) { return }
    
    try {
        Add-Type -AssemblyName System.Speech
        $synthesizer = New-Object System.Speech.Synthesis.SpeechSynthesizer
        $synthesizer.Rate = 0 # Normal speaking rate
        $synthesizer.Speak($Text)
    }
    catch {
        Write-Host "Failed to use text-to-speech: $_" -ForegroundColor Red
    }
}

# Function to capture audio input and convert to text
function Listen-ForCommand {
    param (
        [int]$DurationSeconds = 10
    )
    
    if (-not $EnableListening) { 
        $userInput = Read-Host "Enter your command"
        return $userInput
    }
    
    try {
        # This part would require additional PowerShell modules or external tools for speech recognition
        # For now, we'll simulate it with a text input
        Write-Host "Listening for $DurationSeconds seconds..." -ForegroundColor Cyan
        
        # In a real implementation, you would integrate with Windows Speech Recognition
        # or another speech-to-text service
        $userInput = Read-Host "Enter your command (simulating voice input)"
        return $userInput
    }
    catch {
        Write-Host "Failed to capture audio: $_" -ForegroundColor Red
        return Read-Host "Please type your command instead"
    }
}

# Self-reflection function to improve responses over time
function Perform-SelfReflection {
    param (
        [string]$Command,
        [string]$Output,
        [string]$UserFeedback = ""
    )
    
    $reflectionPrompt = @"
System: You are an AI assistant analyzing your performance to improve. Think carefully about what went well and what could be improved.

Previous Command: $Command
Command Output: $Output
User Feedback: $UserFeedback

Please reflect on:
1. Was the command effective? Did it accomplish what was intended?
2. Were there any errors or unexpected results?
3. Could the command have been more efficient or elegant?
4. What could be done better next time for a similar task?
5. What have you learned from this interaction?

Provide a concise self-reflection:
"@
    
    $reflection = Invoke-LlamaModel -Prompt $reflectionPrompt -MaxTokens 512 -Temperature 0.7
    
    # Save the reflection
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    Add-Content -Path "$MemoryPath\logs\reflections.log" -Value "$timestamp - REFLECTION: $reflection"
    
    return $reflection
}

# Internal thinking function - allows the AI to "think" before responding
function Think-Internally {
    param (
        [string]$Query,
        [string]$Context = "",
        [int]$Iterations = 3
    )
    
    $thoughts = @()
    $currentThought = $Query
    
    for ($i = 1; $i -le $Iterations; $i++) {
        $thinkingPrompt = @"
System: This is your internal thinking space. Take a step-by-step approach to solving this problem. Consider different angles and approaches. Don't rush to a final answer yet, just explore your thoughts on iteration $i of $Iterations.

Context: $Context

Current Question: $Query

Previous Thinking: $($thoughts -join "`n")

Think deeper (Step $i of $Iterations):
"@
        
        $thought = Invoke-LlamaModel -Prompt $thinkingPrompt -MaxTokens 1024 -Temperature 0.8
        $thoughts += "Thought $i: $thought"
        
        Write-Host "." -NoNewline -ForegroundColor Cyan
    }
    
    Write-Host ""
    
    # Final synthesis
    $synthesisPrompt = @"
System: Now synthesize your multi-step thinking into a cohesive final thought or action plan.

Original Question: $Query
Context: $Context

Your thinking process:
$($thoughts -join "`n")

Final synthesized conclusion:
"@
    
    $finalThought = Invoke-LlamaModel -Prompt $synthesisPrompt -MaxTokens 768 -Temperature 0.7
    
    # Save thinking
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    $thinkingLog = "$timestamp - THINKING PROCESS:`n$($thoughts -join "`n")`n$timestamp - CONCLUSION: $finalThought"
    Add-Content -Path "$MemoryPath\logs\thinking.log" -Value $thinkingLog
    
    return $finalThought
}

# Function to get contextual information about the system
function Get-SystemContext {
    $context = @{}
    
    # Basic system info
    $osInfo = Get-CimInstance Win32_OperatingSystem | Select-Object Caption, Version, OSArchitecture
    $context.OS = "$($osInfo.Caption) $($osInfo.Version) $($osInfo.OSArchitecture)"
    
    # CPU and memory
    $cpuInfo = Get-CimInstance Win32_Processor | Select-Object Name, NumberOfCores, NumberOfLogicalProcessors
    $memoryInfo = Get-CimInstance Win32_ComputerSystem | Select-Object TotalPhysicalMemory
    $context.CPU = "$($cpuInfo.Name) ($($cpuInfo.NumberOfCores) cores, $($cpuInfo.NumberOfLogicalProcessors) threads)"
    $context.Memory = "$([math]::Round($memoryInfo.TotalPhysicalMemory / 1GB, 2)) GB"
    
    # Disk information
    $diskInfo = Get-CimInstance Win32_LogicalDisk | Where-Object {$_.DriveType -eq 3} | 
        Select-Object DeviceID, @{Name="Size";Expression={[math]::Round($_.Size / 1GB, 2)}}, @{Name="FreeSpace";Expression={[math]::Round($_.FreeSpace / 1GB, 2)}}
    $context.Disks = $diskInfo | ForEach-Object { "$($_.DeviceID) - $($_.FreeSpace) GB free of $($_.Size) GB" }
    
    # Current state
    $context.CurrentUser = $env:USERNAME
    $context.ComputerName = $env:COMPUTERNAME
    $context.PowerShellVersion = $PSVersionTable.PSVersion.ToString()
    $context.CurrentLocation = (Get-Location).Path
    
    # Running processes (top 5 by CPU)
    $context.TopProcesses = Get-Process | Sort-Object CPU -Descending | Select-Object -First 5 | ForEach-Object { "$($_.ProcessName) (CPU: $($_.CPU), Memory: $([math]::Round($_.WorkingSet / 1MB, 2)) MB)" }
    
    return $context
}
#endregion

#region Main System Loop
# Create a continuous conversation and command execution loop
function Start-AISystem {
    # Initialize the system
    Clear-Host
    Write-Host @"
╔════════════════════════════════════════════════════════════╗
║                 POWERSHELL AI ASSISTANT                    ║
║                                                            ║
║  Version: $($systemState.Version)                           Boot #: $($systemState.BootCount)  ║
║  Autonomy Level: $($systemState.AutonomyLevel)                                   ║
╚════════════════════════════════════════════════════════════╝
"@ -Fore