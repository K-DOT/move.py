#!/usr/bin/python
import os
import sys
import random
import shutil

def movefiles(logdir, verbose):
     for (curdir, subdirs, files) in os.walk(logdir): 
        for file_ in files:
             if file_.endswith('.gz'):
                 fullpath = os.path.join(curdir, file_)
                 newdirpath = os.path.join(curdir, file_.split('-')[0]+'_old', file_)
                 if verbose: print('Moving "%s" to "%s"' % (fullpath, newdirpath))  
                 os.renames(fullpath, newdirpath)

def test():
    basedir = 'logdir'
    nodes = 5
    fakelogs = 50
    for node in range(nodes):
        path = os.path.join(basedir, 'node%s' % node)
        try:
            os.makedirs(path)
        except FileExistsError:
            shutil.rmtree(basedir)
            os.makedirs(path)
        for logcount in range(fakelogs):
            filepath = os.path.join(path, random.choice(['application', 'auth', 'security', 'user', 'kern'])\
            +'-20140429%s%s' % (logcount, random.choice(['.log', '.log.gz']))) 
            with open(filepath, 'w'): pass
    #movefiles(basedir, verbose=True)
    print('Done. See the results.')
    exit(0)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: move.py dir')
        exit(1)
    elif len(sys.argv) == 3:
        if sys.argv[2] == '-t' or sys.argv[2] == '--test':
            test()
        elif sys.argv[2] == '-v' or sys.argv[2] == '--verbose':
            verbose = True
    else:
        verbose = False	

    LOGDIR = sys.argv[1]

    if not os.path.isdir(LOGDIR): print('Error: Directory does not exist!\nExiting...')

    movefiles(LOGDIR, verbose=verbose)

