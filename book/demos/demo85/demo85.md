

<div style="clear: both;">

```{figure} ../../figures/ready.png
---
width: 35%
align: right
```

</div>

# Slow Bulbs: PTC Behavior of Filament Made Visible

Author: Wouter Spaan\
Time:	10-20 minutes\
Age group: 12 - 18\
Concepts:	Elektricity, PTC, series circuit, 

<iframe width="560" height="315" src="https://www.youtube.com/embed/uR8OAaPxcOc?si=9oiqfgcw83XOB3O3" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Introduction

This surprising demonstration makes the PTC (Positive Temperature Coefficient) behavior of light bulbs visible. Explaining the observations requires a lot of [thinking-back-and-forth](../../Pedagogy/BackAndForthThinking.md). The demonstration you can be conducted  at various levels. It is especially suitable for checking students' understanding of resistance, current and voltage in series circuits.

FILMPJE NODIG

## Equipment

- Power source
- 4 or 5 identical light bulbs including connection materials.

## Preparation
Set up and already connect the links between the light bulbs, showing clearly that the light bulbs are in series. Draw the circuit on the board. 

```{figure} demo85_figure1.JPG
---
width: 50%
align: center
---
During the demonstration, you continuously move the connection of the negative terminal from left to right, so that the first time only one bulb is switched on and the last time all bulbs are connected.
```

## Procedure
To start, perform the demo by step-by-step connecting more light bulbs to the power source, with the voltage remaining constant. The students record their observations. Then briefly summarize the observations on the board. Possible observations include:
- Only bulbs between the connections light up.
- The more bulbs are connected, the less brightly they glow.
- The last bulb you connect gradually glows brighter, while the other connected bulbs immediately glow at their final brightness.
- As you connect more bulbs, it takes increasingly longer for the last connected bulb to reach its final brightness.

```{figure} demo85_figure2.JPG
---
width: 50%
align: center
name: demo85_2
---
The situation just after moving the connection. The third bulb is barely visible and needs some time to become as bright as the other two.
```

Then, a discussion follows about possible explanations. The third and fourth observations are the most interesting; you can use the explanation for the first two to retrieve prior knowledge. Explaining all these observations requires thinking-back-and-forth, and it is important to pose probing questions and let students use technical language. 

```{tip}
For explaining the third observation is to ask about what happens to the resistance of a light bulb when the bulb lights up. If the fourth observation hasn't been made yet, it offers an opportunity for a prediction. Students can also predict what happens to the current during the slow brightening of the last connected bulb. It will decrease; visible with a current meter.
```

## Physics background
The explanation is best linked to the third and fourth observations in the situation of {numref}`Figure {number} <demo85_2>` where the third light bulb has just been connected: the temperature of bulb 1 and 2 is higher than that of bulb 3 because bulbs 1 and 2 have already been lit up and bulb 3 has not. Hence, their resistance is higher than that of bulb 3, and thus bulbs 1 and 2 receive a larger share of the voltage. 

After connecting, the temperature (and thus the resistance) of bulb 3 increases, so it receives more and more voltage (and bulbs 1 and 2 receive less, but the decrease in brightness is not visible to the naked eye). The fourth observation: as more bulbs are in series, the total resistance is greater, and thus the current is smaller, causing the temperature of the last bulb to increase more slowly. This leads to a slower increase in voltage across it and thus a slower increase in brightness. Finally, what happens to the current: the resistance of the last connected bulb increases, so the total resistance in the circuit increases and the current decreases.

<iframe width="560" height="315" src="https://www.youtube.com/embed/jCy5vrm7AQo?si=KC8J0k-dzFOa_lHe" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Follow up
The demonstration is suitable for further investigations, especially when senors (or an oscilloscope) are available. In the picture below one can observe [hysteresis](https://en.wikipedia.org/wiki/Hysteresis) when applying a AC signal to a series circuit with an Ohmic resistor and a light bulb.