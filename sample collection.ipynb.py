{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Face not found\n",
      "Face not found\n",
      "Face not found\n",
      "Face not found\n",
      "Face not found\n",
      "Face not found\n",
      "Face not found\n",
      "Face not found\n",
      "Face not found\n",
      "Face not found\n",
      "Face not found\n",
      "Face not found\n",
      "Face not found\n"
     ]
    }
   ],
   "source": [
    "import cv2\n",
    "import numpy as np\n",
    "\n",
    "# Load HAAR face classifier\n",
    "face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')\n",
    "\n",
    "# Load functions\n",
    "def face_extractor(img):\n",
    "    # Function detects faces and returns the cropped face\n",
    "    # If no face detected, it returns the input image\n",
    "   \n",
    "    #gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)\n",
    "    faces = face_classifier.detectMultiScale(img, 1.3, 5)#gray\n",
    "   \n",
    "    if faces is ():\n",
    "        return None\n",
    "   \n",
    "    # Crop all faces found\n",
    "    for (x,y,w,h) in faces:\n",
    "        cropped_face = img[y:y+h, x:x+w]\n",
    "\n",
    "    return cropped_face\n",
    "\n",
    "# Initialize Webcam\n",
    "cap = cv2.VideoCapture(0)\n",
    "count = 0\n",
    "\n",
    "# Collect 100 samples of your face from webcam input\n",
    "while True:\n",
    "\n",
    "    ret, frame = cap.read()\n",
    "    if face_extractor(frame) is not None:\n",
    "        count += 1\n",
    "        face = cv2.resize(face_extractor(frame), (200, 200))\n",
    "        #face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)\n",
    "\n",
    "        # Save file in specified directory with unique name\n",
    "        file_name_path = 'C://Users//user//Desktop//face//' + str(count) + '.jpg'\n",
    "        cv2.imwrite(file_name_path, face)\n",
    "\n",
    "        # Put count on images and display live count\n",
    "        cv2.putText(face, str(count), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)\n",
    "        cv2.imshow('Face Cropper', face)\n",
    "       \n",
    "    else:\n",
    "        print(\"Face not found\")\n",
    "        pass\n",
    "\n",
    "    if cv2.waitKey(1) == 13 or count == 5018: #13 is the Enter Key\n",
    "        break\n",
    "       \n",
    "cap.release()\n",
    "cv2.destroyAllWindows()     \n",
    "print(\"Collecting Samples Complete\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
