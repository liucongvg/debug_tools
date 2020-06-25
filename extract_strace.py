import re
import sys


def main():
    if len(sys.argv) != 4:
        print("extrace_strace.py input_file pid output_file")
        return
    input_file = sys.argv[1]
    pid = sys.argv[2]
    output_file = sys.argv[3]
    print(input_file)
    print(pid)
    print(output_file)
    fd_in = open(input_file)
    fd_out = open(output_file, 'w')
    pid_reg = '\[pid  ' + pid + '\]'
    head_reg = '\[pid  \d+?\]'
    print(pid_reg)
    partern_pid = re.compile(pid_reg)
    partern_head = re.compile(head_reg)
    recheck = False
    line = fd_in.readline()
    while line:
        #print(line)
        if recheck:
            match = partern_head.match(line)
            if not match:
                fd_out.write(line)
                line = fd_in.readline()
                continue
            else:
                recheck = False
        match = partern_pid.match(line)
        if match:
            recheck = True
            fd_out.write(line)
            #print(line,end='')
        line = fd_in.readline()
    fd_in.close()
    fd_out.close()


if __name__ == '__main__':
    main()
