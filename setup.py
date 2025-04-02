import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "1.0.0"  # Yeh line sabse upar honi chahiye

REPO_NAME = "text-summarization-project"
AUTHOR_USER_NAME = "khushi152005"
SRC_REPO = "textsummarizer"
AUTHOR_EMAIL = "khushirathi2022@gmail.com"

setuptools.setup(
    name="textsummarization_project",
    version=__version__,  # Yaha __version__ use karo
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for NLP app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)
