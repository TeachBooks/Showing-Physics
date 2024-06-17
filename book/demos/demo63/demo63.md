```{figure} ../../figures/ready.png
---
width: 35%
align: right
```

# Condensation Heat in Infrared

<table style="width: 100%; border-collapse: collapse; border: none;">
    <tr style="background-color: var(--background-color);">  
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">Author:</td>
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">NAME</td>
    </tr>
    <tr style="background-color: var(--background-color);"> 
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">Time:</td>
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">10-30 minutes</td>
    </tr>
    <tr style="background-color: var(--background-color);"> 
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">Age group:</td>
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">14-18</td>
    </tr>
    <tr style="background-color: var(--background-color);"> 
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">Concepts:</td>
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">CONCEPTS</td>
    </tr>
</table><br>


## Introduction
In this demonstration, you make a nanoscale process visible in a simple way. Due to continuous evaporation water in a cup has a lower temperature than the room its in, even after hours of being in that room. We follow the temperature of a sheet of paper as evaporated water condenses on it. With the measured temperature rise, we estimate the number (layers) of water molecules needed for this increase.

```{figure} demo63_figure1.png
---
width: 50%
align: center
---
Setup for this experiment: FLIR C5 camera connected to a computer. Clamped in a stand clamp perpendicular to the dish under the paper.
```
## Materials Needed
- Infrared camera (Flir C5)
- Round dish (e.g., a petri dish)
- A few sheets of (printer) paper
- Stand clamp


## Preparation
1. Place the infrared camera in a stand so that it is directed from above onto the setup. 
2. Place the dish with water under the camera. 
3. Turn on the camera with streaming mode enabled and connect it to your computer.
4. Open a camera app on the computer and let it display the image from the infrared camera. 
5.Set the distance (on the touchscreen) of the infrared camera to the correct value. Enter the emissivity of paper (approximately 0.70) into the infrared camera.

## Procedure
Students already have knowledge of molecular theory and phase transitions.
1. Set up the apparatus and explain to the students what they see. Tell them you are going to place the sheet of paper on the dish of water. The infrared camera can measure the temperature.
1. *What happens to the temperature of the paper above the water?*
   1. Will remain the same
   2. Will decrease
   3. Will increase
2. Perform the measurement. Read the temperature of the paper above the water and also of the part of the paper that falls beside the dish. Use the movable temperature spot on the touchscreen to measure the temperature of these parts of the paper.
3. Now tell them that you are going to remove the paper from the dish and quickly turn it over. Measure the temperature of the underside of the paper.
4. *What happens to the temperature of the part of the paper that was above the dish with water?*
   1. Will remain the same
   2. Will decrease
   3. Will increase
5. Talk about the condensation and evaporation of water and how energy is needed and released respectively.
6. Control questions: *Why do you blow over a bowl of soup to cool it down? A puddle of rainwater also evaporates even if it is not one hundred degrees Celsius outside. What can you say about the temperature of the puddle compared to the ambient temperature?*
8. Perform the calculation of the number of layers of water molecules on the paper. See physical background.

```{figure} demo63_figure_2.jpg
---
width: 50%
align: center
---
a. The surface of the paper on which water has condensed is clearly visible. On the edge of the paper, you see two water droplets where the water evaporates and causes a lower temperature. b. Cooling of the paper after turning.
```

## Physics Background
This demonstration is extensively described by Xie & Hazzard (2011). The rise in temperature of the paper is caused by the condensation of water vapor from the dish on the underside of the paper. When the water molecules in the vapor condense, they release heat. The heat conducts through the thin paper and causes a temperature rise. The amount of water molecules condensing on the paper is so small that you barely feel moisture when you touch the paper, but it is enough to cause a temperature rise detected by the infrared camera.

This heating mechanism can be confirmed by holding the paper above the cup for a minute until it reaches thermal equilibrium with the surroundings and then removing the paper. IR images of the paper show that the temperature of the originally heated circular zone drops immediately after removal to below the ambient temperature. This can be explained by the water molecules that had condensed on the underside of the paper beginning to evaporate, resulting in rapid cooling of the paper.

The water molecules condensed on the paper apparently cannot penetrate through the paper, otherwise, you would have observed evaporation cooling on the other side of the paper with the infrared camera.

### How thick was the condensed water layer approximately?
For our experiment with a dish with a diameter of 10.5 cm, we measured and looked up the following:
- $ΔΤ ≈ 1.0$ ºC
- $ρ_{paper} = 80$ g/m²
- $c_{paper} = 1.4·10^3$ J/kg·K
- $L_{water} = 2.26·10^3$ J/g
- $M_{water} = 18 $ g/mol

The energy released on the paper is:

$$ ΔQ = ρ_{paper} \cdot A_{paper} \cdot c_{paper} \cdot ΔT $$

$$= 80 \cdot π \cdot 0.0525^2 \cdot 1.4 \cdot 1.0 = 0.97 \text{J} $$

The mass of water condensed on the paper:
$$m = \frac{ΔQ}{L_{water}} = \frac{0.97 \text{J}}{2.26 \cdot 10^3 \text{J/g}} = 4.29 \cdot 10^{-4} \text{g} $$

At room temperature, 1 g of water has a volume of 1 cm³. For the circular part of the paper, this means that a water volume of 4.29·10⁻⁴ cm³ is distributed over a cylindrical surface of the paper. The height $h$ of this water cylinder is then:
$$h = \frac{V}{A} = \frac{4.29 \cdot 10^{-4}}{π \cdot 5.25^2} = 4.95 \cdot 10^{-6} \text{cm} $$

The water layer on the underside of the paper is thus approximately 50 nm thick.

The average volume of a water molecule can be estimated with the molar mass, written as a kind of "molar density" ($M_V = 18$ cm³/mol) and the number of molecules in a mole ($N_A$). With this volume, we calculate the one-dimensional dimension of a water molecule:
$$h_{molecule\,water} = \sqrt[3]{\frac{M_V}{N_A}} = \sqrt[3]{\frac{18 \cdot 10^{-6} \text{m³}}{6.02 \cdot 10^{23}}} = 3.1 \cdot 10^{-10} \text{m} $$

The number of layers ($n$) of water molecules can then be calculated with:
$$ n = \frac{h_{cylinder}}{h_{water\,molecule}} = \frac{4.95 \cdot 10^{-8} \text{m}}{3.1 \cdot 10^{-10} \text{m}} = 159 $$

Considering that not all the heat is released at once, the rate of water vapor deposition is likely a few nanometers per second. So we are studying a nanoscale process.

```{tip}
- Place the setup visibly on the desk. Project the measurement via the computer onto a screen or digital board. Ensure the temperature is easy to follow by, for example, directing a temperature spot of the camera at the spot to be measured. 
- A water droplet on the edge of the paper will also be clearly visible with a lower temperature due to evaporation (see figure 2a). 
- After a few hours, the setup shows the paper has a lower temperature. Paper is porous, and the water molecules evaporate again at the surface of the paper. Hold the paper vertically above the dish as well.
```

## References
```{bibliography}
:filter: docname in docnames
```