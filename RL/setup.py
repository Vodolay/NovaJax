import os.path
import sys
import itertools
import re


from setuptools import find_packages, setup

# Don't import gym module here, since deps may not be installed
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "gym"))
from version import VERSION

# Environment-specific dependencies.
extras = {
    "atari": ["ale-py~=0.8.0"],
    "accept-rom-license": ["autorom[accept-rom-license]~=0.4.2"],
    "box2d": ["box2d-py==2.3.5", "pygame==2.1.0", "swig==4.*"],
    "classic_control": ["pygame==2.1.0"],
    "mujoco_py": ["mujoco_py<2.2,>=2.1"],
    "mujoco": ["mujoco==2.2", "imageio>=2.14.1"],
    "toy_text": ["pygame==2.1.0"],
    "other": ["lz4>=3.1.0", "opencv-python>=3.0", "matplotlib>=3.0", "moviepy>=1.0.0"],
}

# Meta dependency groups.
'''extras["nomujoco"] = list(
    set(
        [
            item
            for name, group in extras.items()
            if name != "mujoco" and name != "robotics"
            for item in group
        ]
    )
)'''

all_groups = set(extras.keys()) - {"accept-rom-license"}
extras["all"] = list(
    set(itertools.chain.from_iterable(map(lambda group: extras[group], all_groups)))
)


setup(
    name="gym",
    version=VERSION,
    description="The OpenAI Gym: A toolkit for developing and comparing your reinforcement learning agents.",
    url="https://github.com/openai/gym",
    author="OpenAI",
    author_email="gym@openai.com",
    license="",
    packages=[package for package in find_packages() if package.startswith("gym")],
    zip_safe=False,
    install_requires=[
        "numpy>=1.18.0",
        "cloudpickle>=1.2.0,<1.7.0",
    ],
    extras_require=extras,
    package_data={
        "gym": [
            "envs/mujoco/assets/*.xml",
            "envs/classic_control/assets/*.png",
            "envs/robotics/assets/LICENSE.md",
            "envs/robotics/assets/fetch/*.xml",
            "envs/robotics/assets/hand/*.xml",
            "envs/robotics/assets/stls/fetch/*.stl",
            "envs/robotics/assets/stls/hand/*.stl",
            "envs/robotics/assets/textures/*.png",
        ]
    },
    tests_require=["pytest", "mock"],
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
