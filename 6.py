import turtle as t

t.tracer(0)
t.left(90)
t.down()
k = 20

for i in range(2):
    t.fd(6 * k)
    t.right(90)
    t.fd(7 * k)
    t.right(90)

t.up()

t.right(180)
t.back(2)
t.right(90)
t.back(3)
t.left(90)

t.down()

for i in range(2):
    t.fd(5 * k)
    t.right(90)
    t.fd(6 * k)
    t.right(90)

t.up()
for x in range(-15, 15):
    for y in range(-15, 15):
        t.goto(x * k, y * k)
        t.dot(3)


t.done()
