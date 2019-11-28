import json

def load_label():
    label_file = open("1.json", "r")
    lable = json.load(label_file)
    gt = list()
    width = lable['size']['width']
    height = lable['size']['height']
    output_file = open("1.txt", "w")
    for chip in lable['outputs']['object']:
        chip_box = chip['bndbox']
        xmid = float(chip_box['xmin'] + chip_box['xmax']) / width / 2
        ymid = float(chip_box['ymin'] + chip_box['ymax']) / height / 2
        wid =  float(chip_box['xmax'] - chip_box['xmin']) / width
        hei =  float(chip_box['ymax'] - chip_box['ymin']) / height
        output_file.write(str(0) + ' ' + str(xmid) + ' ' + str(ymid) + ' ' + str(wid) + ' ' + str(hei) + '\n')
        gt.append([xmid, ymid, wid, hei])
    return gt

load_label()
