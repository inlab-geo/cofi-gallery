import pathlib
import os


_ROOT = pathlib.Path(__file__).resolve().parent.parent
_GALLERY = "gallery"
_GALLERY_PATH = _ROOT / "gallery"
_TEMPLATE_PATH = _ROOT / "tools" / "_template.yml"

def existing_examples():
    return os.listdir(_GALLERY_PATH)
