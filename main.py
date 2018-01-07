import os
import numpy
import cv2
from cv2 import findContours, fillPoly

def file_name(file_dir):
    L=[];
    
    if not(os.path.exists(file_dir+'/labels')):
        os.mkdir(file_dir+'/labels');
    for root, dirs, files in os.walk(file_dir):
        print(root);

        for file in files:
            filename=os.path.splitext(file);
            if filename[1]=='.tiff':
                FileList=[];
                FileList.append(root);
                FileList.append(filename[0]);
                L.append(FileList);
    return L;       

imgpath="/home/dox/Downloads/label"
filepath=file_name(imgpath);
print filepath;
for filepath in file_name(imgpath):
    #print filepath[0]+ '/' + filepath[1] + '.tiff';
    srcimg=cv2.imread(filepath[0]+ '/' + filepath[1] + '.tiff',-1);
#
    if len(srcimg.shape) == 3:
        greyimg=cv2.cvtColor(srcimg, cv2.COLOR_RGB2GRAY);
        
    output=findContours(srcimg, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE);
    resultimg = output[0];
    contours = output[1];
    
    PolyImg=cv2.fillPoly(srcimg,contours,(255.0, 255.0, 255.0))
    
    cv2.imwrite(filepath[0] + '/' + 'labels' + '/' + filepath[1] + '.png', PolyImg);
    cv2.namedWindow("srcimg");
    cv2.imshow("srcimg", PolyImg);
    cv2.waitKey(-1);
