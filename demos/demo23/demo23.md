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

# LEDs and Photons


Author:     Leo te Brinke\
Time:	  	10 minutes\
Age group:	15 - 18\
Concepts:	particle-wave duality of light, quantization, threshold frequency, photons

## Introduction
It is not generally known that a light emitting diode (LED) can be used in reverse mode, as light sensor instead of lamp. A LED can generate a voltage when absorbing light, but under certain conditions ..... Just like a photocell a LED turns out to have a threshold wave length or frequency which also depends on the type of LED. This can only be explained with quantized light. I usually show this demonstration as a first lesson about photons, so before the photocell and the photo-electric effect. 

## Equipment
* Two LEDs with a clearly different color light but preferably in a colorless holder
* A variable voltage source, with cables and appropriate resistors
* A red laser pointer
* A white light
* A green laser pointer
* A voltmeter with a very high internal resistance (10 M$\Ohm$ or higher)

## Preparation
For the first demonstration we make the LEDs shine by connecting each LED in forward direction in series with a resistor and a voltage source. Subsequent demonstrations are done without a voltage source, connecting  the LEDs directly to a Voltmeter and illuminated them with a laser pointer or other source (figures 1 and 2). Set the voltmeter to a range of 0 – 2V.

## Procedure
In this description we use a red and a green LED but it could be other colors as long as one has a large wavelength and the other a much shorter wavelength. We connect both LEDs and make them shine. The LEDs convert electrical energy to light. *Would it be possible to do the opposite, to convert light into electrical energy? How can we investigate that?*

We connect the red LED with the voltmeter and illuminate it with a red laser (figure 1). *Would other colors of light such as white and green also generate a voltage over the LED?* Verify this with the white and green light sources (figure 2).

*Would intensity influence the voltage? How can we investigate this?* Vary the distance between LED and laser pointer, or use a filter that reduces the intensity of the laser pointer. So a LED can act like a solar cell. Please note that the voltage still depends on some other factors apart from the color such as other properties of the LED and resistance of the Voltmeter (should be large).

Then show with the white light source and the green laser pointer that the green LED can also generate a voltage when illuminated with white and green light even at low intensities. However, not when illuminated with red light. Please note that it does not make sense to ask for predictions when this is the first lesson about photons.

The question now is why even a modest intensity of white or green light does generate a voltage across the green LED and red light does not. The explanation of physicists is that light energy is “quantized” in packages and that the energy of a package depends on the frequency of the light. Higher frequencies (thus smaller wavelengths) have more energy. So a green package has more energy than a red package. The green LED apparently needs a bigger energy package than a red LED in order to convert light into electrical energy and generate a voltage. And the voltage generated in a green LED is higher than that in a red LED. These energy packages of light are called light quanta or photons.

To further support this idea we can also look again at the conversion of electrical energy to light. To produce light the green LED needs a higher voltage than the red LED! Then we can get into determining Planck’s constant with LEDs, an experiment described elsewhere in this book.


## Physics background
The main principles have been mentioned above. After this demonstration it will be easier to understand the photo cell. It is better to avoid getting into explanations of how LEDs work. The LED in this demonstration is purely a black box whose behavior we cannot explain by light waves as a continuous flow of energy, but only with energy packages or light quanta which we have named photons.

A practical application of the same phenomenon is the fact that one cannot get a brown skin from visible light (behind a glass window), regardless of the intensity. UV energy packages are needed and they are absorbed by glass. Apparently pigment cells in our skin need energy packages with at least the energy of UV. The teacher can also refer to the fact that traditional photo paper is not sensitive for red light .... but who still knows that?

```{tip}
* As the internal resistance of the Voltmeter is very high, the LED cannot produce a current and retains a fixed voltage. One needs an internal resistance of at least 10 $M\Ohm$ in order to measure the voltage; with 1 $M\Ohm$ the LED will already discharge.
* LEDs in a colored holder may not work in this experiment as there could be light absorption of certain colors in the holder. 
* In our experiments small LEDs reacted better than big ones. It is unclear why.
* The extra resistance is only needed to limit the current when LEDs are on. The magnitude of the resistance depends on the power source and the maximum power of the LEDs. Most LEDs can stand a current of several tens of mA and this is sufficient for well visible light.
* It is possible to continue this demonstration with a determination of Planck’s constant with LEDs.

```

## Follow-up
One could also make a rough estimate of Planck’s constant. If the red LED generates $1.6$ V and you assume that each electron is excited with one photon, then one could determine the minimum energy of the photons and a minimum value of Planck’s constant. With $1.6$ V and a wavelength of $633$ nm (He-Ne-laser) we obtain $5.4\cdot 10^{-34}$ Js.  ($1.6$ eV = hc/$\lambda$).