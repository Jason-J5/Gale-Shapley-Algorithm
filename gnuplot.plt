# Set the output to a png file
set terminal png size 800,500
# The file we'll write to
set output 'runtime.png'
# The graphic title
set title 'Run Time(x)'
#enable grid
set grid
#set x axis to have 500 as the interval
set xtics 500
#plot the graphic
plot "data.txt" with linespoint