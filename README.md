# A university project for detecting cars in an image or video.

The project is done in python.

## Documentation
The code is documented here and through comments.

## Getting started:
### Initializing the project:
Before you can run the project you need to initialize a python virtual environment:

After cloning this repository run the following commands:
```
cd ${your_working_directory}/poos-project
python -m venv .
```

### Installing dependencies:
To install the required dependencies, all of which are located in the included 
`requirements.txt` file simply run:
```
bin/pip install -r requirements.txt
```

### Running:
Once that's done you should be good to go there are two files in this repository but feel free
to use your own photo or video files, simply run:
```
bin/python main.py path_to_file.jpg # Or path_to_file.mp4

# For the preloaded files run the following:
bin/python main.py traffic.jpg
bin/python main.py traffic.mp4
```
## Note:
The first run might take a while since it needs to download the yolov3 weights.

## How it works:
The code uses the YOLO ("You Only Look Once") real-time object detection algorithm.
TOLO divides an image into a grid and for each grid cell predicts bounding boxes, object classes,
and confidence scores for those boxes. You can read more about it [here](https://pjreddie.com/darknet/yolo/)

The image of traffic was taken from: [here](https://www.istockphoto.com/photo/cars-in-rush-hour-with-traffic-at-dawn-gm155287967-19095156)

The video of traffic was taken from: [here](https://pixabay.com/videos/traffic-car-highway-street-27260/)
