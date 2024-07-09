```{figure} ../../figures/ready.png
---
width: 35%
align: right
```
# Alternating voltage over a Lamp

<span style="font-size: 25px; color: gray;">Quick computer measurements to measure alternating voltage and luminosity</span>


<table style="width: 100%; border-collapse: collapse; border: none;">
    <tr style="background-color: var(--background-color);">
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">Author:</td>
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">Norbert van Veen</td>
    </tr>
    <tr style="background-color: var(--background-color);">
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">Time:</td>
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">10-20 minutes</td>
    </tr>
    <tr style="background-color: var(--background-color);">
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">Level:</td>
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">Grade 3 and up</td>
    </tr>
    <tr style="background-color: var(--background-color);">
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">Concepts:</td>
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">Alternating voltage, direction of electric current, power, luminosity, frequency</td>
    </tr>
</table><br>

## Introduction
This demonstration shows the alternating voltage across a (bicycle) lamp, the changing luminosity of the lamp, and the difference between the voltage and luminosity changes. As both quantities change rapidly over time, they need to be measured at a high frequency. This can be easily done using the Coach program. Students will see in a diagram how quickly the voltage changes sign and will be asked to predict how the luminosity changes.

## Equipment
* Setup with lamp and AC power source
* Bicycle lamp
* Voltage sensor
* Luminosity sensor
* Coach7 measurement program
* CMA files

## Preparation
Set up the apparatus as shown in {numref}`Figure {number}<demo48_fig1>`. Connect the voltage and luminosity sensors to an interface and start the Coach measurement program. Ensure the interface is recognized and displays a standard diagram of voltage versus time. Test the luminosity sensor and adjust its distance from the lamp so that the measured luminosity is within the sensor's range. Set a trigger condition to stabilize the display of both signals.

```{figure} demo48_figure1.JPG
---
width: 50%
align: center
name: demo48_fig1
---
The setup includes a voltage sensor (range -10 to 10 V) and a luminosity sensor.
```
```{tip}
* Place the setup on a magnetic board or inclined surface so students can see it clearly.
* Secure the luminosity sensor in a stand to keep it at the correct height above the lamp and prevent it from receiving too much or too little light.
```

## Procedure
1. Point to the fluorescent lights and ask students to sketch a graph of luminosity versus time.
2. Measure the frequency of the light from the fluorescent lights using the light sensor. Do not explain the exact frequency yet; that will come later in the demonstration.
3. Introduce the demonstration to investigate the flickering of light.
4. Place the setup on the desk and discuss the circuit. Draw the circuit diagram on the board and perform an initial measurement showing only the alternating voltage across the lamp.
5. Discuss the shape of the alternating voltage with the students. Ask how the direction of the current changes. (You can also connect a current sensor.)
6. Position the luminosity sensor near the setup. Explain what the sensor measures. Ask students to individually sketch a graph predicting the luminosity measurement.
7. Perform a measurement of both luminosity and alternating voltage. Calculate with the students the frequency of the alternating voltage.
8. Repeat the frequency calculation for the luminosity. Ask students to explain why the luminosity has a frequency that is double that of the voltage.
9. Ask students how the graphs would change if direct current (DC) was used instead of alternating current (AC). Demonstrate this.
10. Extend the demonstration with measurements on LED lighting.

```{figure} B35_NvV03_Fig2_wisselspanninglampje.JPG
---
width: 50%
align: center
name: demo48_fig2
---
Two measurements in one diagram: the alternating voltage across the lamp and the luminosity of the lamp over time.
```
```{tip}
* Ask students to predict what will happen to the luminosity.
* A suggested sequence for the demonstration could be: Measurement 1: AC voltage, Measurement 2: lamp luminosity, Measurement 3: combined measurement in one diagram.
```
## Physics Background
The alternating voltage from our power grid changes at 50 Hz, as does the alternating current. In each period, the voltage and current rise and fall twice. The direction of the current doesn't matter for the lamp to light up. Therefore, the lamp's brightness fluctuates exactly 100 times per second. Students can quickly grasp this explanation, though they might not think of it on their own. There is a common misconception that light sources do not vary in intensity because this fluctuation is not easily perceived {cite}`Bacalla2013`.

## Follow-up
* How does direct current (DC) affect the lamp's luminosity?
* Can this experiment be replicated with LEDs? What frequency is observed?
* Conduct the experiment with both a flashlight LED and a 230 V LED lamp.

## References
```{bibliography}
:filter: docname in docnames
```
