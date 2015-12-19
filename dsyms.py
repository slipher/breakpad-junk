symdir = "xxxxxxxxxxx" 
dumpsyms_path = "xxxxxxxxxxx"
#!/usr/bin/python


import sys
if len(sys.argv) != 2:
    print "dsyms <binary>: dump symbols of <binary> to", symdir
    exit(1)
import os.path
t = sys.argv[-1]
if not os.path.isfile(t):
    print "File doesn't exist:", t
    exit(1)
t = os.path.abspath(t)
tname = os.path.basename(t)


import subprocess, atexit
proc = subprocess.Popen((dumpsyms_path, t), stdin=open(os.devnull), stdout=subprocess.PIPE)
atexit.register(proc.terminate)
out = None
for ln in proc.stdout:
    if ln.startswith('MODULE'):
        if out: out.close()
        spl = ln.split()
        xid = spl[3]
        xnam = spl[4]
        if xid.strip('0') == '':
            print 'Binary lacks build id'
            exit(1)
        outp = '%s/%s/%s/%s.sym' % (symdir, tname, xid, xnam)
        if os.path.isfile(outp):
            print outp, 'already exists'
            exit(1)
        opdn = os.path.dirname(outp)
        if not os.path.exists(opdn):
            os.makedirs(opdn)
        print 'Writing:', outp
        out = open(outp, 'w')
    out.write(ln)
        