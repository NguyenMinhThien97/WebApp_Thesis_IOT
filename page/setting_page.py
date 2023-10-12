import streamlit as st
from st_pages import add_page_title
import pandas as pd

# Local Modules
import settings
import helper


add_page_title(layout="wide")

df = pd.read_csv(settings.FILE_CONFIG)

edited_df = st.data_editor(df, column_config={
    "camera_ip": st.column_config.SelectboxColumn(
        "Camera IP",
        help="IP of camera",
        required=True,
        width="medium",
        options=[
            "10.255.255.1",
            "10.255.255.2",
            "10.255.0.1",
            "10.255.0.2",
        ]
    ),
    "model": st.column_config.SelectboxColumn(
        "Model",
        help="Model AI to apply on video of camera IP",
        required=True,
        width="medium",
        options=[
            "Keras",
            "YoloV8",
            "Coral",
        ]
    ),
    "accuracy": st.column_config.NumberColumn(
        "From accuracy upwards (%)",
        help="Detection accuracy ranges from % or more",
        min_value=0,
        max_value=100,
        default=0,
        step=1,
        format="%d %%",
    ),
    "is_active": st.column_config.CheckboxColumn(
        "Is Active",
        default=False
    )
}, num_rows="dynamic", hide_index=False)

if st.button('Save config'):
    if edited_df['camera_ip'].duplicated().any():
        st.warning(
            "Camera IP is duplicated"
        )
    # elif edited_df['camera_ip', 'model'].isna().any(axis=1).any():
    #     st.warning(
    #         "Camera IP/Model is required"
    #     )
    else:
        edited_df.to_csv(settings.FILE_CONFIG, index=False)
        st.success(
            "Save config successful! 🎉"
        )
