import cv2
import numpy as np

def detect_cars(input_path):
    # Load YOLO
    net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
    classes = []
    with open("coco.names", "r") as f:
        classes = [line.strip() for line in f]

    layer_names = net.getUnconnectedOutLayersNames()

    # Branch if input is an image with the following extensions
    if input_path.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp')):
        image = cv2.imread(input_path)
        height, width, _ = image.shape

        # Detect cars in the image
        blob = cv2.dnn.blobFromImage(image, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
        net.setInput(blob)
        outs = net.forward(layer_names)

        # Process the detected objects
        class_ids = []
        confidences = []
        boxes = []

        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > 0.5 and classes[class_id] == "car":
                    center_x, center_y = int(detection[0] * width), int(detection[1] * height)
                    w, h = int(detection[2] * width), int(detection[3] * height)
                    x, y = int(center_x - w / 2), int(center_y - h / 2)

                    class_ids.append(class_id)
                    confidences.append(float(confidence))
                    boxes.append([x, y, w, h])

        # Apply non-maximum suppression to eliminate redundant boxes
        # You can read more about non-maximum suppression and how it works here:
        # https://builtin.com/machine-learning/non-maximum-suppression
        indices = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

        # Draw rectangles around the detected cars
        for i in range(len(boxes)):
            if i in indices:
                x, y, w, h = boxes[i]
                cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Display the car count
        car_count = len(indices)
        print(f"Number of Cars: {car_count}")

        # Display the window end exit if esc is pressed
        cv2.imshow('Car Detection (ESC TO EXIT)', image)
        key = cv2.waitKey(0)
        if key == 27: 
            cv2.destroyAllWindows()

    # Branch if video with these extensions a lot of the same code as above
    elif input_path.lower().endswith(('.mp4', '.avi', '.mov')):
        cap = cv2.VideoCapture(input_path)

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            height, width, _ = frame.shape

            blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
            net.setInput(blob)
            outs = net.forward(layer_names)

            class_ids = []
            confidences = []
            boxes = []

            for out in outs:
                for detection in out:
                    scores = detection[5:]
                    class_id = np.argmax(scores)
                    confidence = scores[class_id]
                    if confidence > 0.5 and classes[class_id] == "car":
                        center_x, center_y = int(detection[0] * width), int(detection[1] * height)
                        w, h = int(detection[2] * width), int(detection[3] * height)
                        x, y = int(center_x - w / 2), int(center_y - h / 2)

                        class_ids.append(class_id)
                        confidences.append(float(confidence))
                        boxes.append([x, y, w, h])

            indices = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

            for i in range(len(boxes)):
                if i in indices:
                    x, y, w, h = boxes[i]
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            car_count = len(indices)
            print(f"Number of Cars: {car_count}")

            cv2.imshow('Car Detection (ESC TO EXIT)', frame)
            key = cv2.waitKey(30)
            if key == 27: 
                break

        cap.release()
        cv2.destroyAllWindows()

    else:
        print("Unsupported file format. Please provide an image (jpg, jpeg, png, bmp) or a video (mp4, avi, mov).")