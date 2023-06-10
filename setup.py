import setuptools

# Read the contents of README.md file as the long description
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


# Set the package version
__version__ = "0.0.0"


# Set variables for repository, author, and project information
REPO_NAME = "Chicken_diseases_classification"
AUTHOR_USER_NAME = "SatyaNerurkar"
SRC_REPO = "CNNClassifier"
AUTHOR_EMAIL = "satyanerurkar@gmail.com"


# Configure the package setup using setuptools
setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A deep learning project focused on the classification of coccidiosis in chickens.",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)