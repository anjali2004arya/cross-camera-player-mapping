\# 📝 Report – Cross-Camera Player Mapping



\*\*Author\*\*: Anjali Arya  

\*\*Email\*\*: arya.2004anjali@gmail.com



---



\## 🎯 Objective



To detect and track football players across two different camera angles (`broadcast.mp4` and `tacticam.mp4`) and establish a consistent identity for each player across both views.



---



\## ⚙️ Methodology



\### 1. \*\*Detection\*\*

Used a fine-tuned `YOLOv11` model (`best.pt`) for detecting players and the ball in both videos.



\### 2. \*\*Tracking\*\*

Employed \*\*Norfair\*\*, a real-time object tracker, to assign unique IDs to detected players based on their movement across frames.



Separate scripts:

\- `track\_and\_save\_broadcast.py` → creates `broadcast\_tracking.csv`

\- `track\_and\_save\_tacticam.py` → creates `tacticam\_tracking.csv`



\### 3. \*\*Cross-Camera Matching\*\*

Used `match\_players.py` to:

\- Compare positional data of players across videos

\- Calculate Euclidean distances

\- Map `tacticam` players to `broadcast` player IDs

\- Save results in `player\_id\_mapping.csv`



---



\## 🧪 Techniques Tried



\- Norfair + centroid tracking to stabilize player ID assignment

\- Distance-based matching (temporal + spatial)

\- Threshold tuning to improve mapping accuracy



---



\## ⚠️ Challenges Encountered



\- Players look different due to camera angle + occlusion

\- Slight inconsistency in detection between clips

\- Needed to tweak confidence thresholds and tracker parameters

\- Matching fails if players aren't detected in overlapping time windows



---



\## ✅ Final Outcome



\- IDs were successfully tracked in both videos.

\- Matching worked best with threshold tuning (~11 correct matches).

\- Output is reproducible via 3 scripts and saved in CSV files.



---



\## 🚧 Possible Improvements



\- Use visual features (jersey color, appearance) for matching instead of just position

\- Synchronize time across both videos using audio or visual cues

\- Combine appearance-based re-identification (Re-ID) with trajectory matching



---



\## 🗂️ Files Submitted



\- All source code scripts

\- Model weights (`best.pt`)

\- Tracking and mapping CSVs

\- This report

\- `README.md` for instructions



---



✅ \*\*This project is self-contained and fully reproducible.\*\*



