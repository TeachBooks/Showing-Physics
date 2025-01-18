# Blowing out a light bulb

<table style="width: 100%; border-collapse: collapse; border: none;">
    <tr style="background-color: var(--background-color);">  
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">Author:</td>
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">Wouter Spaan</td>
    </tr>
    <tr style="background-color: var(--background-color);"> 
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">Time:</td>
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">15 minutes</td>
    </tr>
    <tr style="background-color: var(--background-color);"> 
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">Age group:</td>
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">13+</td>
    </tr>
    <tr style="background-color: var(--background-color);"> 
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">Concepts:</td>
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">NTC (Negative Temperature Coefficient), series circuit, power, heat generation</td>
    </tr>
</table>

```{figure} demo31_figure1.jpg
---
width: 70%
align: center
name: demo31_fig2
alt: demonstrator heating a light bulb using a bunzenburner
---
If you (carefully!) heat the piece of glass, the resistance value decreases and the light bulb lights up.
```

This demonstration is adapted from {cite:p}`Walravens2011`.

## Introduction
The primary goal of this demonstration is to demonstrate the NTC behavior of glass. You can discuss concepts from electrical engineering at various levels and prompt students to think about heating due to current flow.

## Equipment
* Random light bulb
* 40-60 W light bulb (see tips)
* Two sockets (for mains voltage), preferably one ceramic for fire resistance
* Mains voltage switch
* Plug with grounding
* Gas burner

```{warning}
Make sure to wear safety glasses (the same for the front row of students or place a screen)
```

## Preparation
* Break the glass of one of the light bulbs. This works best with a hammer while the light bulb is completely wrapped in a layer of paper. Then remove the filament from the light bulb. Also remove any support for the filament, for example, with a glass saw. The lamp will then look like in {numref}`Figure {number} <demo31_fig3>` (without it glowing).
* Place the modified bulb and the intact bulb in a suitable socket, which is not too high on the rim (due to later heating). Connect these lamps in series with a switch.

```{warning}
 The glass shards are razor-sharp!
```

```{figure} demo31_figure2.jpg
---
width: 70%
align: center
name: demo31_fig3
alt: heated glass bulb 
---
The piece of glass continues to conduct even after it is removed from the flame. By blowing against this glass, you can cool it down and turn off the light bulb.
```

## Procedure
* Draw the circuit on the schoolboard, set up the equipment, and relate the setup to the circuit. The Bunsen burner is not visible. 
* Ask the class if the bulb will light when the switch is flipped. After the discussion, flip the switch.
* Bring out the Bunsen burner. Carefully heat the glass in the roaring flame: dip it briefly into the flame and then remove it. After heating for a while, the bulb will light up. While continuing heating, you can ask the class what will happen if you stop heating and place the fitting with glass down. This usually leads to lively discussions. After an in-depth discussion, remove the glass from the flame. To the amazement of a large part of the class, the bulb remains on, no matter how long you wait.
* Demonstrate that you can turn off the light by blowing against the bulb. *How can you explain that?*
* If you stop blowing and the power of the bulb is well chosen, the glass will heat up again, and the bulb will slowly light.

```{figure} demo31_figure3.png
---
width: 50%
align: center
name: demo31_fig1
alt: schematic of the circuit, glass represented as resistor 
---
Circuit diagram of the setup. The resistor consists of a piece of glass (see {numref}`Figure {number} <demo31_fig3>`).
```

## Physics background
Glass behaves like an NTC because, in terms of electron structure, it somewhat resembles a semiconductor. At room temperature, the conduction band is empty, and the band gap is too large for the electrons to cross. When heated, the electrons gain enough thermal energy to cross the band gap, and the glass conducts better and better. The ions in the glass play no role in the conduction.

```{tip}
* The power of the light bulb relative to the exact properties and dimensions of the piece of glass is critical: if the power is too low, the current is too small to keep the glass warm. If the power is too high, you cannot blow out the lamp. So, try and optimize! 
* We used lamps of $40$ W, $60$ W, and even $75$ W for the desired result in different versions of this demonstration. This also provides an opportunity to discuss with the students the effect of the power of the burning lamp.
* If you find a well-working combination, stock up on light bulbs (exactly the same); in a few years, they may no longer be available.
```

## References
```{bibliography}
:filter: docname in docnames
```