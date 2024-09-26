# Run the released Application Package

The release 1.0.0 contains the released Application Package include the update docker reference published in the Github container registry.

Run the released Application Package with:

```
cwltool \
    https://github.com/eoap/quickwin-inline-code/releases/download/1.0.0/app-water-body-inline-code.1.0.0.cwl \
    params.yaml 
```