import sys
def ping(host,count):
    """
    Returns True if host responds to a ping request
    """
    import subprocess, platform

    ping_str = "-n "+count if  platform.system().lower()=="windows" else "-c "+count
    args = "ping " + " " + ping_str + " " + host
    need_sh = False if  platform.system().lower()=="windows" else True
    return subprocess.call(args, shell=need_sh) == 0

ping(sys.argv[1], sys.argv[2])


