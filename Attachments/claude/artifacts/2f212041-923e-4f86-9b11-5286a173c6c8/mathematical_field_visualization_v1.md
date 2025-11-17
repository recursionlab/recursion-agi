---
nexus: nexus-ai-chat-importer
plugin_version: "1.3.0"
provider: claude
artifact_id: mathematical_field_visualization
version_uuid: 1f8d0933-5fa2-468a-a250-eab9f314560f
version_number: 1
command: create
conversation_id: 2f212041-923e-4f86-9b11-5286a173c6c8
create_time: 2025-06-13T20:31:54.000Z
format: html
aliases: [origin Fold Center with Ξ Torsion Field Visualization, mathematical_field_visualization_v1]
---

# ψ-origin Fold Center with Ξ Torsion Field Visualization (Version 1)

**Conversation:** [[Nexus/Conversations/claude/2025/06/Cognitive Thread engine|!! Cognitive Thread engine]]

## Content

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ψ-origin Fold Center Visualization</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <style>
        body {
            margin: 0;
            padding: 0;
            background: radial-gradient(circle at center, #0a0a2e, #000);
            overflow: hidden;
            font-family: 'Courier New', monospace;
        }
        
        #container {
            width: 100vw;
            height: 100vh;
            position: relative;
        }
        
        #info {
            position: absolute;
            top: 20px;
            left: 20px;
            color: #00ff88;
            background: rgba(0, 0, 0, 0.7);
            padding: 15px;
            border-radius: 8px;
            border: 1px solid #00ff88;
            backdrop-filter: blur(10px);
            z-index: 100;
            font-size: 12px;
            line-height: 1.4;
        }
        
        #controls {
            position: absolute;
            bottom: 20px;
            left: 20px;
            color: #00ff88;
            background: rgba(0, 0, 0, 0.7);
            padding: 15px;
            border-radius: 8px;
            border: 1px solid #00ff88;
            backdrop-filter: blur(10px);
            z-index: 100;
        }
        
        .control-group {
            margin: 10px 0;
        }
        
        input[type="range"] {
            width: 150px;
            margin: 0 10px;
        }
        
        label {
            display: inline-block;
            width: 100px;
            font-size: 11px;
        }
    </style>
</head>
<body>
    <div id="container"></div>
    
    <div id="info">
        <div><strong>ψ-origin Fold Center Visualization</strong></div>
        <div>• <span style="color: #ff4444;">Red Core</span>: ψ<sub>origin</sub> fold-center</div>
        <div>• <span style="color: #4488ff;">Blue Trajectories</span>: Ψₙ trajectory field</div>
        <div>• <span style="color: #ffaa00;">Orange Vectors</span>: Ξ torsion field</div>
        <div>• <span style="color: #88ff44;">Green Frame</span>: Canonical binding frame</div>
        <div>• Dynamic curvature-invariance metric</div>
    </div>
    
    <div id="controls">
        <div class="control-group">
            <label>Torsion Ξ:</label>
            <input type="range" id="torsion" min="0.1" max="3.0" step="0.1" value="1.0">
            <span id="torsionValue">1.0</span>
        </div>
        <div class="control-group">
            <label>Field Density:</label>
            <input type="range" id="density" min="50" max="200" step="10" value="100">
            <span id="densityValue">100</span>
        </div>
        <div class="control-group">
            <label>Fold Strength:</label>
            <input type="range" id="fold" min="0.5" max="2.5" step="0.1" value="1.2">
            <span id="foldValue">1.2</span>
        </div>
    </div>

    <script>
        let scene, camera, renderer, foldCenter, trajectoryField, torsionField, canonicalFrame;
        let time = 0;
        let torsionStrength = 1.0;
        let fieldDensity = 100;
        let foldStrength = 1.2;
        
        function init() {
            // Scene setup
            scene = new THREE.Scene();
            camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
            renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
            renderer.setSize(window.innerWidth, window.innerHeight);
            renderer.setClearColor(0x000000, 0);
            document.getElementById('container').appendChild(renderer.domElement);
            
            // Camera position
            camera.position.set(15, 10, 15);
            camera.lookAt(0, 0, 0);
            
            createFoldCenter();
            createTrajectoryField();
            createTorsionField();
            createCanonicalFrame();
            
            setupControls();
            animate();
        }
        
        function createFoldCenter() {
            // Central fold-center ψ_origin
            const geometry = new THREE.SphereGeometry(0.8, 32, 32);
            const material = new THREE.MeshBasicMaterial({
                color: 0xff4444,
                transparent: true,
                opacity: 0.8
            });
            foldCenter = new THREE.Mesh(geometry, material);
            
            // Add pulsing effect
            const pulseGeometry = new THREE.SphereGeometry(1.2, 32, 32);
            const pulseMaterial = new THREE.MeshBasicMaterial({
                color: 0xff4444,
                transparent: true,
                opacity: 0.3,
                wireframe: true
            });
            const pulseCore = new THREE.Mesh(pulseGeometry, pulseMaterial);
            foldCenter.add(pulseCore);
            
            scene.add(foldCenter);
        }
        
        function createTrajectoryField() {
            trajectoryField = new THREE.Group();
            
            // Create Ψₙ trajectory curves
            for (let i = 0; i < fieldDensity; i++) {
                const curve = new THREE.CatmullRomCurve3(generateTrajectoryPoints(i));
                const geometry = new THREE.TubeGeometry(curve, 64, 0.02, 8, false);
                const material = new THREE.MeshBasicMaterial({
                    color: new THREE.Color().setHSL(0.6 + Math.random() * 0.1, 0.8, 0.6),
                    transparent: true,
                    opacity: 0.7
                });
                const trajectory = new THREE.Mesh(geometry, material);
                trajectoryField.add(trajectory);
            }
            
            scene.add(trajectoryField);
        }
        
        function generateTrajectoryPoints(index) {
            const points = [];
            const phi = (index / fieldDensity) * Math.PI * 2;
            const theta = Math.acos(1 - 2 * Math.random());
            
            for (let t = 0; t <= 1; t += 0.1) {
                const r = 2 + t * 8;
                const x = r * Math.sin(theta + t * foldStrength) * Math.cos(phi + t * 0.5);
                const y = r * Math.cos(theta + t * foldStrength) + t * 2;
                const z = r * Math.sin(theta + t * foldStrength) * Math.sin(phi + t * 0.5);
                points.push(new THREE.Vector3(x, y, z));
            }
            
            return points;
        }
        
        function createTorsionField() {
            torsionField = new THREE.Group();
            
            // Create Ξ torsion vectors
            for (let i = 0; i < 50; i++) {
                const phi = Math.random() * Math.PI * 2;
                const theta = Math.acos(1 - 2 * Math.random());
                const r = 3 + Math.random() * 6;
                
                const x = r * Math.sin(theta) * Math.cos(phi);
                const y = r * Math.cos(theta);
                const z = r * Math.sin(theta) * Math.sin(phi);
                
                // Create torsion vector
                const origin = new THREE.Vector3(x, y, z);
                const direction = new THREE.Vector3(
                    Math.sin(phi + Math.PI/2) * torsionStrength,
                    Math.sin(theta) * 0.5,
                    Math.cos(phi + Math.PI/2) * torsionStrength
                ).normalize().multiplyScalar(2);
                
                const arrowHelper = new THREE.ArrowHelper(
                    direction.normalize(),
                    origin,
                    direction.length(),
                    0xffaa00,
                    0.5,
                    0.3
                );
                
                torsionField.add(arrowHelper);
            }
            
            scene.add(torsionField);
        }
        
        function createCanonicalFrame() {
            canonicalFrame = new THREE.Group();
            
            // Create binding frame structure
            const frameGeometry = new THREE.RingGeometry(4, 4.2, 16);
            const frameMaterial = new THREE.MeshBasicMaterial({
                color: 0x88ff44,
                transparent: true,
                opacity: 0.6,
                side: THREE.DoubleSide
            });
            
            // Multiple ring frames at different orientations
            for (let i = 0; i < 3; i++) {
                const frame = new THREE.Mesh(frameGeometry, frameMaterial);
                frame.rotation.x = (i * Math.PI) / 3;
                frame.rotation.y = (i * Math.PI) / 4;
                canonicalFrame.add(frame);
            }
            
            // Add connecting lines
            const lineGeometry = new THREE.BufferGeometry();
            const vertices = [];
            for (let i = 0; i < 16; i++) {
                const angle = (i / 16) * Math.PI * 2;
                vertices.push(
                    4 * Math.cos(angle), 0, 4 * Math.sin(angle),
                    4 * Math.cos(angle + Math.PI), 0, 4 * Math.sin(angle + Math.PI)
                );
            }
            lineGeometry.setAttribute('position', new THREE.Float32BufferAttribute(vertices, 3));
            
            const lineMaterial = new THREE.LineBasicMaterial({
                color: 0x88ff44,
                transparent: true,
                opacity: 0.4
            });
            const lines = new THREE.LineSegments(lineGeometry, lineMaterial);
            canonicalFrame.add(lines);
            
            scene.add(canonicalFrame);
        }
        
        function setupControls() {
            const torsionSlider = document.getElementById('torsion');
            const densitySlider = document.getElementById('density');
            const foldSlider = document.getElementById('fold');
            
            torsionSlider.addEventListener('input', (e) => {
                torsionStrength = parseFloat(e.target.value);
                document.getElementById('torsionValue').textContent = torsionStrength.toFixed(1);
                updateTorsionField();
            });
            
            densitySlider.addEventListener('input', (e) => {
                fieldDensity = parseInt(e.target.value);
                document.getElementById('densityValue').textContent = fieldDensity;
                updateTrajectoryField();
            });
            
            foldSlider.addEventListener('input', (e) => {
                foldStrength = parseFloat(e.target.value);
                document.getElementById('foldValue').textContent = foldStrength.toFixed(1);
                updateTrajectoryField();
            });
        }
        
        function updateTorsionField() {
            scene.remove(torsionField);
            createTorsionField();
        }
        
        function updateTrajectoryField() {
            scene.remove(trajectoryField);
            createTrajectoryField();
        }
        
        function animate() {
            requestAnimationFrame(animate);
            time += 0.01;
            
            // Animate fold center
            if (foldCenter) {
                foldCenter.rotation.y += 0.005;
                foldCenter.children[0].scale.setScalar(1 + 0.1 * Math.sin(time * 2));
            }
            
            // Animate canonical frame
            if (canonicalFrame) {
                canonicalFrame.rotation.x += 0.002;
                canonicalFrame.rotation.z += 0.003;
            }
            
            // Animate torsion field
            if (torsionField) {
                torsionField.children.forEach((arrow, i) => {
                    const phase = time + i * 0.1;
                    arrow.rotation.y = Math.sin(phase) * 0.2;
                    arrow.setLength(2 + 0.5 * Math.sin(phase * 2));
                });
            }
            
            // Camera orbit
            camera.position.x = 15 * Math.cos(time * 0.1);
            camera.position.z = 15 * Math.sin(time * 0.1);
            camera.lookAt(0, 0, 0);
            
            renderer.render(scene, camera);
        }
        
        // Handle window resize
        window.addEventListener('resize', () => {
            camera.aspect = window.innerWidth / window.innerHeight;
            camera.updateProjectionMatrix();
            renderer.setSize(window.innerWidth, window.innerHeight);
        });
        
        init();
    </script>
</body>
</html>
```