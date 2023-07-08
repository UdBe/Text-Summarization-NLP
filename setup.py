import setuptools

__version__ = "0.0.0"

REPO_NAME = "Text-Summarization-NLP"
AUTHOR_USER_NAME = "UdBe"
SRC_REPO = "TextSummarization"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    description="End to End Machine Learning project to summarize text using NLP",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)