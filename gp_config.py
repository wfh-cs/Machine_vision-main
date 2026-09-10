"""Runtime configuration loaded from environment variables.

The defaults preserve the original hardware and model settings. Set the
corresponding ``GP_*`` variables to adapt an installation without editing code.
"""

import os
from dataclasses import dataclass
from pathlib import Path


def _project_path(value: str, default: str) -> Path:
    return Path(os.environ.get(value, Path(__file__).resolve().parent / default))


@dataclass(frozen=True)
class RuntimeConfig:
    model_path: Path = _project_path("GP_MODEL_PATH", "best.pt")
    camera_index: int = int(os.environ.get("GP_CAMERA_INDEX", "2"))
    confidence: float = float(os.environ.get("GP_CONFIDENCE", "0.7"))
    detection_interval: float = float(os.environ.get("GP_DETECTION_INTERVAL", "0.1"))
    serial_port: str = os.environ.get("GP_SERIAL_PORT", "/dev/ttyHS1")
    serial_baudrate: int = int(os.environ.get("GP_SERIAL_BAUDRATE", "9600"))
    result_cooldown_ms: int = int(os.environ.get("GP_RESULT_COOLDOWN_MS", "5000"))


CONFIG = RuntimeConfig()
