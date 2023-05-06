runners = [
    (10, 6, 20),
    (8, 8, 25),
    (12, 5, 16),
    (7, 7, 23),
    (9, 4, 32),
    (5, 9, 18)
]

def compute_dist(spec, time):
    speed, duration, rest = spec
    dist = 0

    while time > 0:
        elapsed = min(duration, time)
        dist += elapsed * speed
        time -= elapsed + rest

    return dist

print(max(compute_dist(runner, 1234) for runner in runners))