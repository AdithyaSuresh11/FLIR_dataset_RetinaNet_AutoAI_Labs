



import os


txtlist = os.listdir("C:/Users/adith/FLIR_ADAS/training/PreviewData")

for a in txtlist:
    print("C:/Users/adith/FLIR_ADAS/training/PreviewData"+a, file=open("C:/Users/adith/FLIR_ADAS/training/PreviewData/flir_train.txt","a"))

print("jobs done!")
