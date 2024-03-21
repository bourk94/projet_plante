import subprocess
import os
 
def capture_image(output_path):
    command = ["libcamera-jpeg", "-o", output_path]
    try:
        subprocess.run(command, check=True)
        print("Image captured successfully:", output_path)
    except subprocess.CalledProcessError as e:
        print("Error capturing image:", e)

def main():
    output_directory = "/home/bourk/Pictures/"
    os.makedirs(output_directory, exist_ok=True)
    counter = 1
    while True:
        output_path = output_directory + "image_" + str(counter) + ".jpg"
        capture_image(output_path)
        
        counter += 1
 
if __name__ == "__main__":
    main()