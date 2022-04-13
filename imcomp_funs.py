import cv2
import imutils
import os.path
from skimage import metrics




def calc_psnr(orig_img_path :str,comp_img_path:str):

    if(os.path.exists(orig_img_path) and os.path.exists(comp_img_path)):
        orig_img = cv2.imread(orig_img_path)
        comp_img = cv2.imread(comp_img_path)
        #TODO: Compare x,y size of images

        return cv2.PSNR(orig_img,comp_img)
    else: 
        return -1

def calc_ssim(orig_img_path :str,comp_img_path:str):
    if(os.path.exists(orig_img_path) and os.path.exists(comp_img_path)):
        orig_img = cv2.imread(orig_img_path)
        comp_img = cv2.imread(comp_img_path)
        #TODO: Compare x,y size of images

        orig_img_gray = cv2.cvtColor(orig_img, cv2.COLOR_BGR2GRAY)
        comp_img_gray = cv2.cvtColor(comp_img, cv2.COLOR_BGR2GRAY)

        score = metrics.structural_similarity(orig_img_gray,comp_img_gray)
        
        return score
    else: 
        return -1