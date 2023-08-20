import os
from playsound import playsound
import time

first_line_list = []

def reset_list():
    global first_line_list
    first_line_list.clear()

def get_txt_files(directory):
    txt_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".txt"):
                txt_files.append(os.path.join(root, file))
    return txt_files

def process_txt_files(txt_files):
    global first_line_list
    first_line_list.clear()

    for txt_file in txt_files:
        with open(txt_file, 'r') as file:
            lines = file.readlines()
            if lines:
                first_line = lines[0].split()[0]
                first_line_list.append(int(first_line))


    if 2 in first_line_list:
        playsound('car prohibit.mp3')
        print('car prohibit')
    if 3 in first_line_list:
        playsound('entering prohibit.mp3')
        print('entering prohibit')
    if 5 in first_line_list:
        playsound('left prohibit.mp3')
        print('left prohibit')
    if 6 in first_line_list:
        playsound('turn around prohibit.mp3')
        print('turn around prohibit')
    if 7 in first_line_list:
        playsound('motorcycle prohibit.mp3')
        print('motorcycle prohibit')
    if 9 in first_line_list:
        playsound('right and left prohibit.mp3')
        print('right and left prohibit')
    if 10 in first_line_list:
        playsound('right prohibit.mp3')
        print('right prohibit')
    if 11 in first_line_list:
        playsound('speed limit.mp3')
        print('speed limit')
    if 12 in first_line_list:
        playsound('take photo.mp3')
        print('take photo')
    if 4 in first_line_list:
        playsound('narrow.mp3')
        print('narrow')
    if 0 in first_line_list:
        playsound('be transfer.mp3')
        print('be transfer')
    if 1 in first_line_list:
        playsound('be slow.mp3')
        print('be slow')
    if 8 in first_line_list:
        playsound('parking prohibit.mp3')
        print('parking prohibit')


def delete_txt_files(folder_path):
    try:
        files = os.listdir(folder_path)
        for file in files:
            file_path = os.path.join(folder_path, file)
            if file.endswith('.txt') and os.path.isfile(file_path):
                os.remove(file_path)
                #print(f"Deleted: {file_path}")
    except Exception as e:
        #print(f"Error occurred: {str(e)}")
        pass
txt_directory = "D:\\yolov7\\yolov7\\runs\\detect\\exp\\labels"
txt_files = get_txt_files(txt_directory)
first_line_list = []

while True:
    txt_files = get_txt_files(txt_directory)
    if len(first_line_list) == 0:
        process_txt_files(txt_files)
    
    delete_txt_files(txt_directory)
    #time.sleep(2)
    reset_list()