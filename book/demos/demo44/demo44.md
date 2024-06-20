```{figure} ../../figures/busy.png
---
width: 35%
align: right
```

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
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">Grade 4/5, High school 5</td>
    </tr>
    <tr style="background-color: var(--background-color);"> 
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">Concepts:</td>
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">Frequency, sampling</td>
    </tr>
</table><br>


```{figure} demo44_figure2.JPG
---
width: 50%
align: center
name: demo44_fig2
---
A view as the students will see it.
```

## Introduction
In movies and commercials, you see car wheels spinning backward while the car moves forward. How does that work exactly? And how many measurements do you need to sample an (analog) signal (digitally) so that you can reconstruct the signal?

## Equipment
* Dropper
* Stroboscope
* Collection tray
* Water
* Darkened room
* Pendulum

## Preparation
Place a dropper, similar to the one used for pipetting, on the table. Position the collection tray underneath to catch the droplets. Place a stroboscope next to the setup. Also, prepare the pendulum setup, ensuring that the pendulum length is not too long (measure beforehand what the period is!).

```{figure} demo44_figure1.JPG
---
width: 50%
align: center
name: demo44_fig1
---
The setup.
```

## Procedure
demonstration. The flash of the stroboscope corresponds to one frame of the film. You are sampling the motion.

Turn on the stroboscope and open the faucet slightly so that drops fall quickly in succession. By varying the flash frequency, you can freeze the drops; let them fall slowly or rise upward.

Replace the dropper with the pendulum. Set the flash frequency so that the pendulum is only visible in the extreme positions or at the equilibrium position. First, ask the students if they can tell whether the pendulum is moving back and forth or standing still. Then ask the students what they will see when you slightly increase the flash frequency and verify the answer by increasing the flash frequency.


## Physics background
To be able to construct an analog signal by taking samples (digitally), you need at least 2 measurements per period. This is called the Nyquist criterion. If the sampling frequency is lower than this frequency, aliasing occurs; the effect is seen in the backward spinning wheels of cars in movies.

## References
```{bibliography}
:filter: docname in docnames
```
