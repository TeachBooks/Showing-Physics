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

# High Voltage


Author:     \
Time:	30-50 minutes 	\
Age group:	Grade 10 and up\
Concepts:	transformer, electrical power, voltage division, replacement resistance. 

```{figure} demo94_figure1.jpg
---
width: 50%
align: center
---
No light without transformer
```

## Introduction
A rather complicated demonstration showing that electrical energy transport is more efficient at high voltage. Besides the transformer, almost all basic concepts of electricity are discussed.
```{warning}
In simple form, this experiment can also be used in junior school, without too much theory, to show that transforming can be useful. This demonstration cannot be carried out as a student practical because the 'high-voltage line' can carry more than 40 V AC voltage, which can be dangerous.

Know that this demonstration is carried out in the Netherlands (230V, DC)!
```

## Equipment
* Two demonstration transformers with, if possible, the same transformation ratio (e.g. 50 : 600), or two (preferably equal) mains adapters or bell transformers; 
* AC power supply (0-30 V); AC current meter(s) (range at least 0.5 A); 
* AC voltage meter(s), preferably digital with not too small digits (range depends on the transformers, maybe 500 V). 
* Bulb (e.g. 6 V;0.5 A) in socket; 
* long thin wires with a resistance preferably a bit larger than that of the burning bulb (constantan wire 0.20 mm will do); 
* plug pins and switching or tripod material to build the 'high-voltage line'; 
* various cords, also some very long ones.

## Preparation
1.	Build a 'high voltage line' from the two thin wires, 1.5-2 m long if the demonstration table allows.
2.	Connect the power supply at one end (AC voltage!) and the light bulb at the other.
3.	Connect a voltage meter to the source.
4.	If necessary, prepare a second voltage meter with long cords (must be able to span the length of the high-voltage line).
5.	Out of sight, prepare the two transformers in such a way that they can be incorporated into the circuit in no time.
6.	Prepare two cords as long as the transmission line.
7.	Also prepare the current meter.

```{figure} demo94_figure2.jpg
---
width: 50%
align: center
---
There is light with transformer
```

```{figure} demo94_figure3.jpg
---
width: 50%
align: center
---
Possible in this way as well
```

## Procedure
Turn it into a story; a more detailed example is at www.nvon.nl/showdefysica.

On the left is the power station, on the right is a village or town, in between is the transmission line. (Just put a piece of paper on the wires in case students in the back don't see them). The customer should have 6 volts (depends on the bulb used).
Set the power supply to 6 volts (use the voltage meter), and note that the light is not lit or barely lit. Measure the voltage at the customer's premises: far too low!
If necessary, also measure the current, calculate the power the customer is getting and the loss rate.
Increase the voltage of the power station until the customer does get 6 V; then the power station delivers ... V (measure). The relative loss remains the same.
Problem analysis: the consumer is in series with the transmission lines; so the voltage distributes across lines and customer load. 
Turn down the source to 6 V. Measure the voltage across both lines and the consumer and find that the total is 6 V.
So the lines have too much resistance relative to the consumer. The consumer inevitably has a very small resistance because it is a parallel circuit of countless devices and lamps: that gives a very small replacement resistance.
First solution: make the resistance of the line smaller. Replace the thin wires with 'normal' cords (just connect them in parallel), then the problem is solved. On this scale, it can be done, but in reality it is prohibitively expensive....

Look at it another way: If the resistance of the line cannot be easily reduced, then less current must pass through it, because the energy loss is I2∙R. But the power must remain the same. This is possible if we increase the voltage, because the power transported is U∙I.
So the second solution is: insert two transformers. The first transforms up and the second transforms down. Set the 'power plant' to 6 V again and see that the light does burn properly now. Measure the voltage at the consumer.
Also measure the voltage at the transmission line and see if that matches (approximately) the transformation ratio.
If necessary, measure the current through the line (carefully!) and find that it is much smaller than without the transformers, i.e. I2∙R is much smaller.
Also measure the voltage 'across the line' and find that it is also much smaller. So the voltage drop has become much smaller while the voltage is much larger. Relatively, that chops double...

**Figuren samenvoegen**
```{figure} demo94_figure4a.jpg
---
width: 50%
align: center
---
next to  each other
```

```{figure} demo94_figure4b.jpg
---
width: 50%
align: center
---
next to  each other
```

```{figure} demo94_figure4c.jpg
---
width: 50%
align: center
---
Conclusion
```

Finally, discuss the whole circuit again: there are three separate circuits, each with a source and a consumer. If the transformers are ideal, there is only loss in the transmission line.
If required, everything can then be measured and the whole circuit calculated. For this, the best strategy is to draw the whole circuit, put in all the data and then see where to start calculating.

## Physics background
Obviously, the operation of the transformer must be known here, but almost all the basic concepts of electricity also come into play. These of course need to be known; the 'new' thing about this experiment is mainly the application. As such, the experiment can be a good repetition and integration exercise, especially if it is also calculated through, or if a good calculation example follows. 

```{tips}
- If no suitable lamps can be found with the transformers used, a suitable (power) resistor can be used as a load, with a small lamp parallel to it 'for the eye'.
- Some colleagues have a 'model high voltage' for this demonstration; see photo 3. 
- If you only want to do the test qualitatively, for example in an undergraduate classroom, you can start by connecting the light directly to the power station and setting it so that the light burns properly. Then the transmission line in between and then the transformers.
Then you don't have to measure anything at all to still show the principle.

```
## Follow-up
Of course, there can be plenty of further experimentation, e.g. with different loads, different transformation ratios, different lines. But not without supervision

```{warning}
Depending on the power supply and transformers used, voltages of more than 40 V can be put on the line, even hundreds of volts when using mains adapters or bell transformers. So no students near the setup and no more than one hand on the high voltage....
[Here, if there is enough space, the following piece of spare text can be added].
This is an aspect that could also be discussed in more detail: The voltage on the line is dangerously high. Why can you feel free to grab it with one hand anyway? But what should you definitely not do? And if you were to ground one point? See also www.nvon.nl/showdefysica.
```

## References
```{bibliography}
:filter: docname in docnames
```