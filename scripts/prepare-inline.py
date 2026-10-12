"""Embed the standalone implementation without packing or resolving schema imports."""

import argparse
from pathlib import Path

import yaml

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--version", help="Candidate artifact version")
parser.add_argument("--image", help="Local test image or published image digest")
parser.add_argument("--output", type=Path, default=Path("workflow.cwl"))
args = parser.parse_args()
root = Path(__file__).resolve().parents[1]
document = yaml.safe_load((root / "workflow.cwl.template").read_text())
tool = next(process for process in document["$graph"] if process["id"] == "detect-water-body")
tool["requirements"]["InitialWorkDirRequirement"]["listing"][0]["entry"] = (
    root / "app.py"
).read_text()
if args.version:
    document["s:softwareVersion"] = args.version
if args.image:
    tool["hints"]["DockerRequirement"]["dockerPull"] = args.image
args.output.write_text(yaml.safe_dump(document, sort_keys=False))
