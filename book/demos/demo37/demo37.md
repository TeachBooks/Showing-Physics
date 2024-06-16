```{figure} ../../figures/busy.png
---
width: 35%
align: right
```
# Boyle's Law

<span style="font-size: 25px; color: gray;">How do you verify a physical law?</span>

<table style="width: 100%; border-collapse: collapse; border: none;">
    <tr style="background-color: var(--background-color);">  
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">Author:</td>
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">Norbert van Veen and Ed van den Berg</td>
    </tr>
    <tr style="background-color: var(--background-color);"> 
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">Time:</td>
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">10-20 minutes</td>
    </tr>
    <tr style="background-color: var(--background-color);"> 
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">Age group:</td>
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">14+</td>
    </tr>
    <tr style="background-color: var(--background-color);"> 
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">Concepts:</td>
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">Boyle's Law, volume, pressure</td>
    </tr>
    <tr style="background-color: var(--background-color);"> 
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">Skills:</td>
        <td style="text-align: left; padding: 3px; border: none; color: var(--text-color)">Designing experiment setup, identifying deviations, adjusting model</td>
    </tr>
</table><br>

## Introduction
Experimentally verifying a formula might seem trivial, but when you ask students in a concrete case - such as Boyle's Law - how to do it, problems arise. What do you pose, what do you measure? When do you consider results to sufficiently match theory? With Boyle's law, results often don't align. Where's the issue? With residual volume in the hose and the tip of the syringe. By incorporating that into our model, we can achieve a good fit with the measured data.

## Equipment
* Setup with a syringe
* A pressure sensor
* An interface with Coach7 as a measurement and modeling program
* Coach files (available here [**include link to the coach files**]).

## Preparation
Set up the apparatus as shown in {numref}`Figure {number} <demo37_fig1>`. Connect the pressure sensor to an interface and start the Coach measurement program. Choose from the standard activities (Measure, Upper Level, Physics) activity 7. Boyle's Law. Measure the volume manually and enter it into Coach. Conduct a measurement with at least 8 pressure and volume readings. Especially take measurements at higher pressures and smaller volumes since this is where issues with residual volume manifest. Save the measurement as a separate result file. (The measurement can also be done during the demonstration.)

```{tip}
Place the setup clearly on the lectern.
```

```{figure} A05_NvV02_fig1_opstelling_site.jpg
---
width: 50%
align: center
name: demo37_fig1
---
The experimental setup, with a syringe and a pressure sensor.
```

## Procedure
1.	Draw a closed volume of gas on the board (circle or square). *What happens to the pressure if we decrease the volume?* Students will likely have little trouble with this question.
2.	*But how exactly does it work? Can we encapsulate it in a formula? Boyle posited* $p \cdot V = \text{constant}$, *or for two situations:* $p_1 \cdot V_1 = p_2 \cdot V_2$. *What do you need to do to see if such a theoretical formula aligns with reality? How could you do that?* (very brief student discussion in pairs).
3.	Now the teacher shows the setup with a syringe with volume indication and a pressure sensor. *What should I do now to verify Boyle's Law?* Let the students think for a moment.
4.	Short discussion... Outcome: set different volumes and measure the pressure to see if it matches the formula.
5.	Then measure. Compare measured results with theoretical results.

```{figure} A05_NvV02_fig2_metingen_site.jpg
---
width: 50%
align: center
name: demo37_fig2
---
Measurements of gas pressure against volume.
```

6.	*The measured result don't match, what could be the reason?* (brief student discussion in pairs).
7.	*How can we adjust our model* $p \cdot V = \text{constant}$? (add constant term to $V$, the residual volume).
8.	*How can we determine its size? Is there a clever way to transform our graph and extract it from there?* (from the deviation of the graph).
Plot the graph of $\frac{1}{p}$ against $V$ by creating a variable $\frac{1}{p}$ in the Data Table. Show the graph of $\frac{1}{p}$ against $V$ to the students. Ask the students why it doesn't go through the origin. Have them read the residual volume from the graph.
9.	Save the measurements as a result file. Open and execute the corresponding graphical model and examine the result.
10.	Import the graph of the measurements as a background graph. Have students indicate where the differences are and try to get explanations from them.

```{figure} A05_NvV02_fig4_resultaat_voor_en_na_volumecorrectie_site.jpg
---
width: 50%
align: center
name: demo37_fig4
---
Model comparison Boyle (orange) versus Van der Waals (green).
```

```{tip}
* Clearly show the value of the pressure sensor on the digital board. 
* Show the students that the syringe is being depressed and explicitly mention the volume of the syringe.
```

## Physics background
The pressure and volume of a closed quantity of ideal gas behave according to Boyle's Law. Due to the residual volume of the hose and the pressure sensor, the hyperbola of the measurements will deviate slightly from the volume that is read from the syringe. If we call the residual volume $\Delta V$, then Boyle's Law can be written as:

$$ P \cdot (V + \Delta V) = \text{constant} ( = n \cdot R \cdot T)$$

The ideal gas law assumes that the attraction between molecules is zero and that the molecules themselves are point particles that occupy no volume. Van der Waals took into account the attraction and volume of molecules:

$$ (p + \frac{n^2a}{V^2})(V-n \cdot b) = n \cdot R \cdot T $$

The pressure is corrected for attraction in it, and the volume of molecules is taken into account. These corrections become important at a higher density. The constant b is then roughly the volume of 1 mole, and the constant a depends on the attraction between molecules. These constants are determined empirically. For details, we refer to well-known textbooks such as {cite}`young2014`, chapter 17. Coach models for Boyle's Law and for the Van der Waals version are available on the site [**include link to the coach files**].

```{figure} A05_NvV02_fig3_site.jpg
---
width: 50%
align: center
name: demo37_fig3
---
Graphical model of Van der Waals gas law. 
```

## Follow-up
What influence does a lower or higher temperature have on gas pressure measurements?

The graphical model also shows the Van der Waals gas model. Plot this graph alongside Boyle's law and ask students to explain how the differences arise. At what pressures does Boyle's law deviate from Van der Waals' gas law?


## References
```{bibliography}
:filter: docname in docnames
```