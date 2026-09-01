SCENES = '''  /* ---- toate cele 4 scene stau in acelasi registru tonal:
         fundal palid, tus grafit, un singur accent de joasa saturatie.
         se disting prin forma si miscare, nu prin contrast ---- */
  .v-emas,
  .v-plomus,
  .v-bibliada,
  .v-bnp {--vs-bg:linear-gradient(160deg,#EFEDE5,#E2E0D6);--vs-ink:#232320;--vs-mut:#77746A;--vs-grid:#0000000e;--vs-edge:#00000038;--vs-fill:#00000020;--vs-lit:#0000005e}
  .visual{background:var(--vs-bg)}
  .visual .logotype{color:var(--vs-ink)}
  .visual .sublabel{color:var(--vs-mut)}

  /* 01 EMAS — facade whose units light up, crane sweeping */
  .v-emas .grid-lines{position:absolute;inset:0;z-index:1;background-image:linear-gradient(var(--vs-grid) 1px,transparent 1px),linear-gradient(90deg,var(--vs-grid) 1px,transparent 1px);background-size:38px 38px}
  .v-emas .logotype{font-size:clamp(40px,6vw,64px)}
  .facade{position:absolute;z-index:2;width:40%;height:66%;left:50%;top:52%;transform:translate(-50%,-50%);
    display:grid;grid-template-columns:repeat(4,1fr);grid-template-rows:repeat(7,1fr);gap:7px;
    padding:12px;border:1px solid var(--vs-edge);border-radius:3px}
  .win{background:var(--vs-fill);border-radius:1px;animation:sell 6s ease-in-out infinite}
  .win:nth-child(4n+2){animation-delay:.25s}
  .win:nth-child(4n+3){animation-delay:.5s}
  .win:nth-child(4n+4){animation-delay:.75s}
  .facade .win:nth-child(-n+4){animation-delay:2.2s}
  .facade .win:nth-child(n+5):nth-child(-n+8){animation-delay:1.9s}
  .facade .win:nth-child(n+9):nth-child(-n+12){animation-delay:1.6s}
  .facade .win:nth-child(n+13):nth-child(-n+16){animation-delay:1.3s}
  .facade .win:nth-child(n+17):nth-child(-n+20){animation-delay:1.0s}
  .facade .win:nth-child(n+21):nth-child(-n+24){animation-delay:.7s}
  .facade .win:nth-child(n+25){animation-delay:.4s}
  .crane{position:absolute;top:16%;left:50%;width:40%;height:1px;background:var(--vs-edge);transform-origin:left center;z-index:2;animation:crane 8s ease-in-out infinite}
  .crane::after{content:"";position:absolute;right:0;top:-3px;width:1px;height:26px;background:var(--vs-edge)}
  @keyframes sell{0%,100%{background:var(--vs-fill)}45%,60%{background:var(--vs-lit)}}
  @keyframes crane{0%,100%{transform:rotate(-8deg)}50%{transform:rotate(8deg)}}

  /* 02 PLOMUS — radar: rings, sweep, pings */
  .v-plomus .logotype{font-size:clamp(40px,6vw,62px)}
  .p-grid{position:absolute;inset:0;z-index:1;background-image:linear-gradient(var(--vs-grid) 1px,transparent 1px),linear-gradient(90deg,var(--vs-grid) 1px,transparent 1px);background-size:34px 34px;mask-image:radial-gradient(circle at 50% 52%,#000 55%,transparent 74%)}
  .ring{position:absolute;left:50%;top:52%;transform:translate(-50%,-50%);border-radius:50%;border:1px solid var(--vs-edge);z-index:2}
  .ring.r1{width:24%;aspect-ratio:1}
  .ring.r2{width:48%;aspect-ratio:1}
  .ring.r3{width:72%;aspect-ratio:1}
  .cross{position:absolute;left:50%;top:52%;z-index:2;background:var(--vs-grid)}
  .cross.h{width:78%;height:1px;background:var(--vs-edge);transform:translate(-50%,-50%);opacity:.75}
  .cross.v{height:78%;width:1px;background:var(--vs-edge);transform:translate(-50%,-50%);opacity:.75}
  .sweep{position:absolute;left:50%;top:52%;width:36%;height:36%;transform-origin:top left;z-index:3;
    background:conic-gradient(from 0deg,#00000030,transparent 58deg);border-radius:0 0 100% 0;animation:spin 4.5s linear infinite}
  .sweep-line{position:absolute;left:50%;top:52%;width:36%;height:1px;transform-origin:left center;z-index:3;background:linear-gradient(90deg,var(--vs-ink),transparent);opacity:.8;animation:spin 4.5s linear infinite}
  .blip{position:absolute;width:7px;height:7px;border-radius:50%;background:var(--vs-ink);box-shadow:0 0 10px #00000040;z-index:4;opacity:0;animation:ping 4.5s linear infinite}
  .blip.b1{left:41%;top:38%;animation-delay:.35s}
  .blip.b2{left:63%;top:60%;animation-delay:1.8s}
  .blip.b3{left:58%;top:33%;animation-delay:2.8s}
  .blip.b4{left:35%;top:58%;animation-delay:3.6s}
  @keyframes spin{to{transform:rotate(360deg)}}
  @keyframes ping{0%{opacity:0;transform:scale(.4)}3%{opacity:1;transform:scale(1)}35%{opacity:.7}70%{opacity:0}100%{opacity:0}}

  /* 03 BIBLIADA — passage read line by line under a gilt guide */
  .v-bibliada .logotype{font-size:clamp(38px,5.4vw,56px)}
  .v-bibliada .spine{position:absolute;top:0;bottom:0;left:50%;width:1px;background:var(--vs-edge);z-index:1}
  .passage{position:absolute;top:30px;left:9%;right:9%;z-index:3;font-family:var(--display);font-weight:400;color:var(--vs-ink);text-align:center;line-height:1.9;font-size:14px}
  .passage .ln{display:block;opacity:.3;animation:line 9s ease-in-out infinite}
  .passage .ln:nth-child(1){animation-delay:.3s}
  .passage .ln:nth-child(2){animation-delay:1.1s}
  .passage .ln:nth-child(3){animation-delay:1.9s}
  .passage .ref{display:block;margin-top:6px;font-family:var(--sans);font-size:9px;letter-spacing:.28em;text-transform:uppercase;opacity:0;animation:line 9s ease-in-out infinite;animation-delay:2.7s}
  .gilt{position:absolute;left:9%;right:9%;top:32px;height:22px;z-index:2;background:linear-gradient(90deg,transparent,#0000001f,transparent);animation:readdown 9s ease-in-out infinite}
  @keyframes line{0%,8%{opacity:.3}22%,72%{opacity:1}88%,100%{opacity:.22}}
  @keyframes readdown{0%{top:32px;opacity:0}8%{opacity:1}30%{top:80px}52%{top:128px}64%{top:128px;opacity:1}72%{opacity:0}100%{opacity:0}}

  /* 04 BREAKFAST & PRAY — dawn: rays turn, sun rises, motes lift */
  .v-bnp .logotype{font-size:clamp(30px,4.4vw,46px);font-weight:400}
  .rays{position:absolute;left:50%;top:62%;width:360px;height:360px;transform:translate(-50%,-50%);z-index:1;
    background:repeating-conic-gradient(from 0deg,#00000016 0deg 6deg,transparent 6deg 20deg);
    mask-image:radial-gradient(circle,#000 12%,transparent 62%);animation:turn 30s linear infinite}
  .sun{position:absolute;left:50%;width:120px;height:120px;border-radius:50%;transform:translateX(-50%);z-index:2;
    background:radial-gradient(circle,#ffffff 0%,#ffffffb3 40%,#ffffff00 72%);animation:rise 10s ease-in-out infinite}
  .horizon{position:absolute;left:0;right:0;bottom:26%;height:1px;background:var(--vs-edge);z-index:2}
  .haze{position:absolute;left:-10%;right:-10%;bottom:20%;height:120px;z-index:1;background:radial-gradient(ellipse at center,#ffffff8c,transparent 70%);animation:haze 10s ease-in-out infinite}
  .mote{position:absolute;width:4px;height:4px;border-radius:50%;background:var(--vs-ink);z-index:2;opacity:0;animation:lift 10s ease-in-out infinite}
  .mote.m1{left:38%;animation-delay:.5s}
  .mote.m2{left:56%;animation-delay:3s}
  .mote.m3{left:47%;animation-delay:5.5s}
  .mote.m4{left:63%;animation-delay:7s}
  @keyframes turn{to{transform:translate(-50%,-50%) rotate(360deg)}}
  @keyframes rise{0%{top:78%;opacity:.35}46%{top:38%;opacity:1}56%{top:38%;opacity:1}100%{top:78%;opacity:.35}}
  @keyframes haze{0%,100%{opacity:.35}50%{opacity:.9}}
  @keyframes lift{0%{bottom:24%;opacity:0}15%{opacity:.8}60%{opacity:.45}80%{bottom:60%;opacity:0}100%{opacity:0}}

'''
