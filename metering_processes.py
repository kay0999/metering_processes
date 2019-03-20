# -*- coding: utf-8 -*-

import os
import time
import ConfigParser

s1 = 'nohup '
s2 = ' > '
s3 = ' 2>&1 &'

def fun(s):
    r = os.popen('ps aux | grep %s'%s).read()
    return r

def fun_main():

    cp = ConfigParser.ConfigParser()

    cp.read('metering_processes.conf')

    sts = cp.sections()

    for st in sts:
        command = cp.get(st, 'command')
        execute_file = cp.get(st, 'execute_file')
        log_file = cp.get(st, 'log_file')

        r = fun(execute_file)

        r_vice = command + ' ' + execute_file

        s = s1 + r_vice + s2 +log_file + s3

        if r_vice not in r:
            os.system(s)
            #print 'r: ', r
            #print 'r_vice: ', r_vice
            #print 's: ', s

if __name__ == '__main__':
    while 1:
        fun_main()
        time.sleep(300)
