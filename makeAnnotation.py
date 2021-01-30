#####################################################################
# Convert FLIR annotations to YoloV3 format
# Chunpeng Shao
# Dec 2018
#
# generateList()    -> get all json filenames
# convert()         -> convert one json file to yolo format .txt file
# main()            -> entry point
#####################################################################
# USAGE:
# under Annotation folder
# >$ python3 makeAnnotation.py
# >$ mv *.txt <YOUR NEW ANNOTATION FOLDER PATH>
#####################################################################


import os
import json
import csv

_classIDDict_ = {"1":"People","2":"Bicycles","3":"Cars","18":"Dogs","91":"Other_Vehicles"}

def generateList():
    rlist = []
    flist = os.listdir("../training/Annotations/")
    #flist = os.listdir("../validation/Annotations/")
    #flist.remove("makeAnnotation.py")
    for f in flist:
        f = f[:-5]
        rlist.append(f)
    return rlist

def makeCSV(filename_str,filewriter):
    #os.mknod("/home/ray/Documents/dataset/"+filename_str+".txt")

    fp = open("../training/Annotations/"+filename_str+".json","r")
    #fp = open("../validation/Annotations/"+filename_str+".json","r")

    data = json.load(fp)
    csvstr = ""
    for a in data["annotation"]:
        x = (a["bbox"][0]+a["bbox"][2]/2)/data["image"]["width"]
        y = (a["bbox"][1]+a["bbox"][3]/2)/data["image"]["height"]
        width = (a["bbox"][2]/2)/data["image"]["width"]
        height = (a["bbox"][3]/2)/data["image"]["height"]
        x1 = a["bbox"][0]
        y1 = a["bbox"][1]
        x2 = a["bbox"][0] + a["bbox"][2]
        y2 = a["bbox"][1] + a["bbox"][3]
        categ = _classIDDict_[a["category_id"]]
        #detect if there's annotation :/
        filewriter.writerow(["/adithyasuresh/dr_bingli/RCNN_test_dir/FLIR_ADAS/training/PreviewData/"+filename_str+".jpeg", str(x1), str(y1),str(x2),str(y2),categ])
        csvstr += "/adithyasuresh/dr_bingli/RCNN_test_dir/FLIR_ADAS/training/PreviewData/"+filename_str+".jpeg"+","+str(x1)+","+str(y1)+","+str(x2)+","+str(y2)+","+categ+"\n"
        # filewriter.writerow(["/home/bing/RCNN_test_dir/FLIR_ADAS/validation/PreviewData/"+filename_str+".jpeg", str(x1), str(y1),str(x2),str(y2),categ])
        # csvstr += "/adithyasuresh/dr_bingli/RCNN_test_dir/FLIR_ADAS/validation/PreviewData/"+filename_str+".jpeg"+","+str(x1)+","+str(y1)+","+str(x2)+","+str(y2)+","+categ+"\n"
        print(categ, x, y, width, height, file=open("C:/Users/adith/FLIR_ADAS/Textfiles/flir_text"+filename_str+".txt","a"))
    fp.close()
    print(csvstr)
    return csvstr


def main():
    filename_list = generateList()
    filename_list.sort()
    if filename_list[0]==".Rhi":
        filename_list.pop(0)
    c = 0
    csvstr = ""
    with open('train_annots.csv', 'w') as csvfile:
    #with open('val_annots.csv', 'w') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)

        for f_str in filename_list:
            csvstr+=makeCSV(f_str,filewriter)
            c+=1

    sp = open("Training_values_csv.txt","w+")
    #sp = open("Validation_values_csv.txt","w+")
    sp.write(csvstr[:len(csvstr)-1])
    sp.close()
    csvfile.close()
    print("Jobs done!","total files:", c)

main()
