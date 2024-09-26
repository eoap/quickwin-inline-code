# Generate the Application Package with the inline code

Update the Application Package template `workflow.cwl.template` with the Python `app.py` as the inline code to run:

```
content=`cat app.py` yq eval '.$graph[1].requirements.InitialWorkDirRequirement.listing[0].entry=strenv(content)' workflow.cwl.template > workflow.cwl
```

Here's a breakdown of the command:

* `cat app.py`: This command outputs the contents of the `app.py` file.

* `yq eval '.$graph[1].requirements.InitialWorkDirRequirement.listing[0].entry=strenv(content)' workflow.cwl.template`: This command uses yq to evaluate a YAML expression on the `workflow.cwl.template` file. The expression modifies the entry at a specific path in the CWL `InitialWorkDirRequirement`, setting it to the content of `app.py`.

* `> workflow.cwl`: This part of the command redirects the modified output to a new file named `workflow.cwl`.
