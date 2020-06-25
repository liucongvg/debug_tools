import os
import re
libbacktrace = '~/marshmallow/out/target/product/x86/symbols/system/lib/libbacktrace.so'
libunwind = '~/marshmallow/out/target/product/x86/symbols/system/lib/libunwind.so'
libutils = '~/marshmallow/out/target/product/x86/symbols/system/lib/libutils.so'
libc = '~/marshmallow/out/target/product/x86/symbols/system/lib/libc.so'
libdvm = '~/kitkat/out/target/product/x86/symbols/system/lib/libdvm.so'
libmedia = '~/kitkat/out/target/product/x86/symbols/system/lib/libmedia.so'


def main():
    command = 'adb shell ps | grep com.liucong.video'
    command_output = os.popen(command).read()
    #print(command_output)
    match = re.match('^\w+? +?(\d+)',command_output)
    pid = match.group(1)
    #print(pid)
    #return
    ### libbacktrace
    #command = 'adb shell cat /proc/'+pid+'/maps | grep -E "(libbacktrace\.so)"'
    #command_output = os.popen(command).read()
    #base_addr = '0x'+re.match('^(\w*?)-',command_output).group(1)
    #print('base_addr:'+base_addr)
    #command = 'readelf -S '+libbacktrace+' | grep .text'
    #command_output = os.popen(command).read()
    #offset = '0x'+re.match('.*PROGBITS.*?(\w+) ',command_output).group(1)
    #print('offset:'+offset)
    #final_addr = hex(int(base_addr,16)+int(offset,16))
    #print('add-symbol-file '+libbacktrace +' '+final_addr)
    ### libunwind
    #command = 'adb shell cat /proc/'+pid+'/maps | grep -E "(libunwind\.so)"'
    #command_output = os.popen(command).read()
    #base_addr = '0x'+re.match('^(\w*?)-',command_output).group(1)
    #print('base_addr:'+base_addr)
    #command = 'readelf -S '+libunwind+' | grep .text'
    #command_output = os.popen(command).read()
    #offset = '0x'+re.match('.*PROGBITS.*?(\w+) ',command_output).group(1)
    #print('offset:'+offset)
    #final_addr = hex(int(base_addr,16)+int(offset,16))
    #print('add-symbol-file '+libunwind +' '+final_addr)
    #### libutils
    #command = 'adb shell cat /proc/'+pid+'/maps | grep -E "(libutils\.so)"'
    #command_output = os.popen(command).read()
    #base_addr = '0x'+re.match('^(\w*?)-',command_output).group(1)
    ##print('base_addr:'+base_addr)
    #command = 'readelf -S '+libutils+' | grep .text'
    #command_output = os.popen(command).read()
    #offset = '0x'+re.match('.*PROGBITS.*?(\w+) ',command_output).group(1)
    ##print('offset:'+offset)
    #final_addr = hex(int(base_addr,16)+int(offset,16))
    #print('add-symbol-file '+libutils +' '+final_addr)


    ### libdvm
    command = 'adb shell cat /proc/'+pid+'/maps | grep -E "(libmedia\.so)"'
    command_output = os.popen(command).read()
    base_addr = '0x'+re.match('^(\w*?)-',command_output).group(1)
    print('base_addr:'+base_addr)
    command = 'readelf -S '+libmedia+' | grep .text'
    command_output = os.popen(command).read()
    offset = '0x'+re.match('.*PROGBITS.*?(\w+) ',command_output).group(1)
    print('offset:'+offset)
    final_addr = hex(int(base_addr,16)+int(offset,16))
    print('add-symbol-file '+libmedia +' '+final_addr)

if __name__ == '__main__':
    main()