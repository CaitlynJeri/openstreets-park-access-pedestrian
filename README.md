# Who gains, who loses: open space access during the 2020 playground closure and Open Streets

Code and data for measuring how much open space access New York City's 2020 playground closure removed, how much the Open Streets program restored, and for whom. The analysis disaggregates 2020 census population to tax lots, computes network two-step floating catchment area (2SFCA) accessibility for parks, playgrounds, and Open Streets across six supply scenarios, and relates loss and offset to block group income, race, age, and tenure.

## Repository structure

```
notebooks/
  01_dasymetric_population.ipynb   census population to tax lot pieces (CEDS)
  02_network_accessibility.ipynb   pedestrian network, supply, 2SFCA, sensitivity
  03_substitution_analysis.ipynb   block group aggregation, gradients, regressions
  04_figure_formation.ipynb        figures and pipeline tables
src/
  paths.py                         project paths and projected CRS (EPSG:2263)
data/
  raw/                             inputs
  processed/                       outputs written by the notebooks
figures/                           figures written by 04
```

## Running the analysis

Create the environment from `environment.yml`, start Jupyter from the repository root, and run the notebooks in order, each from top to bottom. Every notebook reads only the inputs in `data/raw/` and files written by earlier notebooks.

| Notebook | Writes | Runtime |
|---|---|---|
| 01 | dasymetric population surface | about 10 minutes |
| 02 | accessibility results, sensitivity table, metadata | about 30 minutes |
| 03 | block group table, gradients, regressions | about 2 minutes |
| 04 | figures and pipeline tables | about 3 minutes |

Notebook 02 needs about 2 GB of free memory; lower `NODE_BATCH` in its configuration cell if memory is tight. Notebooks 01 and 03 download census data on their first run and cache it to `data/raw/`. A Census API key is optional; set the `CENSUS_API_KEY` environment variable to use one.

## Data

This repository holds the smaller inputs. The archived release holds the complete `data/raw/` folder, including MapPLUTO 21v3, LION 21A, the 2020 census block geometry, and the cached OpenStreetMap pedestrian network, so the results reproduce without downloading anything.

| File | Source | Vintage |
|---|---|---|
| `MapPLUTO_21v3.gdb` | NYC Department of City Planning | 21v3, shoreline-clipped |
| `lion/lion.gdb` | NYC Department of City Planning | 21A |
| `nybb.shp` | NYC Department of City Planning, borough boundaries | 2021 |
| `geo_export_8b4f899c-...shp` | NYC Open Data, Parks Properties | export used in the paper |
| `Parks_Closure_Status_Due_to_COVID-19__Playgrounds_20250720.csv` | NYC Open Data, NYC Parks | records edited June to July 2020 |
| `open_streets_2020/open_streets_20210408235257.csv` | Wayback Machine capture of NYC Open Data dataset `uiay-nctu` | captured 8 April 2021 |
| `network_cache/nyc_walk.graphml` | OpenStreetMap via OSMnx 2.1.1, ODbL | as cached for the paper |
| `tl_2020_36_tabblock20.zip` | U.S. Census Bureau TIGER/Line | 2020 |
| `dec2020_p1_blocks_ny.csv` | U.S. Census Bureau, 2020 PL 94-171, table P1 | 2020 |
| `acs2020_bg_nyc.csv` | U.S. Census Bureau, ACS five-year | 2016 to 2020 |

OpenStreetMap and NYC Open Data change over time, so rebuilding these inputs from live sources will not reproduce the published results exactly.