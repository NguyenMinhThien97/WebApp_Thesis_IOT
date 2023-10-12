import streamlit as st
from streamlit_webrtc import WebRtcMode, webrtc_streamer
from st_pages import add_page_title
import pandas as pd

# Local Modules
import settings
import helper

add_page_title(layout="wide")

df = pd.read_csv(settings.FILE_CONFIG)
# Filter data by condition is_active
df = df[df['is_active'] == True]


def load_camera(df, ind):
    st.write(f"IP camera: {df['camera_ip'][ind]} - {df['model'][ind]}")

    def video_frame_callback(frame):
        return helper.process_video(frame, df['model'][ind])

    webrtc_streamer(key=f"camera{ind}", mode=WebRtcMode.SENDRECV,
                    video_frame_callback=video_frame_callback,
                    media_stream_constraints={"video": True, "audio": False}, async_processing=True, )


with st.container():
    col1, col2 = st.columns(2)
    for ind in df.index:
        if ind % 2 == 0:
            with col1:
                load_camera(df, ind)
        else:
            with col2:
                load_camera(df, ind)
