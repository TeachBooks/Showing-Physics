```{figure} ../../figures/confirmed.png
---
width: 35%
align: right
```

# Speed of light in a liquid

<table style="width: 100%; border-collapse: collapse; border: none;">
    <tr style="background-color: var(--background-color);">  
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">Author:</td>
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">Norbert van Veen</td>
    </tr>
    <tr style="background-color: var(--background-color);"> 
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">Time:</td>
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">20-30 minutes</td>
    </tr>
    <tr style="background-color: var(--background-color);"> 
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">Age group:</td>
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">15-18</td>
    </tr>
</table><br>

## Introduction
Modern smartphones have a LiDAR sensor. This sensor allows you to measure the distance to objects. The LiDAR sensor is designed to measure only in air. As the speed of light in a transparent substance is slightly different than the speed of light in air, the measured distance is different. You can use this 'measurement error' to determine the speed of light in a transparent liquid.

```{figure} demo62_figure1.jpg
---
width: 90%
align: center
name: demo62_fig1
---
<br>*left:* LiDAR sensor on the phone.
<br>*right:* Screenshot of LiDAR app.
```

## Materials Needed
- Smartphone with LiDAR sensor (iPhone 12 or higher) and a LiDAR app (phyphox) or a LiDAR pointer
- Tripod
- Pan
- Liquid (e.g. water)
- Tape measure

## Preparation
1. Place the phone in the tripod above the table. Ensure that the phone is perfectly horizontal. This can be checked with an app that indicates the tilt. 
2. Place a pan directly under the phone's LiDAR sensor (see {numref}`Figure {number}<demo62_fig1>` at the right). Make sure the LiDAR sensor is aimed directly at the center of the pan. 
3. Verify the distance from the phone to the bottom of the pan using a tape measure.

## Procedure
1. Provide some explanation about the operation of echo and sonar. Explain that this also works with invisible laser light, such as used in [speed limit enforcement](https://en.wikipedia.org/wiki/Lidar_traffic_enforcement).
2. Explain the demonstration. Indicate that you will perform a distance measurement with a phone with and without water.
3. Draw a diagram on the board, such as the drawing in {numref}`Figure {number}<demo62_fig2>`.
4. Explain how the LiDAR sensor provides a distance measurement.
5. Explain that you will pour water into the pan and then measure the distance again.
6. Let the students predict what effect the water in the pan will have on the measurement.
7. Carefully pour the water into the pan. Ensure that the water has come to rest. Use a water height of 5-8 cm.
8. Perform the measurement and note the measured distance on the phone with (S4) and without water (S1). Note the height of the phone to the water surface (S2). Measure the depth of the water (S3).
9. Calculate the speed of light in water, assuming speed of light in air is 299702547 m/s.
10. The following question can be asked to assess students' understanding: If we were to pour the same amount of another transparent liquid with a higher density into the pan instead of water, what would the LiDAR sensor indicate?
    A. A shorter distance than with water.
    B. A longer distance than with water.
    C. The same distance as with water.
    
```{figure} demo62_figure2.jpg
---
width: 50%
align: center
name: demo62_fig2
---
S1 is the actual distance between the phone and the bottom of the pan, S2 is the distance between the phone and the water surface. S3 is the water depth. S4 is the distance measured by the app.
```

## Physics Background
LiDAR is a technology that determines the distance to an object or surface with laser pulses and works on the same principle as radar. The LiDAR sensor determines the distance to the object or surface by measuring the time elapsed between sending a pulse and receiving a reflection of that pulse: 

$$ s = \frac{c \Delta t}{2} $$

with $s$ the distance in m, $c$ the speed of light in m/s and $\Delta t$ the time between sending and receiving the pulse. The laser pulses will travel more slowly in water:

$$ n_{l\rightarrow w} = \frac{c_{air}}{c_{water}} $$ 

This longer travel time results in an 'erroneous' measured distance (S4) of the distance from the LiDAR sensor to the bottom of the pan. The speed of light in water is calculated using the time that laser light stays in the water, see {cite}`Bewersdorff2022`:

$$ t_{water} = t_{measured} - t_{air} $$

$$ t_{water} = \frac{S4}{c_{air}} - \frac{S2}{c_{air}} $$

$$ c_{water} = \frac{S3}{t_{water}} $$ 

Depending on the measurements, we find deviations from the literature value for $c_{water}$ ($225*10^6$m/s) between 0.5 – 10%.

```{tip}
- Depending on the power of the LiDAR sensor, the water depth cannot be too great. There will be a power loss; maintain a depth between 5-8 cm.
- Ensure the phone is securely fastened, as it may fall into the water.
```

## Follow up
The speed of light in water is determined with a single measurement. Students can repeat the demonstration with different water heights and use a more sophisticated way of determining the speed of light.

## References
```{bibliography}
:filter: docname in docnames
```