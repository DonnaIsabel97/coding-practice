import * as THREE from 'three';

// Creating the scene
const scene = new THREE.Scene();

// Setting up the camera
const camera = new THREE.PerspectiveCamera(
    75,
    window.innerWidth / window.innerHeight,
    0.1,
    1000
);

camera.position.z = 5;

// Creating the render
const renderer = new THREE.WebGLRenderer();

renderer.setSize(
    window.innerWidth,
    window.innerHeight
);

document.body.appendChild(renderer.domElement);

// Creating the Mesh
const geometry = new THREE.BoxGeometry(1,1,1);

const material = new THREE.MeshBasicMaterial(
    {color: 0x8b5cf6}
);

const cube = new THREE.Mesh(geometry, material);

scene.add(cube);

``` To see how the cube can rotate: 
cube.rotation.x = 0.5;
cube.rotation.y = 0.5;
```

renderer.render(scene, camera);

