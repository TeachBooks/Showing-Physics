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

# Singing Rod
### Tones and Overtones


Author:     \
Time:	 10 minutes\
Age group:	14 - 18\
Concepts:	

## Introduction
This demonstration, if executed properly, generates a lot of noise at an irritating pitch. A demonstration that students will certainly not forget. By choosing the correct positions on the rod, you can even 'play' two overtones. Frequency measurements are straightforward, and the link to the physics of musical instruments is quickly established.


```{image} dm81_1_figure1.JPG
:width: 300px
:align: center
```
<center><i> Figure 1. Hold the rod in the middle for the fundamental tone. </i></center>

```{image} dm81_1_figure2.PNG
:width: 300px
:align: center
```
<center><i> Figure 2. Hold the rod a quarter length from the top for the first overtone. </i></center>

## Equipment
Measuring tape; aluminum rod (over 1 m long); fine sandpaper or a hammer; felt-tip pen or pencil; sound sensor with Coach 7 or phyphox app (Audio spectrum).

## Preparation
Mark the middle and a quarter length from the top of the rod with a dash. Ensure you can measure for a short time with a high measurement frequency. Practice beforehand how to achieve a higher sound level. Rub the sandpaper at the right pace and do not press too hard.


## Procedure
Hold the rod loosely in the middle. Rub the fine sandpaper along the rod until the rod starts to 'sing' (squeak/howl). By rubbing at the right pace, you can achieve a reasonable sound level. A short tap with a hammer on the rod also produces a nice tone.
Turn the rod around and ask the students where the sound of the rod is coming from exactly.
How can you stop the 'singing'? Let the students think with that information about whether the vibration of the rod is longitudinal or transverse and how to determine this.
Loosely hold the rod a quarter from the top. Rub the fine sandpaper along the rod until the rod starts to 'sing' (squeak/howl). By rubbing at the right pace, a high sound level can be achieved again. (If rubbing does not work, then tap the rod with a hammer.)
How does this tone differ from the first tone you heard?
Why do you need to hold the rod in a different place to hear this tone?
Measure the frequency of the tones with Coach 7 or phyphox and determine the speed of sound in the rod. The rod has two open ends.
Let the students sketch the vibration modes of the rod for the fundamental tone and overtone.
An experienced demonstrator can even produce a second overtone. Control questions: Where should you hold the rod then? Which tone do you dampen?

## Physics background
By rubbing with sandpaper, the rod vibrates both transversely and longitudinally. This can easily be demonstrated by making the rod 'sing' and then damping it. This damping occurs both at the ends in the longitudinal direction and by holding the rod (width direction). The rod vibrates in both directions.
For the fundamental tone, there is a node in the middle and a antinode at the ends. The wavelength is thus twice the length of the rod. The corresponding frequency can be calculated with:
$$
f = \frac{n \cdot v_{Al}}{2l}
$$
```{image} dm81_1_figure3.JPG
:width: 300px
:align: center
```
<center><i> Figure 3. The transversely drawn fundamental tone and the first overtone. </i></center>

The speed of sound in the rod can be calculated with: $ v = \sqrt{\frac{E}{\rho}} $
Here, E is the elastic modulus of the material used (71 GPa for aluminum) and ρ is the density of the rod. Conversely, you can use the measured frequency to determine the elastic modulus of the material.

When 'playing' the overtone, the nodes are at a quarter and three-quarter length of the rod.

```{image} dm81_1_figure4a.JPG
:width: 300px
:align: center
```
```{image} dm81_1_figure4b.PNG
:width: 300px
:align: center
```
<center><i> Figure 4. Results of audio spectrum measurement with phyphox and Fourier analysis in Coach 7 </i></center>


## Tips
It is important where you need to hold, halfway or a quarter. Rub the bottom of the rod in a short, quick motion. A hammer as a vibration source is handy if you have a rod with high density. When 'playing' the fundamental tone, an analysis tool will also find the second overtone, but not the frequency of the first overtone (figure 5). You can explain why this is with the help of figure 3.
Coach 7 with a short time (≈ 2 s) and a measurement frequency of about 2 kHz to perform as accurate Fourier analysis as possible.
Phyphox (Audio spectrum) quickly provides a measured frequency. The higher overtones are visible, but the corresponding peak values cannot be read. Export the measurement from phyphox to Excel.