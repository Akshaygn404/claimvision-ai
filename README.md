# ClaimVision AI

**AI-Powered Vehicle Damage Assessment for Motor Insurance Claims**

ClaimVision AI is an end-to-end prototype that combines **Computer Vision (YOLOv8)** and **NLP-based claim understanding** to automate the initial stages of motor insurance claim assessment.

The system analyzes accident images, extracts structured information from a customer’s claim description, compares both sources for consistency, and generates a professional insurance-style assessment report through a **Streamlit web application**.

---

## Features

* **Vehicle damage detection** using YOLOv8 object detection
* **Bounding-box visualization** for detected damaged parts
* **Rule-based NLP claim extraction** from free-text accident descriptions
* **Structured JSON output** for downstream processing
* **CV vs NLP consistency checking** to identify mismatches between reported and observed damage
* **Automated assessment report generation**
* **Interactive Streamlit interface** for end-to-end testing

---

## System Architecture

```text
Vehicle Image
      │
      ▼
YOLOv8 Detection
      │
      ▼
predict_json.py
      │
      ├──────────────┐
      ▼              ▼
NLP Extractor    Claim Text
      │              │
      └──────┬───────┘
             ▼
Consistency Checker
             ▼
Report Generator
             ▼
Streamlit UI
```

---

## Tech Stack

| Component        | Technology                   |
| ---------------- | ---------------------------- |
| Computer Vision  | YOLOv8 (Ultralytics)         |
| NLP              | Python rule-based extraction |
| Web App          | Streamlit                    |
| Image Processing | OpenCV, Pillow               |
| Data Handling    | Pandas                       |
| Language         | Python 3.11                  |

---

## Damage Classes

The original 18 dataset classes were consolidated into **8 insurance-oriented damage categories**:

| Final Class         |
| ------------------- |
| `hood_damage`       |
| `door_damage`       |
| `fender_damage`     |
| `bumper_damage`     |
| `windscreen_damage` |
| `light_damage`      |
| `mirror_damage`     |
| `side_panel_damage` |

---

## Project Structure

```text
claimvision-ai/
│
├── app.py
├── train.py
├── detect.py
├── predict_json.py
├── nlp_extractor.py
├── consistency_checker.py
├── report_generator.py
├── test_report.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Akshaygn404/claimvision-ai.git
cd claimvision-ai
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application

Start the Streamlit interface:

```bash
streamlit run app.py
```

Open the URL shown in the terminal (typically `http://localhost:8501`).

---

## Example Workflow

### Input Image

Upload a damaged vehicle image containing visible accident damage.

### Input Claim Text

```text
I hit a pillar while turning left.
The front bumper is cracked and the headlight is broken.
The vehicle is not drivable.
```

### Extracted Claim Data

```json
{
  "impact_side": "front-left",
  "collision_object": "pillar",
  "mentioned_parts": [
    "bumper_damage",
    "light_damage"
  ],
  "damage_keywords": [
    "cracked",
    "broken"
  ],
  "drivable": false
}
```

### Generated Assessment Report

```text
CLAIMVISION AI - VEHICLE DAMAGE ASSESSMENT

ACCIDENT SUMMARY
Impact side: front-left
Collision object: pillar

DETECTED DAMAGE
- bumper_damage
- light_damage

SAFETY ASSESSMENT
Vehicle should be inspected before further driving.

CONSISTENCY CHECK
Customer statement is consistent with image findings.
```

---

## YOLO Training

Train the custom detector using:

```bash
yolo task=detect mode=train model=yolov8n.pt data=data.yaml epochs=30 imgsz=640
```

The trained weights are expected at:

```text
runs/detect/claimvision_damage/weights/best.pt
```

> **Note:** Dataset files and trained model weights are not included in this repository.

---

## Current Implementation Status

| Module                      | Status |
| --------------------------- | ------ |
| YOLOv8 training pipeline    | ✅      |
| Vehicle damage detection    | ✅      |
| JSON prediction export      | ✅      |
| NLP claim extraction        | ✅      |
| Consistency checking        | ✅      |
| Automated report generation | ✅      |
| Streamlit integration       | ✅      |
| End-to-end testing          | ✅      |

---

## Current Limitations

* Rule-based NLP extraction (not yet using spaCy or transformer models)
* No repair cost estimation in v1
* No PDF export functionality in v1
* No LLM-generated claim summaries yet
* Detection accuracy depends on the quality and diversity of training images

---

## Planned Enhancements

* Repair cost estimation engine
* PDF assessment report export
* spaCy-based entity extraction
* LLM-enhanced adjuster notes and customer summaries
* Claim severity scoring
* Fraud and anomaly detection based on image-text inconsistencies
* Multi-image accident assessment support

---

## Screenshots

Create a `screenshots/` folder and add images such as:

```text
screenshots/
├── detection_result.png
├── claim_extraction.png
├── consistency_check.png
└── assessment_report.png
```

Then reference them in the README:

```markdown
![Detection Result](screenshots/detection_result.png)
```

---

## Why This Project Matters

ClaimVision AI demonstrates how **Computer Vision, NLP, and workflow automation** can be combined to reduce manual effort in motor insurance claim processing. The project is designed to simulate a realistic **AI-assisted claim intake and preliminary assessment pipeline** that could later integrate with insurer back-office systems.

---

## Author

**Akshay G N**

* GitHub: https://github.com/Akshaygn404
* LinkedIn: https://www.linkedin.com/in/akshay-gn-5b6932241/

---

## Repository Status

**ClaimVision AI v1.0** — Initial working prototype featuring YOLOv8-based vehicle damage detection, NLP-driven claim extraction, consistency validation, and automated insurance assessment reporting through Streamlit.
