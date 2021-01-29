const {app, BrowserWindow} = require('electron');

function createWindow () {
    window = new BrowserWindow({width: 800, height: 600, fullscreen: false})
    window.loadFile('index.html')
  }

app.on('ready', createWindow)

app.on('window-all-closed', () => {
    // On macOS it is common for applications and their menu bar
    // to stay active until the user quits explicitly with Cmd + Q
    if (process.platform !== 'darwin') {
      app.quit()
    }
  })

const path = require("path")
const url = require("url")
  
let mainWindow
  
function createWindow () {
  mainWindow = new BrowserWindow({width: 800, height: 600})
  
  mainWindow.loadURL(url.format({
    pathname: path.join(__dirname, "index.html"),
    protocol: "file:",
    slashes: true
    
  }))
}