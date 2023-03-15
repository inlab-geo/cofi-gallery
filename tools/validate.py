import sys
import requests
import pathlib
import pytest

from utils import _GALLERY_PATH, existing_examples, read_yml


def examples_to_test():
    to_test = existing_examples()
    if len(sys.argv) > 1:
        specified_examples = sys.argv[1:]
        specified_examples = [f"{e}.yml" for e in specified_examples]
        to_test = [e for e in specified_examples if e in to_test]
    to_test = [f"{_GALLERY_PATH}/{e}" for e in to_test]
    print(f"Collected the following examples to test: {to_test}")
    return to_test

@pytest.fixture(params=examples_to_test())
def yml_path(request):
    return request.param

def check_example_data(yml_content):
    # "title" present and is non-empty
    assert "title" in yml_content
    assert isinstance(yml_content["title"], str)
    assert yml_content["title"]
    # "link_to_example" present and is a valid link
    assert "link_to_example" in yml_content
    response = requests.head(yml_content["link_to_example"])
    assert response.status_code < 400
    # "link_to_thumbnail" present and links to an image
    assert "link_to_thumbnail" in yml_content
    response = requests.head(yml_content["link_to_thumbnail"])
    assert response.status_code == 200
    assert "image" in response.headers['content-type']

def test_example(yml_path):
    yml_content = read_yml(yml_path)
    check_example_data(yml_content)

def main():
    pytest.main([pathlib.Path(__file__)])

if __name__ == "__main__":
    main()
