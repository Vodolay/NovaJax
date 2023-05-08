This folder contains training and visualization code related to Reinforcement Learning. Checkpoints are also provided. Gif's illustrate the actions of the trained agents. The notebooks should work with any of the environment from [Gymnax](https://github.com/RobertTLange/gymnax) with only minor modifications.
Howevere, the visualisation notebook requires gym==0.19.0 which will not install with the current version of setuptools. Please download and insert the file setup.py in the gym-0.19.0 directory and then run 'pip install .'

## Notebooks available

The cartpole_ppo.ipynb notebook trains an agent to control CartPole-v1 (Google Colab [version](https://drive.google.com/file/d/13aaeP5O1ptJAqx4kZ0p9sUwxMPzhoPuD/view?usp=sharing)).
The cartpole_visual.ipynb (Google Colab [version](https://drive.google.com/file/d/19te80gnCa1VYN_aQXYhnPlouE0YL2EFe/view?usp=sharing))
loads the trained agent from a checkpoint and produces the following animation
![CartPole-v1](cartpole.gif). 


