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

# Transit of a Sphere: Simulating Planet Transits

Author:     \
Time:	10 minutes\
Age group:	14 - 18\
Concepts:	

## Introduction
A transit of an exoplanet is a distant concept for many students. With a relatively simple setup, you can give your students a glimpse of how such an observation works. The calculations can be extrapolated to real-life scenarios.

```{figure} demo82_figure1.jpeg
---
width: 50%
align: center 
---
Setup to measure a transit.
```


```{figure} demo82_figure2.png
---
width: 50%
align: center 
---
The light dip of the transit.
```

## Equipment
LED lamp (large opaque lamp) in holder; measuring tape; caliper; light sensor; sphere in a rider of an optical case.

## Preparation
Align the setup so that the light sensor, sphere, and opaque lamp are in line.
Darken the room. Connect the light sensor to an interface and start Coach 7. Ensure that the amount of light from the lamp does not overpower the light sensor. Then, change the distance between the light sensor and the lamp. Use a sphere with a diameter of approximately 1/5 or smaller than the diameter of the lamp. Display the computer screen via a projector or interactive whiteboard.

## Procedure
Start the measurement in Coach 7. Move the rider with the sphere past the lamp at a constant speed. Stop the measurement.
Enlarge the light dip in the graph by zooming in with the mouse. See Figure 2.
How can you determine the duration of the transit?
Ask the students to sketch how the transit curve would look if the planet moved slower/faster.
Ask the students to sketch how the transit curve would look if the planet were larger/smaller.
Provide the formula below and ask the students to apply it to the situation. Provide the diameter of the lamp. Here, H represents the brightness or intensity of the received light.$ 
$H_{dip}/H_{star} =1-(r_{planet}/R_{star})^2$
Have the students calculate the radius of the planet using the formula.
Control question: In what ways does this demonstration deviate from the actual observation of exoplanets?

## Physics background
In this setup, you simulate a transit of an exoplanet with a sphere in front of an opaque lamp. Unlike a 'real' star, the lamp will have a diverging beam of light at the location of the 'planet'. Also, the proportions are not to scale compared to the 'real' situation. Nevertheless, you get a decent dip in light intensity, which can be used to clarify the idea of measuring a transit.
The light sensor used has a spatial measurement angle of 50 degrees and will therefore be able to measure a large part of the light from the opaque lamp at this distance. This explains the relatively large dip you measure.

During a transition, an exoplanet will block a small portion of the light from its star, allowing very advanced equipment to measure a dip in light intensity. The captured starlight is parallel. By measuring multiple consecutive dips, you can derive the orbital period of the planet. Because the mass and luminosity of a star are known, you can derive the orbital radius of the exoplanet using Kepler's third law, and then the mass, density, and gravitational acceleration. In some cases, you can also determine the composition of gases in the planet's atmosphere by measuring its absorption spectrum. Questions about exoplanets and transits have appeared several times in the physics exams (HAVO 2010-1, 2019-2, 2022-3).

## Tips
We used an 8 W LED opaque lamp with a diameter of 95 mm. Make sure the LED lamp does not flicker. Check this with the slow-motion camera mode of a phone. Our planet was a sphere with a diameter of 18 mm. We set the light sensor BT50i to 1500 Lux.
The setup with the rider also reflects light from the lamp, resulting in a slightly higher zero brightness (H0). Try to cover anything that can reflect light. Optionally, slide a PVC pipe over the light sensor to prevent scattered light.
