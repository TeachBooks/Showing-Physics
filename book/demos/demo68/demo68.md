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

# Collisions: Newton's Third Law 

Author: Freek Pols    \
Time:	 15-20 minutes\
Age group:	16 - 18\
Concepts:	

## Introduction
Students find Newton's third law difficult to grasp. It is counterintuitive. This demonstration specifically addresses that aspect: in collisions, there are force pairs, where forces are equal (independent of masses) but opposite in direction. We use two didactic principles in this demonstration: think-pair-share and then P(E)OE.
[End Framework]

```{figure} demo68_figure1.jpg
---
width: 50%
align: center
---
You use two IOlabs, one of which is weighted.
```

```{figure} demo68_figure2.JPG
---
width: 50%
align: center
---
The forces on the IOlabs are equal in magnitude but opposite in direction. These forces also act for the same duration.
```


## Equipment
2x IOlab; mass; double-sided tape; computer.

The IOLabs are available for loan. To borrow them, send an email to c.f.j.pols@tudelft.nl For returning the IOLabs, the shipping costs are borne by the school. Information about using the IOLab can be found here: https://www.iolab.science/getting_started.html and an introductory video below (use automated translation):


<div style='text-align: center;'>

```{code-cell} ipython3
:tags: [remove-input]
from IPython.display import YouTubeVideo
VideoWidth=600
YouTubeVideo("PwPCHZAv_gs", width=VideoWidth, align='center')
```

## Preparation
Ensure that you are familiar with the IOlab, that you can read out sensors, and start and stop a measurement. Wind up the spring on one IOlab and attach the ring to the other. Weight one of the two IOlabs. Affix the weighting with double-sided tape. Create a track so that the motion of the IOlabs before and after the collision remains linear. The IOlab tends to go around the corner during collision.

## Procedure
1. Explain what happens in this demo: one of the carts collides while moving with the other cart. Measure the forces exerted by the carts on each other as a function of time and display them in a graph. Demonstrate the operation of the force sensor by compressing the spring while the measurement is running. 
2. Predict how the two (F,t) graphs will look. Specify specific points in the graph Without giving away too much in the explanation about what might be important points. An alternative is to show a number of (F,t) graphs and let the students choose and justify their choice (think). 
3. Compare your graph with that of your neighbor (pair). 
4. Ask some students to explain their graph (share). 
5. Perform the demo. 
6. Provide an explanation for the similarities and differences between your own graph and the measurements. 
7. Would it matter if the other cart was already moving before the collision? If so, why? Demonstrate it. 
8. Build on students' responses, with some guiding questions, you can help students build a reasoning. Summarize Newton's third law with them. 
9. Control question: A truck has broken down. Fortunately, a motorist is kind enough to push the truck to the nearest garage. Consider the following two situations: 
  9.1) The car accelerates to a speed of 50 km/h 
  9.2) The car travels at a constant speed of 50 km/h. 
  F_auto is the force exerted by the car on the truck. F_v,w is the force exerted by the truck on the car. What applies to the force interaction between the car and the truck?: 
  F_auto > F_v,w in both situations 
  F_auto = F_v,w in both situations 
  F_auto < F_v,w in both situations 
  F_auto > F_v,w in situation 1 but not in situation 2 

```{figure} demo68_figure3.jpg
---
width: 50%
align: center
---
The car pushes the truck to the nearest garage.
```

## Physics background
Forces always come in pairs. Newton's third law provides an even more precise description of those pairs: the magnitudes of the forces are equal and the directions are opposite. Summarized in a formula: $F_{1→2}=-F_{2→1}$.