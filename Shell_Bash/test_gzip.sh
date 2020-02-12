#!/bin/bash

echo "Compress ratio" > measures_gzip_ubuntu.xls

for i in {1..3}
do
	START=$(date +"%T.%3N")
	millisecs="$(date +%s%N)/1000000"
	printf "Loop No: $i\nBegin compression: ${START}\n"
	gzip -c --best file_for_testing.txt > compressed_file_No${i}.gz
	END=$(date +"%T.%3N")
	millisecs="$(($(date +%s%N)/1000000-millisecs))"
	printf "End compression: ${END}\nTime elapsed in millisecs: ${millisecs}\n-----------\n"
	echo "${START}, ${END}, ${millisecs}" >> measures_gzip_ubuntu.xls
	sleep 3
done

echo >> measures_gzip_ubuntu.xls
echo "Uncompress ratio" >> measures_gzip_ubuntu.xls

for file in *.gz;
do
        START=$(date +"%T.%3N")
        millisecs="$(date +%s%N)/1000000"
        printf "Uncompress: $file\nBegin: ${START}\n"
	gunzip -f $file > /home/user/"${file%.*}" ;
        END=$(date +"%T.%3N")
        millisecs="$(($(date +%s%N)/1000000-millisecs))"
        printf "End uncompression: ${END}\nTime elapsed in millisecs: ${millisecs}\n-----------\n"
        echo "${START}, ${END}, ${millisecs}" >> measures_gzip_ubuntu.xls
done

echo "The end" >> measures_gzip_ubuntu.xls

rm compress*
