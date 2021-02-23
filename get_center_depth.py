	
"""
Get the center depth value from _d.csv
Auther : moriitkys@ROBOTAiM

"""
import numpy as np
import glob
import cv2

input_folder = "input_folder_depth_csv"
#input_folder = "input_folder_thermal_csv"

extention = "_d.csv"
extention_out = "_d.png"
#extention = "_t.csv"
#extention_out = "_t.png"

for file in glob.glob(input_folder + "/*" + extention):
    depth_csv = np.loadtxt(file, delimiter=',', dtype='float64')
    h, w = depth_csv.shape[:2]

    #depth_value = depth_csv[int(h/2)][int(w/2)] / 10000 # [m]
    depth_value = depth_csv[int(h/2)][int(w/2)] # [mm]

    out_img_depth = depth_csv.copy()
    out_img_depth = out_img_depth.astype(np.uint8)
    out_img_depth = cv2.cvtColor(out_img_depth, cv2.COLOR_GRAY2BGR)

    cv2.circle(out_img_depth, (int(w/2), int(h/2)), 3, (0,0,255), -1)
    fontType = cv2.FONT_HERSHEY_SIMPLEX
    text = str(depth_value) + 'mm'
    #text = str(depth_value) + 'thermal raw value'
    cv2.putText(out_img_depth, text, (int(w/2) +20, int(h/2) + 20), fontType, 1, (0, 0, 255),2)

    output_path = file.replace(input_folder, output_folder)
    output_path = output_path.replace(extention, extention_out)

    cv2.imwrite(output_path, out_img_depth)
