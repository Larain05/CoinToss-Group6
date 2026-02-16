# Coin Flip Bias & Probability Analysis

**Course:** CSElec 01: Computational Science  
**Activity:** Coin Toss Probability Simulation

This project analyzes the probability of coin flips (Heads vs. Tails) to test for physical bias. We compared two variables—**coin mass** (5-Peso vs. 20-Peso) and **surface friction** (Wood vs. Tile)—to see if they affect the theoretical 50/50 outcome.

The main goal is to visualize the **Law of Large Numbers**: observing how the probability stabilizes as the sample size grows from a single group ($N=200$) to the full class dataset ($N \approx 3000$).

## 👥 Group Members

- **Muhammed Shariff Sumagka**
- **Lara Rain Fuentes**
- **Gerard Carl Palma**

## 🧪 Experiment

We collected binary data (Heads=1, Tails=0) across 15 groups to test three things:

1.  **Coin Bias:** Does the heavier 20-Peso coin land differently than the 5-Peso coin?
2.  **Surface Bias:** Does the high damping of wood vs. the restitution of tiles change the outcome?
3.  **Convergence:** Does the Head/Tail ratio actually settle at 0.5 over time?

## 📂 Files & Visualizations

### 1. Group 6 Analysis (`group6.py`)

Analyzes our specific group data, comparing 100 flips of a 5-Peso coin vs. a 20-Peso coin on a Wood surface.
![Group 6 Animation]

<table>
<tr>
<td><img src="assets/group6_5p.gif" width="300">

<sub>5-Peso (Wood)</sub></td>

<td><img src="assets/group6_20p.gif" width="300">

<sub>20-Peso (Wood)</sub></td>

<td><img src="assets/group6_compare.gif" width="300">

<sub>Comparative Analysis</sub></td>

</tr>
</table>
Importan

### 2. Surface Comparison (`compare_surfaces.py`)

Aggregates data by surface type to compare the behavior of Wood (Groups 1–8) against Tiles (Groups 9–15).
![Surface Comparison Animation](assets/surfaces.gif)

### 3. Global Convergence (`all.py`)

Combines all 3100 data points from all 15 groups to demonstrate the final convergence of the Law of Large Numbers.
![Global Convergence Animation](assets/all_data.gif)

## 🚀 How to Run

1.  **Install dependencies:**

    ```bash
    pip install matplotlib numpy
    ```

2.  **Run the scripts:**
    ```bash
    python group6.py
    python compare_surfaces.py
    python all.py
    ```

## 🎮 Controls

The graph window is interactive:

- **Right Arrow (→)**: Next dataset.
- **Left Arrow (←)**: Previous dataset.
- **Replay ↻**: Restart the simulation to watch the trend form again.
