from setuptools import setup, find_packages

setup(
    name="auto-subtitle-turkish",
    version="1.0.0",
    description="Fork of auto-subtitle with Turkish translation support",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Cayrop/auto-subtitle-turkish",
    packages=find_packages(),
    install_requires=[
        "ffmpeg-python",
        "openai-whisper",
        "transformers",
        "sentencepiece",
        "numpy==1.26.4"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',
    entry_points={
        "console_scripts": [
            "auto-subtitle=auto_subtitle.main:main",
        ],
    },
)
