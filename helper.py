from ultralytics import YOLO
import supervision as sv
import av

import settings

def yolo_process(frame):
    img = frame.to_ndarray(format="bgr24")
    # hiện tại đang sử dụng YOLOv8x với 100 epoch
    model = YOLO(settings.MODEL_YOLO)

    box_annotator = sv.BoxAnnotator(
        thickness=2,
        text_thickness=2,
        text_scale=1
    )

    while True:
        result = model(img, agnostic_nms=True)[0]
        detections = sv.Detections.from_yolov8(result)

        # Lọc detections với độ tin cậy lớn hơn 0.5
        filtered_detections = [
            det for det in detections if det[1] > 0.1  # det[1] là confidence score của detection
        ]

        labels = [
            f"{model.model.names[class_id]} {confidence:0.2f}"
            for _, confidence, class_id, _
            in filtered_detections
        ]
        img = box_annotator.annotate(
            scene=img,
            detections=filtered_detections,
            labels=labels
        )

        return av.VideoFrame.from_ndarray(img, format="bgr24")


def process_video(frame, model_type):
    if model_type == 'YoloV8':
        return yolo_process(frame)
    else:
        return frame
