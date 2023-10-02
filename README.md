This repo contains code for the Nova Science coding group.

This [online book](https://d2l.ai/) is quickly becoming the standard text 
for Deep Learning.

And here is [repo](https://github.com/n2cholas/awesome-jax) with list of projects in JAX. 

## Model notebooks available

The mnist.ipynb notebook builds a simple MNIST classifier. Here is a Google Colab [version](https://drive.google.com/file/d/1BC1wEJzWNIVZipLcmEBGOozb5aQ0uXHN/view?usp=sharing). And for a classification over 99.5% please consult the Jiucheng branch.

The vae_mnist.ipynb notebook builds a very simple Variational Autoencoder for the MNIST dataset. 
Here is a Colab [version](https://drive.google.com/file/d/11Qh29nHsXIM_TXJy-E1syoB2hUjyzfUC/view?usp=sharing). And here is a very readable elementary [introduction](https://www.jeremyjordan.me/variational-autoencoders/) to VAE.

The ppo.ipynb notebook trains an agent to control a cart-pole with reinforcement learning. Here is a Colab [version](https://drive.google.com/file/d/1LLt9nWuoFcJKEFpNYtUrYFsGF1u5UKMS/view?usp=sharing). This blog has a simple [introduction](https://towardsdatascience.com/proximal-policy-optimization-ppo-explained-abed1952457b) to the PPO algorithm. The notebook is an adaptation of a notebook from this [blog](https://chrislu.page/blog/meta-disco/) which also provides evidence for the extereme speedups and new opportunities afforded by using JAX end-to-end in reinforcement learning.

The diffusion.ipynb notebook trains a basic Denoising Diffusion probabilistic model.
## JAX idiosyncrasies notebooks available

The rng.ipynb notebook explains Pseudo Random Number Generation in JAX. Here is a Google Colab [version](https://drive.google.com/file/d/1gXnED5oyTWUazb_z4oJroB54vngdZ6mn/view?usp=sharing).

The autodiff.ipynb looks of examples of how autodiff is used in JAX. Here is a Google Colab [version](https://colab.research.google.com/drive/1ITvjHj_2ykypuAWumTIAwBO28dZ-tUij?usp=sharing).

The pytrees.ipynb looks at structure and utilities for pytrees. Here is a Google Colab [version](https://colab.research.google.com/drive/1PuSNaXscZC7joS4cxl6IqWg6jsNOdWMg?usp=sharing). 

The state.ipynb notebook investigates how program state is handled in purely functional JAX. Here is the Colab [version](https://colab.research.google.com/drive/1ixnTRFpWp_-x7GAfJO3c5cVkNLMw62jj?usp=sharing).

The jtransform.ipynb notebook investigates how JAX tranforms functions based on their intermediate langage *jaxpr* representations. Here is the Colab [version](https://drive.google.com/file/d/1pW7npFTBEom9a_R-qtXghH1syhRkuLjy/view?usp=sharing).
