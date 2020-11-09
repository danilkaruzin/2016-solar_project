# coding: utf-8
# license: GPLv3

gravitational_constant = 6.67208E-11
"""Гравитационная постоянная Ньютона G"""

def length(x1,y1,x2,y2):
    return math.sqrt((x1-x2)**2+(y1-y2)**2)

def calculate_force(body, space_objects):
    """Вычисляет силу, действующую на тело.

    Параметры:

    **body** — тело, для которого нужно вычислить дейстующую силу.
    **space_objects** — список объектов, которые воздействуют на тело.
    """

    body.Fx = body.Fy = 0
    for obj in space_objects:
        if body == obj:
            continue  # тело не действует гравитационной силой на само себя!
        r = length(body.x,body.y,obj.x,obj.y)
        M=gravitational_constant*body.mass*obj.mass
        pcos=(obj.x-body.x)/r
        psin=(obj.y-body.y)/r
        body.Fx +=M/r**2*pcos
        body.Fy +=M/r**2*psin


def move_space_object(body, dt):
    """Перемещает тело в соответствии с действующей на него силой.

    Параметры:

    **body** — тело, которое нужно переместить.
    """

    ax = body.Fx/body.m
    body.x += body.Vx*dt
    body.Vx += ax*dt

    ay = body.Fy / body.m
    body.y += body.Vy * dt
    body.Vy += ay * dt


def recalculate_space_objects_positions(space_objects, dt):
    """Пересчитывает координаты объектов.

    Параметры:

    **space_objects** — список оьъектов, для которых нужно пересчитать координаты.
    **dt** — шаг по времени
    """

    for body in space_objects:
        calculate_force(body, space_objects)
    for body in space_objects:
        move_space_object(body, dt)


if __name__ == "__main__":
    print("This module is not for direct call!")
