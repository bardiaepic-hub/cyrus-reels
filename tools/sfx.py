# Simple synthesized sound design. usage: python3 sfx.py out.wav duration events.json
import numpy as np, json, sys, wave
SR=44100
out,dur,ev=sys.argv[1],float(sys.argv[2]),json.load(open(sys.argv[3]))
N=int(SR*dur); L=np.zeros(N); R=np.zeros(N)
rng=np.random.default_rng(7)
def add(sig,t,g=1.0,pan=0.0):
    i=int(t*SR); j=min(N,i+len(sig))
    if i>=N: return
    L[i:j]+=sig[:j-i]*g*(1-pan)/1; R[i:j]+=sig[:j-i]*g*(1+pan)/1
def env(n,a=.005,d=.2):
    t=np.arange(n)/SR; return np.minimum(1,t/a)*np.exp(-t/d)
def tone(f,len_=.4,d=.12,harm=(1,.3)):
    n=int(len_*SR); t=np.arange(n)/SR
    s=sum(h*np.sin(2*np.pi*f*(k+1)*t) for k,h in enumerate(harm)); return s*env(n,.002,d)
def kick(len_=.35):
    n=int(len_*SR); t=np.arange(n)/SR; f=50+90*np.exp(-t*30)
    return np.sin(2*np.pi*np.cumsum(f)/SR)*env(n,.001,.12)
def noise_sweep(len_=.6,up=True):
    n=int(len_*SR); x=rng.standard_normal(n); t=np.linspace(0,1,n)
    # crude band movement via moving average size
    y=np.zeros(n); k0,k1=(40,4) if up else (4,40)
    for i in range(0,n,512):
        k=int(k0+(k1-k0)*t[i]); seg=x[max(0,i-k):i+512]
        c=np.convolve(seg,np.ones(k)/k,'same')[-min(512,n-i):]; y[i:i+len(c)]=c
    e=np.sin(np.pi*t)**2; return y*e*2.5
def chime(fs=(880,1318.5,1760)):
    return sum(tone(f,1.2,.45,(1,.15)) for f in fs)/len(fs)
def click(): 
    n=int(.03*SR); return rng.standard_normal(n)*env(n,.0005,.006)
for e in ev:
    k,t=e['k'],e['t']; g=e.get('g',1)
    if k=='tick': add(tone(e.get('f',1200),.25,.05,(1,.2)),t,.35*g)
    elif k=='kick': add(kick(),t,.9*g)
    elif k=='whoosh': add(noise_sweep(e.get('len',.6),e.get('up',True)),t,.5*g)
    elif k=='chime': add(chime(),t,.45*g)
    elif k=='click': add(click(),t,.6*g)
    elif k=='pop': add(tone(e.get('f',600),.2,.04,(1,.5,.2)),t,.5*g)
# soft pad bed: two chords
t=np.arange(N)/SR
def pad(fs,a,b):
    m=(t>=a)&(t<b); x=np.zeros(N); tt=t[m]-a; ln=b-a
    sh=np.minimum(1,tt/0.6)*np.minimum(1,(ln-tt)/0.6)
    for f in fs: x[m]+=np.sin(2*np.pi*f*tt+np.sin(2*np.pi*.3*tt))*sh
    return x/len(fs)
bed=np.zeros(N)
for fs,a,b in ev_pad if (ev_pad:=[]) else []: pass
chords=[([110,164.8,220,261.6],0,5.0),([98,146.8,196,246.9],5.0,6.0),([130.8,196,261.6,329.6],6.0,10.2),([146.8,220,293.7,349.2],10.2,dur)]
for fs,a,b in chords: bed+=pad(fs,a,min(b,dur))
L+=bed*.12; R+=bed*.12
# pulse kick bed in fast section
for bt in np.arange(6.4,dur-1,0.6): add(kick(),bt,.35)
mx=max(np.abs(L).max(),np.abs(R).max()); L,R=L/mx*.85,R/mx*.85
fade=int(.5*SR); L[-fade:]*=np.linspace(1,0,fade); R[-fade:]*=np.linspace(1,0,fade)
d=(np.stack([L,R],1)*32767).astype(np.int16)
w=wave.open(out,'wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(d.tobytes()); w.close()
print('ok')
