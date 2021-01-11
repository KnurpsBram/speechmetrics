# -*- coding: utf-8 -*-


from setuptools import setup, find_packages

setup(
    name="speechmetrics",
    version="1.0",
    packages=find_packages(),

    install_requires=[
        'numpy',
        'scipy',
        'tqdm',
        'resampy',
        'pystoi',
        'museval',
        'gammatone @ git+https://github.com/detly/gammatone',
        'pypesq @ git+https://github.com/vBaiCai/python-pesq',
        'srmrpy @ git+https://github.com/KnurpsBram/SRMRpy',
    ],
    extras_require={
        'cpu': ['tensorflow', 'librosa'],
        'gpu': ['tensorflow', 'librosa'],
    },
    include_package_data=True
)
