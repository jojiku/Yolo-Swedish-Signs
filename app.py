import streamlit as st
import os
import subprocess
import time  # Import time module for demonstration purposes
import hydralit_components as hc

# Function to perform road sign detection using YOLOv5
def detect_road_signs(video_file_path):
    command = f"python detect.py --weights C:/Users/Tseh/Documents/YOLO/yolov5/runs/train/exp21/weights/best.pt --img 640 --conf 0.15 --source {video_file_path}"
    subprocess.run(command, shell=True)

st.write("""
# Road signs detection

## Just upload your video in .mp4 to detect any road signs! 
""")

st.sidebar.header('Your file to upload:')
uploaded_file = st.sidebar.file_uploader("Upload your MP4 video", type="mp4")

if uploaded_file is not None:
    st.write("## Uploaded video:")
    st.video(uploaded_file)

    # Display a loading spinner while performing detection
    # with st.spinner('## Detecting road signs...'):
    with hc.HyLoader(' Detecting road signs...', hc.Loaders.standard_loaders, index=[5]):
        # Save the uploaded file to a temporary location
        with open("temp.mp4", "wb") as f:
            f.write(uploaded_file.getvalue())
        time.sleep(5)
        # Perform road sign detection
        detect_road_signs("temp.mp4")

        # Remove the temporary uploaded file
        os.remove("temp.mp4")

    st.write("### Road sign detection complete!")
    result_video_path = "C:/Users/Tseh/Documents/YOLO/yolov5/runs/detect/exp13/test.mp4"
    st.video(result_video_path)