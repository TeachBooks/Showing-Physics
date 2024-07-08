# Falling faster than g
<span style="font-size: 25px; color: gray;">free fall with rotation</span>

<table style="width: 100%; border-collapse: collapse; border: none;">
    <tr style="background-color: var(--background-color);">  
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">Author:</td>
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">Ed van den Berg</td>
    </tr>
    <tr style="background-color: var(--background-color);"> 
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">Time:</td>
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">5 minutes</td>
    </tr>
    <tr style="background-color: var(--background-color);"> 
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">Age group:</td>
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">15 and up</td>
    </tr>
    <tr style="background-color: var(--background-color);"> 
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">Concepts:</td>
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">Acceleration of gravity g (=9.81 m/s2), free fall, rotation</td>
    </tr>
</table>

<div style="display: flex; justify-content: center;">
    <div style="position: relative; width: 70%; height: 0; padding-bottom: 56.25%;">
        <iframe
            src="https://www.youtube.com/embed/nYS1nQh6oLM?si=FWANFCNAw55sEOUG"
            style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"
            frameborder="0"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
            allowfullscreen
        ></iframe>
    </div>
</div>

This description was inspired by {cite:t}`ehrlich1990`.

## Introduction
Everything that falls freely should experience an acceleration $g$? Or not? Are there exceptions? 

## Equipment
* Meter stick or equivalent
* About 30 coins, dices or hex nuts 
* If possible a high-speed camera. Most phones can do 120 or 240 frames per second. Cheap action cameras can do 120 frames/second as well.

## Preparation
Think how the visibility of observations can be maximized. For example, put a chair on top of a table and use that as one of the endpoints of the meter stick. Distribute the coins more or less equally across the length of the stick. 

```{figure} demo11_figure1.jpg
---
width: 350%
align: center
name: demo11_fig1
---
Are some of the dices falling faster than $g$?
```

## Procedure
You can start this demo with some simple illustrations:
* *Can I accelerate my hand faster than $g$? How can we investigate that?*  (Coin or stone on the hand, then pull down the hand as quick as you can). 
* *What is free fall? Can objects in free fall be accelerated faster than g?* 
You then turn to the actual demo.
* Hold the meter stick on an end while the other side rests on the chair on top of the table ({numref}`Figure {number} <demo11_fig1>`). 
* Ask the question: *Suppose I let the end of the stick go, what is then the acceleration of the end? What is the acceleration of other points of the meter stick?* (All points of the meter stick have the same angular acceleration, but must have a different linear acceleration as they cover different vertical distances in the same time.) 
* *How can we investigate this with our set-up?* 
* *Let’s first keep the meterstick horizontal and drop it.* Hold the stick at both ends. Will the coins keep contact with the stick? TRY! If there is a student with an iPhone, then film with 120 or 240 frames/second. 
* Now put the (1m) stick with one end on the chair an holding the other end with one finger. Mark the 67 cm point but do not yet tell students why. Conduct the experiment while one of the students is recording.
* It would be good to repeat and now ask students to specifically pay attention to the end of the stick. 
* Continue with a discussion about the linear acceleration of different points of the meter stick. This cannot be the same in rotational movement. If there are points which accelerate at less than $g$, shouldn’t there be points that accelerate at more than $g$? Have we seen that? 
* From our observations, which points accelerate with $g$ or less? Which points with more than %g%? The 'tipping point' is at 2/3 of the stick, so at 67 cm.
* The physics of rotation is often not in the secondary school physics curriculum. So we will not derive theoretically that the point with acceleration $g$ is at 2/3th of the meter stick. But we do ask our students for examples of similar phenomena. For example, a ladder which is put up too steep and turns over, a factory chimney which is blown up and falls over, a swimmer who stands on the diving board and lets himself fall over without jumping, etc. 

```{tip}
Using the coins as indicator one can investigate shorter and longer sticks. You can move the center of mass of the stick by taping on pieces of wood in different positions. You can also conduct video measurement using films from the iPhone or a high-speed camera. Students could do projects and could then study rotational physics first, for example from well known physics texts such as {cite:t}`young2014`.
```

## Physics background
The moment of force on a meterstick with length $L$ is $\frac{mgL}{2}$. Dividing this by the rotational inertia $(1/3)mL^2$ we obtain $\frac{3g}{2L}$ for the angular acceleration (analog to $\frac{ma}{m}$ for linear movement). 
The linear acceleration at a point on the stick is the product of (distance from point to the rotation) * angular acceleration. This will be greater than $g$ for points farther than $\frac{2L}{3}$.

## References
```{bibliography}
:filter: docname in docnames
```