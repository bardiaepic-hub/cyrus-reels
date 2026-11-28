/* Characters for the Priya salon reel (28 Nov), based on the Danny / Marcus person() code, plus long hair and coloured capes. */
/* Characters for the Danny garage reel (27 Nov), copied from the Marcus series (26 Nov) with overalls, a bun, glasses.
   Characters for the Marcus barber series (26 Nov). Based on person() from 23-25 Nov,
   plus new hair (messy, fade, neat), a barber apron, a cutting cape and clippers. */
const PEOPLE={
 priya:{skin:'#B97A56',skinD:'#9C6243',hair:'#1a1210',top:'#C2416B',topD:'#9e3457',style:'long',apron:true},
 mum:{skin:'#A86E4C',skinD:'#8C573A',hair:'#bdb7b0',top:'#6C5BA8',topD:'#56488a',style:'bun',glasses:true,cardigan:true},
 mumCape:{skin:'#A86E4C',skinD:'#8C573A',hair:'#bdb7b0',top:'#6C5BA8',topD:'#56488a',style:'bun',glasses:true,cape:true,capeC:'#8E6BBF'},
 cA:{skin:'#F0C6A6',skinD:'#D6A684',hair:'#c9a15a',top:'#2a2f36',topD:'#1d2126',style:'long',cape:true,capeC:'#2E2A33'},
 cB:{skin:'#6E4630',skinD:'#59361f',hair:'#120c09',top:'#2a2f36',topD:'#1d2126',style:'bun',cape:true,capeC:'#2E2A33'},
 cC:{skin:'#D9A27C',skinD:'#BD8660',hair:'#7a3b22',top:'#2a2f36',topD:'#1d2126',style:'short',cape:true,capeC:'#2E2A33'},
 q1:{skin:'#F0C6A6',skinD:'#D6A684',hair:'#c9a15a',top:'#C25B4E',topD:'#a24a3f',style:'long'},
 q2:{skin:'#6E4630',skinD:'#59361f',hair:'#120c09',top:'#4D6FB8',topD:'#3d5a98',style:'bun'},
 q3:{skin:'#D9A27C',skinD:'#BD8660',hair:'#3a2618',top:'#3E8E6E',topD:'#2f6f55',style:'short'},
 q4:{skin:'#B98261',skinD:'#9c6847',hair:'#2a1d17',top:'#D69A3A',topD:'#b8822c',style:'long'}
};
const MOUTH={
 smile:'<path d="M172 282 Q200 306 228 282" fill="none" stroke="#3a1f17" stroke-width="7" stroke-linecap="round"/>',
 grin:'<path d="M166 276 Q200 322 234 276 Z" fill="#3a1f17"/><path d="M174 279 Q200 288 226 279 L224 284 Q200 292 176 284Z" fill="#fff"/>',
 flat:'<path d="M180 290 L220 290" stroke="#3a1f17" stroke-width="7" stroke-linecap="round"/>',
 frown:'<path d="M176 298 Q200 280 224 298" fill="none" stroke="#3a1f17" stroke-width="7" stroke-linecap="round"/>',
 o:'<ellipse cx="200" cy="292" rx="12" ry="16" fill="#3a1f17"/>',
 bigo:'<ellipse cx="200" cy="296" rx="20" ry="26" fill="#3a1f17"/>',
 side:'<path d="M182 292 Q205 286 224 280" fill="none" stroke="#3a1f17" stroke-width="7" stroke-linecap="round"/>',
 talk:'<ellipse cx="200" cy="290" rx="16" ry="10" fill="#3a1f17"/>'
};
function prop(kind,x,y,rot){
  if(!kind)return '';
  let s='';
  if(kind==='phone')s=`<rect x="-34" y="-58" width="68" height="116" rx="12" fill="#15171a"/><rect x="-28" y="-50" width="56" height="100" rx="7" fill="#bfe6ff"/>`;
  if(kind==='phoneback')s=`<rect x="-34" y="-58" width="68" height="116" rx="12" fill="#15171a"/><circle cx="-14" cy="-40" r="8" fill="#333"/>`;
  if(kind==='phoneglow')s=`<rect x="-34" y="-58" width="68" height="116" rx="12" fill="#15171a"/><circle cx="0" cy="0" r="120" fill="#bfe6ff" opacity=".18"/>`;
  if(kind==='clippers')s=`<rect x="-16" y="-64" width="32" height="104" rx="14" fill="#2b2f33"/><rect x="-20" y="-74" width="40" height="18" rx="4" fill="#c7ccd0"/><rect x="-10" y="-30" width="20" height="8" rx="3" fill="#1AA6A0"/>`;
  if(kind==='wrench')s=`<g fill="#b9c0c6"><rect x="-9" y="-70" width="18" height="120" rx="7"/><path d="M-26 -96 a30 30 0 1 0 52 0 l-12 0 0 24 -28 0 0 -24 z"/></g>`;
  if(kind==='scissors')s=`<g fill="none" stroke="#c7ccd0" stroke-width="9" stroke-linecap="round"><path d="M-4 -10 L-30 -90"/><path d="M4 -10 L30 -90"/></g><circle cx="-12" cy="14" r="16" fill="none" stroke="#E3536F" stroke-width="8"/><circle cx="14" cy="14" r="16" fill="none" stroke="#E3536F" stroke-width="8"/>`;
  if(kind==='broom')s=`<rect x="-6" y="-150" width="12" height="230" rx="6" fill="#9b7a55"/><path d="M-46 80 L46 80 L36 130 L-36 130 Z" fill="#3c3f44"/>`;
  return `<g transform="translate(${x} ${y}) rotate(${rot||0})">${s}</g>`;
}
function hairBack(P){
  if(P.style==='long')return `<path d="M94 240 C88 128 150 102 200 102 C250 102 312 128 306 240 L322 440 Q200 470 78 440 Z" fill="${P.hair}"/>`;
  if(P.style==='bun')return `<circle cx="200" cy="102" r="46" fill="${P.hair}"/><path d="M104 250 C96 150 150 118 200 118 C250 118 304 150 296 250 Z" fill="${P.hair}"/>`;
  if(P.style==='messy')return `<g>${[[110,170,46],[150,120,50],[200,104,52],[250,120,50],[290,170,46],[300,220,38],[100,220,38]].map(([x,y,r])=>`<circle cx="${x}" cy="${y}" r="${r}" fill="${P.hair}"/>`).join('')}</g>`;
  return '';
}
function hairFront(P){
  if(P.style==='long')return `<path d="M104 236 C98 138 150 114 202 114 C256 114 302 138 296 236 C290 186 266 158 230 150 C204 172 150 176 122 192 C112 206 106 220 104 236Z" fill="${P.hair}"/><path d="M104 220 Q94 300 108 372 L130 372 Q118 296 126 222Z" fill="${P.hair}"/><path d="M296 220 Q306 300 292 372 L270 372 Q282 296 274 222Z" fill="${P.hair}"/>`;
  if(P.style==='bun')return `<path d="M108 220 C104 146 150 124 200 124 C250 124 296 146 292 220 C278 176 246 160 200 166 C156 160 122 176 108 220Z" fill="${P.hair}"/><path d="M200 128 C186 150 180 160 176 168" stroke="#77777b" stroke-width="5" fill="none"/>`;
  if(P.style==='messy')return `<g>${[[120,150,34],[160,118,36],[205,108,38],[248,122,34],[282,156,30],[176,150,22],[230,146,20]].map(([x,y,r])=>`<circle cx="${x}" cy="${y}" r="${r}" fill="${P.hair}"/>`).join('')}<path d="M168 96 q-14 -40 18 -54" stroke="${P.hair}" stroke-width="10" fill="none" stroke-linecap="round"/><path d="M250 104 q22 -34 52 -26" stroke="${P.hair}" stroke-width="10" fill="none" stroke-linecap="round"/></g>`;
  if(P.style==='fade')return `<path d="M112 210 C108 140 152 126 200 126 C248 126 292 140 288 210 C276 168 244 152 200 152 C156 152 124 168 112 210Z" fill="${P.hair}"/><path d="M108 214 L112 250 M292 214 L288 250" stroke="${P.hair}" stroke-width="10" opacity=".35"/>`;
  if(P.style==='short')return `<path d="M108 214 C100 132 152 112 200 112 C252 112 300 132 292 214 C282 172 250 150 206 154 C176 162 138 164 116 178 C110 190 108 200 108 214Z" fill="${P.hair}"/>`;
  if(P.style==='neat')return `<path d="M110 206 C104 130 150 110 202 110 C254 110 298 132 290 206 C284 166 262 144 236 140 C204 150 160 136 134 150 C120 164 112 184 110 206Z" fill="${P.hair}"/><path d="M134 150 C170 122 230 118 262 140" stroke="#3a2a22" stroke-width="5" fill="none" opacity=".6"/>`;
  return '';
}
function person(who,o){
  const P=PEOPLE[who];
  const e=Object.assign({brow:0,browY:0,eye:1,ex:0,ey:0,mouth:'smile',tilt:0,dy:0,lh:[150,470],rh:[250,470],lp:null,rp:null,mid:null,blush:.25,hairBounce:0},o);
  const blink=e.eye;
  let s=`<g transform="translate(0 ${e.dy})">`;
  s+=`<g transform="rotate(${e.tilt} 200 330) translate(0 ${e.hairBounce})">${hairBack(P)}</g>`;
  s+=`<path d="M50 600 C50 440 95 372 200 372 C305 372 350 440 350 600 Z" fill="${P.top}"/>`;
  s+=`<rect x="50" y="596" width="300" height="400" fill="${P.top}"/>`;
  if(P.style==='messy'&&who==='leo')s+=`<path d="M140 386 Q200 440 260 386" fill="none" stroke="${P.topD}" stroke-width="16"/><path d="M178 420 L172 520 M222 420 L228 520" stroke="#e8e8e8" stroke-width="7" stroke-linecap="round"/>`;
  if(P.shirt)s+=`<path d="M164 378 L200 430 L236 378" fill="#f4f4f4"/><path d="M200 430 L200 600" stroke="${P.topD}" stroke-width="5"/>`;
  if(P.overalls)s+=`<path d="M128 470 L272 470 L300 1000 L100 1000 Z" fill="#3E5F8A"/><path d="M140 470 L150 392 M260 470 L250 392" stroke="#3E5F8A" stroke-width="20"/><circle cx="150" cy="470" r="8" fill="#c7ccd0"/><circle cx="250" cy="470" r="8" fill="#c7ccd0"/><rect x="168" y="520" width="64" height="56" rx="6" fill="#33506f"/><ellipse cx="250" cy="640" rx="26" ry="14" fill="#1f2a36" opacity=".55"/><path d="M150 392 Q200 420 250 392" stroke="#d8d8d8" stroke-width="10" fill="none"/>`;
  if(P.polo)s+=`<path d="M160 378 L200 420 L240 378" fill="#174887"/><path d="M178 378 L200 404 L222 378" fill="#fff"/><text x="210" y="520" font-family="Inter,sans-serif" font-weight="800" font-size="30" fill="#fff">PRO</text>`;
  if(P.cardigan)s+=`<path d="M170 380 L200 600 L230 380" fill="#f3e6d8"/><path d="M200 420 L200 1000" stroke="${P.topD}" stroke-width="6"/><circle cx="214" cy="470" r="7" fill="#f3e6d8"/><circle cx="214" cy="540" r="7" fill="#f3e6d8"/>`;
  if(P.apron)s+=`<path d="M120 440 L280 440 L300 1000 L100 1000 Z" fill="#1f2326"/><path d="M150 440 L170 380 M250 440 L230 380" stroke="#1f2326" stroke-width="12"/><rect x="170" y="500" width="60" height="70" rx="8" fill="#2c3136"/><rect x="186" y="490" width="8" height="40" fill="#c7ccd0"/>`;
  if(P.cape)s+=`<path d="M30 430 Q200 360 370 430 L400 1000 L0 1000 Z" fill="${P.capeC||'#2E6F6B'}"/><path d="M150 392 Q200 410 250 392" stroke="#fff" stroke-width="10" fill="none"/>`;
  s+=`<rect x="176" y="300" width="48" height="80" rx="20" fill="${P.skinD}"/>`;
  s+=`<g transform="rotate(${e.tilt} 200 330)">`;
  s+=`<circle cx="108" cy="244" r="17" fill="${P.skinD}"/><circle cx="292" cy="244" r="17" fill="${P.skinD}"/>`;
  s+=`<ellipse cx="200" cy="232" rx="92" ry="100" fill="${P.skin}"/>`;
  s+=`<g transform="translate(0 ${e.hairBounce})">${hairFront(P)}</g>`;
  if(P.beard)s+=`<path d="M118 252 Q122 336 200 342 Q278 336 282 252 Q270 300 200 306 Q130 300 118 252Z" fill="${P.hair}" opacity=".85"/>`;
  const by=200+e.browY, bc=P.hair;
  s+=`<g transform="rotate(${e.brow} 165 ${by})"><path d="M146 ${by} L184 ${by}" stroke="${bc}" stroke-width="8" stroke-linecap="round"/></g>`;
  s+=`<g transform="rotate(${-e.brow} 235 ${by})"><path d="M216 ${by} L254 ${by}" stroke="${bc}" stroke-width="8" stroke-linecap="round"/></g>`;
  s+=`<ellipse cx="${165+e.ex}" cy="${236+e.ey}" rx="10" ry="${Math.max(1.5,13*blink)}" fill="#1b1414"/><ellipse cx="${235+e.ex}" cy="${236+e.ey}" rx="10" ry="${Math.max(1.5,13*blink)}" fill="#1b1414"/>`;
  s+=`<circle cx="145" cy="272" r="16" fill="#e2726b" opacity="${e.blush}"/><circle cx="255" cy="272" r="16" fill="#e2726b" opacity="${e.blush}"/>`;
  s+=`<path d="M200 246 Q192 262 200 266" fill="none" stroke="${P.skinD}" stroke-width="6" stroke-linecap="round"/>`;
  s+=MOUTH[e.mouth]||'';
  if(P.glasses)s+=`<g fill="none" stroke="#3a2a22" stroke-width="6"><circle cx="165" cy="236" r="26"/><circle cx="235" cy="236" r="26"/><path d="M191 234 L209 234"/></g>`;
  s+=`</g>`;
  if(e.mid)s+=prop(e.mid[0],e.mid[1],e.mid[2],e.mid[3]);
  const arm=(sx,sy,h,side)=>{const cx=sx+side*40, cy=(sy+h[1])/2+50;return `<path d="M${sx} ${sy} Q${cx} ${cy} ${h[0]} ${h[1]}" fill="none" stroke="${P.top}" stroke-width="48" stroke-linecap="round"/><path d="M${sx} ${sy} Q${cx} ${cy} ${h[0]} ${h[1]}" fill="none" stroke="${P.topD}" stroke-width="4" stroke-linecap="round" opacity=".5"/>`};
  if(!P.cape)s+=arm(118,420,e.lh,-1)+arm(282,420,e.rh,1);
  if(e.lp)s+=prop(e.lp[0],e.lh[0]+(e.lp[1]||0),e.lh[1]+(e.lp[2]||0),e.lp[3]);
  if(e.rp)s+=prop(e.rp[0],e.rh[0]+(e.rp[1]||0),e.rh[1]+(e.rp[2]||0),e.rp[3]);
  if(!P.cape)s+=`<circle cx="${e.lh[0]}" cy="${e.lh[1]}" r="24" fill="${P.skin}"/><circle cx="${e.rh[0]}" cy="${e.rh[1]}" r="24" fill="${P.skin}"/>`;
  s+=`</g>`;
  return s;
}
function blinkAt(t,seed){const c=(t+seed)%3.7;return c<0.12?Math.abs(c-0.06)/0.06:1;}
function draw(id,who,o){const el=document.getElementById(id);const s=who+JSON.stringify(o);if(el._s!==s){el.innerHTML=person(who,o);el._s=s;}}
/* timing helpers */
const $=id=>document.getElementById(id);
const cl=x=>Math.max(0,Math.min(1,x));
const p=(t,a,b)=>cl((t-a)/(b-a));
const eo=x=>1-Math.pow(1-x,3);
const eio=x=>x<.5?4*x*x*x:1-Math.pow(-2*x+2,3)/2;
const eb=x=>{const c=1.70158,c3=c+1;return 1+c3*Math.pow(x-1,3)+c*Math.pow(x-1,2)};
const lerp=(a,b,k)=>a+(b-a)*k;
function show(el,k,dy=0,sc=1,dx=0){el.style.opacity=k;el.style.transform=`translate(${dx}px,${dy}px) scale(${sc})`;}
function win(t,a,b,f=0.3){return Math.min(p(t,a,a+f),1-p(t,b-f,b));}
function typed(s,k){return s.slice(0,Math.round(s.length*cl(k)));}
function setCap(tv,CAP,from,to){
  let cap='',ca0=0; CAP.forEach(([a,s])=>{if(tv>=a){cap=s;ca0=a;}});
  if(tv<from||tv>=to)cap='';
  const ce=$('cap'); const ch=cap?`<em>${cap}</em>`:''; if(ce._h!==ch){ce.innerHTML=ch;ce._h=ch;}
  const cke=eb(p(tv,ca0,ca0+0.22)); ce.style.opacity=cap?p(tv,ca0,ca0+0.06):0; ce.style.transform=`translateY(${(1-cke)*20}px) scale(${0.95+0.05*cke})`;
}
