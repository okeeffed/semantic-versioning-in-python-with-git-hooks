import setuptools
import toml

with open("pyproject.toml", "r") as fh:
    toml_str = fh.read()

with open("README.md", "r") as fh:
    long_description = fh.read()

parsed_toml = toml.loads(toml_str)

setuptools.setup(
    name="demo_pip_math",
    version=parsed_toml['tool']['commitizen']['version'],
    author="Dennis O'Keeffe",
    author_email="hello@dennisokeeffe.com",
    description="Demo your first Pip package.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/okeeffed/your-first-pip-package-in-python",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    keywords='pip-demo math',
    project_urls={
        'Homepage': 'https://github.com/okeeffed/your-first-pip-package-in-python',
    },

)
