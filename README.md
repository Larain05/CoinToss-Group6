# Coin Toss Probability and Surface Analysis

**Course:** CSElec 01: Computational Science

**Activity:** Coin Toss Probability Simulation

This project analyzes the probability of coin flips to test for physical bias. We compared two specific variables, coin mass (5-Peso vs. 20-Peso) and surface friction (Wood vs. Tile), to observe their effect on the theoretical 50/50 outcome.

The primary objective is to visualize the Law of Large Numbers. We observe how experimental probability stabilizes as the sample size increases from a single group () to the full class dataset ().

## 👥 Group Members

- Muhammed Shariff Sumagka
- Lara Rain Fuentes
- Gerard Carl Palma

## 🧪 Experiment Objectives

We collected binary data (Heads=1, Tails=0) across 15 groups to analyze the following:

1. **Coin Bias:** Testing if the heavier 20-Peso coin lands differently than the 5-Peso coin.
2. **Surface Bias:** Testing if the damping of wood versus the restitution of tiles changes the outcome.
3. **Convergence:** Observing if the Head/Tail ratio settled at 0.5 as the number of trials increased.

## 📂 Files and Visualizations

### 1. Group H & T (`group6.py`)

This script analyzes our specific group data. It compares 100 flips of a 5-Peso coin against 100 flips of a 20-Peso coin on a Wood surface.

<table>
<tr>
<td><img src="assets/group6_5p.gif" width="300">

<sub>5-Peso (Wood)</sub></td>

<td><img src="assets/group6_20p.gif" width="300">

<sub>20-Peso (Wood)</sub></td>

<td><img src="assets/group6_compare.gif" width="300">

<sub>Combined Analysis</sub></td>

</tr>
</table>

### 2. Canvass H & T (`canvass.py`)

This script aggregates data by surface type. It compares the results of flips performed on Wood (Groups 1 to 8) against those performed on Tiles (Groups 9 to 15).

<table>
<tr>
<td><img src="assets/canvass_1.gif" width="300">

<sub>1A (Wood)</sub></td>

<td><img src="assets/canvass_2.gif" width="300">

<sub>1B (Wood)</sub></td>

<td><img src="assets/canvass_3.gif" width="300">

<sub>2 (Wood)</sub></td>

</tr>
<tr>
<td><img src="assets/canvass_4.gif" width="300">

<sub>5A (Wood)</sub></td>

<td><img src="assets/canvass_5.gif" width="300">

<sub>5B (Wood)</sub></td>

<td><img src="assets/canvass_6.gif" width="300">

<sub>10A (Wood)</sub></td>

</tr>
<tr>
<td><img src="assets/canvass_7.gif" width="300">

<sub>10B (Wood)</sub></td>

<td><img src="assets/canvass_8.gif" width="300">

<sub>20 (Wood)</sub></td>

<td><img src="assets/canvass_9.gif" width="300">

<sub>1A (Tiles)</sub></td>

</tr>
<tr>
<td><img src="assets/canvass_10.gif" width="300">

<sub>1B (Tiles)</sub></td>

<td><img src="assets/canvass_11.gif" width="300">

<sub>5A (Tiles)</sub></td>

<td><img src="assets/canvass_12.gif" width="300">

<sub>5B (Tiles)</sub></td>

</tr>
<tr>
<td><img src="assets/canvass_13.gif" width="300">

<sub>10A (Tiles)</sub></td>

<td><img src="assets/canvass_14.gif" width="300">

<sub>10B (Tiles)</sub></td>

<td><img src="assets/canvass_15.gif" width="300">

<sub>20 (Tiles)</sub></td>

</tr>
</table>
Surface Comparison Totals

<table>
<tr>
<td><img src="assets/wood_total.gif" width="460">

<sub>Wood Surface Combined</sub></td>

<td><img src="assets/tiles_total.gif" width="460">

<sub>Tile Surface Combined</sub></td>

</tr>
</table>

### 3. All H & T (`all.py`)

This script combines every flip from all 15 groups. It demonstrates the final convergence of the Law of Large Numbers using the complete dataset of 3100 points.

## 🚀 Installation and Usage

1. **Install dependencies:**

```bash
pip install matplotlib numpy

```

2. **Run the scripts:**

```bash
python group6.py
python canvass.py
python all.py

```

## 🎮 Controls

The visualization window is interactive for easier data inspection:

- **Right Arrow (→):** Switch to the next dataset.
- **Left Arrow (←):** Switch to the previous dataset.
- **Replay ↻ Button:** Restart the simulation to watch the cumulative trend form again.
