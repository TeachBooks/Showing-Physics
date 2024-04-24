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

# Induction Tubes


Author:     \
Time:	10-20 minutes \
Age group:	14 - 18 \
Concepts:	

## Introduction
A magnet falling through a coil generates an induced voltage. In this demonstration, we observe a magnet falling through a plastic tube and an aluminum tube. Both tubes have six identical coils arranged at equal intervals along the tube. We examine the measured induced voltage over time using the Coach 7 program.

```{figure} demo86_figure1.png
---
width: 50%
align: center
---
Setup with the aluminum tube on the left and the plastic tube on the right
```


## Equipment

Plastic tube and aluminum tube each with at least 3 identical coils evenly spaced around them (induction tube set CMA 081 or homemade); interface; voltage sensor (+/- 500 mV and +/- 10 V); stands; bar magnet; soft surface beneath the tube.

## Preparation

Secure the tubes in the stands. Position the tubes perfectly vertically. Connect a voltage sensor (+/- 10 V) to the coils around the plastic tube. Connect the sensor to an input on the interface. For the aluminum tube, a voltage sensor (+/- 500 mV) is more suitable. Set the voltage sensor to 0 V. Set up the Coach 7 activity to perform 1000 measurements per second. Set a trigger time of 0.1 s (trigger on the voltage sensor at 100 mV) and let the measurement last for a maximum of 2 s.

## Procedure

Move a magnet through a coil and demonstrate that it generates a voltage.
(Sketch the graph of one movement of a magnet through a coil on the board.)
Project the Coach 7 screen during the measurement on the whiteboard.
Press start measurement or F9, Coach 7 will wait for the trigger condition. Let the magnet fall through the plastic tube.
1. Display the (U,t) diagram of the magnet falling through the plastic tube (see Figure 2).

```{figure} demo86_figure2.jpg
---
width: 50%
align: center
---
Each of the six coils of the plastic tube produces a signal as the falling magnet passes. The differences between the graphs per coil allow for discussion.
```

2. How do the six graphs differ from each other? Provide an explanation.
3. Use the area determination under the Analysis/Processing option to show that the area under each peak of the coil graph gives the same value. The area value of such a peak is also equal to the area under a trough. (See Figure 3)

```{figure} demo86_figure3.png
---
width: 50%
align: center
---
With Coach 7, you can determine the value of the area in Vs.
```

4. Why should this area be equal?
5. Repeat the experiment with the aluminum tube.
6. Control question: What do you expect from the graph that will be measured?

## Physics background

An approaching magnetic field induces a current in a coil that opposes the approaching magnetic field by creating an opposing magnetic field (Lenz's Law). The coil also opposes a disappearing magnetic field by creating an attracting magnetic field. Thus, the direction of the current in the coil windings changes.

As the magnet falls and accelerates, the velocity per coil will be different. You get the lowest average velocity at the first coil and the highest average velocity at the bottom coil. If we take a plastic tube with six coils, you only get an opposing magnetic field in the six coils. In the aluminum tube, the magnet will "feel" the opposing magnetic fields throughout its entire fall. Also, see demonstration B27 in Show Physics 2.

The induced voltage can be calculated using Faraday's law:

and thus:

Because the product of N·ΔΦ is constant (the number of turns per coil is equal and also the magnet strength and the area of the coils), the product must also be equal. This product is the area under the graphs. As the magnet falls faster, the induced voltage increases and the time interval Δt becomes smaller.

## Tips
• Tester Timon Vrijmoeth notes that it is also feasible with only three coils per tube.
• If you take the absolute value of Uind, then the change in Uind over time can be seen with only positive peaks. Then the increase in falling speed is clearly visible. You can potentially use this to determine the acceleration due to gravity.

## References

```{bibliography}
:filter: docname in docnames
```

FORMULES NIET OVERGENOMEN, BESTANDEN NOG