

upper = int(input('Enter upper range limit '))

lower = int(input('Enter lower range limit '))

divide = int(input('Enter the number to be divided by '))


for i in range (lower,upper+1):
    if(i%divide==0):
        print(i)