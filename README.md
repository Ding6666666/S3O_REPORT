# Singapore Solar Site Optimization System (S3O)

## Overview
A data-driven approach to optimize solar power station locations in Singapore through cloud coverage analysis and terrain evaluation.

## Features
- Multi-source geospatial data integration
- Cloud pattern analysis (2018-2023)
- Terrain suitability assessment
- Deep learning-based site evaluation
- Location optimization visualization

## Data Sources
| Data Type | Source | Resolution | Collection |
|-----------|---------|------------|------------|
| Cloud Optical Thickness | Copernicus Sentinel-5P L3_CLOUD | 1km/Daily | Manual |
| Digital Elevation Model | HydroSHEDS DEM | 90m | Manual |
| Land Cover | MODIS MCD12Q1 | 500m/Year | Manual |
| Surface Radiation | GLDAS Noah | 0.25°/3h | Manual |
| Building Footprints | OSM | Vector | Manual |

## Project Structure
```
project/
├── data/
│   ├── raw/                  # Original datasets
│   │   ├── GEE_exports/     # Cloud thickness data
│   │   └── DEM/             # Elevation data
│   └── processed/           # Processed data
├── notebooks/
│   ├── 1_data_preprocessing.ipynb
│   ├── 2_feature_extraction.ipynb
│   ├── 3_model_training.ipynb
│   └── 4_evaluation_and_visualization.ipynb
└── result/                  # Output files
```

## Setup and Installation

1. Environment Setup
```bash
conda create -n s3o_env python=3.9
conda activate s3o_env
```

2. Install Dependencies
```bash
conda install -c conda-forge numpy pandas matplotlib seaborn
conda install -c conda-forge rasterio geopandas shapely fiona contextily
conda install -c conda-forge scikit-learn pytorch torchvision
conda install -c conda-forge opencv jupyter notebook ipykernel
```

## Usage Guide

1. Data Processing
   - Run `1_data_preprocessing.ipynb` for cloud data processing
   - Execute `2_feature_extraction.ipynb` for terrain analysis

2. Model Development
   - Train the evaluation model using `3_model_training.ipynb`

3. Results Analysis
   - Visualize results with `4_evaluation_and_visualization.ipynb`

## Output
- Suitability heat maps
- Top 10 recommended locations
- Regional distribution analysis
- Detailed site evaluation metrics

## Requirements
See `requirements.txt` for complete dependency list.

## License
MIT License