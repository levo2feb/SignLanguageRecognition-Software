# 🤟 Sign Language Recognition System

A real-time sign language gesture recognition system that uses computer vision and machine learning to identify hand signs from a webcam feed. The system translates simple hand gestures into corresponding text, helping to bridge communication gaps for individuals with hearing or speech impairments.



## 📌 Features

- Real-time hand gesture recognition using webcam
- Hand landmark detection using MediaPipe
- Custom dataset creation via webcam
- Trained machine learning model using Random Forest classifier
- Recognizes 3 signs: `Hi`, `Thumbs up`, and `Victory`



## 🖥️ Technologies Used

- Python 3
- OpenCV – Real-time image capture and processing
- MediaPipe – Hand landmark detection
- scikit-learn – Model training and classification
- Pickle – Model persistence



## 🗂️ Project Structure

├── 1_collect_imgs.py # Collect images for each gesture class               <br>
├── 2_create_dataset.py # Create dataset using MediaPipe                    <br>
├── 3_train_classifier.py # Train classifier using extracted features       <br>
├── 4_inference_classifier.py # Real-time prediction using webcam           <br> 
├── cameracheck.py # Check if webcam is accessible                          <br>
├── data/ # Folder containing gesture image data                            <br>
├── data.pickle # Processed gesture landmark dataset                        <br>
├── model.p # Trained classifier model                                      <br>




## 🚀 How to Run This Project

**1. 📦 Install Dependencies -** Ensure you have Python 3 installed. Then install the required packages:
```bash
pip install opencv-python mediapipe scikit-learn matplotlib
```

**2. 🎥 Check Camera Access -** Press q to exit the camera feed.
```bash
python cameracheck.py  
```


**3. 📸 Collect Gesture Images -** Follow the prompts to press Q to start capturing for each gesture. This will save images in ./data/0, ./data/1, and ./data/2.
```bash
python 1_collect_imgs.py
```

**4. 🧪 Generate Dataset -** This will generate data.pickle, containing the processed data and labels.
```bash
python 2_create_dataset.py
```


**5. 🧠 Train Classifier -** This will save the trained model in model.p. You'll also see the classification accuracy in the console.
```bash
python 3_train_classifier.py
```


**6. 🖥️ Run Real-time Inference -** Use your webcam to predict gestures in real time:
```bash
python 4_inference_classifier.py
```

## 📝 Notes
- You can modify the number of gesture classes or dataset size by editing 1_collect_imgs.py.
- Make sure you collect consistent and clear images for better accuracy.
- You can expand labels_dict in 4_inference_classifier.py to add new gestures.


## 💡 Future Improvements
- Add more gesture classes
- Use a deep learning model for improved accuracy
- Add voice output for recognized gestures
- Build a mobile app version



