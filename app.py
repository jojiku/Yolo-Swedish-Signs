import streamlit as st
import os
import subprocess
import time  # Import time module for demonstration purposes
import hydralit_components as hc
from ultralytics import YOLO
import moviepy.editor as moviepy
n = 0
# Function to perform road sign detection using YOLOv5
def detect_road_signs(video_file_path):
    model = YOLO('C:/Users/Tseh/Documents/YOLO/yolov8/nikita_best.pt')
    results = model(source=video_file_path, save=True, save_txt=False, conf=0.5, project="C:/Users/Tseh/Documents/YOLO/detection_results")

st.write("""
# Road signs detection

## Just upload your video in .mp4 to detect any road signs! 
""")

st.sidebar.header('Your file to upload:')
uploaded_file = st.sidebar.file_uploader("Upload your MP4 video", type="mp4")

if uploaded_file is not None:
    st.write("## Uploaded video:")
    st.video(uploaded_file)
    
    detect_video = st.sidebar.button("Detect Road Signs")
    n=+1
    if detect_video:
        with hc.HyLoader(' Detecting road signs...', hc.Loaders.standard_loaders, index=[5]):
            with open(f"test_{n}.mp4", "wb") as f:
                f.write(uploaded_file.getvalue())
            detect_road_signs(f"test_{n}.mp4")


        st.write("### Road sign detection complete!")
        result_video_path = f"C:/Users/Tseh/Documents/YOLO/detection_results/predict/test_{n}.avi"

        clip = moviepy.VideoFileClip(result_video_path)

        clip.write_videofile(f"C:/Users/Tseh/Documents/YOLO/detection_results/predict/test_{n}.mp4")
        st.video(f"C:/Users/Tseh/Documents/YOLO/detection_results/predict/test_{n}.mp4")
        download_button = st.button("Download Result")
