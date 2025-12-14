from fastapi import FastAPI, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from libs.system_info import get_system_info
from libs.port_utils import runPort
from libs.wifi_utils import connect_to_network, scan_networks

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def root():
    return FileResponse("static/index.html")

@app.get("/api/system")
async def systemInfo():
    info = get_system_info()
    return info

@app.post("/api/run-port")
async def openPort(
    port: str = Form(...),
    loc: str = Form(...)
):
    server = runPort(port, loc)
    return server

@app.get("/api/wifi/scan")
async def scanWifi():
    networks = scan_networks()
    return networks

@app.post("/api/wifi/connect")
async def connectWifi(
    ssid: str = Form(...),
    pswd: str = Form(...)
):
    connect = connect_to_network(ssid, pswd)
    return connect
