import pandas as pd
import numpy as np
from scipy.spatial.distance import cdist

# Load tracking data
broadcast_df = pd.read_csv("broadcast_tracking.csv")
tacticam_df = pd.read_csv("tacticam_tracking.csv")

# Only consider players tracked in at least 30 frames
MIN_FRAMES = 5

def get_player_trajectories(df):
    player_trajectories = {}
    for player_id, group in df.groupby("id"):
        if len(group) < MIN_FRAMES:
            continue
        # Sort by frame and get x, y sequence
        trajectory = group.sort_values("frame")[["x", "y"]].to_numpy()
        player_trajectories[player_id] = trajectory
    return player_trajectories

broadcast_trajectories = get_player_trajectories(broadcast_df)
tacticam_trajectories = get_player_trajectories(tacticam_df)

print(f"📽️ Players in broadcast: {len(broadcast_trajectories)}")
print(f"🎥 Players in tacticam: {len(tacticam_trajectories)}")

# Normalize trajectory lengths (pad with last position or truncate)
def normalize(traj, length):
    if len(traj) == length:
        return traj
    elif len(traj) < length:
        pad = np.tile(traj[-1], (length - len(traj), 1))
        return np.vstack([traj, pad])
    else:
        return traj[:length]

# Set a fixed length for comparison
TRAJ_LEN = 30

# Prepare final matches
matches = []

for tid, t_traj in tacticam_trajectories.items():
    t_norm = normalize(t_traj, TRAJ_LEN)
    best_match = None
    best_distance = float("inf")

    for bid, b_traj in broadcast_trajectories.items():
        b_norm = normalize(b_traj, TRAJ_LEN)
        dist = np.mean(np.linalg.norm(t_norm - b_norm, axis=1))

        if dist < best_distance:
            best_distance = dist
            best_match = bid

    matches.append((tid, best_match, round(best_distance, 2)))

# Show results
print("\n🔗 Cross-Camera Player Mapping:")
print("Tacticam_ID  -->  Broadcast_ID   |   Distance")
for tid, bid, dist in matches:
    print(f"     {tid:<10} -->     {bid:<10} |   {dist}")

# Optionally save to CSV
pd.DataFrame(matches, columns=["tacticam_id", "broadcast_id", "distance"]).to_csv("player_id_mapping.csv", index=False)
print("\n✅ Mapping saved to player_id_mapping.csv")
