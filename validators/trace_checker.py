import csv

def check_trace(csv_path: str, max_dt_ms: int = 50) -> list[str]:
    errors = []
    prev_ts = None
    with open(csv_path, newline="") as f:
        for row_num, row in enumerate(csv.DictReader(f), start=2):
            ts = int(row["timestamp_ms"])
            speed = float(row["ego_speed_mps"])
            if prev_ts is not None and (ts - prev_ts) > max_dt_ms:
                errors.append(f"Row {row_num}: timestamp gap {ts - prev_ts}ms > {max_dt_ms}ms")
            if speed < 0.0 or speed > 70.0:
                errors.append(f"Row {row_num}: invalid ego_speed_mps={speed}")
            prev_ts = ts
    return errors
