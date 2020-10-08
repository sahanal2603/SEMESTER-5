echo "Enter basic salary: "
read sal
echo "Enter DA and HRA"
read da
read hra
printf "Total salary is "
expr $sal + $da + $hra
