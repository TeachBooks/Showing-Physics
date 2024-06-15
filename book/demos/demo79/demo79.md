---

<div style="clear: both;">

```{figure} ../../figures/ready.png
---
width: 35%
align: right
```

</div>
jupytext:
<table style="width: 100%; border-collapse: collapse; border: none;">
    <tr style="background-color: white;"> 
        <td style="text-align: left; padding: 3px; border: none;">Author:</td>
        <td style="text-align: left; padding: 3px; border: none;">NAME</td>
    </tr>
    <tr style="background-color: white;">
        <td style="text-align: left; padding: 3px; border: none;">Time:</td>
        <td style="text-align: left; padding: 3px; border: none;">TIME</td>
    </tr>
    <tr style="background-color: white;">
        <td style="text-align: left; padding: 3px; border: none;">Age group:</td>
        <td style="text-align: left; padding: 3px; border: none;">GRADE OR AGE</td>
    </tr>
    <tr style="background-color: white;">
        <td style="text-align: left; padding: 3px; border: none;">Concepts:</td>
        <td style="text-align: left; padding: 3px; border: none;">CONCEPTS</td>
    </tr>
</table><br>
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

# Physics of the Panflute: Determination of the Speed of Sound

Author:     \
Time:	  	15-20 minutes\
Age group:	16 - 18\
Concepts:	

## Introduction
In this demonstration, we use a homemade panflute and take measurements of the lengths of the tubes and the corresponding frequency using the Phyphox app. The theory of standing waves in an open and closed tube then provides an accurate determination of the speed of sound.

```{figure} demo79_figure1.jpg
---
width: 50%
align: center
---
The demonstration requires minimal equipment: a few PVC tubes of different lengths and your phone.
```


## Equipment
5 PVC tubes of different lengths but with the same diameter; phone with Phyphox app.

## Preparation
Start the Phyphox app and load the Jupyter Notebook.

## Procedure
1. Blow over the top end of a long tube with your thumb on the bottom end of the tube.\
*Is the pitch higher/lower or equal to the pitch you get when blowing over a short tube? Why?*\
Blow over the short tube to confirm.
2. Explain that you want to determine the relationship between the length of the tube and the pitch (resonant frequency). Then measure the corresponding frequencies for all tube lengths using the Phyphox app for frequency measurements.
3. Record the data in the Notebook. You can ask the students to determine the speed of sound themselves, assuming L = λ/4. They will then see that the calculated wave speed increases each time. This is strange! You can exploit this experience of 'strangeness' to make it plausible that it is useful to analyze the results with the computer/graphically. Then run the cells so that you see the graphs. *Is it true that the frequency decreases as the tube length increases?*
4. Pay attention during the explanation to the linear relationship between the frequency of the fundamental tone f and the reciprocal of the tube length l. The slope coefficient gives the speed of sound.\
*But does the value actually match when using only one measurement? Why not?*
5. Blow hard over the tube. You will clearly hear an overtone that you can measure. Check: *Make a drawing of a possible overtone in the tube. Calculate the resonant frequency based on that drawing.*\
Verify this frequency with a measurement.

```{figure} demo79_figure2.jpg
---
width: 50%
align: center
---
The data presented with coordinate transformation. Based on the function fit, the speed of sound in air is determined.
```

## Physics background
In the open-closed tube, the fundamental frequency is equal to:
$$f=\frac{v}{\lambda}=\frac{v}{4 l^{\prime}}$$

Here, we note l' because the node does not lie exactly at the opening of the tube but just outside it. So:
$$l^{\prime}=l+\Delta l$$

Where ∆l is a systematic deviation. This also explains why you need measurements at multiple lengths.

```{tip}
*	When blowing hard on the tube, you clearly hear one of the overtones. The HAVO exam 2017-2 (question 1) also addresses this demonstration and can be used for further practice. Instead of using tubes of different lengths, you can also submerge one end in a tall measuring cylinder. The effective length of the tube is then easily adjustable. An interesting variant of this demonstration can be seen here: (https://youtu.be/eaeyIJAYsvo).
```
