import pathlib
import os
import yaml


_ROOT = pathlib.Path(__file__).resolve().parent.parent
_GALLERY = "gallery"
_GALLERY_PATH = _ROOT / "gallery"
_TEMPLATE_PATH = _ROOT / "tools" / "_template.yml"

def existing_examples():
    return os.listdir(_GALLERY_PATH)

def read_yml(yml_path):
    with open(yml_path, "r") as f:
        content = yaml.safe_load(f)
    return content
