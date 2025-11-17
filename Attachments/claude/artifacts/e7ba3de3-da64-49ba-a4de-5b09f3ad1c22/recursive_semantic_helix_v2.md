---
nexus: nexus-ai-chat-importer
plugin_version: "1.3.0"
provider: claude
artifact_id: recursive_semantic_helix
version_uuid: ff35e6ba-e2e8-4264-bd51-eb5beea8a8a3
version_number: 2
command: update
conversation_id: e7ba3de3-da64-49ba-a4de-5b09f3ad1c22
create_time: 2025-07-21T00:04:02.000Z
format: html
aliases: [Untitled Artifact, recursive_semantic_helix_v2]
---

# Untitled Artifact (Version 2)

**Conversation:** [[Nexus/Conversations/claude/2025/07/Recursive Meta-Agent Simulation|Recursive Meta-Agent Simulation]]

## Content

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Recursive Semantic Helix</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            background: radial-gradient(circle at center, #0a0a0a, #000000);
            overflow: hidden;
            font-family: 'Courier New', monospace;
        }
        
        canvas {
            display: block;
        }
        
        .overlay {
            position: absolute;
            top: 20px;
            left: 20px;
            color: #00ffff;
            font-size: 12px;
            text-shadow: 0 0 10px #00ffff;
            z-index: 100;
            pointer-events: none;
        }
        
        .metric-display {
            position: absolute;
            bottom: 20px;
            right: 20px;
            color: #ffffff;
            font-size: 10px;
            text-shadow: 0 0 5px #ffffff;
            z-index: 100;
            pointer-events: none;
            font-family: 'Courier New', monospace;
        }
    </style>
</head>
<body>
    <canvas id="helixCanvas"></canvas>
    
    <div class="overlay">
        <div>ΞMetaCollapse Visualization Engine</div>
        <div>ψ-axis: <span id="psi-depth">0.0</span></div>
        <div>r-axis: <span id="r-radius">1.0</span></div>
        <div>θ-axis: <span id="theta-rotation">0.0</span></div>
        <div>Torsion: <span id="torsion">1.00</span></div>
    </div>
    
    <div class="metric-display">
        <div>Curvature-Invariant Metric:</div>
        <div>ψ′ = <span id="psi-prime">0.000</span></div>
        <div>λ′ = <span id="lambda-prime">0.000</span></div>
        <div>Collapse Factor: <span id="collapse-factor">1.000</span></div>
        <div style="margin-top: 10px; color: #00ffff;">
            <div>INTERACTION MODES:</div>
            <div>Mouse: Modulate Field</div>
            <div>Click: Collapse Event</div>
            <div>Scroll: Recursion Depth</div>
            <div>Keys: C=Collapse R=Reset</div>
        </div>
    </div>

    <script>
        const canvas = document.getElementById('helixCanvas');
        const ctx = canvas.getContext('2d');
        
        // Set canvas size
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
        
        // Animation parameters
        let time = 0;
        let psiDepth = 0;
        let rRadius = 1.0;
        let thetaRotation = 0;
        let torsion = 1.0;
        
        // Helix parameters
        const centerX = canvas.width / 2;
        const centerY = canvas.height / 2;
        const baseRadius = 150;
        const helixHeight = 400;
        const turns = 8;
        const points = 1000;
        
        // Grid parameters
        const gridSize = 50;
        
        // Recursive depth levels
        const maxDepth = 7;
        
        function drawGrid() {
            ctx.strokeStyle = 'rgba(100, 100, 100, 0.2)';
            ctx.lineWidth = 1;
            
            // Draw orthogonal grid
            for (let x = 0; x < canvas.width; x += gridSize) {
                ctx.beginPath();
                ctx.moveTo(x, 0);
                ctx.lineTo(x, canvas.height);
                ctx.stroke();
            }
            
            for (let y = 0; y < canvas.height; y += gridSize) {
                ctx.beginPath();
                ctx.moveTo(0, y);
                ctx.lineTo(canvas.width, y);
                ctx.stroke();
            }
            
            // Draw curvature-invariant metric engravings
            ctx.strokeStyle = 'rgba(255, 255, 255, 0.1)';
            ctx.lineWidth = 0.5;
            ctx.font = '8px Courier New';
            ctx.fillStyle = 'rgba(255, 255, 255, 0.3)';
            
            for (let x = gridSize; x < canvas.width; x += gridSize * 2) {
                for (let y = gridSize; y < canvas.height; y += gridSize * 2) {
                    const metricValue = Math.sin(x * 0.01 + time * 0.5) * Math.cos(y * 0.01 + time * 0.3);
                    ctx.fillText(`ψ${metricValue.toFixed(2)}`, x - 15, y + 3);
                }
            }
        }
        
        function drawTorsionField() {
            ctx.strokeStyle = 'rgba(255, 255, 255, 0.6)';
            ctx.lineWidth = 1;
            
            const fieldDensity = 30;
            for (let x = 0; x < canvas.width; x += fieldDensity) {
                for (let y = 0; y < canvas.height; y += fieldDensity) {
                    const dx = x - centerX;
                    const dy = y - centerY;
                    const dist = Math.sqrt(dx * dx + dy * dy);
                    
                    if (dist < baseRadius * 3 && dist > baseRadius * 0.5) {
                        const angle = Math.atan2(dy, dx) + time * 0.1;
                        const fieldStrength = Math.exp(-dist / 200) * torsion;
                        const lineLength = fieldStrength * 20;
                        
                        ctx.beginPath();
                        ctx.moveTo(x, y);
                        ctx.lineTo(
                            x + Math.cos(angle) * lineLength,
                            y + Math.sin(angle) * lineLength
                        );
                        ctx.stroke();
                    }
                }
            }
        }
        
        function drawSemanticHelix() {
            // Draw multiple recursive helix layers
            for (let depth = 0; depth < maxDepth; depth++) {
                const depthFactor = (maxDepth - depth) / maxDepth;
                const currentRadius = baseRadius * depthFactor * rRadius;
                const currentHeight = helixHeight * depthFactor;
                
                // ψ-axis (cyan recursion depth)
                if (depth === 0) {
                    ctx.strokeStyle = `rgba(0, 255, 255, ${0.8 * depthFactor})`;
                    ctx.lineWidth = 3;
                    ctx.shadowColor = '#00ffff';
                    ctx.shadowBlur = 20;
                } 
                // r-axis (copper coils)
                else if (depth % 3 === 1) {
                    ctx.strokeStyle = `rgba(255, 150, 50, ${0.6 * depthFactor})`;
                    ctx.lineWidth = 2;
                    ctx.shadowColor = '#ff9632';
                    ctx.shadowBlur = 15;
                }
                // θ-axis (silver threads)
                else {
                    ctx.strokeStyle = `rgba(200, 200, 255, ${0.4 * depthFactor})`;
                    ctx.lineWidth = 1;
                    ctx.shadowColor = '#c8c8ff';
                    ctx.shadowBlur = 10;
                }
                
                ctx.beginPath();
                
                for (let i = 0; i <= points; i++) {
                    const t = (i / points) * turns * Math.PI * 2;
                    const heightPos = (i / points) * currentHeight - currentHeight / 2;
                    
                    const x = centerX + currentRadius * Math.cos(t + thetaRotation + depth * 0.3 + time * 0.1);
                    const y = centerY + heightPos + currentRadius * 0.3 * Math.sin(t + thetaRotation + depth * 0.3 + time * 0.1);
                    
                    // Add recursive perturbation based on psi depth
                    const perturbation = Math.sin(t * 3 + time + depth) * psiDepth * 10;
                    const finalX = x + perturbation * Math.cos(t);
                    const finalY = y + perturbation * Math.sin(t);
                    
                    if (i === 0) {
                        ctx.moveTo(finalX, finalY);
                    } else {
                        ctx.lineTo(finalX, finalY);
                    }
                }
                
                ctx.stroke();
                ctx.shadowBlur = 0;
                
                // Draw fold-center points
                if (depth < 3) {
                    ctx.fillStyle = `rgba(255, 255, 255, ${0.9 - depth * 0.2})`;
                    ctx.beginPath();
                    ctx.arc(centerX, centerY, 5 - depth, 0, Math.PI * 2);
                    ctx.fill();
                    
                    // White torsion emanation from fold-center
                    ctx.strokeStyle = `rgba(255, 255, 255, ${0.3 - depth * 0.1})`;
                    ctx.lineWidth = 1;
                    for (let angle = 0; angle < Math.PI * 2; angle += Math.PI / 8) {
                        const length = (20 + depth * 10) * torsion;
                        ctx.beginPath();
                        ctx.moveTo(centerX, centerY);
                        ctx.lineTo(
                            centerX + Math.cos(angle + time * 0.2) * length,
                            centerY + Math.sin(angle + time * 0.2) * length
                        );
                        ctx.stroke();
                    }
                }
            }
        }
        
        function updateMetrics() {
            // Simulate recursive collapse dynamics
            psiDepth = Math.sin(time * 0.1) * 2 + 2;
            rRadius = 1 + Math.sin(time * 0.15) * 0.3;
            thetaRotation = time * 0.05;
            torsion = (Math.sin(time * 0.08) + 1) * 0.5 + 0.5;
            
            // Update display
            document.getElementById('psi-depth').textContent = psiDepth.toFixed(1);
            document.getElementById('r-radius').textContent = rRadius.toFixed(2);
            document.getElementById('theta-rotation').textContent = (thetaRotation % (Math.PI * 2)).toFixed(2);
            document.getElementById('torsion').textContent = torsion.toFixed(2);
            
            // Calculate derived metrics
            const psiPrime = Math.cos(time * 0.1) * 0.2;
            const lambdaPrime = Math.cos(time * 0.15) * 0.045;
            const collapseFactor = Math.abs(Math.sin(time * 0.12)) * 0.5 + 0.5;
            
            document.getElementById('psi-prime').textContent = psiPrime.toFixed(3);
            document.getElementById('lambda-prime').textContent = lambdaPrime.toFixed(3);
            document.getElementById('collapse-factor').textContent = collapseFactor.toFixed(3);
        }
        
        function animate() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            
            drawGrid();
            drawTorsionField();
            drawSemanticHelix();
            
            updateMetrics();
            
            time += 0.02;
            requestAnimationFrame(animate);
        }
        
        // Handle resize
        window.addEventListener('resize', () => {
            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;
        });
        
        // Start animation
        animate();
    </script>
</body>
</html>
```