from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
PROCESSED = ROOT / "data" / "processed"
CRS_PROJECTED = "EPSG:2263"   # NAD83 / New York Long Island, feet

for p in (RAW, PROCESSED):
    p.mkdir(parents=True, exist_ok=True)
