---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.10.3
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

# Radioactive decay - A simulation

Author:     \
Time:	one hour\
Age group:	Grade 11 and above\
Concepts:	radiation, radioactive decay, half-life

## Introduction
Radioactive decay is a statistical process. Radioactive decay is difficult to imagine. The statistical nature unknown to students can be visualised with this demonstration.
You have at your disposal a large number of cubes, cubes, with a rib of about 1.5 cm. Assume, for example, 300 cubes. Each cube is painted blue on one side and red on two sides. The other three sides are blank.
The statistical aspect of radioactive decay is simulated by throwing the coloured cubes. If you throw the cubes on the table like dice, about 1/6 part will end up with the blue side up, 2/6 part red, 3/6 part white.
You can remove the cubes with the red top and throw the rest back on the table. Again take away the cubes with the red top. And so on. After a number of throws, all the cubes with red tops have been taken away.
You could also have removed the blocks with a blue top. Then it will take more throws before all cubes are removed. 


```{figure} demo97_figure1.jpg
---
width: 50%
align: center
---
All cubes after the first roll.
```

```{figure} demo97_figure2.jpg
---
width: 50%
align: center
---
The cubes whose blue side ended up on top after this first roll are set aside.
```


## Equipment
For a good statistical approximation, an initial number of three hundred cubes is sufficient

## Preparation
You make the three hundred cubes by starting from a lath that has a square cross-section. You paint one side blue, two sides red. After sawing, three sides of the cubes are blank.

## Procedure
1a) Count the initial number of cubes.You denote that number by O(0). The letter O stands for Remaining. The number 0 stands for thrown 0 times.
Throw all cubes for the first time. Remove all the cubes that were placed with the red side up. The number of cubes remaining is called O(1).
This is the number of cubes remaining after one throw.
Throw the remaining cubes for the second time. Remove the red cubes again. Now the number of O(2) remains.
Do about 10 throws like this unless you run out of cubes before then.
1b) Draw the graph of the number of remaining cubes plotted against the number of throws, i.e. O(n) against n.
1c) Devise a formula showing the relationship between O(n) and the initial number of O(0).
1d) Draw the graph associated with this formula.
1e) Comment on the degree of agreement between the graph of counts and the graph of the formula.

2a) Predict the graph if you remove the cubes with blue top instead of those with red top.
2b) Do the counts and check how well the graph fits the theoretical graph.

Show a graph of the number of radioactive nuclei as a function of time. (Or of the radiation activity of a radioactive substance.) To that graph belongs the formula:
N(t)=N(0) (1/2)^(t/τ) or rather N(t)=k^t N(0)
The shape of the graph is very similar to that of the graphs of the counts of the remaining cubes. 

## Physics background
for the cubes, the number of cubes remaining depends on the number you start with as well as the probability that the red colour comes up;
	for the atomic nuclei, the number of times that remain depends on the number you start with as well as on the probability of a nucleus decaying. 

## Follow-up
In radioactive processes, a radioactive substance A decays into substance B. 
This was simulated by throwing the cubes (substance A). The red cubes (substance B) were taken away.
It is quite possible that substance B is itself radioactive and decays to substance C. So A → B→C.
Thereby, on the one hand, the number of nuclei B increases due to decay of A and, on the other hand, the number of nuclei B decreases due to decay to C. If substance C is stable, the amount of C will only increase.
You can also simulate this and do so by performing two kinds of throws in parallel. The first kind is the series described above. The second proceeds as follows.
Always collect the removed red cubes (substance B), but also throw them. Take them away when they turn blue (substance C). 
On the one hand, the number of red cubes taken away grows. But it also decreases because they turn blue when thrown.
The number of blue cubes will only increase.

```{tip}
Ìt is fairly easy to make a computer simulations of this 'decay process'.
```

## References
```{bibliography}
:filter: docname in docnames
```