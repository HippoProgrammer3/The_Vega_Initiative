// main.js

const app = new PIXI.Application({ width: 800, height: 600, backgroundColor: 0xCCCCCC });
document.body.appendChild(app.view);

// Define tile size (in pixels)
const tileSize = 32;
let buildingWidth = 2; // in tiles
let buildingHeight = 2; // in tiles

// Create a container for the tile grid
const tileContainer = new PIXI.Container();
app.stage.addChild(tileContainer);

// (Optional) Create a container for placement overlay
const overlayContainer = new PIXI.Container();
app.stage.addChild(overlayContainer);

// Function to draw the tile map grid.
// In a real game you might load tile graphics; here we draw simple rectangles.
function drawTileMap(tileMap, cols, rows) {
    tileContainer.removeChildren();
    for (let y = 0; y < rows; y++) {
        for (let x = 0; x < cols; x++) {
            let tile = new PIXI.Graphics();
            tile.lineStyle(1, 0x000000);
            // Fill color based on tile type (only "empty" or not for this example)
            if (tileMap[y][x] === "empty") {
                tile.beginFill(0xAAAAAA);
            } else {
                tile.beginFill(0x555555);
            }
            tile.drawRect(x * tileSize, y * tileSize, tileSize, tileSize);
            tile.endFill();
            tileContainer.addChild(tile);
        }
    }
}

// Load game state from Python using pyodide (assumes game.py has run and tile_map is available)
async function loadGameState() {
    // Get the world dimensions from Python:
    let state = await pyodide.runPythonAsync("get_game_state()");
    let worldWidth = state.world_width;
    let worldHeight = state.world_height;
    // Convert Python list to JavaScript array:
    let tileMap = state.tile_map;
    drawTileMap(tileMap, worldWidth, worldHeight);
}
loadGameState();

// Create an overlay graphic for placement preview.
const placementOverlay = new PIXI.Graphics();
overlayContainer.addChild(placementOverlay);

// Listen for mouse movement on the canvas
app.view.addEventListener("mousemove", async (event) => {
    // Get canvas position and scale (assuming no CSS scaling for simplicity)
    const rect = app.view.getBoundingClientRect();
    const mouseX = event.clientX - rect.left;
    const mouseY = event.clientY - rect.top;
    
    // Calculate the tile coordinates based on mouse position
    const tileX = Math.floor(mouseX / tileSize);
    const tileY = Math.floor(mouseY / tileSize);
    
    // Call the Python function to check placement validity.
    // We pass tileX, tileY, and the building dimensions.
    let valid = await pyodide.runPythonAsync(
      `can_place_building(${tileX}, ${tileY}, ${buildingWidth}, ${buildingHeight})`
    );
    
    // Clear previous overlay graphics.
    placementOverlay.clear();
    
    // Set the overlay color based on the result.
    let color = valid ? 0x00FF00 : 0xFF0000;
    placementOverlay.beginFill(color, 0.5);
    placementOverlay.drawRect(tileX * tileSize, tileY * tileSize, buildingWidth * tileSize, buildingHeight * tileSize);
    placementOverlay.endFill();
});

// Listen for clicks to place the building.
app.view.addEventListener("click", async (event) => {
    const rect = app.view.getBoundingClientRect();
    const mouseX = event.clientX - rect.left;
    const mouseY = event.clientY - rect.top;
    const tileX = Math.floor(mouseX / tileSize);
    const tileY = Math.floor(mouseY / tileSize);
    
    // Attempt to place the building via Python
    let result = await pyodide.runPythonAsync(
      `place_building(${tileX}, ${tileY}, ${buildingWidth}, ${buildingHeight}, "generic")`
    );
    console.log(result);
    
    // After placement, refresh the tile map display.
    loadGameState();
});
