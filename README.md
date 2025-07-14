### ✅ Final `README.md`

```markdown
# 🎯 Cross-Camera Player Mapping

This project was developed as part of an internship assignment by **Anjali Arya**.  
It focuses on identifying and consistently tracking football players across two different video perspectives — `broadcast.mp4` and `tacticam.mp4`.

---

## 🧠 Problem Statement

Given two video feeds of the same football match:
- 📽️ `broadcast.mp4` (TV view)
- 🎥 `tacticam.mp4` (top-down view)

The task is to:
1. Detect and track players in both videos.
2. Assign consistent IDs across both views.
3. Output the mapping in a structured CSV format.

---

## 🗂️ Folder Structure

```

cross-camera-player-mapping/
├── best.pt                    # YOLOv11 trained model weights
├── broadcast.mp4              # Broadcast camera input
├── tacticam.mp4               # Tacticam camera input
├── broadcast\_tracking.csv     # Tracking results for broadcast video
├── tacticam\_tracking.csv      # Tracking results for tacticam video
├── player\_id\_mapping.csv      # Final cross-view player ID mapping
├── track\_and\_save\_broadcast.py # Script for broadcast tracking
├── track\_and\_save\_tacticam.py  # Script for tacticam tracking
├── match\_players.py           # Script for cross-camera ID matching
├── requirements.txt           # Dependency list
├── report.md                  # Methodology & observations
└── README.md                  # This file

````

---

## 🧪 Installation

Install the required Python packages:

```bash
pip install -r requirements.txt
````

✅ Tested on **Python 3.10**

---

## 🚀 Usage

### 1️⃣ Track players in broadcast video

```bash
python track_and_save_broadcast.py
```

➡️ Generates `broadcast_tracking.csv`

---

### 2️⃣ Track players in tacticam video

```bash
python track_and_save_tacticam.py
```

➡️ Generates `tacticam_tracking.csv`

---

### 3️⃣ Match players across both videos

```bash
python match_players.py
```

➡️ Generates `player_id_mapping.csv`

---

## 🧾 Sample Output (From `match_players.py`)

```
📽️ Players in broadcast: 11
🎥 Players in tacticam: 21

Tacticam_ID  -->  Broadcast_ID   |   Distance
     2        -->     5          |   3.19
     9        -->     7          |   11.10
    13        -->     5          |   145.53

✅ Mapping saved to player_id_mapping.csv
```

---

## 💡 Features

* 🧠 Fine-tuned YOLOv11 model for accurate player detection
* 🔁 Real-time multi-object tracking using Norfair
* 🔗 Cross-camera identity consistency using trajectory similarity
* 🧾 Clean CSV outputs for all stages

---

## ⚠️ Note

Due to GitHub’s 100 MB file limit, the model file `best.pt` is not included in this repo.
Please place your own trained `best.pt` in the project root directory before running the scripts.

---

## 👩‍💻 Author

**Anjali Arya**
📧 [arya.2004anjali@gmail.com](mailto:arya.2004anjali@gmail.com)
🔗 [GitHub: @anjali2004arya](https://github.com/anjali2004arya)

---

## ✅ Status

🟢 Project complete and functional.
Ready for submission.


