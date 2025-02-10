from setuptools import setup, find_packages

setup(
    name='musicanalysis',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'librosa',
        'pydub',
        'SpeechRecognition',
        'madmom',
        'essentia',
    ],
    entry_points={
        'console_scripts': [
            # Add any command line scripts here
        ],
    },
)
