import csv
from typing import Optional

def min_ttc_seconds(csv_path: str) -> Optional[float]:
    min_ttc: Optional[float] = None
    with open(csv_path, newline="") as f:
        rows = list(csv.DictReader(f))

    for i in range(1, len(rows)):
        dt_s = (int(rows[i]["timestamp_ms"]) - int(rows[i - 1]["timestamp_ms"])) / 1000.0
        if dt_s <= 0.0:
            continue
        dist = float(rows[i]["lead_dist_m"])
        prev_dist = float(rows[i - 1]["lead_dist_m"])
        closing_speed = (prev_dist - dist) / dt_s
        if closing_speed > 0.1 and dist >= 0.0:
            ttc = dist / closing_speed
            min_ttc = ttc if min_ttc is None else min(min_ttc, ttc)
    return min_ttc
