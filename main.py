from count_cars import detect_cars
from fetch import fetch_weights
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_video>")
    else:
        fetch_weights("https://pjreddie.com/media/files/yolov3.weights", "yolov3.weights")
        file_path = sys.argv[1]
        detect_cars(file_path)