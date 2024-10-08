from Crypto.Util.number import getPrime, getRandomInteger


def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = egcd(b % a, a)
        return g, y - (b // a) * x, x


def modinv(b, n):
    g, x, _ = egcd(b, n)
    if g == 1:
        return x % n


def crack_unknown_increment(states, modulus, multiplier):
    increment = (states[1] - states[0] * multiplier) % modulus
    return increment


def crack_unknown_multiplier(states, modulus):
    multiplier = (states[2] - states[1]) * modinv(states[1] - states[0], modulus) % modulus
    return multiplier


class FlipCongruentialGenerator:
    def __init__(self, m, a, c, state):
        self.m = m
        self.a = a
        self.c = c
        self.state = state
        self.flip = False

    def next(self):
        m, a, c, state = self.m, self.a, self.c, self.state
        if self.flip:
            self.state = (a * state + c) % m
        else:
            self.state = (c * state + a) % m

        self.flip = not self.flip
        return self.state

    def next_lcg(self):
        m, a, c, state = self.m, self.a, self.c, self.state
        self.state = (a * state + c) % m

        return self.state


m = 12253448351401201741
flag = [4673213239943043323, 8221638981680790387, 10262626592948164978, 9103898174641198916, 5814630391539498027, 11984692438022052316, 4514896651440866764, 11316648659700461444, 10051146413780444818, 11739955844300434473, 9852255651004109934, 2354437779110952546, 577570354625253276, 4319750024397664812, 4900061330707356798, 9366218780535240159, 578147900463173874, 5197506326475729078, 7224529931879733464, 3108967044078983817, 7364401944640401107, 3124927689850311563, 2742499351154071808, 10728700001668761261, 332452402524143405, 2009074149438245159, 145011792420003790, 2710996083536840699, 980435831497149946, 4786005963732987185, 5921529715587351894, 1795989943364161402, 5592220649973097021, 7016867542585054019]

states = [flag[0] ^ ord('g'), flag[1] ^ ord('i'), flag[2] ^ ord('g'), flag[3] ^ ord('e'), flag[4] ^ ord('m'), flag[5] ^ ord('{')]

flip_false = [s for s in states[::2]]
flip_true = [s for s in states[1::2]]

false_mult = crack_unknown_multiplier(flip_false, m)
true_mult = crack_unknown_multiplier(flip_true, m)

false_inc = crack_unknown_increment(flip_false, m, false_mult)
true_inc = crack_unknown_increment(flip_true, m, true_mult)

fcg_false = FlipCongruentialGenerator(m, false_mult, false_inc, flip_false[-1])
fcg_true = FlipCongruentialGenerator(m, true_mult, true_inc, flip_true[-1])

flip_false = [s for s in flag[::2]]
flip_true = [s for s in flag[1::2]]

print('gigem{', end="")
for i in range(3, len(flip_false)):
    print(chr(fcg_false.next_lcg() ^ flip_false[i]), end="")
    print(chr(fcg_true.next_lcg() ^ flip_true[i]), end="")

print()
