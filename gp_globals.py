import threading
from ultralytics import YOLO

from gp_config import CONFIG


#一些全局变量
frame_lock = threading.Lock()
results_lock = threading.Lock()
frame = None

MODEL_PATH = CONFIG.model_path
if not MODEL_PATH.is_file():
    raise FileNotFoundError(f"YOLO model file was not found: {MODEL_PATH}")
model = YOLO(str(MODEL_PATH))


detection_results = None

running = True
