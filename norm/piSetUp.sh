#! /usr/bin/env bash
#clear file allVec.txt
echo > allVec.txt

python MakeShell.py




#Copy shell to all pis
while read line
do
echo $line
scp shell.txt pi@$line:~/Documents/norm/ 
done <hosts.txt


mpirun -hostfile hosts.txt python FindMaxMin.py





#Collect all vec files
#while read line
#do
#echo $line
#scp -r pi@$line:/home/pi/Documents/norm/output/* /home/pi/Documents/norm/output/
#done <hosts.txt

#mv net.txt output/

#cat output/* >> allVec.txt
 
#clear
#cat allVec.txt
