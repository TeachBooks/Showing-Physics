# Upward dripping

<span style="font-size: 25px; color: gray;">Sampling</span>

<table style="width: 100%; border-collapse: collapse; border: none;">
    <tr style="background-color: var(--background-color);">  
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">Author:</td>
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">Freek Pols</td>
    </tr>
    <tr style="background-color: var(--background-color);"> 
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">Time:</td>
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">15 minutes</td>
    </tr>
    <tr style="background-color: var(--background-color);"> 
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">Age group:</td>
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">Grade 11</td>
    </tr>
    <tr style="background-color: var(--background-color);"> 
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">Concepts:</td>
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">Frequency, sampling, NyQuist</td>
    </tr>
</table>

<div style="display: flex; justify-content: center;">
    <div style="position: relative; width: 70%; height: 0; padding-bottom: 56.25%;">
        <iframe
            src="https://www.youtube.com/embed/C9cByXAXkRw?si=nm_BLzKo5BOkISQT"
            style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"
            frameborder="0"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
            allowfullscreen
        ></iframe>
    </div>
</div>

## Introduction
In movies and commercials, you see car wheels spinning backward while the car moves forward. How does that work? And how many measurements do you need to sample an (analog) signal (digitally) so that you can reconstruct the signal?

## Equipment
* Dropper (best with larger reservoir on top)
* Stroboscope (or ledstrip and frequency generator with adjustable duty cycle)
* Collection tray
* Water
* Darkened room
* Pendulum

```{warning}
Some people are sensitive for flashing light... check beforehand!
```

## Preparation
Place a dropper, similar to the one used for pipetting, on the table. Position the collection tray underneath to catch the droplets. Place a stroboscope next to the setup. Try beforehand what the dripping rate and frequency for the stroboscope should be. Also, prepare the pendulum setup, ensuring that the pendulum length is not too long (measure beforehand what the period is!).

```{figure} demo44_figure1.JPG
---
width: 70%
align: center
name: demo44_fig1
---
The setup.
```

```{tip}
Determine the frequency with which the droplets fall in succession. Set your frequency generator to this frequency.
```

## Procedure
Show your students the experimental setup. Turn on the stroboscope and open the faucet slightly so that water droplets fall quickly in succession. By varying the flash frequency, you can 'freeze' the drops; let them fall slowly, or even rise upward.

Replace the dropper with the pendulum. Set the flash frequency so that the pendulum is only visible in the extreme positions or at the equilibrium position. Ask the students if they can tell whether the pendulum is moving back and forth or standing still. Then ask the students what they will see when you slightly increase the flash frequency. Verify their answers by increasing the flash frequency.

## Physics background
If the frequency of the stroboscope is the same as the frequency of dripping water, subsequent water droplets are seen at the same position. Hence, the water droplets are 'frozen' in air. If you increase the frequency slightly, the sequent water droplet is seen just above the earlier one. The water droplets then seem to move slowly upward.

```{tip}
Phyphox can be used to determine the frequency of the water droplets, you can use the acoustic chronometer for this. 
```

Each flash of the stroboscope corresponds to one frame of the film. You are sampling the motion.

To be able to construct an analog signal by taking samples (digitally), you need at least 2 measurements per period. This is called the NyQuist criterion. If the sampling frequency is lower than this frequency, aliasing occurs; the effect is seen in the backward spinning wheels of cars in movies.

```{note}
One of our testers stated: " 'Upward dripping' is a really fun demonstration which arouses amazement among students. Many students quickly realized the relationship between the flash frequency and the drop frequency in the way they saw the droplet moving.
```

## Follow up
Let students make a stop-motion movie with small cars making uniform motion and uniform accelerated motion. Ask them how the stop-motion movie relates to this demonstration. 