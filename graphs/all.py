import matplotlib
# Force standard GUI backend to prevent "invalid command" errors
matplotlib.use('TkAgg') 

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Button
import numpy as np

# Import your theme file
# NOTE: Ensure theme.py is inside the 'graphs' folder and you are running from the parent directory.
import theme

# =========================
# 1. THE DATA
# =========================
groups_data = {
    "Group 1": {
        "1B": [0,1,0,0,1,1,1,0,0,0,1,0,0,0,0,1,0,1,1,1,0,1,0,0,0,0,0,1,1,0,0,1,1,0,1,0,1,1,0,0,1,1,1,1,1,1,1,0,1,0,0,1,1,1,0,0,0,1,0,0,1,0,1,1,1,0,1,1,1,1,0,1,0,1,1,1,0,1,0,1,0,0,1,0,1,0,0,0,0,0,0,0,0,1,1,0,1,1,0,1],
        "2": [1,0,1,0,0,1,0,1,0,0,0,1,1,1,0,1,1,0,0,1,0,0,1,0,0,1,0,1,1,1,0,1,0,0,0,1,1,0,0,0,1,0,1,1,0,1,1,0,1,0,0,0,0,1,1,1,0,0,0,1,0,0,1,1,1,1,0,1,1,0,0,0,1,0,1,0,0,0,0,1,1,0,1,1,0,1,1,1,0,0,0,0,1,1,1,0,0,0,0,0]
    },
    "Group 2": {
        "5A": [1,1,1,0,0,1,1,1,0,1,0,1,0,0,1,0,0,0,0,0,1,1,1,1,0,1,0,1,0,1,1,0,1,1,0,0,0,1,1,1,0,0,0,0,1,1,1,0,0,1,0,1,1,0,1,0,1,1,1,1,1,1,0,0,1,0,1,1,1,1,0,0,1,1,0,0,1,0,0,1,1,1,0,1,0,1,1,1,0,0,0,1,0,0,0,1,0,1,0,1],
        "1B": [0,0,1,0,1,1,1,0,0,0,1,0,0,0,1,1,1,1,1,0,1,1,0,0,1,0,1,0,1,0,0,0,0,1,1,1,1,1,0,0,0,1,0,1,1,1,0,0,1,0,0,1,0,1,1,1,0,1,1,0,1,0,0,0,1,1,0,1,0,1,0,1,0,0,1,0,1,1,0,1,1,0,0,1,0,1,0,0,0,1,1,0,1,0,1,1,1,0,1,0,0]
    },
    "Group 3": {
        "10A": [0,0,1,0,1,1,0,1,1,0,0,0,0,0,1,0,1,1,0,0,1,0,1,1,1,1,0,1,1,1,0,0,0,0,0,1,0,0,0,0,1,1,1,0,0,1,1,1,1,1,1,0,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,0,0,1,0,0,0,0,0,0,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,0,0],
        "1B": [1,1,1,0,1,0,1,1,1,0,1,0,1,1,1,0,1,1,0,1,0,1,0,1,1,0,1,0,1,0,1,1,1,1,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,0,1,1,0,1,0,1,0,1,0,1,1,1,1,0,1,1,0,1,0,1,1,0,1,0,1,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    },
    "Group 4": {
        "5B": [0,1,0,1,0,0,1,0,0,1,0,1,1,1,0,1,1,1,1,0,1,0,1,0,0,1,0,1,0,0,0,1,1,1,0,0,1,0,0,1,0,1,1,0,0,1,1,1,0,1,1,1,0,0,1,0,0,1,0,0,0,1,0,1,0,1,0,1,1,0,0,1,1,0,1,1,1,0,1,1,1,1,0,0,1,1,0,1,1,1,0,1,1,0,0,0,0,0,1,1],
        "5A": [0,1,0,1,1,0,1,1,0,1,0,1,1,0,0,1,1,0,1,1,0,1,0,1,1,0,0,0,1,1,0,0,0,0,1,1,0,1,0,0,0,0,1,0,0,0,1,1,0,1,0,1,0,1,1,1,1,1,0,0,1,0,1,1,0,1,1,0,1,1,0,0,1,1,1,0,1,1,1,0,0,1,0,1,0,1,0,1,0,0,0,1,0,1,1,1,1,1,1,1]
    },
    "Group 5": {
        "1A": [0,1,0,1,1,1,1,0,1,0,1,0,1,1,0,1,1,1,0,1,1,1,0,0,1,1,1,1,1,1,1,0,1,1,1,0,0,1,1,0,0,0,1,0,0,1,1,1,1,0,1,0,0,1,0,0,1,0,1,1,0,0,0,1,0,1,1,1,0,0,0,1,0,0,0,1,0,1,1,0,1,1,0,1,1,1,0,1,1,1,1,1,0,1,1,0,1,0,1,0],
        "1B": [1,1,0,1,0,0,1,0,1,0,0,0,1,0,1,1,0,0,0,0,0,1,0,1,1,1,1,0,1,1,0,1,0,0,0,1,0,1,0,1,1,1,0,0,0,0,0,1,0,0,1,0,0,1,0,1,0,0,1,0,1,0,0,0,0,0,0,1,0,1,0,1,1,1,1,0,1,0,0,0,0,0,1,1,1,1,1,0,1,0,0,1,0,0,0,0,0,1,0,1]
    },
    "Group 6": {
        "20": [0,0,1,1,0,0,0,1,0,1,1,0,0,1,1,0,0,0,0,0,1,0,1,0,1,0,1,0,1,0,1,0,0,0,0,0,1,0,1,0,0,1,1,0,0,0,1,1,0,0,1,1,1,1,0,0,1,1,0,0,1,1,0,0,1,1,1,0,1,0,0,0,1,0,0,1,0,0,1,0,1,1,1,0,0,0,1,1,0,0,1,1,1,1,1,1,0,1,1,1],
        "5B": [1,1,1,0,1,1,0,1,0,1,1,0,0,0,1,1,1,0,0,0,1,1,0,1,0,0,1,1,0,0,0,1,1,1,0,1,0,0,1,0,0,0,0,1,0,1,1,0,1,0,0,0,1,1,0,0,0,1,1,0,1,1,0,0,0,1,0,0,0,1,1,0,1,1,0,1,1,1,0,0,0,0,1,0,0,0,0,1,0,1,0,0,1,1,0,0,1,0,1,0]
    },
    "Group 7": {
        "10A": [1,1,0,1,0,0,0,0,1,1,0,0,1,0,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,1,1,0,0,0,0,1,0,0,0,1,0,1,1,0,1,1,0,0,1,1,0,1,0,0,1,1,0,0,0,1,0,1,0,0,1,1,1,0,0,1,1,0,0,1,1,0,0,0,1,0,1,0,0,1,0,1,0,0,1,0,0,0,0,1,1,1,1,0],
        "5A": [1,0,1,0,1,1,0,0,1,1,0,1,1,1,0,0,0,1,0,1,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,1,0,1,0,0,1,0,0,1,1,1,1,0,0,1,1,0,1,1,1,1,0,1,1,0,1,0,0,1,1,0,1,0,0,0,0,1,1,1,1,0,1,0,0,1,0,0,1,0,1,0,1,0,1,0,1,1,1]
    },
    "Group 8": {
        "10B": [0,1,0,1,0,0,1,0,0,1,0,1,1,1,0,1,1,1,1,0,1,0,1,0,0,1,0,1,0,0,0,1,1,1,0,0,1,0,0,1,0,1,1,0,0,1,1,1,0,1,1,1,0,0,1,0,0,1,0,0,0,1,0,1,0,1,0,1,1,0,0,1,1,0,1,1,1,0,1,1,1,1,0,0,1,1,0,1,1,1,0,1,1,0,1,1,1,0,1,1],
        "1A": [0,1,0,1,1,0,1,1,0,1,0,1,1,0,0,1,1,0,1,1,0,1,0,1,1,0,0,0,1,1,0,0,0,0,1,1,0,1,0,0,0,0,1,0,0,0,1,1,0,1,0,1,0,1,1,1,1,1,0,0,1,0,1,1,0,1,1,0,1,1,0,0,1,1,1,0,1,1,1,0,0,1,0,1,0,1,0,1,0,0,0,1,0,1,1,0,0,0,1,1]
    },
    "Group 9": {
        "20": [0,0,1,1,1,1,0,0,0,0,1,1,1,0,0,0,0,0,1,1,1,0,0,0,0,1,1,1,0,0,0,1,0,0,0,1,1,0,0,0,1,1,1,0,0,1,0,0,0,1,1,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,1,1,0,1,0,0,0,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0,0,1,1,0,1,1,1,0,0,0],
        "5B": [1,0,1,1,1,0,0,1,1,0,1,1,0,0,1,1,0,1,1,0,0,0,1,1,0,0,1,1,0,0,1,0,1,0,0,0,0,1,1,0,0,1,1,1,1,0,0,0,1,1,0,0,1,1,0,0,1,1,1,0,0,0,1,0,0,1,1,1,0,0,0,1,0,0,0,0,0,1,1,0,0,0,0,1,1,1,0,0,0,0,1,1,0,0,1,1,1,0,1,1],
        "1B": [0,0,1,1,0,1,0,1,1,0,0,1,1,1,0,0,0,1,1,1,0,1,0,0,1,1,0,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1,0,0,1,1,0,0,0,1,1,0,1,1,0,1,1,1,1,0,0,0,1,1,1,1,0,0,0,1,0,0,0,1,1,0,0,1,1,0,0,0,0,1,1,1,0,0,1,0,1,1,0,0,1,0,0,1,1,0]
    },
    "Group 10": {
        "10B": [0,0,1,0,0,1,0,1,1,0,1,1,1,0,0,1,0,0,1,1,0,1,0,1,1,1,0,1,1,1,0,0,1,0,0,0,1,0,1,0,1,0,0,1,1,0,1,0,0,1,0,0,1,1,0,0,1,1,1,0,0,0,0,1,0,0,1,0,0,0,0,0,0,1,1,0,1,1,1,0,0,0,0,1,0,0,1,0,0,0,1,1,0,0,0,1,1,1,1,0],
        "5B": [1,1,1,0,0,1,0,1,1,0,0,1,0,0,0,1,1,1,1,0,1,0,0,1,0,1,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,1,1,0,1,0,0,0,0,1,1,1,1,1,1,1,1,0,1,0,1,0,0,0,1,1,0,0,0,1,1,1,0,1,0,1,1,0,0,1,0,1,1,1,0,1,1,1,1,0,1,0,0,1,0,1,0,0,1,1]
    },
    "Group 11": {
        "10B": [1,0,0,0,1,1,0,1,0,0,0,1,0,1,0,1,0,1,0,1,1,1,0,0,1,1,0,1,1,0,1,1,0,0,1,1,0,0,1,0,1,1,1,1,0,0,0,0,1,1,1,1,0,0,1,1,0,1,0,0,1,0,1,0,1,0,1,0,1,0,0,1,1,1,1,0,1,1,1,0,1,1,1,0,1,0,1,0,1,1,1,0,1,1,1,0,0,0,0,0],
        "1A": [1,0,1,1,0,0,0,1,1,1,1,1,0,0,0,1,1,0,1,0,1,1,0,1,0,1,0,1,1,0,1,0,0,1,0,0,0,1,0,1,1,1,0,1,0,1,0,1,0,0,0,1,1,0,0,1,0,0,0,0,0,1,1,0,0,0,1,1,1,0,1,0,1,0,1,1,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,1,0,1,0,0,0,1,0]
    },
    "Group 12": {
        "5B": [1,1,1,0,1,0,0,1,0,0,1,0,1,0,0,0,0,1,0,1,1,0,0,1,1,0,1,1,0,1,1,1,0,0,1,0,0,1,0,0,0,1,1,1,1,1,0,1,0,1,0,1,1,1,1,0,0,0,0,0,0,1,1,0,1,1,1,1,0,1,0,1,0,1,1,1,1,0,1,1,0,1,1,0,0,1,1,1,1,0,0,0,0,0,1,0,0,0,0,1],
        "5A": [0,0,0,0,0,0,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,1,0,0,1,0,1,1,1,0,1,0,1,1,0,1,1,0,1,0,0,1,0,1,0,1,1,0,0,1,1,0,1,0,1,0,0,0,0,1,1,1,1,0,1,1,0,0,0,0,1,0,1,0,1,0,1,1,1,1,1,0,0,1,1,1,0,0,1,1,1,0,1,0,1,0,0,1,1,1]
    },
    "Group 13": {
        "10A": [0,0,0,1,0,0,0,1,0,0,0,0,0,0,1,1,1,0,0,0,1,0,0,0,0,0,0,1,1,1,0,1,1,0,1,1,1,1,0,1,0,1,0,1,0,1,0,1,1,0,1,1,0,1,1,1,1,0,1,0,0,0,0,0,0,1,1,1,1,1,0,0,1,1,1,0,1,0,0,0,1,1,1,0,0,0,1,1,0,1,0,0,1,1,0,1,0,1,0,1],
        "1A": [1,1,1,0,1,1,1,0,1,1,1,1,1,1,0,0,0,1,1,1,0,1,1,1,1,1,1,0,0,0,1,0,0,1,0,0,0,0,1,0,1,0,1,0,1,0,1,0,0,1,0,0,1,0,0,0,0,1,0,1,1,1,1,1,1,0,0,0,0,0,1,1,0,0,0,1,0,1,1,1,0,0,0,1,1,0,0,0,0,0,1,1,1,0,0,0,0,0,1,0]
    },
    "Group 14": {
        "20": [0,1,1,1,1,1,0,1,1,1,0,0,1,1,0,1,1,0,0,0,1,0,0,0,0,0,0,1,0,0,1,0,0,1,1,1,0,1,0,0,1,0,1,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1,1,0,0,1,1,1,0,0,0,0,0,1,0,0,1,1,0,0,1,1,0,1,1,1,0,1,0,1,1,1],
        "1A": [0,0,0,1,1,1,1,1,0,1,1,0,0,0,1,0,1,0,0,0,0,1,1,0,1,1,1,0,1,0,1,0,0,0,1,0,1,1,0,0,0,1,0,1,1,0,0,0,0,0,1,0,1,0,0,1,1,0,1,1,0,0,0,1,1,1,0,0,1,1,1,0,1,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,0,1,1,0,0,0,1,0,0,0,1,0,0]
    },
    "Group 15": {
        "5B": [0,0,1,1,0,0,1,0,1,1,1,0,1,0,0,1,1,1,0,1,1,1,1,0,0,0,0,0,0,1,1,0,1,1,1,1,1,1,0,1,1,1,1,1,1,0,0,1,1,1,0,0,0,1,0,0,1,1,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,1,1,1,1,0,1,1,1,1,0,1,0,0,1,0,1,0,1,0,0,0,0,0,0,1,0,1],
        "1B": [0,0,1,1,1,0,0,0,1,1,1,1,1,1,0,0,0,1,1,1,1,1,0,0,0,0,1,0,0,1,0,1,1,1,0,0,0,1,0,1,0,0,1,1,0,1,0,0,0,0,1,0,1,1,1,0,1,1,0,0,0,0,1,1,0,0,1,0,1,0,1,1,0,0,0,1,1,1,1,0,0,1,0,1,0,1,1,0,1,0,0,1,1,0,0,0,0,1,0,1]
    }
}

# =========================
# PROCESS DATA
# =========================
coin_order = ["1A", "1B", "2", "5A", "5B", "10A", "10B", "20"]
combined_data = {coin: [] for coin in coin_order}
all_flips = []

for group in groups_data.values():
    for coin_class, flips in group.items():
        first_100 = flips[:100]
        if coin_class in combined_data:
            combined_data[coin_class].extend(first_100)
        all_flips.extend(first_100)

datasets = []
for coin in coin_order:
    if len(combined_data[coin]) > 0:
        datasets.append((f"{coin} Coin - Cumulative", combined_data[coin]))

# Append Canvas Summaries (ONLY ALL COMBINED, NO WOOD/TILES)
datasets.append(("ALL COINS COMBINED", all_flips))

# =========================
# 2. THE ANIMATION CLASS
# =========================

class CoinAnimator:
    def __init__(self, datasets):
        self.datasets = datasets
        self.index = 0
        
        # Load Theme from the other file
        self.style = theme.THEME
        
        # Turn interactive mode OFF
        plt.ioff()
        
        self.fig, self.ax = plt.subplots(figsize=(10, 6))
        self.fig.patch.set_facecolor(self.style["bg_color"])
        plt.subplots_adjust(bottom=0.2) 
        
        self.ani = None 
        self.fig.canvas.mpl_connect('key_press_event', self.on_key)

        # BUTTONS
        ax_prev = plt.axes([0.2, 0.05, 0.15, 0.075])
        self.btn_prev = Button(ax_prev, '< Prev', color=self.style["btn_color"], hovercolor=self.style["btn_hover"])
        self.btn_prev.label.set_color(self.style["tails_color"])
        self.btn_prev.on_clicked(self.prev_graph)

        ax_replay = plt.axes([0.425, 0.05, 0.15, 0.075])
        self.btn_replay = Button(ax_replay, 'Replay ↻', color=self.style["btn_color"], hovercolor=self.style["btn_hover"])
        self.btn_replay.label.set_color('white')
        self.btn_replay.on_clicked(self.replay_graph)

        ax_next = plt.axes([0.65, 0.05, 0.15, 0.075])
        self.btn_next = Button(ax_next, 'Next >', color=self.style["btn_color"], hovercolor=self.style["btn_hover"])
        self.btn_next.label.set_color(self.style["tails_color"])
        self.btn_next.on_clicked(self.next_graph)

        self.start_new_graph()

    def cumulative(self, H_list):
        cumH, cumT = [], []
        h_sum, t_sum = 0, 0
        for h in H_list:
            h_sum += h
            t_sum += (1 - h)
            cumH.append(h_sum)
            cumT.append(t_sum)
        return cumH, cumT

    def update(self, frame, trials, cumH, cumT, lineH, lineT, markerH, markerT):
        lineH.set_data(trials[:frame], cumH[:frame])
        lineT.set_data(trials[:frame], cumT[:frame])
        
        if frame > 0:
            markerH.set_data([trials[frame-1]], [cumH[frame-1]])
            markerT.set_data([trials[frame-1]], [cumT[frame-1]])
            
        return lineH, lineT, markerH, markerT

    def start_new_graph(self):
        try:
            if self.ani is not None and self.ani.event_source is not None:
                self.ani.event_source.stop()
        except Exception:
            pass 
        
        self.ax.clear()
        self.ax.set_facecolor(self.style["plot_bg"])
        
        title, H_list = self.datasets[self.index]
        cumH, cumT = self.cumulative(H_list)
        trials = list(range(1, len(H_list) + 1))
        
        self.ax.set_xlim(0, len(H_list))
        self.ax.set_ylim(0, len(H_list))
        
        # Titles & Labels (CENTERED)
        self.ax.set_title(f"{title} ({self.index + 1}/{len(self.datasets)})", 
                          fontsize=15, fontweight='bold', color=self.style["title_color"], loc='center')
        self.ax.set_xlabel("Trials", color=self.style["text_color"])
        self.ax.set_ylabel("Cumulative Count", color=self.style["text_color"])
        
        self.ax.grid(True, linestyle='--', alpha=0.3, color=self.style["grid_color"])
        self.ax.tick_params(colors=self.style["text_color"])
        for spine in self.ax.spines.values():
            spine.set_edgecolor(self.style["spine_color"])
        
        lineH, = self.ax.plot([], [], label="Heads", color=self.style["heads_color"], linewidth=2.5)
        lineT, = self.ax.plot([], [], label="Tails", color=self.style["tails_color"], linewidth=2.5, linestyle="-")
        
        markerH, = self.ax.plot([], [], marker='*', color=self.style["marker_fill"], markersize=8, markeredgecolor=self.style["heads_color"])
        markerT, = self.ax.plot([], [], marker='d', color=self.style["marker_fill"], markersize=6, markeredgecolor=self.style["tails_color"])
        
        legend = self.ax.legend(loc="upper left", facecolor=self.style["bg_color"], edgecolor=self.style["text_color"])
        for text in legend.get_texts():
            text.set_color(self.style["text_color"])
        
        fast_frames = range(0, len(H_list) + 5, 5) 
        
        self.ani = FuncAnimation(
            self.fig, 
            self.update, 
            frames=fast_frames, 
            fargs=(trials, cumH, cumT, lineH, lineT, markerH, markerT),
            interval=1,     
            repeat=False,
            blit=False      
        )
        
        plt.draw()

    def next_graph(self, event=None):
        self.index = (self.index + 1) % len(self.datasets)
        self.start_new_graph()

    def prev_graph(self, event=None):
        self.index = (self.index - 1) % len(self.datasets)
        self.start_new_graph()

    def replay_graph(self, event=None):
        self.start_new_graph()

    def on_key(self, event):
        if event.key == 'right':
            self.next_graph()
        elif event.key == 'left':
            self.prev_graph()

# =========================
# 3. RUN IT
# =========================

print("Controls: Click buttons or use LEFT/RIGHT keys.")
viewer = CoinAnimator(datasets)

# PRINT TOTALS (Only All Combined)
print(f"\n===== ALL COINS COMBINED =====")
print(f"Total Flips: {len(all_flips)}")
print(f"Total Heads: {sum(all_flips)}")
print(f"Total Tails: {len(all_flips) - sum(all_flips)}")

plt.show(block=True)