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

# Up and down the hill: Accelerating along a Slope


Author: Freek Pols    \
Time:	20-30 minutes\
Age group:	16 - 18\
Concepts:	Newton's first law; acceleration

## Introduction
Students often find interpreting and connecting position, velocity, and acceleration in diagrams challenging. In this demonstration, we create a ($v,t$) graph during the motion, making it clear that the cart at the highest point does not have an acceleration of 0 m/s²! We use the didactic principles: think-pair-share.
[End Framework]

```{figure} demo69_figure1.jpg
---
width: 50%
align: center
---
The setup consists of the IOlab and a slope.
```

```{figure} demo69_figure2.JPG
---
width: 50%
align: center
---
Position, velocity, and acceleration
```

## Equipment
IOlab\
slope ~15 cm wide, 50 cm long\ 
computer and projection.

The IOLabs are available for loan. To borrow them, send an email to c.f.j.pols@tudelft.nl For returning the IOLabs, the shipping costs are borne by the school. Information about using the IOLab can be found here: https://www.iolab.science/getting_started.html and an introductory video below (use automated translation):


<div style='text-align: center;'>

```{code-cell} ipython3
:tags: [remove-input]
from IPython.display import YouTubeVideo
VideoWidth=600
YouTubeVideo("PwPCHZAv_gs", width=VideoWidth, align='center')
```

</div>  

## Preparation
Ensure that you are familiar with the IOlab, that you can read out sensors, and start and stop a measurement. Set up the apparatus, distribute graph paper, and connect the IOlab to the computer. Choose the "Wheel 100 Hz" option.

## Procedure
1. Explain what will happen in this demonstration. You give a cart a push, providing it with enough speed to travel up the slope and then roll back down. You decelerate the cart again. Measure the velocity of the cart and represent it in the ($v,t$) graph.
2. What ($v,t$) graph will emerge? Specify specific points in the graph (the intersection with the y-axis, the cart at the highest point, etc.) (think)
3. Ask students to compare their graph with that of their neighbors. (pair)
4. Ask a few students to show and explain their graph. (share)
5. Perform the demo: give the cart a good push up the hill (let go!) and catch it again on the way back down at roughly the same point.
6. Ask students to reflect on the similarities and differences between their graph and the measurements. Provide, when necessary, the correct interpretation of the measurement results, explicitly link the three graphs to each other and to the motion of the cart. This way, you can address: \
  a. At which point in the graph does the cart reach the highest point? \
  b. What does negative velocity mean?
7. Control question. A fun children's game is shooting a ball and then catching it. Draw the (v,t) graph of the ball from the moment you shoot it until you catch it.

```{figure} demo69_figure3.jpg
---
width: 50%
align: center
---
Shooting a ball
```


## Physics background
The kink in the ($v,t$) graph at 0 occurs because the friction force changes direction.

## Tips
• Graphically predicting velocity and acceleration is an essential part of this demonstration. Students must realize that what they thought may not match the measurements. Once such a 'cognitive conflict' arises, it can result in learning.
• The IOlab can be used in the same way for other motions, such as the transition from uniformly accelerated to uniform motion. Start the car at the top of the slope and let it drive horizontally. Follow the above steps again.
• If you weigh down the IOlab with, for example, 100 g, you will get data with less noise.
