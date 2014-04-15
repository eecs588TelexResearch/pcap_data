#!/bin/sh
for ((i=0; i < $1; i++ ))
do
    curl -silent -o curl_out.html $2
    curl -silent -o curl_out.html $3
    printf '%d of %d \r' $i $1

done
