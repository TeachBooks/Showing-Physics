# On a roll

<table style="width: 100%; border-collapse: collapse; border: none;">
    <tr style="background-color: var(--background-color);"> 
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">Author:</td>
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">Peter Dekkers</td>
    </tr>
    <tr style="background-color: var(--background-color);"> 
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">Time:</td>
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">30-50 minutes</td>
    </tr>
    <tr style="background-color: var(--background-color);"> 
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">Age group:</td>
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">Grade 10</td>
    </tr>
    <tr style="background-color: var(--background-color);"> 
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">Concepts:</td>
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">potential and kinetic energy, moment of inertia, translational energy</td>
    </tr>
</table>

## Introduction
If you let a bunch of different round objects roll down a slope, some will be faster than others. Careful study will show that the mass and size do not matter, but the shape does. This is difficult to understand or infer from observations. However the observations can encourage students to propose systematic investigations to establish which objects roll faster. In this demonstration, the teacher can help students develop skills in planning of an investigation as well as systematic collection, representation and interpretation of data. The test is inspired by a question in an old old televised science quiz: if you let a boiled and a raw egg roll down a slope simultaneously, which will arrive at the bottom first? 

```{figure} demo92_figure1.jpg
---
width: 80%
align: center
---
Which rolling object reaches the bottom first?
```

This demonstration has been published in the Dutch magazine for science teachers {cite:t}`dekkers1999drogen`.

## Equipment
* A variety of objects that can roll. 
* Long wide board (with edges if possible); 
* Tripods
* Block and cushion of the same width as the board
* Scales
* Stopwatch
* Ruler\
Ideally: include among the objects solid and hollow cylinders and spheres of equal size but different mass, and of the same material but different size (e.g. practical sets for density measurements).

## Preparation
Turn the board and tripods into a slope, make it easily visible for all, place the block at the top and the cushion at the bottom. Place round objects of varying mass, size and shape at the top of the slope, against the block, side by side. 
Practice pulling away from the block so that all objects start rolling at the same time.



<div style="display: flex; justify-content: center;">
    <div style="position: relative; width: 70%; height: 0; padding-bottom: 56.25%;">
        <iframe
            src="https://www.youtube.com/embed/PY2blUzvXvQ?si=PzcmCcQzGvPmgHVM"
            style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"
            frameborder="0"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
            allowfullscreen
        ></iframe>
    </div>
</div>

*A slightly altered version of the demo, the materials used in the video are shown in {numref}`Figure {number} <demo92_figure3>`.*

```{figure} demo92_figure3.jpg
---
width: 70%
align: center
name: demo92_figure3
---
The materials as used in the video.
```

## Procedure
**Predict** The class probably already knows, that all objects fall equally fast. But does the same apply to rolling objects? Explain that you are going to remove the block so that all objects start at the same time in rolling down. Will they all stay next to each other? Will some roll faster? If so, which will be faster and why? 

**Observe** Next pull the block away. Ideally, as everything starts rolling, there are a clear differences in the way the objects roll, but it's not at all clear which kinds of object are faster. A more systematic and clearer approach is clearly needed. Your students can probably come up with that kind of plan if you help them a little, and will be happy to assist with its implementation.

```{figure} demo92_figure2.jpg
---
width: 70%
align: center
---
Can we create order?
```

Some suggestions:
- Investigate (first) simple shapes: hollow and full spheres and cylinders are easiest.
- Isolate relevant factors: pupils can probably come up with mass and radius. You will want to add 'shape' if they don't mention it, and 'hollow or full'.
- Most pupils do understand that it is necessary to vary possibly relevant factors one by one (fair measurement) if you want to establish the influence of each: let them make a plan for doing so. Encourage them to justify their method and finding a systematic way to organize data. Looking at a collection of cylinders and spheres can already help organize their thinking; you may want to suggest to investigate only two objects at a time.
- A method that works well is: place two objects at the high end touching each other, one in front of the other, and let go. First one in front, then the other. If one of the two is faster, that is quite easy to see (if you insist on a quantitative approach you may want to use a stopwatch, but this may be less convincing).
- Divide the tasks: making a plan that takes all factors into account maybe be too difficult for the students, but planning research on whether mass in cylinders matters often succeeds.

**Explain** Discuss which of the predictions turned out to be correct and which were not. Evaluate the explanations given. If necessary, explain how physicists explain the phenomena.

## Physics background
When rolling down a slope, potential energy is converted into kinetic energy which is partly translational, partly rotational energy, and satisfies the equation: 

$$
    E_p = E_{k,r} + E_{k,t} <=> mgh = ½Iω^2 + ½mv^2
$$ 

Moment of inertia I is proportional to mass m and radius R squared for simple shapes (see table):
 $I = CmR^2$, where $C$ is determined by the shape. 
So (with $v = ωR$): 

$$
    v(h) = \sqrt{\frac{2gh}{1+C}}
$$

In short: the speed at a given height, i.e. also the average speed after descent over that height, does not depend on mass or radius, only on the moment of inertia, the 'shape'. The object whose mass is situated closest to the axis of rotation receives relatively the most translational energy and 'wins'. All spheres roll equally fast, so do all tubes , all discs and all balls. But spheres roll faster than discs, discs faster than balls, and tubes arrive last.

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
