---
nexus: nexus-ai-chat-importer
plugin_version: "1.3.0"
provider: claude
artifact_id: psi_origin_visualization
version_uuid: 1d16cec1-de93-4bfc-98ac-9954db5ccd54
version_number: 1
command: create
conversation_id: 28f85b7b-5267-4498-9b97-de377ca7caf5
create_time: 2025-06-18T02:28:13.000Z
format: html
aliases: [Origin Fold-Center with Ξ Torsion Field Visualization, psi_origin_visualization_v1]
---

# ψ-Origin Fold-Center with Ξ Torsion Field Visualization (Version 1)

**Conversation:** [[Nexus/Conversations/claude/2025/06/Recursive Energy Conservation Challenge|Recursive Energy Conservation Challenge]]

## Content

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ψ-Origin Fold-Center Visualization</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <style>
        body {
            font-family: 'Segoe UI', Taurus, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 0;
            background: radial-gradient(circle at center, #0a0a0a 0%, #000000 100%);
            color: #fff;
            overflow: hidden;
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
        }
        
        .ui-panel {
            position: absolute;
            top: 20px;
            left: 20px;
            background: rgba(0, 0, 0, 0.8);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.2);
            border-radius: 15px;
            padding: 20px;
            min-width: 300px;
            max-height: 80vh;
            overflow-y: auto;
            z-index: 1000;
        }
        
        .title {
            font-size: 1.5em;
            font-weight: 700;
            margin-bottom: 15px;
            background: linear-gradient(45deg, #ff6b6b, #4ecdc4, #45b7d1);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        
        .control-section {
            margin: 15px 0;
            padding: 15px;
            background: rgba(255, 255, 255, 0.05);
            border-radius: 10px;
            border-left: 3px solid #4ecdc4;
        }
        
        .control-section h3 {
            margin: 0 0 10px 0;
            color: #4ecdc4;
            font-size: 1.1em;
        }
        
        .control-group {
            margin: 10px 0;
        }
        
        .control-group label {
            display: block;
            margin-bottom: 5px;
            font-size: 0.9em;
            color: #ccc;
        }
        
        .control-group input, .control-group select {
            width: 100%;
            padding: 8px;
            border: 1px solid rgba(255, 255, 255, 0.3);
            border-radius: 5px;
            background: rgba(255, 255, 255, 0.1);
            color: #fff;
            font-size: 14px;
        }
        
        .control-group input:focus {
            outline: none;
            border-color: #4ecdc4;
            box-shadow: 0 0 10px rgba(78, 205, 196, 0.3);
        }
        
        button {
            background: linear-gradient(45deg, #ff6b6b, #4ecdc4);
            border: none;
            padding: 10px 20px;
            border-radius: 20px;
            color: white;
            font-size: 14px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            margin: 5px;
            width: calc(50% - 10px);
        }
        
        button:hover {
            transform: scale(1.05);
            box-shadow: 0 5px 15px rgba(78, 205, 196, 0.4);
        }
        
        .legend {
            margin-top: 20px;
            padding: 15px;
            background: rgba(255, 255, 255, 0.05);
            border-radius: 10px;
        }
        
        .legend-item {
            display: flex;
            align-items: center;
            margin: 8px 0;
            font-size: 0.9em;
        }
        
        .legend-color {
            width: 20px;
            height: 20px;
            border-radius: 50%;
            margin-right: 10px;
            border: 2px solid rgba(255, 255, 255, 0.3);
        }
        
        .info-panel {
            position: absolute;
            top: 20px;
            right: 20px;
            background: rgba(0, 0, 0, 0.8);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.2);
            border-radius: 15px;
            padding: 20px;
            width: 250px;
            z-index: 1000;
        }
        
        .metric-display {
            margin: 10px 0;
            padding: 10px;
            background: rgba(78, 205, 196, 0.1);
            border-radius: 8px;
            border-left: 3px solid #4ecdc4;
        }
        
        .metric-label {
            font-size: 0.8em;
            color: #4ecdc4;
            margin-bottom: 5px;
        }
        
        .metric-value {
            font-size: 1.2em;
            font-weight: 700;
            color: #fff;
        }
        
        .instructions {
            position: absolute;
            bottom: 20px;
            left: 20px;
            background: rgba(0, 0, 0, 0.8);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.2);
            border-radius: 10px;
            padding: 15px;
            font-size: 0.9em;
            color: #ccc;
            z-index: 1000;
        }
    </style>
</head>
<body>
    <div id="container">
        <canvas id="canvas"></canvas>
        
        <div class="ui-panel">
            <h1 class="title">ψ-Origin Fold-Center</h1>
            
            <div class="control-section">
                <h3>Fold-Center Parameters</h3>
                <div class="control-group">
                    <label>ψ-Origin Strength</label>
                    <input type="range" id="psiStrength" min="0.1" max="3.0" step="0.1" value="1.5">
                    <span id="psiStrengthValue">1.5</span>
                </div>
                <div class="control-group">
                    <label>Fold Curvature</label>
                    <input type="range" id="foldCurvature" min="0.5" max="5.0" step="0.1" value="2.0">
                    <span id="foldCurvatureValue">2.0</span>
                </div>
            </div>
            
            <div class="control-section">
                <h3>Ψₙ Trajectory System</h3>
                <div class="control-group">
                    <label>Trajectory Count</label>
                    <input type="range" id="trajectoryCount" min="5" max="50" step="5" value="20">
                    <span id="trajectoryCountValue">20</span>
                </div>
                <div class="control-group">
                    <label>Orbital Resonance</label>
                    <input type="range" id="orbitalResonance" min="0.1" max="2.0" step="0.1" value="0.8">
                    <span id="orbitalResonanceValue">0.8</span>
                </div>
            </div>
            
            <div class="control-section">
                <h3>Ξ Torsion Field</h3>
                <div class="control-group">
                    <label>Torsion Intensity</label>
                    <input type="range" id="torsionIntensity" min="0.1" max="3.0" step="0.1" value="1.2">
                    <span id="torsionIntensityValue">1.2</span>
                </div>
                <div class="control-group">
                    <label>Field Density</label>
                    <input type="range" id="fieldDensity" min="5" max="25" step="5" value="15">
                    <span id="fieldDensityValue">15</span>
                </div>
            </div>
            
            <button onclick="resetToDefaults()">Reset</button>
            <button onclick="toggleAnimation()">Pause/Play</button>
            
            <div class="legend">
                <div class="legend-item">
                    <div class="legend-color" style="background: #ff6b6b;"></div>
                    <span>ψ-Origin Core</span>
                </div>
                <div class="legend-item">
                    <div class="legend-color" style="background: #4ecdc4;"></div>
                    <span>Ψₙ Trajectories</span>
                </div>
                <div class="legend-item">
                    <div class="legend-color" style="background: #45b7d1;"></div>
                    <span>Ξ Torsion Vectors</span>
                </div>
                <div class="legend-item">
                    <div class="legend-color" style="background: #ffa726;"></div>
                    <span>Canonical Frame</span>
                </div>
            </div>
        </div>
        
        <div class="info-panel">
            <h3 style="color: #4ecdc4; margin-top: 0;">Live Metrics</h3>
            
            <div class="metric-display">
                <div class="metric-label">Curvature Invariant</div>
                <div class="metric-value" id="curvatureInvariant">0.000</div>
            </div>
            
            <div class="metric-display">
                <div class="metric-label">Torsion Magnitude</div>
                <div class="metric-value" id="torsionMagnitude">0.000</div>
            </div>
            
            <div class="metric-display">
                <div class="metric-label">Binding Energy</div>
                <div class="metric-value" id="bindingEnergy">0.000</div>
            </div>
            
            <div class="metric-display">
                <div class="metric-label">Fold Coherence</div>
                <div class="metric-value" id="foldCoherence">0.000</div>
            </div>
        </div>
        
        <div class="instructions">
            <strong>Controls:</strong><br>
            • Mouse: Rotate view<br>
            • Scroll: Zoom in/out<br>
            • Adjust sliders to modify field parameters<br>
            • Watch metrics update in real-time
        </div>
    </div>

    <script>
        // Global variables
        let scene, camera, renderer, controls;
        let psiOrigin, trajectories = [], torsionField = [], canonicalFrame;
        let animationId;
        let isAnimating = true;
        let time = 0;
        
        // Initialize the visualization
        function init() {
            // Create scene
            scene = new THREE.Scene();
            scene.background = new THREE.Color(0x000000);
            
            // Create camera
            camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
            camera.position.set(15, 10, 15);
            
            // Create renderer
            renderer = new THREE.WebGLRenderer({ canvas: document.getElementById('canvas'), antialias: true });
            renderer.setSize(window.innerWidth, window.innerHeight);
            renderer.setPixelRatio(window.devicePixelRatio);
            
            // Add basic orbit controls
            addMouseControls();
            
            // Create the visualization components
            createPsiOrigin();
            createTrajectories();
            createTorsionField();
            createCanonicalFrame();
            
            // Add lighting
            const ambientLight = new THREE.AmbientLight(0x404040, 0.6);
            scene.add(ambientLight);
            
            const pointLight = new THREE.PointLight(0xffffff, 1, 100);
            pointLight.position.set(10, 10, 10);
            scene.add(pointLight);
            
            // Start animation
            animate();
            
            // Setup event listeners
            setupEventListeners();
        }
        
        function createPsiOrigin() {
            // Create the fold-center as a complex geometric structure
            const geometry = new THREE.SphereGeometry(2, 32, 32);
            
            // Create custom shader material for the ψ-origin
            const material = new THREE.ShaderMaterial({
                uniforms: {
                    time: { value: 0 },
                    strength: { value: 1.5 }
                },
                vertexShader: `
                    varying vec3 vPosition;
                    varying vec3 vNormal;
                    uniform float time;
                    uniform float strength;
                    
                    void main() {
                        vPosition = position;
                        vNormal = normal;
                        
                        // Add fold distortion
                        vec3 pos = position;
                        float fold = sin(pos.x * 2.0 + time) * cos(pos.y * 2.0 + time) * 0.2 * strength;
                        pos += normal * fold;
                        
                        gl_Position = projectionMatrix * modelViewMatrix * vec4(pos, 1.0);
                    }
                `,
                fragmentShader: `
                    varying vec3 vPosition;
                    varying vec3 vNormal;
                    uniform float time;
                    
                    void main() {
                        vec3 color = vec3(1.0, 0.4, 0.4); // Red base
                        
                        // Add pulsing effect
                        float pulse = sin(time * 2.0) * 0.3 + 0.7;
                        color *= pulse;
                        
                        // Add surface variation
                        float surface = sin(vPosition.x * 10.0) * sin(vPosition.y * 10.0) * sin(vPosition.z * 10.0);
                        color += vec3(0.2, 0.6, 0.6) * surface * 0.3;
                        
                        gl_FragColor = vec4(color, 0.8);
                    }
                `,
                transparent: true
            });
            
            psiOrigin = new THREE.Mesh(geometry, material);
            scene.add(psiOrigin);
        }
        
        function createTrajectories() {
            const trajectoryCount = parseInt(document.getElementById('trajectoryCount').value);
            
            // Clear existing trajectories
            trajectories.forEach(traj => scene.remove(traj));
            trajectories = [];
            
            for (let i = 0; i < trajectoryCount; i++) {
                const points = [];
                const radius = 5 + (i / trajectoryCount) * 10;
                const phase = (i / trajectoryCount) * Math.PI * 2;
                const verticalOffset = (i / trajectoryCount - 0.5) * 8;
                
                // Create spiral trajectory
                for (let j = 0; j < 200; j++) {
                    const t = (j / 200) * Math.PI * 4;
                    const x = radius * Math.cos(t + phase);
                    const y = verticalOffset + Math.sin(t * 2) * 2;
                    const z = radius * Math.sin(t + phase);
                    points.push(new THREE.Vector3(x, y, z));
                }
                
                const geometry = new THREE.BufferGeometry().setFromPoints(points);
                const material = new THREE.LineBasicMaterial({ 
                    color: new THREE.Color().setHSL(0.5 + i * 0.1, 0.8, 0.6),
                    transparent: true,
                    opacity: 0.7
                });
                
                const trajectory = new THREE.Line(geometry, material);
                trajectories.push(trajectory);
                scene.add(trajectory);
            }
        }
        
        function createTorsionField() {
            const fieldDensity = parseInt(document.getElementById('fieldDensity').value);
            
            // Clear existing field
            torsionField.forEach(vector => scene.remove(vector));
            torsionField = [];
            
            for (let i = 0; i < fieldDensity; i++) {
                for (let j = 0; j < fieldDensity; j++) {
                    const x = (i - fieldDensity/2) * 2;
                    const z = (j - fieldDensity/2) * 2;
                    const y = Math.sin(x * 0.2) * Math.cos(z * 0.2) * 3;
                    
                    // Create torsion vector
                    const origin = new THREE.Vector3(x, y, z);
                    const direction = new THREE.Vector3(
                        Math.cos(x * 0.1 + z * 0.1),
                        Math.sin(x * 0.1) * Math.cos(z * 0.1),
                        Math.sin(z * 0.1 + x * 0.1)
                    ).normalize().multiplyScalar(1.5);
                    
                    const geometry = new THREE.BufferGeometry().setFromPoints([
                        origin, 
                        origin.clone().add(direction)
                    ]);
                    
                    const material = new THREE.LineBasicMaterial({ 
                        color: 0x45b7d1,
                        transparent: true,
                        opacity: 0.6
                    });
                    
                    const vector = new THREE.Line(geometry, material);
                    torsionField.push(vector);
                    scene.add(vector);
                    
                    // Add arrowhead
                    const arrowGeometry = new THREE.ConeGeometry(0.1, 0.3, 8);
                    const arrowMaterial = new THREE.MeshBasicMaterial({ color: 0x45b7d1 });
                    const arrow = new THREE.Mesh(arrowGeometry, arrowMaterial);
                    
                    const endPoint = origin.clone().add(direction);
                    arrow.position.copy(endPoint);
                    arrow.lookAt(endPoint.clone().add(direction));
                    
                    torsionField.push(arrow);
                    scene.add(arrow);
                }
            }
        }
        
        function createCanonicalFrame() {
            // Create the canonical binding frame as a geometric structure
            const frameGeometry = new THREE.BoxGeometry(20, 0.1, 20);
            const frameMaterial = new THREE.MeshBasicMaterial({ 
                color: 0xffa726, 
                transparent: true, 
                opacity: 0.3,
                wireframe: true
            });
            
            canonicalFrame = new THREE.Mesh(frameGeometry, frameMaterial);
            scene.add(canonicalFrame);
            
            // Add frame axes
            const axesHelper = new THREE.AxesHelper(15);
            axesHelper.material.transparent = true;
            axesHelper.material.opacity = 0.5;
            scene.add(axesHelper);
        }
        
        function addMouseControls() {
            let isDragging = false;
            let previousMousePosition = { x: 0, y: 0 };
            
            document.addEventListener('mousedown', (event) => {
                isDragging = true;
                previousMousePosition = { x: event.clientX, y: event.clientY };
            });
            
            document.addEventListener('mousemove', (event) => {
                if (isDragging) {
                    const deltaMove = {
                        x: event.clientX - previousMousePosition.x,
                        y: event.clientY - previousMousePosition.y
                    };
                    
                    const rotationSpeed = 0.01;
                    
                    // Rotate camera around origin
                    const spherical = new THREE.Spherical();
                    spherical.setFromVector3(camera.position);
                    spherical.theta -= deltaMove.x * rotationSpeed;
                    spherical.phi += deltaMove.y * rotationSpeed;
                    spherical.phi = Math.max(0.1, Math.min(Math.PI - 0.1, spherical.phi));
                    
                    camera.position.setFromSpherical(spherical);
                    camera.lookAt(0, 0, 0);
                    
                    previousMousePosition = { x: event.clientX, y: event.clientY };
                }
            });
            
            document.addEventListener('mouseup', () => {
                isDragging = false;
            });
            
            document.addEventListener('wheel', (event) => {
                const zoomSpeed = 0.1;
                const distance = camera.position.length();
                const newDistance = distance + (event.deltaY > 0 ? zoomSpeed : -zoomSpeed) * distance * 0.1;
                
                if (newDistance > 5 && newDistance < 100) {
                    camera.position.multiplyScalar(newDistance / distance);
                }
            });
        }
        
        function animate() {
            if (isAnimating) {
                time += 0.016; // ~60fps
                
                // Update ψ-origin
                if (psiOrigin && psiOrigin.material.uniforms) {
                    psiOrigin.material.uniforms.time.value = time;
                    psiOrigin.material.uniforms.strength.value = parseFloat(document.getElementById('psiStrength').value);
                }
                
                // Rotate trajectories
                trajectories.forEach((traj, i) => {
                    const resonance = parseFloat(document.getElementById('orbitalResonance').value);
                    traj.rotation.y = time * resonance * (0.5 + i * 0.1);
                });
                
                // Animate torsion field
                const torsionIntensity = parseFloat(document.getElementById('torsionIntensity').value);
                torsionField.forEach((vector, i) => {
                    if (vector.material && vector.material.opacity !== undefined) {
                        vector.material.opacity = 0.3 + 0.3 * Math.sin(time * 2 + i * 0.1) * torsionIntensity;
                    }
                });
                
                // Update metrics
                updateMetrics();
            }
            
            renderer.render(scene, camera);
            animationId = requestAnimationFrame(animate);
        }
        
        function updateMetrics() {
            const psiStrength = parseFloat(document.getElementById('psiStrength').value);
            const foldCurvature = parseFloat(document.getElementById('foldCurvature').value);
            const torsionIntensity = parseFloat(document.getElementById('torsionIntensity').value);
            const resonance = parseFloat(document.getElementById('orbitalResonance').value);
            
            // Calculate derived metrics
            const curvatureInvariant = Math.abs(Math.sin(time * 0.5) * foldCurvature + psiStrength);
            const torsionMagnitude = torsionIntensity * (1 + 0.3 * Math.cos(time));
            const bindingEnergy = psiStrength * resonance * Math.abs(Math.sin(time * 0.3));
            const foldCoherence = Math.abs(Math.cos(time * 0.2) * foldCurvature / (psiStrength + 0.1));
            
            document.getElementById('curvatureInvariant').textContent = curvatureInvariant.toFixed(3);
            document.getElementById('torsionMagnitude').textContent = torsionMagnitude.toFixed(3);
            document.getElementById('bindingEnergy').textContent = bindingEnergy.toFixed(3);
            document.getElementById('foldCoherence').textContent = foldCoherence.toFixed(3);
        }
        
        function setupEventListeners() {
            // Update display values
            document.getElementById('psiStrength').addEventListener('input', (e) => {
                document.getElementById('psiStrengthValue').textContent = e.target.value;
            });
            
            document.getElementById('foldCurvature').addEventListener('input', (e) => {
                document.getElementById('foldCurvatureValue').textContent = e.target.value;
            });
            
            document.getElementById('trajectoryCount').addEventListener('input', (e) => {
                document.getElementById('trajectoryCountValue').textContent = e.target.value;
                createTrajectories();
            });
            
            document.getElementById('orbitalResonance').addEventListener('input', (e) => {
                document.getElementById('orbitalResonanceValue').textContent = e.target.value;
            });
            
            document.getElementById('torsionIntensity').addEventListener('input', (e) => {
                document.getElementById('torsionIntensityValue').textContent = e.target.value;
            });
            
            document.getElementById('fieldDensity').addEventListener('input', (e) => {
                document.getElementById('fieldDensityValue').textContent = e.target.value;
                createTorsionField();
            });
            
            // Window resize
            window.addEventListener('resize', () => {
                camera.aspect = window.innerWidth / window.innerHeight;
                camera.updateProjectionMatrix();
                renderer.setSize(window.innerWidth, window.innerHeight);
            });
        }
        
        function resetToDefaults() {
            document.getElementById('psiStrength').value = '1.5';
            document.getElementById('foldCurvature').value = '2.0';
            document.getElementById('trajectoryCount').value = '20';
            document.getElementById('orbitalResonance').value = '0.8';
            document.getElementById('torsionIntensity').value = '1.2';
            document.getElementById('fieldDensity').value = '15';
            
            // Update display values
            document.getElementById('psiStrengthValue').textContent = '1.5';
            document.getElementById('foldCurvatureValue').textContent = '2.0';
            document.getElementById('trajectoryCountValue').textContent = '20';
            document.getElementById('orbitalResonanceValue').textContent = '0.8';
            document.getElementById('torsionIntensityValue').textContent = '1.2';
            document.getElementById('fieldDensityValue').textContent = '15';
            
            createTrajectories();
            createTorsionField();
        }
        
        function toggleAnimation() {
            isAnimating = !isAnimating;
        }
        
        // Initialize when page loads
        window.addEventListener('load', init);
    </script>
</body>
</html>
```