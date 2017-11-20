import face_recognition
import cv2
from time import sleep

def wait_recognize_face():
    # Get a reference to webcam #0 (the default one)
    video_capture = cv2.VideoCapture(0)

    # Load a sample picture and learn how to recognize it.
    dataset = []
    for i in range(1,3):
        obama_image = face_recognition.load_image_file("data/{0}.jpg".format(i))
        obama_face_encoding = face_recognition.face_encodings(obama_image)[0]
        dataset.append(obama_face_encoding)

    # Initialize some variables
    face_locations = []
    face_encodings = []
    
    while True:
        # Grab a single frame of video
        ret, frame = video_capture.read()

        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(small_frame)
        face_encodings = face_recognition.face_encodings(small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            match = face_recognition.compare_faces(dataset, face_encoding)
            found = [x for x in match if x]
            if len(found) > 0:
                print("Found user")
                video_capture.release()
                return


        sleep(.5)

    # Release handle to the webcam
    video_capture.release()