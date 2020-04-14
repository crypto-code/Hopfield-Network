# Hopfield-Network
Create a Hopfield Network for Image Reconstruction

## What is a Hopefield Network ?

At its core a Hopfield Network is a model that can reconstruct data after being fed with corrupt versions of the same data. This neural network proposed by Hopfield in 1982 can be seen as a network with associative memory.

Lets say you hear a melody of a song and suddenly remember when you where on a concert hearing your favorite band playing just that song. That is associative memory. You get an input, which is a fragment of a memory you have stored in your brain, and get an output of the entire memory you have stored in your brain.

<p align="center">
<img src="https://github.com/crypto-code/Hopfield-Network/blob/master/assets/model.gif" align="middle" />   </p>

The Hopfield network here works in the same way. When the network is presented with an input, i.e. put in a state, the networks nodes will start to update and converge to a state which is a previously stored pattern. The learning algorithm “stores” a given pattern in the network by adjusting the weights. There is off course a limit to how many “memories” you can store correctly in the network, and empirical results show that for every pattern to be stored correctly, the number of patterns has to between 10-20% compared to the number of nodes.

## How it Works ?

The units in Hopfield nets are binary threshold units, i.e. the units only take on two different values for their states and the value is determined by whether or not the units' input exceeds their threshold. Hopfield nets normally have units that take on values of 1 or -1. 

Hopfield nets have a scalar value associated with each state of the network, referred to as the "energy", E, of the network, where:

<p align="center">
  <img src="https://github.com/crypto-code/Hopfield-Network/blob/master/assets/energy.svg" align="middle"/> </p>

This quantity is called "energy" because it either decreases or stays the same upon network units being updated. Furthermore, under repeated updating the network will eventually converge to a state which is a local minimum in the energy function.

Training a Hopfield net involves lowering the energy of states that the net should "remember". This allows the net to serve as a content addressable memory system, that is to say, the network will converge to a "remembered" state if it is given only part of the state. The net can be used to recover from a distorted input to the trained state that is most similar to that input. This is called associative memory because it recovers memories on the basis of similarity. For example, if we train a Hopfield net with five units so that the state (1, -1, 1, -1, 1) is an energy minimum, and we give the network the state (1, -1, -1, -1, 1) it will converge to (1, -1, 1, -1, 1). Thus, the network is properly trained when the energy of states which the network should remember are local minima.

## Usage

- To train a Hopfield Network on a dataset of images, first place the images in the /train folder (A few images are already provided). Then run train.py script.

### Result:
<p align="center">
  <img src="https://github.com/crypto-code/Hopfield-Network/blob/master/assets/result_0.png" height=400 align="middle"/> </p>
  
 <p align="center">
  <img src="https://github.com/crypto-code/Hopfield-Network/blob/master/assets/result_1.png" height=400 align="middle"/> </p>

This script trains the network on the provided images and tests image recounstruction by using the "images+random noise" as input. As seen above the images are reconstructed almost perfectly.


- To train a Hopfield Network to reconstruct images from custom noisy images, first place the train images in the /train_custom folder and the noisy images in /test_custom folder (A few images are already provided). Then run train_custom.py script.

**Note: The noisy images should have same name as its corresponding train image**

### Result

<p align="center">
  <img src="https://github.com/crypto-code/Hopfield-Network/blob/master/assets/result_0_custom.png" height=400 align="middle"/> </p>
  
As you can see above the unwanted parts of the images are removed. In the first image the **&** is removed and in the second the man's glasses is removed almost perfectly.


### Model Weights:
**Note: If you want to plot the weights of the network, just uncomment line:116 in train.py and line:124 in train_custom.py**
<p align="center">
  <img src="https://github.com/crypto-code/Hopfield-Network/blob/master/assets/weights.png" align="middle"/> </p>
  
# G00D LUCK

For doubts email me at:
atinsaki@gmail.com
