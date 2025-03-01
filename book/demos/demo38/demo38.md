# Miscommunicating vessels

<table style="width: 100%; border-collapse: collapse; border: none;">
    <tr style="background-color: var(--background-color);">  
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">Author:</td>
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">Peter Dekkers</td>
    </tr>
    <tr style="background-color: var(--background-color);"> 
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">Time:</td>
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">5-15 minutes</td>
    </tr>
    <tr style="background-color: var(--background-color);"> 
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">Age group:</td>
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">14-16</td>
    </tr>
    <tr style="background-color: var(--background-color);"> 
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">Concepts:</td>
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">density, pressure</td>
    </tr>
</table>

```{figure} demo38_figure2.jpg
---
width: 70%
align: center
name: demo38_fig2
alt: U-shaped tube, liquid at the left is lower than at the right
---
U-tube after removal of the stopper.
```

## Introduction
The situation seems very normal - a U-tube filled with a clear liquid, with both sides at the same height. It's unclear what the cork on one side is for. That becomes apparent when you remove it, and the situation becomes incomprehensible unless you realize that there are not one but two liquids at play here. In the lower grades, this simple experiment challenges students to think about material properties. In the upper grades, it's a conceptual challenge regarding density and pressure, and a framework for some solid calculations.

This demonstration is adapted from {cite:t}`liem1991invitations`

## Equipment
* U-tube
* Cork that can seal one side of the U-tube
* Ethanol (as pure as possible)
* Water
* Stand with clamp
* If available, a camera that projects onto the smartboard

## Preparation
1. Attach the tube to the stand with the openings upward and fill roughly one-third of the tube's volume with ethanol.
2. Carefully add about a quarter of the tube volume of water to one side. Tilt the tube to prevent the liquids from mixing.
3. The water level is higher on the ethanol side. Push a cork onto that end (not too tight because it will need to be removed later, but airtight). The level on the corked side still needs to be higher than the level on the open side, or at least equal. If that is not the case, start over with less water.
4. Now carefully add water until both levels are equal, see {numref}`Figure {number} <demo38_fig1>`.

## Procedure
Conduct a conversation with the students along the following lines:
* *What do you notice about this situation? What can you see here?*
* *Do you see that the liquid levels on both sides are the same height? Why is that?*
* *Why is there a stopper? Does that make a difference?*
* *What do you think will happen if I remove the stopper? Will anything change, or will everything stay the same?*

Once it's clear what the class thinks, remove the stopper. The liquid level rises on the side where the stopper was, and it decreases on the other side. In these communicating vessels, the liquid levels are at unequal heights!

```{figure} demo38_figure1.jpg
---
width: 70%
align: center
name: demo38_fig1
alt: U shape tube with liquid and stopper, liquid left and right are at same level
---
U-tube with liquid and stopper.
```

* *Explain what's happening here and how the liquid levels can be at unequal heights.*

A suitable activity for this question is, for example, Think-Pair-Share, in which students first individually, then in pairs, and finally as a class come up with and share answers. As a teacher, maintain balance between supporting (hints) and encouraging, provide your own answer only if they can't figure it out on their own, or as a summary at the end.

```{tip}
Don't forget to come back to the initial situation after discussing the final situation. Students who have the necessary prior knowledge will mostly have said that the liquid levels were initially at the same height *because the pressure on both sides was equal*. But that's only the case after the cork is removed: then atmospheric pressure prevails on both sides. Yet the liquid levels were initially at the same height - how can that be? Hopefully, they can figure it out themselves, based on the developed description of the final situation: there must have been overpressure in the air under the cork to compensate for the extra weight of the water in the other leg. Water was poured into the tube until that was the case. So the fact that the levels were the same height didn't happen 'by itself,' you deliberately misled your students (to teach them something about pressure and density, of course).
```

## Physics background
In communicating vessels, the liquid levels are always at the same height (provided a single liquid is used). This is because the same air pressure pushes on the surface of all vessels - for an equally large force upwards, liquid columns of equal height are needed. If the forces are not equal the water would experience a net force and flow until they are. So how can the liquid in these vessels be at unequal heights?

The situation is easiest to understand by looking at the bottom point of the tube. The liquid there is stationary, so the pressure from the right and from the left is equal. Then the liquid mass must be equal on both sides, so their densities must be different. It seems there's only one liquid in the tube, but there are two, with different densities. If you look closely, you can see the interface between the ethanol and the water as a slight cloudiness in the liquid. (Presumably, the refractive index varies irregularly there because the ethanol is in the process of dissolving into the water.)

If the vessels were communicating, the liquids would have flowed if their initial levels were the same, but the cork prevented that.

At ages 16-18, you can calculate together where the separation should be: with $dh$ the height difference and $h$ the height at the water side we can write:

$$ \rho_e (h + dh) = \rho_w (h – x) + \rho_e \cdot x $$

which can be rewritten as follows:

$$ x = \frac{(\rho_e–\rho_w)h + \rho_e \cdot dh}{\rho_w+\rho_e}$$

If a negative value for $x$ is obtained, the interface is on the ethanol side; if a positive value is obtained, $x$ is on the water side. 

## Follow-up
You could calculate together and test what the greatest height difference is that you can achieve with water and ethanol in this tube. It may also be interesting to observe that a candle floats in water but not in ethanol.

## References
```{bibliography}
:filter: docname in docnames
```