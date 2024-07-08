```{figure} ../../figures/confirmed.png
---
width: 35%
align: right
```

# Pulling a spool

<table style="width: 100%; border-collapse: collapse; border: none;">
    <tr style="background-color: var(--background-color);">  
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">Author:</td>
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">Ineke Frederik</td>
    </tr>
    <tr style="background-color: var(--background-color);"> 
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">Time:</td>
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">10 minutes</td>
    </tr>
    <tr style="background-color: var(--background-color);"> 
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">Age group:</td>
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">Grade 10</td>
    </tr>
    <tr style="background-color: var(--background-color);"> 
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">Concepts:</td>
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">Mechanics, pivot point, torque, rolling</td>
    </tr>
</table><br>

<div style="display: flex; justify-content: center;">
    <div style="position: relative; width: 70%; height: 0; padding-bottom: 56.25%;">
        <iframe
            src="https://www.youtube.com/embed/YDBr1Lof_mI?si=RhTC31XHv-6gL4Kl"
            style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"
            frameborder="0"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
            allowfullscreen
        ></iframe>
    </div>
</div>


## Introduction
Wires are wound on a spool, cables on a reel. If you need a small piece of cable, you pull the cable. But what happens to the reel if it is on the ground or table? Which way does a wire spool move?

```{figure} demo56_figure1.JPG
---
width: 50%
align: center
---
Cables on a reel.
```

## Equipment
- Large wire spool with preferably colored wire
- Choose a spool with a clear difference between inner and outer diameter
- For a follow up, have various spools ready

## Preparation
None

```{figure} demo56_figure2.jpg
---
width: 50%
align: center
class: margin
---
Large wire spool. Which way will it roll?   
```

## Procedure
1. If the wire spool is on a rod, it simply rotates when you pull the wire. But now place the spool on the ground. Which way does it move when you pull the wire?
2. Hold one end of the wire in your fingers; keep the wire horizontal. <br>*Which way does the spool move* (*Predict*) *when you gently pull the wire?*<br>
    - To the left
    - To the right
    - Does not move
    - I don't know
    <iframe src="https://tudelft.h5p.com/content/1292318675152841697/embed" width="1088" height="350" frameborder="0" allowfullscreen="allowfullscreen" allow="autoplay *; geolocation *; microphone *; camera *; midi *; encrypted-media *" aria-label="Demo 56 Q1"></iframe><script src="https://tudelft.h5p.com/js/h5p-resizer.js" charset="UTF-8"></script>
3. Ask the students to discuss with their neighbor. They explain their choice to each other and why they chose their answer (*Explain*). Do they agree? Collect the answers.
4. Perform the demonstration (*Observe*).
5. Did the predictions come true? Why or why not? (*Explain*)
6. Hold one end of the wire in your fingers and ensure the wire is now vertical. <br>*Which way does the spool move* (*Predict*) *when you pull the wire?*
    - To the left
    - To the right
    - Does not move
    - I don't know
7. Ask the students to discuss with their neighbor again. They explain their choice to each other (*Explain*). Collect the answers again.
8. Perform the demonstration again (*Observe*).
9. Did the predictions come true? Why or why not? (*Explain*)
10. *To the left or to the right? Is there a pull direction where the spool stays put when you pull the wire? Can you make the wire spool move any way you want? What factors may be relevant?

## Physics Background
The wire spool can move to the left or right depending on the pull direction ({numref}`Figure {number}<fig:schematic>`). Logically, it seems that if you pull to the right on a horizontal wire, the wire spool will move to the right as well. Doesn't an object always move in the direction of the force?

For a simple explanation of the movement direction, look at the torque that the pulling force $F$ creates relative to the pivot point $P$. This torque depends on the angle the wire makes with the horizontal. A clockwise torque causes the spool to roll to the right, a counterclockwise torque causes it to roll to the left. The critical angle that determines whether the spool will move left or right is determined by checking if the extension of the force lies to the left or right of the pivot point $P$ (see {numref}`Figure {number}<fig:schematic>`).

```{figure} demo56_figure4.png
---
width: 50%
align: center
name: fig:schematic
---
Schematic of the wire spool. The critical angle can be found when the line of the pulling force coincides with point P where the spool makes contact with the table.
```

Moreover, according to {cite:t}`mungan2023pulling`, the acceleration of the center of mass is given by:

$$a_x = F\frac{cos(\theta)-cos(\theta_c)}{M+I/R_o^2}$$

with:

$$\theta_c=cos^{-1}(R_i/R_o)$$

this holds that the spools: 
* rolls rightwards ($a_x > 0$), for $0° \le \theta < \theta_c,$
* does not roll ($a_x = 0$) when $\theta = \theta_c$, and
* rolls leftward ($a_x < 0$) for $\theta_c \le \theta < 90°$.


```{tip}
This demonstration works even better if you wind a ribbon instead of a wire around the spool. You can also play a bit with the wire spool by gently pulling while the pull wire moves around the critical angle. The wire spool will then alternately move left and right on the table while the observer barely notices that the teacher slightly varies the pull angle.

There are many articles on the physics of pulling a spool available (see, e.g., {cite:t}`mungan2023pulling`, {cite:t}`cross2023comment` and {cite:t}`schmidt2024experimental`).
```

## References
```{bibliography}
:filter: docname in docnames
```