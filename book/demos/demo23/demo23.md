# LEDs and photons

<table style="width: 100%; border-collapse: collapse; border: none;">
    <tr style="background-color: var(--background-color);">  
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">Author:</td>
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">Leo te Brinke</td>
    </tr>
    <tr style="background-color: var(--background-color);"> 
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">Time:</td>
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">10 minutes</td>
    </tr>
    <tr style="background-color: var(--background-color);"> 
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">Age group:</td>
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">15 - 18</td>
    </tr>
    <tr style="background-color: var(--background-color);"> 
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">Concepts:</td>
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">particle-wave duality of light, quantization, threshold frequency, photons</td>
    </tr>
</table>

```{figure} demo23_figure1.jpg
---
width: 70%
align: center
name: demo23_fig1
---
Red light shined on a green LED: no voltage.
``` 

## Introduction
It is not generally known that a light emitting diode (LED) can be used in reverse mode, as light sensor instead of light source. A LED can generate a voltage when absorbing light, but only when certain conditions are met... Just like a photocell a LED turns out to have a threshold wave length or frequency which also depends on the type of LED. This can only be explained with quantized light. This demonstration can be used in the first lesson about photons, so before the photocell and the photo-electric effect. 

## Equipment
* Two LEDs with a clearly different color light but preferably in a colorless holder
* A variable voltage source, with cables and appropriate resistors
* A red laser pointer
* A white light
* A green laser pointer
* A voltmeter with a very high internal resistance (10 M$\Omega$ or higher)

```{warning}
Adhere to the regular safety rules when using with lasers!
```

```{figure} demo23_figure2.jpg
---
width: 70%
align: center
name: demo23_fig2
---
With white light, the DMM measures a voltage.
``` 

## Preparation
For the first demonstration we make the LEDs shine by connecting each LED in forward direction in series with a resistor and a voltage source. Subsequent demonstrations are done without a voltage source, connecting  the LEDs directly to a Voltmeter and illuminated them with a laser pointer or other source ({numref}`Figures {number} <demo23_fig1>` and {numref}`{number} <demo23_fig2>`). Set the voltmeter to a range of 0 – 2V.

## Procedure
Here we use a red and a green LED but it could be other colors as long as one has a large wavelength and the other a much shorter wavelength. We connect both LEDs to the power supply and make them light. The LEDs convert electrical energy to light. *Would it be possible to do the opposite, to convert light into electrical energy? How can we investigate that?*

We connect the red LED with the voltmeter and illuminate it with a red laser ({numref}`Figures {number} <demo23_fig1>`). *Would other colors of light such as white and green also generate a voltage over the LED?* Verify this with the white and green light sources ({numref}`Figures {number} <demo23_fig2>`).

*Would intensity influence the voltage? How can we investigate this?* Vary the distance between LED and laser pointer, or use a filter that reduces the intensity of the laser pointer. So a LED can act like a solar cell. 

```{note}
The voltage still depends on some other factors apart from the color such as other properties of the LED and resistance of the Voltmeter (should be large).
```

Then, show with the white light source and the green laser pointer that the green LED can also generate a voltage when illuminated with white and green light even at low intensities. However, not when illuminated with red light. 

```{tip}
As described in [POE](../../Pedagogy/PoE.md), it does not make sense to ask for predictions when this is the first lesson about photons. Students do not have sufficient understanding yet to make meaningful predictions.
```

The question now is why even a modest intensity of white or green light does generate a voltage across the green LED and red light does not. The explanation of physicists is that light energy is “quantized” in packages and that the energy of a package depends on the frequency of the light. Higher frequencies (thus smaller wavelengths) have more energy. So a green package has more energy than a red package. The green LED apparently needs a bigger energy package than a red LED in order to convert light into electrical energy and generate a voltage, and the voltage generated in a green LED is higher than that in a red LED. These energy packages of light are called light quanta or photons (see e.g. [Fluorescent olive oil](../demo87/demo87.md)).

To further support this idea we can also look again at the conversion of electrical energy to light. To produce light the green LED needs a higher voltage than the red LED! Then we can get into determining Planck’s constant with LEDs.

```{figure} demo23_figure3.png
---
width: 70%
align: center
---
A concept cartoon can be used to elicit students' ideas.
``` 

## Physics background
The main principles have been mentioned above. After this demonstration it will be easier for students to understand the photo cell. It is better to avoid getting into explanations of how LEDs work. The LED in this demonstration is purely a black box whose behavior we cannot explain by light waves as a continuous flow of energy, but only with energy packages or light quanta which we have named photons.

A practical application of the same phenomenon is the fact that one cannot get a brown skin from visible light (behind a glass window), regardless of the intensity. UV energy packages are needed and they are absorbed by glass. Apparently pigment cells in our skin need energy packages with at least the energy of UV (there is a nice [Dutch exam question on the use of suncream](https://newsroom.nvon.nl/files/default/nav191vb.pdf)). The teacher can also refer to the fact that traditional photo paper is not sensitive for red light .... but who still knows that?

```{tip}
* As the internal resistance of the Voltmeter is very high, the LED cannot produce a current and retains a fixed voltage. One needs an internal resistance of at least 10 $\text{M}\Omega$ in order to measure the voltage; with 1 $\text{M}\Omega$ the LED will already discharge.
* LEDs in a colored holder may not work in this experiment as there could be light absorption of certain colors in the holder. 
* In our experiments small LEDs reacted better than big ones. It is unclear why.
* The extra resistance is only needed to limit the current when LEDs are on. The magnitude of the resistance depends on the power source and the maximum power of the LEDs. Most LEDs can stand a current of several tens of mA and this is sufficient for well visible light.
* It is possible to continue this demonstration with a determination of Planck’s constant with LEDs.
```

## Follow-up
One could also make a rough estimate of Planck’s constant. If the red LED generates $1.6$ V and you assume that each electron is excited with one photon, then one could determine the minimum energy of the photons and a minimum value of Planck’s constant. With $1.6$ V and a wavelength of $633$ nm (He-Ne-laser) we obtain $5.4\cdot 10^{-34}$ Js.  ($1.6 \text{eV} = \frac{hc}{\lambda}$).

