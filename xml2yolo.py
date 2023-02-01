import os
import shutil

from bs4 import BeautifulSoup
from IPython.display import clear_output

def getYoloFormat(filename, label_path, img_path, yolo_path, newname):    
    with open(label_path+filename, 'r') as f:        
        soup = BeautifulSoup(f.read(), 'xml')    # Read xml
        imgname = soup.select_one('filename').text         
        image_w = soup.select_one('width').text
        image_h = soup.select_one('height').text
        ary = []
        for obj in soup.select('object'):
            # Find out xmin, xmax, ymin, ymax and name                  
            xmin = int(obj.select_one('xmin').text)          
            xmax = int(obj.select_one('xmax').text)
            ymin = int(obj.select_one('ymin').text)
            ymax = int(obj.select_one('ymax').text)
            # Using status_dictionary to convert name(Classes) to label, good => 2            
            objclass = status_dic.get(obj.select_one('name').text)
            # Convert to YOLO format: class, x, y, w and h
            x = (xmin + (xmax-xmin)/2) * 1.0 / float(image_w)
            y = (ymin + (ymax-ymin)/2) * 1.0 / float(image_h)
            w = (xmax-xmin) * 1.0 / float(image_w)
            h = (ymax-ymin) * 1.0 / float(image_h)
            ary.append(' '.join([str(objclass), str(x), str(y), str(w), str(h)]))
      
        try:
            """
            1. Copy image to YOLO folder
            2. write label.txt
            """
            shutil.copyfile(img_path+imgname, yolo_path+'image/'+newname+'.png')    
            with open(yolo_path+'label/'+newname+'.txt', 'w') as f:
                f.write('\n'.join(ary))
        except:
            print("Error with Worth Path: "+img_path+imgname)
                
def update_progress(progress):
    bar_length = 20
    if isinstance(progress, int):
        progress = float(progress)
    if not isinstance(progress, float):
        progress = 0
    if progress < 0:
        progress = 0
    if progress >= 1:
        progress = 1

    block = int(round(bar_length * progress))
    clear_output(wait = True)
    text = "Progress: [{0}] {1:.1f}%".format( "#" * block + "-" * (bar_length - block), progress * 100)
    print(text)

def check_path(path):
    if not os.path.exists(path):
        os.mkdir(path)


def main():
    check_path(SAVE_PATH)
    check_path(SAVE_PATH+'image/')
    check_path(SAVE_PATH+'label/')

    total_progress = len(os.listdir(LABEL_PATH))
    progress = 0
    for idx, f in enumerate(os.listdir(LABEL_PATH)):   #透過getYoloFormat將圖像和參數檔全部寫到YOLO下
        progress += 1
        try:
            if f.split('.')[1] == 'xml':
                getYoloFormat(f, LABEL_PATH, IMAGE_PATH, SAVE_PATH, str(idx//2))
        except Exception as e:
            print(e)

        update_progress(progress/total_progress)

if __name__ in '_main_':   
    #Setting relative path
    LABEL_PATH = '/train_coco_format/'           
    IMAGE_PATH = '/train_coco_format/'
    SAVE_PATH = '/train_yolo_format/'
    # Saving Label of Classse by Using dictionary
    status_dic = {
                'Text':0, 'Table':1, 'Picture':2, 'Page-header':3, 'Page-footer':4, 
                'Caption':0, 'Formula':0, 'List-item':0, 'Section-header':0, 'Title':0,
                'Footnote':4
                }             

    main()