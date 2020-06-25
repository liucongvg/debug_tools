import re
import sys


def main():
    if len(sys.argv) != 2:
        print("extrace_strace.py input_file")
        return
    input_file = sys.argv[1]
    print(input_file)
    fd_in = open(input_file,encoding="ISO-8859-1")
    pid_reg = '\[pid  (\d+?)\].*PR_SET_NAME'
    print(pid_reg)
    partern = re.compile(pid_reg)
    line = fd_in.readline()
    pids = list()
    while line:
        match = partern.match(line)
        if match:
            #print(line,end='')
            pid = match.group(1)
            if pid not in pids:
                #print(pid)
                pids.append(pid)
        line = fd_in.readline()
    fd_in.close()
    print(pids)


if __name__ == '__main__':
    main()
