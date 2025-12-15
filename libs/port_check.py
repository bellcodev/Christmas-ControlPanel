import subprocess

def portCheck(address, port):
    result = subprocess.run(['powershell.exe', '-ExecutionPolicy', 'ByPass', '-File','.\libs\powershell\port_check.ps1', address, port], capture_output=True, text=True, check=True)
    return result.stdout
