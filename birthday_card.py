import turtle
import threading
from playsound import playsound

# === Fungsi Musik ===
def play_music():
    playsound("happy_birthday.mp3")

def on_click():
    threading.Thread(target=play_music, daemon=True).start()

# === Setup Layar ===
screen = turtle.Screen()
screen.title("🎂 Selamat Ulang Tahun! 🎉")
screen.bgcolor("#FFCC99")
screen.setup(width=1000, height=700)
screen.tracer(0)

# === Tambahkan Gambar Karakter Melambai ===
screen.addshape("wave1.gif")
screen.addshape("wave2.gif")
char = turtle.Turtle()
char.penup()
char.goto(350, -100)
char.shape("wave1.gif")

# Animasi melambai
def wave_animation():
    current = "wave1.gif"
    def switch():
        nonlocal current
        current = "wave2.gif" if current == "wave1.gif" else "wave1.gif"
        char.shape(current)
        screen.ontimer(switch, 500)
    switch()

# === Matahari dan Awan ===
sun = turtle.Turtle()
sun.penup()
sun.shape("circle")
sun.color("yellow")
sun.goto(-400, 250)

clouds = []
for x in [-300, 0, 300]:
    c = turtle.Turtle()
    c.penup()
    c.color("white")
    c.shape("circle")
    c.goto(x, 200)
    clouds.append(c)

def animate_sky():
    x = sun.xcor()
    sun.goto(x + 0.5, 250 if x < 400 else -400)
    for c in clouds:
        cx = c.xcor()
        c.goto(cx + 0.3 if cx < 500 else -500, c.ycor())
    screen.update()
    screen.ontimer(animate_sky, 30)

# === Gambar Kue dan Lilin ===
t = turtle.Turtle()
t.hideturtle()
t.penup()
t.speed(0)

def draw_layer(color, border, x, y, w, h):
    t.goto(x, y)
    t.pendown()
    t.pensize(3)
    t.color(border, color)
    t.begin_fill()
    for _ in range(2):
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)
    t.end_fill()
    t.penup()

def draw_candle():
    t.goto(-15, 30)
    t.color("yellow")
    t.begin_fill()
    for _ in range(2):
        t.forward(30)
        t.left(90)
        t.forward(60)
        t.left(90)
    t.end_fill()

def draw_flame():
    flame = turtle.Turtle()
    flame.hideturtle()
    flame.penup()
    flame.goto(0, 100)
    flame.shape("circle")
    flame.color("orange")

    def flicker():
        flame.color("orange" if flame.color()[0] == "red" else "red")
        screen.ontimer(flicker, 300)

    flame.showturtle()
    flicker()

def draw_cake():
    draw_layer("#A020F0", "#000000", -100, -100, 200, 30)
    draw_layer("#55FF55", "#000000", -85, -70, 170, 20)
    draw_layer("#B87333", "#000000", -70, -50, 140, 60)
    draw_candle()
    draw_flame()

# === Tombol Play Musik ===
btn = turtle.Turtle()
btn.hideturtle()
btn.penup()
btn.goto(-70, -250)
btn.color("white", "blue")
btn.begin_fill()
for _ in range(2):
    btn.forward(140)
    btn.left(90)
    btn.forward(50)
    btn.left(90)
btn.end_fill()
btn.goto(-30, -235)
btn.color("white")
btn.write("TEKAN INI", font=("Arial", 16, "bold"))

# Klik deteksi
screen.onclick(lambda x, y: on_click() if -70 <= x <= 70 and -250 <= y <= -200 else None)

# === Tulisan Ucapan ===
title = turtle.Turtle()
title.hideturtle()
title.penup()
title.goto(0, 250)
title.color("black")
title.write("🎉 Selamat Ulang Tahun! 🎉", align="center", font=("Arial", 26, "bold"))

# === Jalankan Semua Animasi ===
wave_animation()
animate_sky()
draw_cake()
screen.update()
turtle.done()
