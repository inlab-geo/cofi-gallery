import sys

from utils import _GALLERY, _GALLERY_PATH, _TEMPLATE_PATH, existing_examples


def get_example_name():
    if len(sys.argv) < 2:
        raise ValueError(
            "Please specify an example name in snake case. "
            "e.g. `python tools/new_example.py my_cool_example`"
        )
    name = sys.argv[-1]
    print(f"[INFO] Collected example name: {name}")
    return name

def validate_example_name(example_name):
    existing_names = existing_examples()
    if f"{example_name}.yml" in existing_names:
        raise ValueError(
            "Your name clashes with an existing example. Please provide another name."
        )

def generate_yml_file(example_name):
    print(f"[INFO] Generating a new yml file: `{_GALLERY}/{example_name}.yml`")
    dst_path = _GALLERY_PATH / f"{example_name}.yml"
    with open(_TEMPLATE_PATH, "r") as f:
        template_content = f.read()
    with open(dst_path, "w") as f:
        f.write(template_content)

def post_generate(example_name):
    print(f"[INFO] New file generated from template")
    print(f"[INFO] Please navigate to {_GALLERY_PATH}/{example_name}.yml "
           "to insert your example information")

def main():
    name = get_example_name()
    validate_example_name(name)
    generate_yml_file(name)
    post_generate(name)

if __name__ == "__main__":
    main()
