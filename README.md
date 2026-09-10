# GearPro Machine Vision

GearPro is a PyQt5 desktop application for real-time industrial part inspection. It combines an OpenCV camera stream, local Ultralytics YOLO inference, and optional serial commands for downstream equipment.

## Production-focused improvements

- Runtime configuration uses `GP_*` environment variables; original camera, serial, model, confidence, and cooldown defaults are unchanged.
- Camera initialization supports Linux V4L2 and allows OpenCV to select a native backend on Windows and macOS.
- Detection pacing is configurable and stop requests interrupt the worker promptly.
- Serial resources are released during shutdown.
- A package entry point, dependency list, and GitHub Actions compile check make installation and review repeatable.

## Quick start

Use Python 3.10 or newer. Install a PyTorch build suitable for the target CPU/GPU first, then install the rest of the dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip install -e .
gearpro
```

The project contains its pinned `ultralytics` source tree, so launch commands must be run from the repository root (or use the editable install above).

## Configuration

All configuration is optional. These values preserve the previous runtime behavior:

| Variable | Default | Purpose |
| --- | --- | --- |
| `GP_MODEL_PATH` | `best.pt` | Local YOLO model path |
| `GP_CAMERA_INDEX` | `2` | OpenCV camera index |
| `GP_CONFIDENCE` | `0.7` | YOLO confidence threshold |
| `GP_DETECTION_INTERVAL` | `0.1` | Seconds between inference cycles |
| `GP_SERIAL_PORT` | `/dev/ttyHS1` | Serial actuator port |
| `GP_SERIAL_BAUDRATE` | `9600` | Serial baud rate |
| `GP_RESULT_COOLDOWN_MS` | `5000` | Delay before another actuator command |

Example for a Windows test station:

```powershell
$env:GP_CAMERA_INDEX = "0"
$env:GP_SERIAL_PORT = "COM3"
$env:GP_MODEL_PATH = "C:\models\best.pt"
gearpro
```

## Hardware behavior

The application sends `01` when it detects the `good` class and `02` for `miss`. Commands are throttled by `GP_RESULT_COOLDOWN_MS`. Validate camera framing, class semantics, serial wiring, and actuator safety in a supervised test before connecting production equipment.

## Repository layout

| Path | Responsibility |
| --- | --- |
| `gp_main.py` | Application entry point |
| `gp_config.py` | Environment-backed runtime configuration |
| `gp_cameradisplaywidget.py` | Camera capture and raw-frame display |
| `gp_detectionworker.py` | YOLO inference worker |
| `gp_detectiondisplaywidget.py` | Detection UI and serial trigger logic |
| `gp_serial.py` | Serial transport |
| `.github/workflows/python-checks.yml` | GitHub compile check |

## Licensing and publishing

This repository includes a vendored Ultralytics source tree marked AGPL-3.0 by its upstream project. The project-level `LICENSE.md` applies only to original GearPro files and does not replace third-party notices. Review the model-weight ownership, all third-party licenses, and the obligations of the AGPL before making a public release or distributing an executable.

See [NOTICE.md](NOTICE.md) for the release checklist.
