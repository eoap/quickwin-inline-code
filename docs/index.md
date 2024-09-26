# Quickwin - An Application Package with inline Python code

This documentation describes a simple Python application `app.py`, including a simple unit test, as a demonstration of a "real" yet very simple Python EO application.

Using CWL's [InitialWorkDirRequirement](https://www.commonwl.org/v1.2/CommandLineTool.html#InitialWorkDirRequirement), a requirement that defines a list of files and subdirectories that must be staged by the workflow platform prior to executing the command line tool, the Python script `app.py` is staged and executed in a container.

For easing the development of the Python script `app.py`, its content is added to a template named `workflow.cwl.template` by this repository Github actions.

The CWL document generated is available in the [releases section](https://github.com/eoap/quickwin-inline-code/releases/tag/1.0.0).
