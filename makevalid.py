



import os


txtlist = os.listdir("C:/Users/adith/FLIR_ADAS/validation/PreviewData/")

for a in txtlist:
    print("C:/Users/adith/FILRdataset/FLIR_ADAS/validation/PreviewData/"+a, file=open("C:/Users/adith/FLIR_ADAS/validation/PreviewData/flir_valid.txt","a"))

print("jobs done!")
