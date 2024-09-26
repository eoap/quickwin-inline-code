# Application Package - Background

The Application Package defines a workflow for detecting water bodies based on Normalized Difference Water Index (NDWI) and Otsu threshold using Sentinel-2 data.

The key components of this CWL document are:

* Name: Water bodies detection based on NDWI and the Otsu threshold.
* Description: Workflow for detecting water bodies based on NDWI and Otsu threshold applied to a single Sentinel-2 Cloud-Optimized GeoTIFF (COG) SpatioTemporal Asset Catalog (STAC) item.
* Inputs:

    * `aoi`: Area of interest as a bounding box.
    * `epsg`: EPSG code (default: "EPSG:4326").
    * `bands`: Bands used for NDWI (default: ["green", "nir"]).
    * `item`: Reference to a STAC item.

* Outputs:

    * `stac_catalog`: Output directory containing the STAC catalog.

* Steps:

    * `node_detect`: Executes the detect-water-body tool with specified inputs and produces a STAC catalog in the output directory.

* Tool: detect-water-body:

    * A CommandLineTool written in Python that uses various libraries such as rasterio, skimage, pyproj, shapely and loguru.
    * It performs operations like cropping, thresholding, and creating a STAC catalog for the detected water bodies.
    * It takes inputs like STAC item URL, area of interest, EPSG code, and band names.

* Tool Requirements:

    * Uses Docker.
    * Specifies resource requirements (`coresMax: 1`, `ramMax: 512`).
    * Sets up initial working directory with an entry script (`app.py`).

* Execution:

    * The workflow runs the detect-water-body tool with specified inputs.
    * Generates a STAC catalog with the detected water bodies.
    * Cleans up temporary files after completion.
