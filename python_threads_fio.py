'''
# yum install -y python3

 nohup python3 -u Fio-Threads.py > nohup.log &

'''
# Must use Python 3.6 or above
# yum install centos-release-scl
# yum install rh-python36
# scl enable rh-python36 bash
# python --version



import threading 
import subprocess
import time
import os
import math
import re

 
dut_port1='/dev/sdi'
dut_port2='/dev/sdq'
 

FIO_4k = 'fio --filename=' + dut_port1 +' --name=RandomperformancetestPort1  --blocksize=4k --iodepth=8 --rw=rw --numjobs=1 --ioengine=libaio --nice=-19 --prio=0 --prioclass=1 --rwmixread=100 --time_based --runtime=60 --direct=1 --norandommap --randrepeat=0 --ramp_time=10 --log_avg_msec=1000 --write_iops_log=TC7.RandomperformancetestDualPort.NumPorts_1.Port_1.Testsize_4k.QD_8.NW_1.Read_0.RT_60.iops.log --group_reporting --output-format=json --random_generator=tausworthe64 --output=TC_7.RandomperformancetestDualPort.NumPorts_1.Port_1.Testsize_4k.QD_8.NW_1.Read_0.RT_60.output'

FIO_512 = 'fio --filename=' + dut_port2 +' --name=RandomperformancetestPort1  --blocksize=512 --iodepth=1 --rw=rw --numjobs=1 --ioengine=libaio --nice=-19 --prio=0 --prioclass=1 --rwmixread=100 --time_based --runtime=60 --direct=1 --norandommap --randrepeat=0 --ramp_time=10 --log_avg_msec=1000 --write_iops_log=TC7.RandomperformancetestDualPort.NumPorts_1.Port_1.Testsize_512.QD_1.NW_1.Read_0.RT_60.iops.log --group_reporting --output-format=json --random_generator=tausworthe64 --output=TC_7.RandomperformancetestDualPort.NumPorts_1.Port_1.Testsize_512.QD_1.NW_1.Read_0.RT_60.output'
  
def send_fio1(num): 	
	print(FIO_4k)
	p1=subprocess.Popen(FIO_4k, stdout=subprocess.PIPE, encoding='utf-8', shell=True)
	(output, err) = p1.communicate()
	p_status = p1.wait()
	#print(output)
  
def send_fio2(num): 	
	print(FIO_512)
	p1=subprocess.Popen(FIO_512, stdout=subprocess.PIPE, encoding='utf-8', shell=True)
	(output, err) = p1.communicate()
	p_status = p1.wait()
	#print(output)
  
if __name__ == "__main__": 
    # creating thread 
    t1 = threading.Thread(target=send_fio1, args=(10,)) 
    t2 = threading.Thread(target=send_fio2, args=(10,)) 
  
    # starting thread 1 
    t1.start() 
    # starting thread 2 
    t2.start() 
  
    # wait until thread 1 is completely executed 
    t1.join() 
    # wait until thread 2 is completely executed 
    t2.join() 
  
    # both threads completely executed 
    print("Done!") 
