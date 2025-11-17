---
nexus: nexus-ai-chat-importer
plugin_version: "1.3.0"
provider: claude
artifact_id: hott-loop-meme
version_uuid: 8fb5bc07-4eb4-4312-a81e-f3dc75aec927
version_number: 1
command: create
conversation_id: 2b1d28b2-8d85-4d06-9d01-f4e1c4370456
create_time: 2025-07-07T01:59:04.000Z
format: html
aliases: [HoTT Loop Meme Widget, hott-loop-meme_v1]
---

# HoTT Loop Meme Widget (Version 1)

**Conversation:** [[Nexus/Conversations/claude/2025/07/HoTT Loop Meme 4D Hypersphere Visualization|HoTT Loop Meme: 4D Hypersphere Visualization]]

## Content

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HoTT Loop Meme Widget</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            background: linear-gradient(135deg, #0a0a0a, #1a1a2e, #16213e);
            font-family: 'Courier New', monospace;
            overflow: hidden;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }

        .widget-container {
            position: relative;
            width: 100vw;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .canvas-container {
            position: relative;
            border: 2px solid #00ff88;
            border-radius: 20px;
            background: rgba(0, 0, 0, 0.8);
            box-shadow: 0 0 50px rgba(0, 255, 136, 0.3);
            backdrop-filter: blur(10px);
        }

        canvas {
            border-radius: 18px;
            display: block;
        }

        .controls {
            position: absolute;
            bottom: 20px;
            left: 50%;
            transform: translateX(-50%);
            display: flex;
            gap: 15px;
            z-index: 10;
        }

        .control-btn {
            padding: 8px 16px;
            background: rgba(0, 255, 136, 0.2);
            border: 1px solid #00ff88;
            border-radius: 20px;
            color: #00ff88;
            cursor: pointer;
            transition: all 0.3s ease;
            font-family: 'Courier New', monospace;
            font-size: 12px;
        }

        .control-btn:hover {
            background: rgba(0, 255, 136, 0.4);
            box-shadow: 0 0 20px rgba(0, 255, 136, 0.5);
        }

        .info-panel {
            position: absolute;
            top: 20px;
            left: 20px;
            background: rgba(0, 0, 0, 0.8);
            border: 1px solid #00ff88;
            border-radius: 10px;
            padding: 15px;
            color: #00ff88;
            font-size: 12px;
            max-width: 300px;
            backdrop-filter: blur(5px);
        }

        .meme-overlay {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            color: #fff;
            font-size: 24px;
            font-weight: bold;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.8);
            pointer-events: none;
            z-index: 5;
            text-align: center;
        }

        .export-btn {
            position: absolute;
            top: 20px;
            right: 20px;
            padding: 10px 20px;
            background: linear-gradient(45deg, #ff6b6b, #ff8e8e);
            border: none;
            border-radius: 25px;
            color: white;
            cursor: pointer;
            font-family: 'Courier New', monospace;
            font-weight: bold;
            transition: all 0.3s ease;
        }

        .export-btn:hover {
            transform: scale(1.05);
            box-shadow: 0 0 20px rgba(255, 107, 107, 0.5);
        }

        .hott-formula {
            position: absolute;
            bottom: 20px;
            right: 20px;
            color: #00ff88;
            font-size: 14px;
            font-family: 'Courier New', monospace;
        }
    </style>
</head>
<body>
    <div class="widget-container">
        <div class="canvas-container">
            <canvas id="hott-canvas" width="800" height="600"></canvas>
        </div>
        
        <div class="info-panel">
            <strong>HoTT Loop Space Ω(X)</strong><br>
            4D → 3D Hypersphere Projection<br>
            <br>
            <em>Visualizing homotopy equivalences</em><br>
            Loop space: Ω(X) = {f: S¹ → X | f(1) = x₀}<br>
            Dimension: 4D → 3D stereographic projection
        </div>

        <div class="meme-overlay" id="meme-text">
            WHEN YOU FINALLY UNDERSTAND<br>
            HOMOTOPY TYPE THEORY
        </div>

        <div class="controls">
            <button class="control-btn" onclick="toggleRotation()">⟲ Rotate</button>
            <button class="control-btn" onclick="togglePulsation()">💓 Pulse</button>
            <button class="control-btn" onclick="changeMeme()">🎭 Meme</button>
            <button class="control-btn" onclick="toggleWireframe()">🔗 Wire</button>
        </div>

        <button class="export-btn" onclick="exportGIF()">📱 Export GIF</button>

        <div class="hott-formula">
            π₄(S³) ≅ ℤ/2ℤ
        </div>
    </div>

    <script>
        const canvas = document.getElementById('hott-canvas');
        const ctx = canvas.getContext('2d');
        const centerX = canvas.width / 2;
        const centerY = canvas.height / 2;

        let time = 0;
        let isRotating = true;
        let isPulsating = true;
        let isWireframe = false;
        let currentMeme = 0;

        const memeTexts = [
            "WHEN YOU FINALLY UNDERSTAND<br>HOMOTOPY TYPE THEORY",
            "LOOP SPACES BE LIKE<br>*PULSATES MATHEMATICALLY*",
            "4D HYPERSPHERE GOES<br>BRRRRR IN 3D",
            "MATHEMATICIAN: IT'S JUST<br>A SIMPLE PROJECTION",
            "WHEN THE TOPOLOGY<br>HITS DIFFERENT",
            "HOTT TAKE:<br>INFINITY GROUPOIDS > SETS"
        ];

        // 4D to 3D projection parameters
        const projection = {
            w: 2, // 4D viewing distance
            scale: 150,
            rotationSpeed: 0.02
        };

        // Hypersphere vertices (4D)
        function generateHypersphere(radius, detail) {
            const vertices = [];
            const phi = Math.PI * (3 - Math.sqrt(5)); // Golden angle
            
            for (let i = 0; i < detail; i++) {
                const theta = phi * i;
                const y = 1 - (i / (detail - 1)) * 2;
                const radiusAtY = Math.sqrt(1 - y * y);
                
                // Generate points on S³ (3-sphere in 4D)
                for (let j = 0; j < 8; j++) {
                    const angle = (j / 8) * Math.PI * 2;
                    const x = Math.cos(theta) * radiusAtY;
                    const z = Math.sin(theta) * radiusAtY;
                    const w = Math.cos(angle) * Math.sin(Math.acos(y));
                    
                    vertices.push([x * radius, y * radius, z * radius, w * radius]);
                }
            }
            return vertices;
        }

        // 4D rotation matrices
        function rotateXY(point, angle) {
            const [x, y, z, w] = point;
            const cos = Math.cos(angle);
            const sin = Math.sin(angle);
            return [
                x * cos - y * sin,
                x * sin + y * cos,
                z, w
            ];
        }

        function rotateZW(point, angle) {
            const [x, y, z, w] = point;
            const cos = Math.cos(angle);
            const sin = Math.sin(angle);
            return [
                x, y,
                z * cos - w * sin,
                z * sin + w * cos
            ];
        }

        function rotateXZ(point, angle) {
            const [x, y, z, w] = point;
            const cos = Math.cos(angle);
            const sin = Math.sin(angle);
            return [
                x * cos - z * sin,
                y,
                x * sin + z * cos,
                w
            ];
        }

        // 4D to 3D stereographic projection
        function projectTo3D(point4D) {
            const [x, y, z, w] = point4D;
            const denominator = projection.w - w;
            if (Math.abs(denominator) < 0.001) return null; // Avoid division by zero
            
            return [
                (x / denominator) * projection.scale,
                (y / denominator) * projection.scale,
                (z / denominator) * projection.scale
            ];
        }

        // 3D to 2D projection
        function projectTo2D(point3D, distance = 400) {
            const [x, y, z] = point3D;
            const scale = distance / (distance + z);
            return [
                centerX + x * scale,
                centerY - y * scale,
                scale
            ];
        }

        function drawHypersphere() {
            const baseRadius = isPulsating ? 1 + 0.3 * Math.sin(time * 3) : 1;
            const vertices4D = generateHypersphere(baseRadius, 20);
            
            // Apply 4D rotations
            const rotatedVertices = vertices4D.map(v => {
                let rotated = v;
                if (isRotating) {
                    rotated = rotateXY(rotated, time * projection.rotationSpeed);
                    rotated = rotateZW(rotated, time * projection.rotationSpeed * 0.7);
                    rotated = rotateXZ(rotated, time * projection.rotationSpeed * 0.5);
                }
                return rotated;
            });

            // Project to 3D then 2D
            const projected = rotatedVertices
                .map(v => projectTo3D(v))
                .filter(v => v !== null)
                .map(v => {
                    const [x2d, y2d, scale] = projectTo2D(v);
                    return { x: x2d, y: y2d, scale, depth: v[2] };
                })
                .sort((a, b) => a.depth - b.depth); // Sort by depth

            // Clear canvas
            ctx.clearRect(0, 0, canvas.width, canvas.height);

            // Draw connections (wireframe or filled)
            if (isWireframe) {
                ctx.strokeStyle = `rgba(0, 255, 136, 0.6)`;
                ctx.lineWidth = 1;
                
                for (let i = 0; i < projected.length; i++) {
                    for (let j = i + 1; j < projected.length; j++) {
                        const dist = Math.sqrt(
                            Math.pow(projected[i].x - projected[j].x, 2) +
                            Math.pow(projected[i].y - projected[j].y, 2)
                        );
                        
                        if (dist < 50) {
                            ctx.beginPath();
                            ctx.moveTo(projected[i].x, projected[i].y);
                            ctx.lineTo(projected[j].x, projected[j].y);
                            ctx.stroke();
                        }
                    }
                }
            }

            // Draw vertices
            projected.forEach(point => {
                const size = Math.max(1, point.scale * 3);
                const alpha = Math.min(1, point.scale);
                
                ctx.beginPath();
                ctx.arc(point.x, point.y, size, 0, Math.PI * 2);
                
                if (isWireframe) {
                    ctx.strokeStyle = `rgba(0, 255, 136, ${alpha})`;
                    ctx.stroke();
                } else {
                    const hue = (point.depth + 200) % 360;
                    ctx.fillStyle = `hsla(${hue}, 100%, 60%, ${alpha})`;
                    ctx.fill();
                    
                    // Add glow effect
                    ctx.shadowBlur = 10;
                    ctx.shadowColor = `hsla(${hue}, 100%, 60%, 0.5)`;
                    ctx.fill();
                    ctx.shadowBlur = 0;
                }
            });

            // Add mathematical annotations
            ctx.fillStyle = 'rgba(0, 255, 136, 0.7)';
            ctx.font = '12px Courier New';
            ctx.fillText(`t = ${time.toFixed(2)}`, 10, canvas.height - 60);
            ctx.fillText(`vertices = ${projected.length}`, 10, canvas.height - 40);
            ctx.fillText(`Ω(X) ≅ Map(S¹,X)`, 10, canvas.height - 20);
        }

        function animate() {
            time += 0.016; // ~60fps
            drawHypersphere();
            requestAnimationFrame(animate);
        }

        function toggleRotation() {
            isRotating = !isRotating;
        }

        function togglePulsation() {
            isPulsating = !isPulsating;
        }

        function toggleWireframe() {
            isWireframe = !isWireframe;
        }

        function changeMeme() {
            currentMeme = (currentMeme + 1) % memeTexts.length;
            document.getElementById('meme-text').innerHTML = memeTexts[currentMeme];
        }

        function exportGIF() {
            // Simple export simulation - in real implementation would use gif.js
            const link = document.createElement('a');
            link.download = 'hott-loop-meme.png';
            link.href = canvas.toDataURL();
            link.click();
            
            // Show export message
            const exportMsg = document.createElement('div');
            exportMsg.textContent = 'Frame exported! Use #HoTTLoop on X 🚀';
            exportMsg.style.cssText = `
                position: fixed;
                top: 80px;
                right: 20px;
                background: rgba(0, 255, 136, 0.9);
                color: black;
                padding: 10px 20px;
                border-radius: 20px;
                font-family: 'Courier New', monospace;
                font-weight: bold;
                z-index: 100;
                animation: fadeInOut 3s ease-in-out;
            `;
            
            document.body.appendChild(exportMsg);
            setTimeout(() => exportMsg.remove(), 3000);
        }

        // Add CSS animation for export message
        const style = document.createElement('style');
        style.textContent = `
            @keyframes fadeInOut {
                0%, 100% { opacity: 0; transform: translateY(-20px); }
                10%, 90% { opacity: 1; transform: translateY(0); }
            }
        `;
        document.head.appendChild(style);

        // Custom element definition
        class HoTTLoopMeme extends HTMLElement {
            connectedCallback() {
                this.innerHTML = document.body.innerHTML;
                // Initialize the widget when used as custom element
                animate();
            }
        }

        if (typeof customElements !== 'undefined') {
            customElements.define('hott-loop-meme', HoTTLoopMeme);
        }

        // Start animation
        animate();
    </script>
</body>
</html>
```