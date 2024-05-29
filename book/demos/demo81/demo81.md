

# Singing Rod: Tones, Overtones, Waves and Vibrations 


Author:     \
Time:	 10 minutes\
Age group:	14 - 18\
Concepts:	

## Introduction
This demonstration consists of two parts, and, if executed properly, the second part generates a lot of noise at an irritating pitch; it's a demonstration that students will certainly not forget. By choosing the correct positions on the rod, you can even 'play' two overtones. Frequency measurements are straightforward, and the link to the physics of musical instruments is quickly established.

```{figure} demo81_1_figure1.jpg
---
width: 50%
align: center 
---
Hold the rod in the middle for the fundamental tone.
```


```{figure} demo81_1_figure2.png
---
width: 50%
align: center 
---
Hold the rod a quarter length from the top for the first overtone.
```

## Equipment
- Measuring tape; aluminum rod (over 1 m long)
- Fine sandpaper or a hammer
- Felt-tip pen or pencil
- Sound sensor with Coach 7 or phyphox app (Audio spectrum).

## Preparation
For the first part of the demonstration, test beforehand where to tap the rod and hold it in various places to get an idea of how it sounds. Optionally, try another rod made of different material.

For the second part: mark the middle and a quarter length from the top of the rod with a dash. Ensure you can measure for a short time with a high measurement frequency. Practice beforehand how to achieve a higher sound level. Rub the sandpaper at the right pace and do not press too hard.

## Procedure
### Resonating Rod: waves and vibrations
1. Hold the rod in the middle and let it resonate by tapping it against a table as in {numref}`Figure {number}<fig:demo81_2_figure1>`

```{figure} demo81_2_figure1.JPG
---
width: 50%
align: center 
name: fig:demo81_2_figure1
---
Holding the rod in the middle and tapping it against a table or striking it in another way produces a nice sound.
```


2. What do you hear and why?
3. Then hold the rod a quarter from the top.
4. Can you predict whether you will hear a higher, lower, or the same tone now? (Predict-Explain-Observe-Explain)
5. In a class discussion, the intention is for students to understand that this relates to nodes and antinodes and overtones.
6. After that, you can choose another place to hold the rod one or two more times.
7. Control question: What will you hear if you hold the rod at one of the ends and let it resonate? 
```{figure} demo81_2_figure2.JPG
---
width: 50%
align: center 
---
If you hold the rod at the end, you only hear a dull thud. The rod does not resonate.
```

### Singing Rod: Tones and overtones
Hold the rod loosely in the middle. Rub the fine sandpaper along the rod until the rod starts to 'sing' (squeak/howl). By rubbing at the right pace, you can achieve a reasonable sound level. A short tap with a hammer on the rod also produces a nice tone.

Turn the rod around and ask the students where the sound of the rod is coming from exactly.
How can you stop the 'singing'? Let the students think with that information about whether the vibration of the rod is longitudinal or transverse and how to determine this.

Loosely hold the rod a quarter from the top. Rub the fine sandpaper along the rod until the rod starts to 'sing' (squeak/howl). By rubbing at the right pace, a high sound level can be achieved again. (If rubbing does not work, then tap the rod with a hammer.)
How does this tone differ from the first tone you heard?
Why do you need to hold the rod in a different place to hear this tone?

Measure the frequency of the tones with Coach 7 or phyphox and determine the speed of sound in the rod. The rod has two open ends.
Let the students sketch the vibration modes of the rod for the fundamental tone and overtone.
An experienced demonstrator can even produce a second overtone. Control questions: Where should you hold the rod then? Which tone do you dampen?

## Physics Background
By striking the rod at one end (for example, against the table), many different vibrations are created in the rod. By holding the rod in the middle, a node is created there, leaving only vibrations with a node in the middle. Vibrations with a higher frequency dampen faster. Therefore, you hear the relatively low fundamental tone the best. Sometimes you have to wait for the overtones to die out.
By holding the rod a quarter length from the top, a vibration with a complete wavelength, thus resulting in an octave higher tone, fits as the fundamental tone.

By rubbing with sandpaper, the rod vibrates both transversely and longitudinally. This can easily be demonstrated by making the rod 'sing' and then damping it. This damping occurs both at the ends in the longitudinal direction and by holding the rod (width direction). The rod vibrates in both directions.
For the fundamental tone, there is a node in the middle and a antinode at the ends. The wavelength is thus twice the length of the rod. The corresponding frequency can be calculated with:
$$
f = \frac{n \cdot v_{Al}}{2l}
$$

```{figure} demo81_1_figure3.JPG
---
width: 50%
align: center 
name: fig:tone_drawings
---
The transversely drawn fundamental tone and the first overtone.
```

The speed of sound in the rod can be calculated with: $ v = \sqrt{\frac{E}{\rho}} $
Here, E is the elastic modulus of the material used (71 GPa for aluminum) and ρ is the density of the rod. Conversely, you can use the measured frequency to determine the elastic modulus of the material.

When 'playing' the overtone, the nodes are at a quarter and three-quarter length of the rod.

```{figure} demo81_1_figure4a.jpg
---
width: 50%
align: center 
---
```

```{figure} demo81_1_figure4b.png
---
width: 50%
align: center 
name: fig:coach7_result
---
Results of audio spectrum measurement with phyphox and Fourier analysis in Coach 7 
```


```{tip}
- Do not hold the rod too tightly, as this will cause excessive damping.
- It is important where you hold the rod: halfway or at a quarter. Rub the bottom of the rod in a short, quick motion. A hammer as a vibration source is handy if you have a rod with high density. 
- When 'playing' the fundamental tone, an analysis tool will also find the second overtone, but not the frequency of the first overtone ({numref}`Figure {number}<fig:coach7_result>`). You can explain why this is with the help of {numref}`Figure {number}<fig:tone_drawings>`.
- Use Coach 7 with a short time (≈ 2 s) and a measurement frequency of about 2 kHz to perform as accurate Fourier analysis as possible.
- Phyphox (Audio spectrum) quickly provides a measured frequency. The higher overtones are visible, but the corresponding peak values cannot be read. Export the measurement from phyphox to Excel.

