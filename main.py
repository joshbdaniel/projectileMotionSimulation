from vpython import (
    color,
    canvas,
    vector,
    sphere,
    box,
    slider,
    wtext,
    rate,
    pi,
    cos,
    sin,
)

scene = canvas(title="Projectile Motion Simulation", width=800, height=450)
box(pos=vector(20, -0.25, 0), size=vector(500, 0.5, 5), color=color.green)

ball = sphere(
    pos=vector(0, 5, 0),
    radius=4,
    color=color.cyan,
    make_trail=True,
)

gravity = 9.81
deltaT = 0.01

height_slider = slider(min=0, max=40, value=5, bind=lambda s: reset())
height_text = wtext(text=" Height: 5.0 m\n")

velocity_slider = slider(min=1, max=50, value=20, bind=lambda s: reset())
velocity_text = wtext(text=" Velocity: 20.0 m/s\n")

angle_slider = slider(min=0, max=90, value=45, bind=lambda s: reset())
angle_text = wtext(text=" Angle: 45.0 deg\n")

velocity = vector(0, 0, 0)


def reset():
    global velocity
    height_text.text = f" Height: {height_slider.value:.1f} m\n"
    velocity_text.text = f" Velocity: {velocity_slider.value:.1f} m/s\n"
    angle_text.text = f" Angle: {angle_slider.value:.1f} deg\n"

    ball.clear_trail()
    ball.pos = vector(0, height_slider.value, 0)

    angle_rad = angle_slider.value * (pi / 180)
    velocity = vector(
        velocity_slider.value * cos(angle_rad),
        velocity_slider.value * sin(angle_rad),
        0,
    )


reset()

while True:
    rate(100)
    if ball.pos.y >= 0:
        velocity.y -= gravity * deltaT
        ball.pos += velocity * deltaT