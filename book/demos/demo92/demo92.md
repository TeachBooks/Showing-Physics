```{figure} ../../figures/confirmed.png
---
width: 35%
align: right
```

# Rollin' in the deep

This demonstration has been published in the Dutch magazin for science teachers {cite:t}`dekkers1999drogen`.

</table><br>
        <td style="text-align: left; padding: 3px; border: none;">Author:</td>
        <td style="text-align: left; padding: 3px; border: none;">Peter Dekkers</td>
    </tr>
    <tr style="background-color: white;">
        <td style="text-align: left; padding: 3px; border: none;">Time:</td>
        <td style="text-align: left; padding: 3px; border: none;">30-50 minutes</td>
    </tr>
    <tr style="background-color: white;">
        <td style="text-align: left; padding: 3px; border: none;">Age group:</td>
        <td style="text-align: left; padding: 3px; border: none;">Grade 10</td>
    </tr>
    <tr style="background-color: white;">
        <td style="text-align: left; padding: 3px; border: none;">Concepts:</td>
        <td style="text-align: left; padding: 3px; border: none;">potential and kinetic energy, moment of inertia, translational energy</td>
    </tr>
</table>

## Introduction
If you roll a bunch of round objects down a slope, the mass and size do not matter, but the shape does. This is difficult to understand or infer from observations. It, however, may encourage students to propose systematic investigations to establish order. In this demonstration, the teacher can manage planning, execution and interpretation. The test is inspired by an old science quiz question: do a boiled and a raw egg roll at the same rate? 

```{figure} demo92_figure1.jpg
---
width: 50%
align: center
---
Which rolling object reachers the bottom first?
```

## Equipment
* Anything that can roll. 
* Long wide board (with edges if possible); 
* Tripods
* Block and cushion the same width as the board
* Scales
* Stopwatch
* Ruler\
Ideally: solid and hollow cylinders and spheres of equal size but different mass, and of the same material but different size (e.g. practical sets for density measurements).

## Preparation
Turn the board and tripods into an easily perceptible slope, place the block at the top and the cushion at the bottom. Place round objects of varying mass, size and shape at the top of the slope, against the block, side by side. 
Practice pulling away from the block so that all objects start rolling at the same time.

## Procedure
**Predict** The class probably already knows, that all objects fall equally fast. But does the same apply to rolling objects? Explain that later you will pull away the block so that all objects come down. Will they all stay next to each other? Why do they, or why not? 

**Observe** Then pull the block away. Ideally, everything rolls together: there is a clear difference, but you don't see which object is earlier. Some systematics are clearly needed, a clear approach too. I'm sure the students can come up with most of that, and help with implementation.

Some suggestions:
- Investigate (first) simple shapes: hollow and full spheres and cylinders are easiest.
- Isolate relevant factors: pupils can think of mass and radius, add 'shape' if necessary, and 'hollow or full' themselves.
- Most pupils do understand that you have to vary possible factors one by one if you want to measure fairly: let them think of how, and justify it themselves, but help with concreteness. Looking at a collection of cylinders and spheres can already help.
- Place two objects on top against each other and let go. First one in front, then the other. If one is faster, then that one runs out (this is sometimes more efficient than a stopwatch).
- Divide the tasks: making a plan that takes all factors into account is too difficult for most students, but planning research on whether mass in cylinders matters often succeeds.

**Explain** Discuss which of the predictions has or has not come true. Evaluate the explanations given. If necessary, explain what physicists think about them.



```{figure} demo92_figure2.jpg
---
width: 50%
align: center
---
Can we create order?
```

## Physics background
When rolling, potential energy is converted into partly translational partly rotational energy, according to: 

$$
    E_p = E_{k,r} + E_{k,t} <=> mgh = ½Iω^2 + ½mv^2
$$ 

Moment of inertia I is proportional to mass m and radius R squared for simple shapes (see table):
 $I = CmR^2$, where $C$ is determined by the shape. 
So (with $v = ωR$): 

$$
    v(h) = \sqrt{\frac{2gh}{1+C}}
$$

In short: the speed at given height, i.e. also the average speed after descent over that height, does not depend on mass or radius, only on the 'shape'. The object whose mass is closest to the axis of rotation receives relatively the most translational energy and 'wins'. All spheres roll equally fast, so do all tubes , all discs and all balls. But spheres roll faster than discs, discs faster than balls, and tubes are last down.

|Shape|C|
|---|---|
|Solid sphere|2/5|
|Hollow sphere|2/3|
|Solid cylinder|1/2|
|Hollow cylinder|1|

## Follow-up
There are practical sets that contain, for example, a hollow and full cylinder of equal mass and radius. You could verify some of the values in the table with that. But here theory is less important than systematic measurement, and coming up with an approach for it. 

```{tip}
Using material from a density practice set, it can be plausibly demonstrated that, successively, mass, material and radius do not affect the rolling time in the case of solid cylinders. A visit to a local hardware store may yield additional useful material. 
```

## References
```{bibliography}
:filter: docname in docnames
```