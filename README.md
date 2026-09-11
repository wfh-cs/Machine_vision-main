# GearPro 机器视觉

GearPro 是一个基于 PyQt5 的桌面应用，用于工业零件的实时检测。它集成了 OpenCV 摄像头视频流、本地 Ultralytics YOLO 推理，以及面向下游设备的可选串口指令。

## 面向生产环境的改进

- 运行时配置改用 `GP_*` 环境变量；摄像头、串口、模型、置信度和冷却时间等原有默认值保持不变。
- 摄像头初始化支持 Linux V4L2，并允许 OpenCV 在 Windows 和 macOS 上自动选择原生后端。
- 检测节拍可配置，停止请求能够及时中断工作线程。
- 程序退出时会释放串口资源。
- 提供包入口、依赖清单和 GitHub Actions 编译检查，使安装与评审可重复执行。

## 快速开始

请使用 Python 3.10 或更高版本。先安装与目标 CPU/GPU 匹配的 PyTorch 构建，再安装其余依赖：

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip install -e .
gearpro
```

本项目包含已锁定版本的 `ultralytics` 源码树，因此启动命令必须在仓库根目录下执行（或使用上面的可编辑安装方式）。

## 配置

所有配置项均为可选。以下取值保持原有运行时行为：

| 变量 | 默认值 | 用途 |
| --- | --- | --- |
| `GP_MODEL_PATH` | `best.pt` | 本地 YOLO 模型路径 |
| `GP_CAMERA_INDEX` | `2` | OpenCV 摄像头索引 |
| `GP_CONFIDENCE` | `0.7` | YOLO 置信度阈值 |
| `GP_DETECTION_INTERVAL` | `0.1` | 相邻两次推理之间的间隔秒数 |
| `GP_SERIAL_PORT` | `/dev/ttyHS1` | 串口执行机构端口 |
| `GP_SERIAL_BAUDRATE` | `9600` | 串口波特率 |
| `GP_RESULT_COOLDOWN_MS` | `5000` | 下发下一条执行指令前的延迟 |

Windows 测试工位示例：

```powershell
$env:GP_CAMERA_INDEX = "0"
$env:GP_SERIAL_PORT = "COM3"
$env:GP_MODEL_PATH = "C:\models\best.pt"
gearpro
```

## 硬件行为

检测到 `good` 类时，应用发送 `01`；检测到 `miss` 时，应用发送 `02`。指令发送受 `GP_RESULT_COOLDOWN_MS` 限流。在接入生产设备之前，请在有人监护的测试环境中验证摄像头取景、类别语义、串口接线以及执行机构的安全性。

## 仓库结构

| 路径 | 职责 |
| --- | --- |
| `gp_main.py` | 应用入口 |
| `gp_config.py` | 基于环境变量的运行时配置 |
| `gp_cameradisplaywidget.py` | 摄像头采集与原始帧显示 |
| `gp_detectionworker.py` | YOLO 推理工作线程 |
| `gp_detectiondisplaywidget.py` | 检测界面与串口触发逻辑 |
| `gp_serial.py` | 串口传输 |
| `.github/workflows/python-checks.yml` | GitHub 编译检查 |

## 许可与发布

本仓库包含一份内嵌的 Ultralytics 源码树，其上游项目以 AGPL-3.0 授权。项目级的 `LICENSE.md` 仅适用于 GearPro 自有文件，不替代第三方声明。在公开发布或分发可执行文件之前，请核实模型权重的归属、所有第三方许可证，以及 AGPL 所要求的义务。

发布检查清单见 [NOTICE.md](NOTICE.md)。
