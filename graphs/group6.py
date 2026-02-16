import matplotlib
# Force standard GUI backend
matplotlib.use('TkAgg') 

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Button
import theme  # <--- Uses your Keqing theme file

# =========================
# 1. THE DATA (CORRECTED)
# =========================

# 5 Peso Coin (Exact 100 digits you provided)
H_5peso_str = "1110110101100011100011010011000111010010000101101000110001101100010001101101110000100001010011001010"
H_5peso = [int(x) for x in H_5peso_str]

# 20 Peso Coin (From your previous message)
H_20peso_str = "0011000101100110000010101010101000001010011000110011110011001100111010001001001011100011001111110111"
H_20peso = [int(x) for x in H_20peso_str]

# Automatically combine them (Should be 200 total)
H_combined = H_5peso + H_20peso

datasets = [
    ("5 Peso Coin", H_5peso),
    ("20 Peso Coin", H_20peso),
    ("Combined Coins", H_combined)
]

# =========================
# 2. THE ANIMATION CLASS
# =========================

class CoinAnimator:
    def __init__(self, datasets):
        self.datasets = datasets
        self.index = 0
        
        # Load Theme
        self.style = theme.THEME
        
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
            # FIX: Clamp index to prevent crash at end of animation
            safe_idx = min(frame - 1, len(trials) - 1)
            
            markerH.set_data([trials[safe_idx]], [cumH[safe_idx]])
            markerT.set_data([trials[safe_idx]], [cumT[safe_idx]])
            
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
        
        max_val = len(H_list)
        self.ax.set_xlim(0, max_val)
        self.ax.set_ylim(0, max_val)
        
        # Dynamic Ticks (every 10%)
        step = max(1, max_val // 10)
        self.ax.set_xticks(range(0, max_val + 1, step))
        self.ax.set_yticks(range(0, max_val + 1, step))
        
        # Title Centered
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
        
        # Buffer frames at the end
        fast_frames = range(0, len(H_list) + 5, 2) 
        
        self.ani = FuncAnimation(
            self.fig, 
            self.update, 
            frames=fast_frames, 
            fargs=(trials, cumH, cumT, lineH, lineT, markerH, markerT),
            interval=20,     
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
        elif event.key == ' ':
            self.replay_graph()

# =========================
# 3. RUN IT
# =========================

if __name__ == "__main__":
    print("Controls: Click buttons or use LEFT/RIGHT keys.")
    viewer = CoinAnimator(datasets)

    # PRINT TOTALS
    total_flips = len(H_combined)
    total_heads = sum(H_combined)
    total_tails = total_flips - total_heads

    print(f"\n===== COMBINED COINS SUMMARY =====")
    print(f"Total Flips: {total_flips}")
    print(f"Total Heads: {total_heads}")
    print(f"Total Tails: {total_tails}")

    plt.show(block=True)