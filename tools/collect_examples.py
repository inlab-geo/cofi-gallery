import requests
import shutil
import os
import pathlib

from utils import _GALLERY_PATH, existing_examples, read_yml


_output_path = _GALLERY_PATH.parent / "build"

def mkdir_output_path(output_path):
    pathlib.Path(output_path).mkdir(parents=True, exist_ok=True)

def collect_all():
    all_examples = existing_examples()
    all_data = list()
    for example in all_examples:
        yml_content = read_yml(f"{_GALLERY_PATH}/{example}")
        all_data.append((yml_content, example))
    return all_data

def load_thumbnail(yml_content, example_path):
    link_to_thumbnail = yml_content["link_to_thumbnail"]
    response = requests.get(link_to_thumbnail, stream=True)
    if response.status_code != 200:
        raise ConnectionError(
            f"unable to get image for {example_path} from {link_to_thumbnail}"
        )
    image_file = example_path.replace(".yml", ".png")
    with open(_output_path / image_file, "wb") as f:
        response.raw.decode_content = True
        shutil.copyfileobj(response.raw, f) 

def main():
    all_data = collect_all()
    mkdir_output_path(_output_path)
    for example_data in all_data:
        load_thumbnail(*example_data)

if __name__ == "__main__":
    main()
