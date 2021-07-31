import sys
def dig(host):
    """
    Returns True if host responds to a ping request
    """
    import subprocess, platform
    args = "dig" + " " + host
    need_sh = False if  platform.system().lower()=="windows" else True

    return subprocess.call(args, shell=need_sh) == 0
    
dig(sys.argv[1])
