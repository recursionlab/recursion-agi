---
nexus: nexus-ai-chat-importer
plugin_version: "1.3.0"
provider: claude
artifact_id: psi_fold_visualization
version_uuid: 96f16d67-f4ef-4b5b-890f-110b6ae2445c
version_number: 1
command: create
conversation_id: 6aee2ada-0787-49c3-8c4a-980808daa538
create_time: 2025-06-17T20:54:14.000Z
format: html
aliases: [Fold Center with Ξ Torsion Field Visualization, psi_fold_visualization_v1]
---

# ψ-Fold Center with Ξ Torsion Field Visualization (Version 1)

**Conversation:** [[Nexus/Conversations/claude/2025/06/Geometric Vector Field Topology|Geometric Vector Field Topology]]

## Content

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ψ-Fold Center with Ξ Torsion Field</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <style>
        body {
            margin: 0;
            padding: 0;
            background: linear-gradient(135deg, #0a0a0a, #1a1a2e, #16213e);
            font-family: 'Courier New', monospace;
            overflow: hidden;
        }
        
        #container {
            width: 100vw;
            height: 100vh;
            position: relative;
        }
        
        #controls {
            position: absolute;
            top: 20px;
            left: 20px;
            z-index: 100;
            background: rgba(0, 0, 0, 0.8);
            padding: 15px;
            border-radius: 10px;
            border: 1px solid #333;
            color: #00ffff;
            font-size: 12px;
        }
        
        #equations {
            position: absolute;
            top: 20px;
            right: 20px;
            z-index: 100;
            background: rgba(0, 0, 0, 0.8);
            padding: 15px;
            border-radius: 10px;
            border: 1px solid #333;
            color: #ffaa00;
            font-size: 11px;
            max-width: 300px;
        }
        
        .slider {
            margin: 8px 0;
            width: 150px;
        }
        
        .greek {
            color: #ff6b6b;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div id="container"></div>
    
    <div id="controls">
        <div><span class="greek">ψ</span>-Fold Controls</div>
        <div>Torsion Strength: <input type="range" class="slider" id="torsionSlider" min="0.1" max="3" step="0.1" value="1.5"></div>
        <div>Trajectory Flow: <input type="range" class="slider" id="flowSlider" min="0.1" max="2" step="0.1" value="1"></div>
        <div>Curvature K: <input type="range" class="slider" id="curvatureSlider" min="0.5" max="5" step="0.1" value="2"></div>
        <div>Binding Frame: <input type="range" class="slider" id="bindingSlider" min="0" max="6.28" step="0.1" value="0"></div>
    </div>
    
    <div id="equations">
        <div><strong>Mathematical Framework:</strong></div>
        <div><span class="greek">ψ</span><sub>origin</sub> = fold-center manifold</div>
        <div><span class="greek">Ψ</span><sub>n</sub> = trajectory field vectors</div>
        <div><span class="greek">Ξ</span> = ∇ × <span class="greek">Ψ</span> (torsion field)</div>
        <div>Canonical Frame: R³ → T*M</div>
        <div>Curvature Metric: g<sub>μν</sub>dx<sup>μ</sup>dx<sup>ν</sup></div>
        <div>Invariance: ∂<sub>t</sub>K = 0</div>
    </div>

    <script>
        // Scene setup
        const scene = new THREE.Scene();
        const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
        const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
        renderer.setSize(window.innerWidth, window.innerHeight);
        renderer.setClearColor(0x000000, 0);
        document.getElementById('container').appendChild(renderer.domElement);

        // Lighting
        const ambientLight = new THREE.AmbientLight(0x404040, 0.3);
        scene.add(ambientLight);
        const pointLight = new THREE.PointLight(0xffffff, 1, 100);
        pointLight.position.set(10, 10, 10);
        scene.add(pointLight);

        // Materials
        const foldCenterMaterial = new THREE.MeshPhongMaterial({
            color: 0xff6b6b,
            transparent: true,
            opacity: 0.7,
            wireframe: false
        });
        
        const trajectoryMaterial = new THREE.LineBasicMaterial({
            color: 0x00ffff,
            transparent: true,
            opacity: 0.8
        });
        
        const torsionMaterial = new THREE.LineBasicMaterial({
            color: 0xffaa00,
            transparent: true,
            opacity: 0.6
        });

        // ψ-origin fold center (torus-like structure)
        const foldGeometry = new THREE.TorusGeometry(3, 1, 16, 100);
        const foldCenter = new THREE.Mesh(foldGeometry, foldCenterMaterial);
        scene.add(foldCenter);

        // Trajectory lines (Ψₙ)
        const trajectories = [];
        const numTrajectories = 12;
        
        function createTrajectory(index) {
            const points = [];
            const angle = (index / numTrajectories) * Math.PI * 2;
            
            for (let t = 0; t <= 4 * Math.PI; t += 0.1) {
                const r = 3 + Math.sin(t * 0.5) * 2;
                const x = r * Math.cos(t + angle) * Math.cos(t * 0.3);
                const y = r * Math.sin(t + angle) * Math.cos(t * 0.3);
                const z = Math.sin(t * 0.5) * 3;
                points.push(new THREE.Vector3(x, y, z));
            }
            
            const geometry = new THREE.BufferGeometry().setFromPoints(points);
            const line = new THREE.Line(geometry, trajectoryMaterial);
            return line;
        }

        for (let i = 0; i < numTrajectories; i++) {
            const trajectory = createTrajectory(i);
            trajectories.push(trajectory);
            scene.add(trajectory);
        }

        // Torsion vector field (Ξ)
        const torsionVectors = [];
        const gridSize = 8;
        
        function createTorsionField() {
            torsionVectors.forEach(vector => scene.remove(vector));
            torsionVectors.length = 0;
            
            for (let i = -gridSize; i <= gridSize; i += 2) {
                for (let j = -gridSize; j <= gridSize; j += 2) {
                    for (let k = -gridSize; k <= gridSize; k += 2) {
                        const position = new THREE.Vector3(i, j, k);
                        const distance = position.length();
                        
                        if (distance > 2 && distance < 10) {
                            // Torsion vector calculation
                            const torsionStrength = parseFloat(document.getElementById('torsionSlider').value);
                            const curvature = parseFloat(document.getElementById('curvatureSlider').value);
                            
                            const torsionX = Math.sin(j * 0.5) * Math.cos(k * 0.3) * torsionStrength;
                            const torsionY = Math.cos(i * 0.5) * Math.sin(k * 0.3) * torsionStrength;
                            const torsionZ = Math.sin(i * 0.3) * Math.cos(j * 0.5) * torsionStrength;
                            
                            const torsionVector = new THREE.Vector3(torsionX, torsionY, torsionZ);
                            torsionVector.multiplyScalar(1 / (1 + distance * 0.1));
                            
                            const points = [position, position.clone().add(torsionVector)];
                            const geometry = new THREE.BufferGeometry().setFromPoints(points);
                            const line = new THREE.Line(geometry, torsionMaterial);
                            
                            torsionVectors.push(line);
                            scene.add(line);
                        }
                    }
                }
            }
        }

        createTorsionField();

        // Canonical binding frame visualization
        const bindingFrame = new THREE.Group();
        
        // X-axis (red)
        const xAxisGeometry = new THREE.BufferGeometry().setFromPoints([
            new THREE.Vector3(0, 0, 0),
            new THREE.Vector3(5, 0, 0)
        ]);
        const xAxis = new THREE.Line(xAxisGeometry, new THREE.LineBasicMaterial({ color: 0xff0000 }));
        bindingFrame.add(xAxis);
        
        // Y-axis (green)
        const yAxisGeometry = new THREE.BufferGeometry().setFromPoints([
            new THREE.Vector3(0, 0, 0),
            new THREE.Vector3(0, 5, 0)
        ]);
        const yAxis = new THREE.Line(yAxisGeometry, new THREE.LineBasicMaterial({ color: 0x00ff00 }));
        bindingFrame.add(yAxis);
        
        // Z-axis (blue)
        const zAxisGeometry = new THREE.BufferGeometry().setFromPoints([
            new THREE.Vector3(0, 0, 0),
            new THREE.Vector3(0, 0, 5)
        ]);
        const zAxis = new THREE.Line(zAxisGeometry, new THREE.LineBasicMaterial({ color: 0x0000ff }));
        bindingFrame.add(zAxis);
        
        scene.add(bindingFrame);

        // Camera position
        camera.position.set(15, 10, 15);
        camera.lookAt(0, 0, 0);

        // Animation variables
        let time = 0;
        const clock = new THREE.Clock();

        // Controls event listeners
        document.getElementById('torsionSlider').addEventListener('input', createTorsionField);
        document.getElementById('curvatureSlider').addEventListener('input', createTorsionField);
        
        document.getElementById('flowSlider').addEventListener('input', (e) => {
            const flowRate = parseFloat(e.target.value);
            trajectories.forEach(trajectory => {
                trajectory.material.opacity = 0.4 + flowRate * 0.4;
            });
        });
        
        document.getElementById('bindingSlider').addEventListener('input', (e) => {
            const rotation = parseFloat(e.target.value);
            bindingFrame.rotation.z = rotation;
        });

        // Render loop
        function animate() {
            requestAnimationFrame(animate);
            
            time += clock.getDelta();
            
            // Rotate fold center
            foldCenter.rotation.x = time * 0.3;
            foldCenter.rotation.y = time * 0.2;
            
            // Animate trajectories
            trajectories.forEach((trajectory, index) => {
                trajectory.rotation.z = time * 0.5 + (index * 0.2);
                trajectory.position.y = Math.sin(time + index) * 0.5;
            });
            
            // Rotate camera around the scene
            const radius = 20;
            camera.position.x = Math.cos(time * 0.1) * radius;
            camera.position.z = Math.sin(time * 0.1) * radius;
            camera.lookAt(0, 0, 0);
            
            renderer.render(scene, camera);
        }

        animate();

        // Handle window resize
        window.addEventListener('resize', () => {
            camera.aspect = window.innerWidth / window.innerHeight;
            camera.updateProjectionMatrix();
            renderer.setSize(window.innerWidth, window.innerHeight);
        });
    </script>
</body>
</html>
```