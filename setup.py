from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="bartscore",
    version="0.1.0",
    author="NeuLab",
    author_email="",
    description="BARTScore: A text generation evaluation metric based on BART",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/neulab/BARTScore",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Text Processing :: Linguistic",
    ],
    python_requires=">=3.6",
    install_requires=[
        "torch>=1.6.0",
        "transformers>=4.6.1",
        "numpy>=1.18.5",
        "tqdm>=4.60.0",
        "tabulate>=0.8.9",
        "scipy>=1.4.1",
        "nltk>=3.6.2",
        "sacrebleu>=1.5.1",
    ],
    extras_require={
        "full": requirements,
    },
)
