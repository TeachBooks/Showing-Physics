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

# Self-propelling car violates conservation of momentum?

Author:     Leo te Brinke\
Time:	  	  15 minutes\
Age group:	15 - 18\
Concepts:	  (conservation of) linear momentum, Newtons third law, rolling resistance

## Introduction
Conservation of linear momentum can be shown by mounting a pendulum on an easy-rolling cart. Pendulum and cart will always move in opposite directions. At the moment the pendulum is released the total linear momentum is zero, and of course it will stay that way.
If the cart turns out to ride away, even if it is in a jerky way, something must be wrong with a fundamental conservation law, isn’t it?
Most of us know from our childhood that if you’re sitting in a cart, you can move forward without touching the ground, just by moving your upper body back and forward in the right way.
This experiment will only succeed if the cart is not running too smoothly, so friction is part of the secret. It’s not really a spectacular experiment, but it’s something that gets you thinking about physics.

```{figure} demo15_figure1.jpg
---
width: 300px
align: center
---
The demo is easy to set up
```

## Equipment
A suitable cart with a specially-prepared asymmetric pendulum, with a suitable mass on a suitable surface.

## Preparation
The cart should run with a small amount of friction, and it is important that this rolling resistance force with the underlying surface is constant. Our cart isn’t much more than a block of wood with three ball-bearings as wheels.
•	Mount a pendulum on the cart, make sure the whole construction, including the pendulum plus weights, is stable.
•	Mount about halfway the pendulum a cross bar to stop the string of the pendulum. It must be easily removable and adjustable in height.
So this pendulum is alternatingly long during half a period and short during the other half period.
Now it’s a matter of trial-and error: due to resistance the cart should only move during the ‘short’ half-period, and not during the ‘long’ half-period. To achieve that you can vary and tune the following variables to maximum effect:
•	the amplitude 
•	the mass of the pendulum
•	the height of the cross-bar
•	the mass of the cart itself 
•	de underlying surface
After all the cart should jerkily ride into one direction, after releasing the pendulum. 

<div style='text-align: center;'>

```{code-cell} ipython3
:tags: [remove-input]
from IPython.display import YouTubeVideo
VideoWidth=600
YouTubeVideo("AlzA5F4IBhw", width=VideoWidth, align='center')
```

</div>

Our cart has a total mass of about one kilogram (including the pendulum), the mass of the pendulum is 0,10 kg, the pendulum has a length of 65 cm and the crossbar is about 45 cm underneath the point of suspension.

## Procedure
First show the cart without cross-bar and ask for predictions what will happen after the pendulum has been released. Verify the predictions and discuss the outcome; this can be done considering conservation of momentum or Newtons third law.
Then show that the cart doesn’t move when the amplitude is too small, and discuss the reason for this.
The final question is whether there is a way to get the cart moving in one direction. After having discussed that, it is time for the experiment: mount the cross-bar and show it…
Ask the audience to look closely at the motion of the cart: during which stage of the oscillation does it move?

```{figure} demo15_figure2.jpg
---
width: 300px
align: center
---
The demo is easy to set up
```

The discussion that follows must make clear in which way the properties of rolling resistance are responsible for this phenomenon.
After that there might be discussion about the question if this could also work with a sleigh, an air-cushion vehicle, or a boat.

```{tip}
A thorough preparation is very important for this experiment to make sure it will work. In the case your demonstration table is not perfectly horizontal: don’t try to ride uphill but accept a little help from gravity…
The demonstration could be expanded by using two different surfaces. On a very smooth surface conservation of momentum will occur regardless of the pendulum’s properties, on a surface with more friction it won’t. 
This experiment can be used as a design assignment too. In that case the cart must be built with hardly any instructions and then be optimised for the experiment. That’s only feasible when all the variables are being changed one-by-one in a very systematic way.
```

## Physics background
The pendulum bob is alternatingly accelerated and decelerated to the left and to the right.  So there must be an alternating force from the suspension point on the pendulum bob and - according to Newtons third law - also from the pendulum bob on the suspension point. It is important to realize that a force on the suspension point also means a force on the cart. 
If there is only mutual interaction the total linear momentum will be conserved which causes the momentums of the cart and the pendulum to be equal and have opposite directions. A small resistance between the underlying surface and the cart will cause gradual loss of energy but this won’t change the equality of momentums. And if the amplitude is sufficiently small the force on the suspension point will not exceed the maximum rolling resistance and the cart will not move.
But if the pendulum is asymmetric, the force between pendulum and suspension point in one direction will be smaller but lasting longer than the force in the opposite direction. In this situation you can arrange it in such way that in one direction the force exceeds the maximal rolling resistance, but in the opposite direction it does not. So the cart will have a pulsed acceleration in one direction. In this situation there is an external force (friction), so linear momentum is no longer conserved. 
The phenomenon can also be explained with Newtons laws: if the forces in both directions are equal and acting for equal intervals, then the acceleration in both directions will be equal too, as well as the increase and decrease of velocity. A friction force will not change that as long as it is equally strong in both directions. But due to the fact that rolling resistance has a maximum value, things are different as soon as the forces to the left and to the right are different.
This experiment could work with a sleigh (sliding resistance) as well, but not with a boat or a flying vehicle, because air-resistance and resistance in liquids are velocity-dependent and don’t have a maximum value. 


## Follow-up
The phenomenon can be visualised by making graphs of the forces vs. time. You might sketch graphs of:
-	the force on the suspension point
-	the rolling resistance force
-	the resultant force
just straight above one another with the same time axis.
Instead of sketching the graphs you could also have them calculated and drawn by means of a mathematics modelling programme.

NOTE: Here still to put graphs generated by a modelling program which will be available on the website.

Of course, the motion of the cart and the pendulum can also be measured and analysed, e.g. by means of a video-measurement. In the case of a symmetric pendulum the amplitudes of the cart and the pendulum could be compared to their masses.

## References
```{bibliography}
:filter: docname in docnames
```