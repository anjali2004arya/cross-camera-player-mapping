\### ✅ `README.md` (fully ready)



```markdown

\# 🎯 Cross-Camera Player Mapping – Internship Assignment



This project was completed as part of an internship assignment by \*\*Anjali Arya\*\*. The goal is to track football players across two different video feeds (`broadcast.mp4` and `tacticam.mp4`) and consistently match their identities across both views.



---



\## 📁 Folder Structure



```



cross-camera-player-mapping/

├── best.pt                     # YOLOv11 trained model weights

├── broadcast.mp4               # Broadcast camera video (input)

├── tacticam.mp4                # Tacticam view video (input)

├── broadcast\\\_tracking.csv      # Tracked player positions from broadcast

├── tacticam\\\_tracking.csv       # Tracked player positions from tacticam

├── player\\\_id\\\_mapping.csv       # Final ID mappings across both views

├── track\\\_and\\\_save\\\_broadcast.py # Tracking script for broadcast video

├── track\\\_and\\\_save\\\_tacticam.py  # Tracking script for tacticam video

├── match\\\_players.py            # Script to perform ID matching

├── requirements.txt            # Python dependencies

├── report.md                   # Methodology \& analysis

└── README.md                   # Setup and usage guide



````



---



\## 🧪 Requirements



Install dependencies using:



```bash

pip install -r requirements.txt

````



\### Libraries used:



\* `ultralytics`

\* `norfair`

\* `opencv-python`

\* `filterpy`

\* `numpy`



Tested on Python 3.10+



---



\## 🚀 How to Run the Project



\### 1️⃣ Track Broadcast Video



```bash

python track\_and\_save\_broadcast.py

```



➡️ Generates: `broadcast\_tracking.csv`



---



\### 2️⃣ Track Tacticam Video



```bash

python track\_and\_save\_tacticam.py

```



➡️ Generates: `tacticam\_tracking.csv`



---



\### 3️⃣ Match Players Across Views



```bash

python match\_players.py

```



➡️ Generates: `player\_id\_mapping.csv`



---



\## 🎯 Sample Output (from match\\\_players.py)



```

📽️ Players in broadcast: 11

🎥 Players in tacticam: 21



Tacticam\_ID  -->  Broadcast\_ID   |   Distance

&nbsp;    2       -->     5           |   3.19

&nbsp;    9       -->     7           |   11.10

&nbsp;   13       -->     5           |   145.53



✅ Mapping saved to player\_id\_mapping.csv

```



---



\## 📊 What This Project Demonstrates



\* ⚽ Player detection with a fine-tuned YOLOv11 model

\* 🔁 Real-time multi-object tracking using Norfair

\* 🔗 Cross-camera identity matching based on trajectory similarity

\* 📈 Output in CSV format for easy evaluation



---



\## 👩‍💻 Author



\*\*Anjali Arya\*\*

📧 email: `arya.2004anjali@gmail.com`

🔗 GitHub: \[github.com/anjaliarya](https://github.com/anjaliarya)



---



> 💡 This repo is fully self-contained. Just place your `broadcast.mp4`, `tacticam.mp4`, and `best.pt` in the root folder and run the scripts.



```



