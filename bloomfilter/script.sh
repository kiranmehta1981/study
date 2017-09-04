#!/bin/sh

for k in {1..6}
do
python bloomfilter.py  59999  $k /root/work/study/bloomfilter/config.movies << EOF
4
5
EOF

done
rm output_all
cat output* > output_all
