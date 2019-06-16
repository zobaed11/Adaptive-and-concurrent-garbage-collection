#!/bin/bash  
allgcs=("UseParallelGC" "UseConcMarkSweepGC" "UseG1GC" "UseParNewGC" "UseSerialGC")
#param1=("Xmx16m" "Xmx32m" "Xmx48m" "Xmx64m" "Xmx96m" "Xmx128m" "Xmx160m" "Xmx192m" "Xmx224m" "Xmx256m" "Xmx512m")
#param2=("Xms16m" "Xms32m" "Xms48m" "Xms64m" "Xms96m" "Xms128m" "Xms160m" "Xms192m" "Xms224m" "Xms256m" "Xms512m")
#param3=("Xmn16m" "Xmn32m" "Xmn48m" "Xmn64m" "Xmn96m" "Xmn128m" "Xmn160m" "Xmn192m" "Xmn224m" "Xmn256m" "Xmn512m")


param1=("Xmx512m")
param2=("Xms512m")
param3=("Xmn160m" "Xmn192m" "Xmn224m" "Xmn256m" "Xmn512m")
param4=("avrora" "batik")
param5=("30")
#"eclipse" "fop" "h2" "jython" "luindex" "lusearch" "lusearch-fix" "pmd" "sunflow" "tomcat" "tradebeans" "tradesoap" "xalan"
for var in ${allgcs[@]}
do
	for par1 in ${param1[@]}
	do
        #num_per1=$(echo $par1 | tr -dc '0-9')
		for par2 in ${param2[@]}
		do
            
            #num_per1=$(echo $par2 | tr -dc '0-9')
            #if [ $num_per1 -ge $num_per2 ];then
			for par3 in ${param3[@]}
			do
				for par4 in ${param4[@]}
				do


					#echo $filename
					str="java -$par1 -$par2 -$par3 -verbose:gc -XX:+$var -XX:+PrintGCDetails -jar  dacapo.jar $par4 --max-iterations 20"
					filename=$var"_"$par1"_"$par2"_"$par3
					$str>"raw_data"/"dacapo_"$par4"_"$filename".txt"		
					python execution_time_parser.py "dacapo_"$par4"_"$filename".txt"
				done
		
			done
            #fi
		done
     	done	
done
