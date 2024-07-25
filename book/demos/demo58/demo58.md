```{figure} ../../figures/checked.png
---
width: 35%
align: right
```
# Rotating cubes

<table style="width: 100%; border-collapse: collapse; border: none;">
    <tr style="background-color: var(--background-color);">  
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">Author:</td>
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">Karel Langendonck</td>
    </tr>
    <tr style="background-color: var(--background-color);"> 
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">Time:</td>
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">10-30 minutes</td>
    </tr>
    <tr style="background-color: var(--background-color);"> 
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">Age group:</td>
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">Grade 10 and higher</td>
    </tr>
    <tr style="background-color: var(--background-color);"> 
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">Concepts:</td>
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">Angular velocity, orbital velocity, centripetal force</td>
    </tr>
</table>

## Introduction
Students often find concepts linked to circular motion difficult. Examples include the difference between orbital velocity and angular velocity and understanding the centripetal force. In this demonstration, you combine these concepts with the frictional force to create a situation where only one force provides the centripetal force. 

```{figure} demo58_figure1.JPG
---
width: 50%
align: center
name: fig:turntable
---
The turntable with LEGO bricks
```

## Equipment
- Turntable 
- Cubes of not too large mass (e.g. LEGO bricks or DUPLO dolls)
- Scales
- Ruler

## Preparation
Place a cube on the turntable of a record player, as shown in {numref}`Figure {number} <fig:turntable>`. LEGO bricks have been used as mass cubes in this setup. Determine the distance from the centre at which the cube will just slide when the turntable is turned on.

## Procedure
1.	Place a cube at a not too large distance from the centre of the turntable and measure this distance (r).
2.	Turn on the turntable. If all goes well, the cube will remain on the turntable.
3.	Have students calculate the orbital velocity and angular velocity of the cube. Have them do this for both a turntable frequency of 33 rpm and 45 rpm.
4.	Have students calculate the sliding friction force acting on the cube.
5.	Stop the turntable again, place the cube slightly further from the centre of the turntable, measure the radius of the circular path again and turn the turntable on again. 
6.	Have students again calculate the orbital velocity, angular velocity and working sliding friction force.
7.	Repeat the above step as many times as necessary until the point is reached at which the cube swings off the turntable. At that point, the point is reached where the maximum sliding friction force on the cube is an issue. You can now calculate (or have calculated) the maximum value for the static coefficient of friction (and hence the dynamic coefficient of friction).
8.	Control question: *Can you get a coefficient of friction greater than 1?*

## Physics background
```{figure} demo58_figure2.jpg
---
width: 50%
align: center
name: fig:force_balance
---
Three forces on the cube
```
Three forces act on the cube (see {numref}`Figure {number}<fig:force_balance>`): the gravitational force $F_G$, the normal force $F_N$ and the shear friction force $F_F$. At the moment the cube is on the turntable of the record player, it is the sliding friction force that provides the centripetal force. The following then applies:

$$F_F=F_{c}=\frac{mv^2}{r}$$

In this equation, $F_F$ represents the friction force (in N), $F_c$ represents the centripetal force (in N), $m$ is the mass of the block (in kg), $v$ is the tangential velocity of the block (in m/s), and $r$ is the radius of the circular path (in m).

The friction force can also be calculated by multiplying the normal force on the block by the static friction coefficient. The normal force is, of course, equal to the gravitational force. In formula form, this yields:

$F_F = \mu _s \cdot F_N = \mu _s \cdot m  g$ 

In this formula, $F_F$ again represents the kinetic friction force (in N),  is the static friction coefficient, $F_N$ represents the normal force (in N), $m$ is the mass of the block (in kg), and *g* is the acceleration due to gravity (9.81 m/s$^2$).

By combining both expressions for the kinetic friction force, you can derive a formula for the static friction coefficient for this situation:

$$ \mu _s \cdot m g = \frac{mv^2}{r} \quad \rightarrow \quad \mu _s = \frac{v^2}{rg} $$

In the above expression, you can also substitute the formula for the tangential velocity ($v = \frac{2 \pi r}{T}$, with $T$ being the period (in s)). This gives:

$$ \mu_ s = \frac{\left( \frac{2 \pi r}{T} \right)^2}{r g} = \frac{4 \pi^2 r}{T^2 \cdot g} $$ 

From this expression, the directly proportional relationship between the static friction coefficient and the radius of the circular path can be recognized. At the point where the block is flung off the turntable, the maximum value for the static friction coefficient has been reached.


```{tip}
- A few testers reported that the turntable was not smooth enough. Without a rubber mat or with a plastic cover around the mat or smeared with oil, it went well.
- This experiment is not very exciting in its execution, so it is important to involve the students well in the execution and collection of the measurement results. You can then let the students calculate some things in between. 
- Calculating the orbital period of the cube (and thus the orbital and angular velocity) will not be as simple and logical for all pupils. Pay explicit attention to this.
```
## Further investigation
In the experiment, you can vary the orbital time (where a frequency of 78 rpm is also possible on certain types of turntables), the mass of the cube and the type of surface of the cube and/or turntable. This allows experimentation with a diversity of variables, which also makes the experiment suitable as a practical for students.
One of the testers reports: On the same radius, you can apply different masses and compare whether the mass makes a difference. Is a larger mass more likely to be thrown off the turntable?


## References
```{bibliography}
:filter: docname in docnames
```