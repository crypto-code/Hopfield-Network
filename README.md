# Hopfield-Network
Create a Hopfield Network for Image Reconstruction

# What is a Hopefield Network ?

At its core a Hopfield Network is a model that can reconstruct data after being fed with corrupt versions of the same data. This neural network proposed by Hopfield in 1982 can be seen as a network with associative memory.

Lets say you hear a melody of a song and suddenly remember when you where on a concert hearing your favorite band playing just that song. That is associative memory. You get an input, which is a fragment of a memory you have stored in your brain, and get an output of the entire memory you have stored in your brain.

The Hopfield network here works in the same way. When the network is presented with an input, i.e. put in a state, the networks nodes will start to update and converge to a state which is a previously stored pattern. The learning algorithm “stores” a given pattern in the network by adjusting the weights. There is off course a limit to how many “memories” you can store correctly in the network, and empirical results show that for every pattern to be stored correctly, the number of patterns has to between 10-20% compared to the number of nodes.
