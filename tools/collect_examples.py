import requests
import shutil
import pathlib

from utils import _GALLERY_PATH, existing_examples, read_yml


_output_path = _GALLERY_PATH.parent / "generated"


# --------------- read data -----------------------------------------------------------
def collect_all():
    all_examples = existing_examples()
    all_data = list()
    for example in all_examples:
        yml_content = read_yml(f"{_GALLERY_PATH}/{example}")
        all_data.append((yml_content, example))
    return all_data


# --------------- load images ---------------------------------------------------------
def mkdir_output_path(output_path):
    pathlib.Path(output_path).mkdir(parents=True, exist_ok=True)

def load_thumbnail(yml_content, example_path, output_path):
    link_to_thumbnail = yml_content["link_to_thumbnail"]
    response = requests.get(link_to_thumbnail, stream=True)
    if response.status_code != 200:
        raise ConnectionError(
            f"unable to get image for {example_path} from {link_to_thumbnail}"
        )
    image_file = example_path.replace(".yml", ".png")
    image_path = output_path / image_file
    with open(image_path, "wb") as f:
        response.raw.decode_content = True
        shutil.copyfileobj(response.raw, f) 
    return image_file

def load_all_images(all_data, output_path):
    mkdir_output_path(output_path)
    all_images = []
    for (yml_content, example) in all_data:
        img_file = load_thumbnail(yml_content, example, output_path)
        all_images.append(img_file)
    return all_images


# --------------- read README.rst -----------------------------------------------------
def read_readme(path_to_readme):
    with open(path_to_readme, "r") as f:
        readme_rst = f.read()
    return readme_rst


# --------------- format rst ----------------------------------------------------------
THUMBNAIL_PARENT_DIV = """
.. raw:: html

    <div class="sphx-glr-thumbnails">

"""

THUMBNAIL_PARENT_DIV_CLOSE = """
.. raw:: html

    </div>

"""

THUMBNAIL_TEMPLATE = """
.. raw:: html

    <a href="{link_to_example}">
    <div class="sphx-glr-thumbcontainer" tooltip="{title}" >

.. only:: html

  .. image:: {thumbnail}
    :alt:

.. raw:: html

      <div class="sphx-glr-thumbnail-title">{title}</div>
    </div>
    </a>

"""

def generate_thumbnail_rst(yml_content, image_file):
    return THUMBNAIL_TEMPLATE.format(
        link_to_example=yml_content["link_to_example"],
        title=yml_content["title"],
        thumbnail=image_file,
    )

def generate_gallery_rst(all_data, all_images):
    index_rst = ""
    index_rst += THUMBNAIL_PARENT_DIV
    for (yml_content, _), image_file in zip(all_data, all_images):
        example_rst = generate_thumbnail_rst(yml_content, image_file)
        index_rst += example_rst
    index_rst += THUMBNAIL_PARENT_DIV_CLOSE
    return index_rst

# --------------- write to file -------------------------------------------------------
def write_index_rst(readme_rst, gallery_rst, output_path):
    output_file = output_path / "index.rst"
    with open(output_file, "w") as f:
        f.write(readme_rst)
        f.write(gallery_rst)


# --------------- main ----------------------------------------------------------------
def main():
    all_data = collect_all()
    all_images = load_all_images(all_data, _output_path)
    readme_rst = read_readme(_GALLERY_PATH.parent / "README.rst")
    gallery_rst = generate_gallery_rst(all_data, all_images)
    write_index_rst(readme_rst, gallery_rst, _output_path)

if __name__ == "__main__":
    main()
