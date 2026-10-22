# First Scene

## Creation of the Project

### Project Setup

Open a terminal inside first-scene and run:

``` bash
npm init -y
npm install three
npm install -D vite
```

- *** npm init -y ***: Initializes a Node.js project and creates package.json with default settings.

- *** npm install three ***: Installs Three.js as a runtime dependency for creating and rendering 3D graphics.

- *** npm install -D vite ***: Installs Vite as a development dependency to provide a local server and build the application.

### Project Structure

index.html: Entry HTML file that loads the application.

src/main.js: Main JavaScript file where we initialize and manage the Three.js scene.

### Development Script

Add to package.json:

```json
"scripts": {
  "dev": "vite"
}
```

- *** "dev": "vite" ***: Defines a command to start Vite's development server.

Run the application:

``` bash
npm run dev
```

- *** npm run dev ***: Executes the dev script defined in package.json, starting the local development server.

