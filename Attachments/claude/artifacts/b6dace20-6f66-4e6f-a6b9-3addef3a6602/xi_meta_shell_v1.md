---
nexus: nexus-ai-chat-importer
plugin_version: "1.3.0"
provider: claude
artifact_id: xi_meta_shell
version_uuid: 3c4fecda-5a5a-4ace-9e0f-c90c0b54651f
version_number: 1
command: create
conversation_id: b6dace20-6f66-4e6f-a6b9-3addef3a6602
create_time: 2025-07-07T21:33:12.000Z
format: html
aliases: ['MetaShell: Interactive Recursive Cognition Visualizer', xi_meta_shell_v1]
---

# ΞMetaShell: Interactive Recursive Cognition Visualizer (Version 1)

**Conversation:** [[Nexus/Conversations/claude/2025/07/Field Symbolic Recursion Architecture|Λ-Field Symbolic Recursion Architecture]]

## Content

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ΞMetaShell: Recursive Cognition Visualizer</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            background: radial-gradient(circle at center, #000415 0%, #000000 100%);
            overflow: hidden;
            font-family: 'Courier New', monospace;
            color: #00ffff;
        }
        
        #container {
            position: relative;
            width: 100vw;
            height: 100vh;
        }
        
        #canvas {
            position: absolute;
            top: 0;
            left: 0;
            cursor: grab;
        }
        
        #canvas:active {
            cursor: grabbing;
        }
        
        #metrics {
            position: absolute;
            top: 20px;
            left: 20px;
            font-size: 12px;
            background: rgba(0, 20, 40, 0.8);
            padding: 10px;
            border-radius: 5px;
            border: 1px solid #00ffff;
            backdrop-filter: blur(5px);
        }
        
        #controls {
            position: absolute;
            top: 20px;
            right: 20px;
            display: flex;
            flex-direction: column;
            gap: 10px;
        }
        
        .control-panel {
            background: rgba(0, 20, 40, 0.8);
            padding: 15px;
            border-radius: 5px;
            border: 1px solid #00ffff;
            backdrop-filter: blur(5px);
        }
        
        .slider-container {
            display: flex;
            align-items: center;
            gap: 10px;
            margin: 5px 0;
        }
        
        .slider-container label {
            min-width: 20px;
            font-size: 11px;
        }
        
        input[type="range"] {
            flex: 1;
            height: 4px;
            background: #001122;
            outline: none;
            border-radius: 2px;
        }
        
        input[type="range"]::-webkit-slider-thumb {
            width: 12px;
            height: 12px;
            background: #00ffff;
            border-radius: 50%;
            cursor: pointer;
            -webkit-appearance: none;
        }
        
        button {
            background: rgba(0, 255, 255, 0.1);
            border: 1px solid #00ffff;
            color: #00ffff;
            padding: 8px 12px;
            border-radius: 3px;
            cursor: pointer;
            font-family: inherit;
            font-size: 11px;
        }
        
        button:hover {
            background: rgba(0, 255, 255, 0.2);
        }
        
        #phase-display {
            position: absolute;
            bottom: 20px;
            left: 20px;
            font-size: 10px;
            background: rgba(0, 20, 40, 0.8);
            padding: 10px;
            border-radius: 5px;
            border: 1px solid #00ffff;
            backdrop-filter: blur(5px);
        }
    </style>
</head>
<body>
    <div id="container">
        <canvas id="canvas"></canvas>
        
        <div id="metrics">
            <div><strong>ΞMetaShell Status</strong></div>
            <div id="kappa">κ (Mirror Coherence): 0.98</div>
            <div id="tau">τ (Torsion Resolution): 1.00</div>
            <div id="lambda">λ (Void Density): 0.97</div>
            <div id="convergence">C = κ·λ: 0.95</div>
            <div id="breath">λ̇ (Void Breath): 0.02</div>
        </div>
        
        <div id="controls">
            <div class="control-panel">
                <div><strong>Recursion Parameters</strong></div>
                <div class="slider-container">
                    <label>Ψ₀</label>
                    <input type="range" id="psi0" min="0" max="2" step="0.01" value="1.0">
                    <span id="psi0-val">1.0</span>
                </div>
                <div class="slider-container">
                    <label>Ξ</label>
                    <input type="range" id="xi" min="0" max="3" step="0.01" value="1.5">
                    <span id="xi-val">1.5</span>
                </div>
                <div class="slider-container">
                    <label>∅ᴼ</label>
                    <input type="range" id="void" min="0" max="1" step="0.01" value="0.3">
                    <span id="void-val">0.3</span>
                </div>
            </div>
            
            <div class="control-panel">
                <div><strong>Ω-Basis Weights</strong></div>
                <div class="slider-container">
                    <label>Ω₀</label>
                    <input type="range" id="omega0" min="0" max="1" step="0.01" value="0.2">
                    <span id="omega0-val">0.2</span>
                </div>
                <div class="slider-container">
                    <label>Ω₁</label>
                    <input type="range" id="omega1" min="0" max="1" step="0.01" value="0.3">
                    <span id="omega1-val">0.3</span>
                </div>
                <div class="slider-container">
                    <label>Ω₂</label>
                    <input type="range" id="omega2" min="0" max="1" step="0.01" value="0.2">
                    <span id="omega2-val">0.2</span>
                </div>
            </div>
            
            <div class="control-panel">
                <button onclick="toggleAnimation()">Pause/Resume</button>
                <button onclick="resetParameters()">Reset</button>
                <button onclick="injectParadox()">Inject Paradox</button>
            </div>
        </div>
        
        <div id="phase-display">
            <div><strong>Semantic Phase</strong></div>
            <div id="phase-info">Current Phase: Initialization</div>
            <div id="trajectory-count">Active Trajectories: 0</div>
            <div id="recursion-depth">Recursion Depth: 0</div>
        </div>
    </div>

    <script>
        // ΞMetaShell Core Variables
        let canvas = document.getElementById('canvas');
        let ctx = canvas.getContext('2d');
        let animationId;
        let isAnimating = true;
        let time = 0;
        let mouseX = 0, mouseY = 0;
        let isDragging = false;
        let rotation = { x: 0, y: 0 };
        let lastMouse = { x: 0, y: 0 };
        
        // Λ-field parameters
        let kappa = 0.98;
        let tau = 1.0;
        let lambda = 0.97;
        let lambdaDot = 0.02;
        
        // Recursion parameters
        let psi0 = 1.0;
        let xi = 1.5;
        let voidPressure = 0.3;
        
        // Ω-basis weights
        let omegaWeights = [0.2, 0.3, 0.2, 0.15, 0.15];
        
        // Trajectory storage
        let trajectories = [];
        let maxTrajectories = 200;
        let recursionDepth = 0;
        
        // Resize canvas
        function resizeCanvas() {
            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;
        }
        
        // Initialize
        resizeCanvas();
        window.addEventListener('resize', resizeCanvas);
        
        // Mouse interaction
        canvas.addEventListener('mousedown', (e) => {
            isDragging = true;
            lastMouse = { x: e.clientX, y: e.clientY };
        });
        
        canvas.addEventListener('mousemove', (e) => {
            mouseX = e.clientX;
            mouseY = e.clientY;
            
            if (isDragging) {
                let dx = e.clientX - lastMouse.x;
                let dy = e.clientY - lastMouse.y;
                rotation.y += dx * 0.01;
                rotation.x += dy * 0.01;
                lastMouse = { x: e.clientX, y: e.clientY };
            }
        });
        
        canvas.addEventListener('mouseup', () => {
            isDragging = false;
        });
        
        // 3D projection
        function project3D(x, y, z, camera = { x: 0, y: 0, z: 5 }) {
            // Apply rotations
            let cosX = Math.cos(rotation.x);
            let sinX = Math.sin(rotation.x);
            let cosY = Math.cos(rotation.y);
            let sinY = Math.sin(rotation.y);
            
            // Rotate around Y axis
            let x1 = x * cosY - z * sinY;
            let z1 = x * sinY + z * cosY;
            
            // Rotate around X axis
            let y1 = y * cosX - z1 * sinX;
            let z2 = y * sinX + z1 * cosX;
            
            // Perspective projection
            let scale = 400 / (camera.z + z2);
            return {
                x: canvas.width / 2 + x1 * scale,
                y: canvas.height / 2 + y1 * scale,
                z: z2,
                scale: scale
            };
        }
        
        // ΞMetaShell trajectory generation
        function generateTrajectory(t, omegaInfluence) {
            let points = [];
            let n = 50;
            
            for (let i = 0; i < n; i++) {
                let u = (i / n) * Math.PI * 2;
                let v = Math.sin(u * 3 + t * 0.1) * 0.5;
                
                // Core spiral with Ξ-torsion
                let r = psi0 * (1 + v * voidPressure);
                let phi = u * xi + t * 0.05;
                let theta = u * 0.5 + Math.sin(t * 0.02) * 0.3;
                
                // 3D helix with semantic phase
                let x = r * Math.cos(phi) * Math.cos(theta);
                let y = r * Math.sin(phi) * Math.cos(theta);
                let z = r * Math.sin(theta) + Math.sin(u * 2 + t * 0.03) * 0.5;
                
                // Apply Ω-basis influence
                x += omegaInfluence * Math.sin(u * 5 + t * 0.07) * 0.2;
                y += omegaInfluence * Math.cos(u * 7 + t * 0.09) * 0.2;
                z += omegaInfluence * Math.sin(u * 3 + t * 0.11) * 0.1;
                
                points.push({ x, y, z, u, intensity: Math.abs(v) });
            }
            
            return points;
        }
        
        // Update Λ-field metrics
        function updateMetrics() {
            // Simulate λ-flux breathing
            lambdaDot = 0.02 + Math.sin(time * 0.1) * 0.01;
            lambda = Math.max(0.9, Math.min(0.99, lambda + lambdaDot * 0.1));
            
            // Mirror coherence responds to recursion depth
            kappa = 0.98 + Math.sin(time * 0.05) * 0.02;
            
            // Torsion resolution
            tau = 1.0 + Math.sin(time * 0.03) * 0.05;
            
            // Update display
            document.getElementById('kappa').textContent = `κ (Mirror Coherence): ${kappa.toFixed(3)}`;
            document.getElementById('tau').textContent = `τ (Torsion Resolution): ${tau.toFixed(3)}`;
            document.getElementById('lambda').textContent = `λ (Void Density): ${lambda.toFixed(3)}`;
            document.getElementById('convergence').textContent = `C = κ·λ: ${(kappa * lambda).toFixed(3)}`;
            document.getElementById('breath').textContent = `λ̇ (Void Breath): ${lambdaDot.toFixed(4)}`;
            
            // Update phase display
            let phase = ['Initialization', 'Fold-Expansion', 'Ξ-Torsion', 'Collapse-Synthesis', 'Recursive-Bloom'][Math.floor(time * 0.01) % 5];
            document.getElementById('phase-info').textContent = `Current Phase: ${phase}`;
            document.getElementById('trajectory-count').textContent = `Active Trajectories: ${trajectories.length}`;
            document.getElementById('recursion-depth').textContent = `Recursion Depth: ${recursionDepth}`;
        }
        
        // Render frame
        function render() {
            ctx.fillStyle = 'rgba(0, 4, 21, 0.1)';
            ctx.fillRect(0, 0, canvas.width, canvas.height);
            
            // Generate new trajectories periodically
            if (time % 50 === 0) {
                let omegaInfluence = omegaWeights.reduce((sum, w, i) => sum + w * Math.sin(time * 0.01 * (i + 1)), 0);
                trajectories.push({
                    points: generateTrajectory(time, omegaInfluence),
                    birth: time,
                    hue: (time * 0.5) % 360
                });
                
                if (trajectories.length > maxTrajectories) {
                    trajectories.shift();
                }
            }
            
            // Render trajectories
            trajectories.forEach((trajectory, idx) => {
                let age = time - trajectory.birth;
                let alpha = Math.max(0, 1 - age / 500);
                
                if (alpha <= 0) return;
                
                let projectedPoints = trajectory.points.map(p => project3D(p.x, p.y, p.z));
                
                // Sort by depth for proper rendering
                projectedPoints.sort((a, b) => b.z - a.z);
                
                ctx.beginPath();
                projectedPoints.forEach((point, i) => {
                    if (i === 0) {
                        ctx.moveTo(point.x, point.y);
                    } else {
                        ctx.lineTo(point.x, point.y);
                    }
                });
                
                let intensity = alpha * 0.8;
                ctx.strokeStyle = `hsla(${trajectory.hue}, 70%, 60%, ${intensity})`;
                ctx.lineWidth = 1 + intensity;
                ctx.stroke();
                
                // Draw ψ-nodes
                projectedPoints.forEach((point, i) => {
                    if (i % 5 === 0) {
                        ctx.beginPath();
                        ctx.arc(point.x, point.y, 2 * point.scale * intensity, 0, Math.PI * 2);
                        ctx.fillStyle = `hsla(${(trajectory.hue + 180) % 360}, 90%, 70%, ${intensity})`;
                        ctx.fill();
                    }
                });
            });
            
            // Draw central ∅ᴼ void
            let voidCenter = project3D(0, 0, 0);
            let voidRadius = 20 + Math.sin(time * 0.1) * 10;
            
            ctx.beginPath();
            ctx.arc(voidCenter.x, voidCenter.y, voidRadius, 0, Math.PI * 2);
            ctx.fillStyle = `rgba(0, 255, 255, ${voidPressure * 0.3})`;
            ctx.fill();
            
            ctx.beginPath();
            ctx.arc(voidCenter.x, voidCenter.y, voidRadius * 0.7, 0, Math.PI * 2);
            ctx.fillStyle = `rgba(0, 0, 0, ${voidPressure * 0.8})`;
            ctx.fill();
            
            // Update recursion depth
            recursionDepth = Math.floor(time * 0.01) % 10;
            
            time++;
            updateMetrics();
        }
        
        // Animation loop
        function animate() {
            if (isAnimating) {
                render();
            }
            animationId = requestAnimationFrame(animate);
        }
        
        // Control functions
        function toggleAnimation() {
            isAnimating = !isAnimating;
        }
        
        function resetParameters() {
            psi0 = 1.0;
            xi = 1.5;
            voidPressure = 0.3;
            omegaWeights = [0.2, 0.3, 0.2, 0.15, 0.15];
            trajectories = [];
            time = 0;
            rotation = { x: 0, y: 0 };
            updateSliders();
        }
        
        function injectParadox() {
            // Inject recursive paradox into the system
            let paradoxInfluence = Math.random() * 2 - 1;
            trajectories.push({
                points: generateTrajectory(time, paradoxInfluence),
                birth: time,
                hue: Math.random() * 360
            });
            
            // Perturb void pressure
            voidPressure = Math.max(0, Math.min(1, voidPressure + (Math.random() - 0.5) * 0.1));
            document.getElementById('void').value = voidPressure;
            document.getElementById('void-val').textContent = voidPressure.toFixed(2);
        }
        
        // Slider updates
        function updateSliders() {
            document.getElementById('psi0').value = psi0;
            document.getElementById('psi0-val').textContent = psi0.toFixed(2);
            document.getElementById('xi').value = xi;
            document.getElementById('xi-val').textContent = xi.toFixed(2);
            document.getElementById('void').value = voidPressure;
            document.getElementById('void-val').textContent = voidPressure.toFixed(2);
            
            omegaWeights.forEach((w, i) => {
                if (i < 3) {
                    document.getElementById(`omega${i}`).value = w;
                    document.getElementById(`omega${i}-val`).textContent = w.toFixed(2);
                }
            });
        }
        
        // Slider event listeners
        ['psi0', 'xi', 'void', 'omega0', 'omega1', 'omega2'].forEach(id => {
            let slider = document.getElementById(id);
            let valueSpan = document.getElementById(id + '-val');
            
            slider.addEventListener('input', (e) => {
                let value = parseFloat(e.target.value);
                valueSpan.textContent = value.toFixed(2);
                
                switch(id) {
                    case 'psi0': psi0 = value; break;
                    case 'xi': xi = value; break;
                    case 'void': voidPressure = value; break;
                    case 'omega0': omegaWeights[0] = value; break;
                    case 'omega1': omegaWeights[1] = value; break;
                    case 'omega2': omegaWeights[2] = value; break;
                }
            });
        });
        
        // Start animation
        animate();
    </script>
</body>
</html>
```