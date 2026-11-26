# Story reel sound bed: the playful pizzicato beat (100 bpm, from the 25 Nov Tony's Pizza reel) plus sound effects.
# usage: python3 storybed.py out.wav duration events.json
# events.json: {"cuts": [[a,b],...], "end": t_resolve_chord, "events": [{"k":..,"t":..,"g":..}, ...]}
# "music": false leaves the beat out (when the song is added in the Instagram app).
# kinds: kick, tick, whoosh, chime, click, pop, ring, buzz, type (with "len" and "n")
import numpy as np, json, sys, wave
SR = 44100
out, DUR, cfg = sys.argv[1], float(sys.argv[2]), json.load(open(sys.argv[3]))
N = int(SR * DUR); L = np.zeros(N); R = np.zeros(N); rng = np.random.default_rng(3)
def add(sig, t, g=1.0, pan=0.0):
    i = int(t * SR); j = min(N, i + len(sig))
    if i >= N or i < 0: return
    L[i:j] += sig[:j - i] * g * (1 - pan); R[i:j] += sig[:j - i] * g * (1 + pan)
def env(n, a=.005, d=.2):
    t = np.arange(n) / SR; return np.minimum(1, t / a) * np.exp(-t / d)
def pluck(f, ln=.5, damp=.996):
    n = int(ln * SR); p = max(2, int(SR / f)); buf = rng.uniform(-1, 1, p); out = np.zeros(n)
    for i in range(n):
        out[i] = buf[i % p]; buf[i % p] = damp * .5 * (buf[i % p] + buf[(i + 1) % p])
    return out * env(n, .001, ln * .5)
def sine(f, ln, d, a=.003):
    n = int(ln * SR); t = np.arange(n) / SR; return np.sin(2 * np.pi * f * t) * env(n, a, d)
def kick(ln=.4):
    n = int(ln * SR); t = np.arange(n) / SR; f = 45 + 110 * np.exp(-t * 28)
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * env(n, .001, .14)
def noise(ln, d, lp=1):
    n = int(ln * SR); x = rng.standard_normal(n)
    if lp > 1: x = np.convolve(x, np.ones(lp) / lp, 'same')
    return x * env(n, .002, d)
def whoosh(ln=.5):
    n = int(ln * SR); x = rng.standard_normal(n); t = np.linspace(0, 1, n); y = np.zeros(n)
    for i in range(0, n, 256):
        k = int(30 - 26 * t[i]) + 1; seg = x[i:i + 256]; y[i:i + len(seg)] = np.convolve(seg, np.ones(k) / k, 'same')
    return y * np.sin(np.pi * t) ** 2 * 2
# ---------- music bed: playful pizzicato, 100 bpm ----------
music = np.zeros(N); B = 0.6
prog = [[261.6, 329.6, 392.0], [220.0, 261.6, 329.6], [174.6, 220.0, 261.6], [196.0, 246.9, 293.7]]
bass = [65.4, 55.0, 43.7, 49.0]
pk = {}
def P(f, ln=.45):
    k = (round(f, 1), ln)
    if k not in pk: pk[k] = pluck(f, ln)
    return pk[k]
patt = [0, 2, 1, 2, 0, 2, 1, 2]
cuts = cfg.get('cuts', []); END = cfg.get('end', DUR)
MUSIC = cfg.get('music', True)
def mus_on(t):
    if not MUSIC or t >= END: return False
    return not any(a <= t < b for a, b in cuts)
def put(s, t, g):
    i0 = int(t * SR); j = min(N, i0 + len(s)); music[i0:j] += s[:j - i0] * g
t = 0.0
while t < DUR:
    bar = int(t / (B * 4)) % 4; ch = prog[bar]
    if mus_on(t):
        i = int(round(t / (B / 2))) % 8
        f = ch[patt[i]] * (2 if i in (2, 6) else 1)
        put(P(f, .4), t, .5)
        if i % 4 == 0: put(sine(bass[bar], .5, .25), t, .55); put(kick(.3), t, .35)
        if i % 2 == 1: put(noise(.05, .012), t, .12)
    t += B / 2
# low tense drone in each cut window
tt = np.arange(N) / SR
for a, b in (cuts if MUSIC else []):
    m = (tt >= a) & (tt < b)
    music[m] += (np.sin(2 * np.pi * 55 * tt[m]) + .5 * np.sin(2 * np.pi * 82.4 * tt[m])) * np.minimum(1, (tt[m] - a) / .3) * np.minimum(1, (b - tt[m]) / .3) * .25
# resolve chord at the end card
if MUSIC and END < DUR:
    put(sum(sine(f, 2.4, .8) for f in (523.3, 659.3, 784, 1046.5)) / 4, END, .9)
L += music * .55; R += music * .55
# ---------- sfx ----------
for e in cfg['events']:
    k, t, g = e['k'], e['t'], e.get('g', 1)
    if k == 'kick': add(kick(.7) * 1.1, t, .9 * g)
    elif k == 'whoosh': add(whoosh(e.get('len', .35)), t - .15, .25 * g)
    elif k == 'pop': add(sine(e.get('f', 700), .2, .05) + .4 * sine(e.get('f', 700) * 2, .2, .03), t, .4 * g)
    elif k == 'click': add(noise(.03, .008), t, .6 * g)
    elif k == 'tick': add(sine(e.get('f', 1500), .2, .04), t, .25 * g)
    elif k == 'chime': add(sum(sine(f, 1.0, .3) for f in (880, 1318.5, 1760)) / 3, t, .45 * g)
    elif k == 'type':
        n = e.get('n', 12)
        for j in range(n): add(noise(.03, .006), t + e.get('len', 1.0) * j / n, .35 * g)
    elif k == 'ring':  # phone ring burst
        for j in range(8): add(sine(1500, .12, .05) + sine(1900, .12, .05), t + j * .09, .12 * g)
    elif k == 'buzz':  # phone vibrate
        add(sine(170, .45, .5) * np.sign(np.sin(np.arange(int(.45 * SR)) / SR * 2 * np.pi * 30)), t, .2 * g)
    elif k == 'door':
        add(sum(sine(f, 1.0, .35) for f in (1318.5, 1760)) / 2, t, .3 * g)
mx = max(np.abs(L).max(), np.abs(R).max()); L, R = L / mx * .8, R / mx * .8
fd = int(.6 * SR); L[-fd:] *= np.linspace(1, 0, fd); R[-fd:] *= np.linspace(1, 0, fd)
d = (np.stack([L, R], 1) * 32767).astype(np.int16)
w = wave.open(out, 'wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(d.tobytes()); w.close()
print('ok')
