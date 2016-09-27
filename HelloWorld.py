import sys,time


width=50

price_width = 10
item_width =width - price_width

header_format = '%-*s%*s'
formatx = '%-*s%*s'

print ('='*width)
print (header_format % (item_width, 'Item', price_width, 'num'))
print ('-' * width)

print (formatx % (item_width, 'byte' ,price_width, 128))
print ('='*width)




for i in range(100):
    sys.stdout.write("Data:" + str(i) + "% \r")
    sys.stdout.flush()
    time.sleep(0.1)



print ("Data:100%")
