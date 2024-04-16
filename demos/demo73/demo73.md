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

# Determination of g: But with precision!


Author: Freek Pols     \
Time:	 20 minutes 	\
Age group:	14 - 18\
Concepts:	

## Introduction
In physics class, you can experimentally determine the acceleration due to gravity. But how precise is the result? What should you pay attention to if you want to make a very precise determination? How do you quantify the accuracy with which you have determined the gravitational acceleration? Not ready for the mathematical side? Then you can also do this demonstration perfectly at the open evening by using the phyphox app without emphasizing the associated uncertainty.

```{figure} demo73_figure1.jpg
---
width: 300px
align: center
---
The hammer is suspended at a great height with a string attached to a balloon.
```


## Equipment
Fully inflated balloon; hammer; phone with phyphox app; string; wooden plank; framework for the setup; needle; measuring tape.

## Preparation
Inflate the balloon and hang the hammer with a string from the balloon. Hang the whole setup on the framework and ensure the wooden plank is directly beneath the hammer. Use the acoustic chronometer with a threshold value of 0.35 and a delay of 0.3 s.

## Procedure
Begin the demonstration by discussing what a precise measurement entails and why an accurate value of g can be important. It's interesting to know that oil exploration relies on determining the acceleration due to gravity very precisely.

You can then explain the experiment: With a single measurement and using the equation , we will determine g as accurately as possible. Piercing the balloon starts the acoustic chronometer, and the hammer's impact on the ground stops the timer.
• Is it necessary for a good measurement to have the largest or smallest possible falling height? Are there any conditions on the extreme values you choose?
• Where should you hold the phone? At the top, bottom, middle, or does it not matter? Why?
• How precisely do we measure the time and height?

Have students brainstorm answers to the questions in pairs, write down the answers, and then invite students to share their answers (think, pair, share).
After measuring the falling height (with an estimate for the uncertainty) and determining the fall time, you can start a discussion about the uncertainty in the time measurement. Is it 1.0 s, 0.1 s, 0.01 s, or 0.001 s? Or is it something in between?

Normally, you determine the uncertainty in time based on repeated measurements, but what numbers do you expect to see when you repeat the measurement? And which decimal digit will vary?
By using the provided Jupyter Notebook file, you can calculate the final value of g with its associated uncertainty.

```{figure} demo73_figure2.jpg
---
width: 300px
align: center
---
The measurement results obtained in the experiment.
```

Control Question: We obtained the measurement results from figure 2. What information is needed to make a statement about the reliability of the measurements?

```{note}
Jupyter Notebook is een open-source webtoepassing die verschillende programmeertalen ondersteunt, waaronder Python. Het makkelijkst om de Notebook te gebruik is via https://colab.google/ Je kunt daar de Notebook uploaden. Zie https://youtu.be/C2yunJ9o2yo voor een verdere instructie.
```

## Physics background
Every measurement can only be done with a certain precision. Sometimes the precision is determined by the equipment, and sometimes by the property you are measuring. In science, the answer is always given with the associated uncertainty, where the chance that a repeated measurement falls within the value with its associated uncertainty is equal to 68% (). When multiple quantities play a role, as in the determination of the acceleration due to gravity, each measurement contributes. The final value of the uncertainty in this equation is given by:

The uncertainty is always given with only one significant figure. The final answer is given with the same decimal digit (e.g., 9.8 ± 0.3 m/s²).

```{tip}
The NLT module Measuring and Interpreting provides more starting points around the theme of measurement uncertainty. A nice follow-up is to have students work with one of the various methods to determine g (e.g., with a pendulum, ball with magnetic switch, Ehrlig's drop method, acceleration along a slope with an air-cushioned track) and present the method (with its pros and cons). The University of Aachen has a video demonstrating this experiment: https://youtu.be/zRGh9_a1J7s.
```