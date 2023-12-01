# Application Package Quickwin for inline code

## Generate the Application Package with the inline code

Update the Application Package template `workflow.cwl.template` with the Python `app.py` as the inline code to run:

```
content=`cat app.py` yq eval '.$graph[1].requirements.InitialWorkDirRequirement.listing[0].entry=strenv(content)' workflow.cwl.template > workflow.cwl
```

Here's a breakdown of the command:

* `cat app.py``: This command outputs the contents of the `app.py` file.

* `yq eval '.$graph[1].requirements.InitialWorkDirRequirement.listing[0].entry=strenv(content)' workflow.cwl.template`: This command uses yq to evaluate a YAML expression on the `workflow.cwl.template` file. The expression seems to modify the entry at a specific path in the YAML structure, setting it to the content of `app.py`.

* `> workflow.cwl`: This part of the command redirects the modified output to a new file named `workflow.cwl`.

## Running the CWL Application Package

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