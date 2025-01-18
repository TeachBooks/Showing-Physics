# Alternating voltage across a lamp

<span style="font-size: 25px; color: gray;">Quick computer measurements to measure alternating voltage and luminosity</span>

<table style="width: 100%; border-collapse: collapse; border: none;">
    <tr style="background-color: var(--background-color);">
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">Author:</td>
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">Norbert van Veen and Freek Pols</td>
    </tr>
    <tr style="background-color: var(--background-color);">
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">Time:</td>
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">10-20 minutes</td>
    </tr>
    <tr style="background-color: var(--background-color);">
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">Level:</td>
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">Grade 9 and up</td>
    </tr>
    <tr style="background-color: var(--background-color);">
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">Concepts:</td>
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">Alternating voltage, direction of electric current, power, luminosity, frequency</td>
    </tr>
</table>

## Introduction
This demonstration shows the alternating voltage across a (incandescent-bicycle) lamp and the changing luminosity of the lamp. Is the frequency the same? Are the voltage and luminosity in phase? 

```{figure} demo48_figure1.JPG
---
width: 70%
align: center
name: demo48_fig1
alt: the setup with light bulbs in series and a voltage meter
---
The setup includes a voltage sensor (range -10 to 10 V) and a luminosity sensor.
```

## Equipment
* Setup with lamp and AC power source
* Incandescent lamp (6V)
* Voltage sensor
* Luminosity sensor
* Educational science software or an oscilloscope
* Optional: table top set of fluorescent light, see {numref}`Figure {number}<demo48_fig3>`

```{figure} demo48_figure3.jpg
---
width: 70%
align: center
name: demo48_fig3
alt: a setup with a incandescent lamp and a photodiode
---
Optionally one can do measurement on a fluorescent light.
```

## Preparation
Set up the apparatus as shown in {numref}`Figure {number}<demo48_fig1>`. Connect the voltage and luminosity sensors to your measurement device. Ensure the digital readings can be seen by all students. Test the luminosity sensor and adjust its distance from the lamp so that the measured luminosity is within the sensor's range. Set a trigger condition to enhance the display of both signals.

```{tip}
Secure the luminosity sensor in a stand to keep it at the correct height above the lamp and prevent it from receiving too much or too little light.
```

```{figure} demo48_figure2.JPG
---
width: 70%
align: center
name: demo48_fig2
alt: the graphs in one diagram showing the applied and measured voltage. Frequency of measured voltage across light is twice as high.
---
Two measurements in one diagram: the alternating voltage across the lamp and the luminosity of the lamp over time.
```

## Procedure
1. Point to the fluorescent lights at the ceiling, and ask students to sketch a graph of luminosity versus time. Is it constant or does it alter as function of time?
2. Determine the frequency of the light from the fluorescent lights using the light sensor. Do not explain the exact frequency yet; this will come later in the demonstration. If you have a tabletop set available, you can show how the luminosity changes as function of the position (the luminosity is far less at both ends of the lamp).
3. Introduce the demonstration to further investigate the flickering of light.
4. Place the setup on the desk and discuss the circuit. Draw the circuit diagram on the board and perform an initial measurement showing only the alternating voltage across the lamp.
5. Discuss the shape of the alternating voltage with the students. Ask how the direction of the current changes. Discuss the frequency and whether it is familiar to them. 
6. Position the luminosity sensor near the setup. If you haven't done yet with the fluorescent lights, explain what the sensor measures. Ask students to individually sketch a graph predicting the luminosity measurement.
7. Perform a measurement of both luminosity and alternating voltage. Determine the frequency of the alternating voltage and the luminosity. Do they have the same frequency? Why (not)? 
8. Ask students how the graphs would change if direct current (DC) was used instead of alternating current (AC). Demonstrate this.
9. Extend the demonstration with measurements on LED lighting. You can discuss why it is important in various workplaces that special lighting is used, see also our [demonstration on sampling](../demo44/demo44.md).

```{figure} demo48_figure4.jpg
---
width: 70%
align: center
name: demo48_fig4
alt: oscilloscope showing the actual measurement
---
Why is the measured frequency 100 Hz?
```

## Physics background
The alternating voltage from our power grid changes at 50 Hz (60Hz in the US), as does the alternating current. In each period, the voltage and current rise and fall twice. The direction of the current does not influence the lightning of an incandescent lamp. Therefore, the lamp's brightness fluctuates exactly twice as much. Students can quickly grasp this explanation, though they might not think of it on their own. Students have often the idea that light sources do not vary in intensity as they do not perceive this {cite}`Bacalla2013`.

## References
```{bibliography}
:filter: docname in docnames
```
