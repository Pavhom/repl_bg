import os
import time
from rembg import remove
from PIL import Image
from alive_progress import alive_bar


def repl_bg():
    img_path_list = []

    for root, dirs, files in os.walk(r'input'):
        for file_name in files:
            if file_name.endswith(".png") or file_name.endswith(".jpg") or file_name.endswith(".jpeg"):
                path = os.path.join(root, file_name) 
                img_path_list.append(path)  

    with alive_bar(len(img_path_list)) as bar:      
        for img in img_path_list:
            dirs = img.split(os.sep)[1:-1]
            file_name = os.path.basename(img)
            clear_name = os.path.splitext(file_name)[0]
            output_path = os.path.join('output', *dirs)
            
            if not os.path.exists(output_path):
                os.makedirs(output_path, exist_ok=False)
            
            input_img = Image.open(img)
            output_img = remove(input_img)
            output_img.save(fr'{output_path}/{clear_name}.png')

            time.sleep(0.05)
            bar()

def main():
    repl_bg()


if __name__ == '__main__':
    main()    