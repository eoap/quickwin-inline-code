# Application Package Quickwin with inline code

This repository contains a simple Python application `app.py` including a simple unit test as a demonstration of a "real" yet very simple Python EO application.

This `app.py` is added to a CWL template as inline code that is staged and executed in a container.

## Generate the Application Package with the inline code

Update the Application Package template `workflow.cwl.template` with the Python `app.py` as the inline code to run:

```
content=`cat app.py` yq eval '.$graph[1].requirements.InitialWorkDirRequirement.listing[0].entry=strenv(content)' workflow.cwl.template > workflow.cwl
```

Here's a breakdown of the command:

* `cat app.py`: This command outputs the contents of the `app.py` file.

* `yq eval '.$graph[1].requirements.InitialWorkDirRequirement.listing[0].entry=strenv(content)' workflow.cwl.template`: This command uses yq to evaluate a YAML expression on the `workflow.cwl.template` file. The expression modifies the entry at a specific path in the CWL `InitialWorkDirRequirement`, setting it to the content of `app.py`.

* `> workflow.cwl`: This part of the command redirects the modified output to a new file named `workflow.cwl`.

## Run the Application Package

The new `workflow.cwl` can be executed with:

```
cwltool workflow.cwl params.yaml
```

Where `params.yaml` contains:

```yaml
item: "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs/items/S2B_10TFK_20210713_0_L2A"
aoi: "-121.399,39.834,-120.74,40.472"
epsg: "EPSG:4326"
```

## Run the released Application Package

The release 1.0.0 contains the released Application Package include the update docker reference published in the Github container registry.

Run the released Application Package with:

```
cwltool \
    https://github.com/eoap/quickwin-inline-code/releases/download/1.0.0/app-water-body-inline-code.1.0.0.cwl \
    params.yaml 
```

## Explanation

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
