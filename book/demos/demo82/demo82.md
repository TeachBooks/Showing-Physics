```{figure} ../../figures/ready.png
---
width: 35%
align: right
```

# Transit of a Sphere: Simulating Planet Transits

<table style="width: 100%; border-collapse: collapse; border: none;">
    <tr style="background-color: white;"> 
        <td style="text-align: left; padding: 3px; border: none;">Author:</td>
        <td style="text-align: left; padding: 3px; border: none;">Norbert van Veen</td>
    </tr>
    <tr style="background-color: white;">
        <td style="text-align: left; padding: 3px; border: none;">Time:</td>
        <td style="text-align: left; padding: 3px; border: none;">10 minutes</td>
    </tr>
    <tr style="background-color: white;">
        <td style="text-align: left; padding: 3px; border: none;">Age group:</td>
        <td style="text-align: left; padding: 3px; border: none;">14 - 18</td>
    </tr>
    <tr style="background-color: white;">
        <td style="text-align: left; padding: 3px; border: none;">Concepts:</td>
        <td style="text-align: left; padding: 3px; border: none;">Transits, planets, observation, exoplanet</td>
    </tr>
</table><br>


## Introduction
Most students will not be familiar with the transit of an exoplanet, though exoplants might facinate them. With a relatively simple setup, you can give your students a glimpse of how such an observation works. The calculations can be extrapolated to real-life scenarios.

```{figure} demo82_figure1.jpeg
---
width: 80%
align: center 
---
Setup to measure a transit.
```

## Equipment
* LED lamp (large opaque lamp) in holder
* Measuring tape
* Caliper
* Light sensor
* Sphere in a rider of an optical case

## Preparation
1. Align the setup so that the light sensor, sphere, and opaque lamp are in line.
2. Darken the room. 
3. Connect the light sensor to a real-time measurement device or datalogger. Ensure that the amount of light from the lamp does not overpower the light sensor. 
4. Change the distance between the light sensor and the lamp. Use a sphere with a diameter of approximately 1/5 or smaller than the diameter of the lamp.
5. Display the computer screen via a projector or interactive whiteboard.

## Procedure
1. Start the measurement. Move the rider with the sphere past the lamp at a constant speed. Stop the measurement.
2. Enlarge the light dip in the graph by zooming in with the mouse. See {numref}`Figure {number} <demo82transit>`.
3. How can you determine the duration of the transit?
4. Ask the students to sketch how the transit curve would look if the planet moved slower/faster.
5. Ask the students to sketch how the transit curve would look if the planet were larger/smaller.
6. Provide the formula below and ask the students to apply it to the situation. Provide the diameter of the lamp. Here, $H$ represents the brightness or intensity of the received light. 
    $H_{dip}/H_{star} =1-(r_{planet}/R_{star})^2$
7. Let students calculate the radius of the planet using the formula.
8. Control question: In what way(s) does this demonstration deviate from the actual observation of exoplanets?

```{figure} demo82_figure2.png
---
width: 70%
align: center 
name: demo82transit
---
The light dip of the transit, measurements taken using the software Coach.
```

## Physics background
In this setup, you simulate a transit of an exoplanet with a sphere in front of an opaque lamp. Unlike a 'real' star, the lamp will have a diverging beam of light at the location of the 'planet'. Also, the proportions are not to scale compared to the 'real' situation. Nevertheless, you get a decent dip in light intensity, which can be used to clarify the idea of measuring a transit.

The light sensor used has a spatial measurement angle of 50 degrees and will therefore be able to measure a large part of the light from the opaque lamp at this distance. This explains the relatively large dip you measure.

During a transition, an exoplanet will block a small portion of the light from its star, allowing very advanced equipment to measure a dip in light intensity. The captured starlight is parallel. By measuring multiple consecutive dips, you can derive the orbital period of the planet. Because the mass and luminosity of a star are known, you can derive the orbital radius of the exoplanet using Kepler's third law, and then the mass, density, and gravitational acceleration. In some cases, you can also determine the composition of gases in the planet's atmosphere by measuring its absorption spectrum. 

```{tip}
- We used an 8 W LED opaque lamp with a diameter of 95 mm. Make sure the LED lamp does not flicker. Check this with the slow-motion camera mode of a phone. Our planet was a sphere with a diameter of 18 mm. We set the light sensor to 1500 Lux.
- The setup with the rider also reflects light from the lamp, resulting in a slightly higher zero brightness ($H_0$). Try to cover anything that can reflect light. Optionally, slide a PVC pipe over the light sensor to prevent scattered light.
```
