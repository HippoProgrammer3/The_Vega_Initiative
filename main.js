const app = new PIXI.Application({ width: 800, height: 600 });
document.body.appendChild(app.view);

// Example: Draw a simple rectangle (house)
let house = new PIXI.Graphics();
house.beginFill(0x66ccff);
house.drawRect(100, 100, 50, 50);
house.endFill();
app.stage.addChild(house);
