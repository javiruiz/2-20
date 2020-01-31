power=2^20
pwgen 1 $(echo ${power} | bc)  > ${power}.txt
