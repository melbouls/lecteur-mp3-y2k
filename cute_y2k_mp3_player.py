import tkinter as tk
from tkinter import filedialog
import pygame
import os

pygame.mixer.init()

class MP3PlayerPhysicalY2K:
    def __init__(self, root):
        self.root = root
        self.root.title("Cute Y2K MP3 Player 💿✨")
        self.root.geometry("400x600")
        self.root.configure(bg="#ffffff")

        # Stockage
        self.music_files = []
        self.current_index = 0
        self.is_paused = False

        # --- Dégradé Y2K ---
        self.canvas = tk.Canvas(root, width=380, height=580, highlightthickness=0)
        self.canvas.pack(pady=10)
        self.draw_gradient(self.canvas, 380, 580, "#ffb6f9", "#a7c7ff")

        # --- Écran central ---
        self.screen = tk.Label(root, text="♪ Aucun morceau ♪", font=("Comic Sans MS", 12, "bold"),
                               bg="#222", fg="#39ff14", width=30, height=2, relief="sunken")
        self.screen.place(x=60, y=60)

        # --- Boutons ronds pastel ---
        btn_size = 70

        self.play_btn = tk.Button(root, text="▶", font=("Arial", 16, "bold"),
                                  bg="#ffb6c1", width=4, height=2,
                                  command=self.play_music)
        self.play_btn.place(x=165, y=200, width=btn_size, height=btn_size)

        self.pause_btn = tk.Button(root, text="⏸", font=("Arial", 16, "bold"),
                                   bg="#add8e6", width=4, height=2,
                                   command=self.pause_music)
        self.pause_btn.place(x=80, y=200, width=btn_size, height=btn_size)

        self.stop_btn = tk.Button(root, text="⏹", font=("Arial", 16, "bold"),
                                  bg="#90ee90", width=4, height=2,
                                  command=self.stop_music)
        self.stop_btn.place(x=250, y=200, width=btn_size, height=btn_size)

        self.prev_btn = tk.Button(root, text="⏮", font=("Arial", 16, "bold"),
                                  bg="#dda0dd", width=4, height=2,
                                  command=self.prev_music)
        self.prev_btn.place(x=80, y=300, width=btn_size, height=btn_size)

        self.next_btn = tk.Button(root, text="⏭", font=("Arial", 16, "bold"),
                                  bg="#dda0dd", width=4, height=2,
                                  command=self.next_music)
        self.next_btn.place(x=250, y=300, width=btn_size, height=btn_size)

        # --- Bouton charger ---
        self.load_btn = tk.Button(root, text="💿 Ajouter MP3", font=("Comic Sans MS", 12, "bold"),
                                  bg="#fff0f5", command=self.load_music)
        self.load_btn.place(x=140, y=400)

        # --- Volume ---
        self.volume_slider = tk.Scale(root, from_=0, to=1, resolution=0.1,
                                      orient="horizontal", length=200,
                                      label="🔊 Volume", command=self.set_volume,
                                      bg="#ffb6f9")
        self.volume_slider.set(0.5)
        self.volume_slider.place(x=100, y=480)

    # --- Dégradé ---
    def draw_gradient(self, canvas, width, height, color1, color2):
        r1, g1, b1 = canvas.winfo_rgb(color1)
        r2, g2, b2 = canvas.winfo_rgb(color2)
        r_ratio = (r2 - r1) / height
        g_ratio = (g2 - g1) / height
        b_ratio = (b2 - b1) / height

        for i in range(height):
            nr = int(r1 + (r_ratio * i))
            ng = int(g1 + (g_ratio * i))
            nb = int(b1 + (b_ratio * i))
            color = f"#{nr>>8:02x}{ng>>8:02x}{nb>>8:02x}"
            canvas.create_line(0, i, width, i, fill=color)

    # --- Fonctions lecteur ---
    def load_music(self):
        files = filedialog.askopenfilenames(filetypes=[("MP3 Files", "*.mp3")])
        for file in files:
            self.music_files.append(file)
        if self.music_files:
            self.screen.config(text=f"Chargé: {os.path.basename(self.music_files[0])}")

    def play_music(self):
        if not self.music_files:
            return
        song = self.music_files[self.current_index]
        pygame.mixer.music.load(song)
        pygame.mixer.music.play()
        self.is_paused = False
        self.screen.config(text=f"Lecture: {os.path.basename(song)}")

    def pause_music(self):
        if not self.is_paused:
            pygame.mixer.music.pause()
            self.is_paused = True
            self.screen.config(text="⏸ Pause")
        else:
            pygame.mixer.music.unpause()
            self.is_paused = False
            self.screen.config(text="▶ Lecture reprise")

    def stop_music(self):
        pygame.mixer.music.stop()
        self.screen.config(text="⏹ Arrêt")

    def next_music(self):
        if self.music_files:
            self.current_index = (self.current_index + 1) % len(self.music_files)
            self.play_music()

    def prev_music(self):
        if self.music_files:
            self.current_index = (self.current_index - 1) % len(self.music_files)
            self.play_music()

    def set_volume(self, value):
        pygame.mixer.music.set_volume(float(value))


# Lancer l’app
root = tk.Tk()
app = MP3PlayerPhysicalY2K(root)
root.mainloop()
