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
else:
    print("Data-OK")


print ("Data:100%")

dic_l={"Test_A":"00%","Test_B":"20%","Test_C":"40%","Test_D":"60%","Test_E":"80%","Test_F":"100%"}
dic_l= sorted(dic_l.items(),key=lambda d:d[0])

for i in dic_l:
    sys.stdout.write("dic_data Key:" + i[0] + " Value:" + i[1] + "\r")
    sys.stdout.flush()
    time.sleep(1)

print ("\n")
print ("OK!")

