"""Project paths. Import in notebooks so no absolute paths get committed."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

DATA = ROOT / "data"
RAW = DATA / "raw"
INTERIM = DATA / "interim"
PROCESSED = DATA / "processed"

DOCS = ROOT / "docs"

# NAD83 / New York Long Island (ftUS). Distances in degrees are meaningless here.
CRS_PROJECTED = "EPSG:2263"
CRS_GEOGRAPHIC = "EPSG:4326"

for _p in (RAW, INTERIM, PROCESSED):
    _p.mkdir(parents=True, exist_ok=True)