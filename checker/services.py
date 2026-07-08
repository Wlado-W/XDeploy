import paramiko
import subprocess

def ping_server(ip):
    try:
        result = subprocess.run(["ping", "-c", "1", ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=5)
        return result.returncode == 0
    except Exception:
        return False
    
def ssh_command(server, command):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=server.ip, port=server.ssh_port, username=ssh_user, password=ssh_password, timeout=10)
        stdin, stdout, stderr = ssh.exec_command(command)
        result = stdout.read().decode().strip()
        ssh.close()
        return result
    except Exception as e:
        return str(e)
    
def check_server(server):
    result = {
        "name": server.name, "ip": server.ip, "ping": False, "ssh": False, "os": "", "xray": "", "xui": False,
    }
    result["ping"] = ping_server(server.ip)
    if result["ping"]:
        os_info = ssh_command(server, "uname -a")
        if "Permission denied" not in os_info:
            result["ssh"] = True
            result["os"] = os_info
            xray = ssh_command(server, "xray version")
            result["xray"] = xray
            xui = ssh_command(server, "systemctl status x-ui")
            if "active" in xui:
                result["xui"] = True
    return result