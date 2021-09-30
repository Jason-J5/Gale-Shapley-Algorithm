#Program name:  model.plt
#Purpose:       Plot the data from data.txt
y(x)=a0 + a1*x + a2 * x**2

a0=1
a1=0.1
a2=1

fit y(x) "data.txt" via a0, a1,a2

set xlabel "Input size"
set ylabel "Time (milisecs.)"
set nokey

plot y(x), "data.txt"