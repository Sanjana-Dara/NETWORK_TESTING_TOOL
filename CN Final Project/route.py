
def ifconfig():
    """
    Returns True if host responds to a ping request
    """
    import subprocess, platform
    args = "route " 
    need_sh = False if  platform.system().lower()=="windows" else True

    return subprocess.call(args, shell=need_sh) == 0
    
ifconfig()
