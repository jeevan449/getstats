"""

loadstats:api
~~~~~~~~~~~~
This module implements getting system & process stats.
:license: Apache2, see LICENSE for more details.

"""


import sys
import argparse
import subprocess
import threading
import time
import datetime


"""
####  This file is used to get total CPU,MEM, IO(wa) stats and individual
process

"""


class getstats():
    def __init__(self, comm=None,**jee):
        if comm:
            if comm.filename:
                self.filename = comm.filename
            else:
                now = datetime.datetime.now()
                self.filename = "stats_"+now.strftime("%Y-%m-%d_%H-%M-%S")+"_.csv"
                self.duration = comm.dur
                self.rate = comm.rate
                self.pids = comm.pid
                self.pnames = comm.pnames
                if self.pnames:
                    self.pnames1 = self.pnames.split(',')
                    self.plist = []
        else:
            if 'dur' in jee:
                self.duration = jee['dur']
            if 'filename' in jee:
                self.filename = jee['filename']
            else:
                now = datetime.datetime.now()
                self.filename = "stats_"+now.strftime("%Y-%m-%d_%H-%M-%S")+"_.csv"
            if 'rate' in jee:
                self.rate = jee['rate']
            else:
                self.rate = 1
            if 'pid' in jee:
                self.pids = jee['pid']
            if 'pnames' in jee:
                self.pnames = jee['pnames']
                self.pnames1 = self.pnames.split(',')
            else:
                self.pnames = None
            self.initalize_csvnames()
            print(self.duration)
            print(self.rate)

    def get_usage(self):
        mem = '''vmstat -s | grep 'used memory' | cut -b 1-15'''
        cpu = "top -bn1 | grep \"Cpu(s)\" | sed \"s/.*, *\([0-9.]*\)%* id.*/\\1/\" | awk '{print 100 - $1\"%\"}'"
        io_wa = "top -b -n 1 | grep 'Cpu(s)' | cut -b 45-52"
        comm_list = [mem, cpu, io_wa]
        if self.pnames:
            commands = self.get_commands(self.pnames)
            for i in range(len(commands)):
                comm_list.append(commands[i])
            return self.run_command(comm_list)
        else:
            return self.run_command(mem, cpu, io_wa)

    def get_commands(self, *comm):
        com_lst = []
        for i in range(len(self.pnames1)):
            command = "top -b -n 1 -p $(pgrep " + \
                self.pnames1[i]+") |  tail -1 | head -1 | cut -b 48-58"
            com_lst.append(command)
        return com_lst

    def run_stats(self):
        print(' Running..........')
        # if self.pids:
        #    self.pids1 = self.pids.split('.')
        # if self.pnames:
        #    self.pnames1 = self.pnames.split(',')
        if not self.rate:
            self.rate = 1
        run_dur = int(int(self.duration)/int(self.rate))

        for i in range(run_dur):
            self.get_usage()
            time.sleep(int(self.rate))
        print('***** Completed capturing the STATS ***** ')

        for i in range(len(self.filename)+10):
            sys.stdout.write('#')
        print('')
        print('#    {}    #'.format(self.filename))
        for i in range(len(self.filename)+10):
            sys.stdout.write('#')
        print('\n')


        sys.stdout.flush()
        return self.filename






    def get_pid(self):
        pass

    def get_pname(self):
        pass

    def get_current_time(self):
        now = datetime.datetime.now()
        return now.strftime("%Y-%m-%d_%H-%M-%S")

    def initalize_csvnames(self):
        file = open(self.filename, "a")
        header = "DateTime, CPU_Used(%), MEM_Used(KB), I/O \n"
        file.write(header)
        file.close()

    def store_output(self, *value):
        pass

    def run_command(self, *command):
        global test
        global lst
        global count
        global str1
        count = 1
        test = []
        lst = []
        if len(command) == 1:
            com1 = command[0]
        else:
            com1 = command

        def store_csv(value):
            str3 = ''
            for i in range(len(value)):
                str2 = str(value[i])+","
                str3 = str3 + str2

            file = open(self.filename, "a")
            file.write(self.get_current_time()+","+str3+"\n")
            file.close()

        def result(value, i):
            j = 0
            if (i > 2):
                for j in range(2):
                    lst.append(value[j])
                j = i-2
            else:
                lst.append(value[0])
            if len(com1) == (len(lst)-j):
                store_csv(lst)
                del lst[:]

        def executec(comm, i):
            process = subprocess.Popen(
                comm, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            output, error = process.communicate()
            rout = output.split()
            result(rout, i)
        if (len(command) < 3):
            comm1 = command[0]
            for i in range(len(comm1)):
                executec(comm1[i], i)
            return lst
        else:
            for i in range(len(command)):
                # th = threading.Thread(target=executec,args=(command[i],test,))
                # th.start()
                executec(command[i], i)
            return lst


def get_parser():
    try:
        par = argparse.ArgumentParser()
        par.add_argument('-pn', action='store',
                dest='pnames', help='process names ex: -p mysql,java')
        par.add_argument('-f', action='store', dest='filename',
                         help='File name for storing stats.Default file will be generated with current date time if filename not provided')
        par.add_argument('-d', action='store',
                         dest='dur', help='Test duration')
        par.add_argument('-r', action='store', dest='rate',
                         help='Stats frequency')
        par.add_argument('-p', action='store', dest='pid',
                help='Process IDs ex: -p 1234,1111')
        results = par.parse_args()
        if len(sys.argv) < 2:
            par.print_help()
            par.exit()
            sys.exit(1)
        print(results,type(results))
        return results
    except Exception as e:
        print(e)


def main():
    #start_time = time.time()
    arg = get_parser()
    stat_obj = getstats(arg)
    stat_obj.initalize_csvnames()
    stat_obj.run_stats()
    #print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == '__main__':
    main()
