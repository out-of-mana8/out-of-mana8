<div align="center">

![Typing SVG](https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=700&size=20&duration=3000&pause=800&color=00F0C8&center=true&vCenter=true&width=650&lines=Hardware+Engineering+Student;Schematic+%E2%86%92+PCB+%E2%86%92+Firmware+%E2%86%92+Server+%E2%86%92+UI;MIPI+CSI-2+%C2%B7+I%C2%B2S+%C2%B7+Mixed-Signal+%C2%B7+Edge+AI;Avionics+%C2%B7+Medical+%C2%B7+Audio+%C2%B7+Vision)

</div>

---

```text
┌─────────────────────────────────────────────────────────────────┐
│  > whoami                                                       │
│                                                                 │
│  Studying ECE at Vanderbilt. Building devices from schematic to │
│  silicon — analog signal chains, high-speed interfaces,         │
│  embedded firmware, and the full-stack infrastructure           │
│  around them.                                                   │
│                                                                 │
│  Domains:                                                       │
│    ├─ Edge AI · Full-duplex audio · Voice pipelines             │
│    ├─ MIPI camera systems · Custom SoC boards                  │
│    ├─ Avionics EE validation · GPS/RTK · Mesh networking       │
│    └─ Mixed-signal PCBs · Medical devices · Env. sensing       │
│                                                                 │
│  > _                                                            │
└─────────────────────────────────────────────────────────────────┘
```

---

### Domains

| | | |
|---|---|---|
| 🎙 **Audio / Voice AI** | 📷 **Vision / Camera** | ✈️ **Avionics / Aerospace** |
| Full-duplex pipelines · AEC · VAD | MIPI CSI-2 · IMX708 · DSI display | EE validation · GPS RTK prototyping |
| Custom I²S signal chains | Custom ESP32-P4 board design | ESP32 mesh networking |
| Edge STT/LLM/TTS inference | IMU · LiPo power management | Ground equipment systems |
| | | |
| 🧪 **Mixed-Signal / Sensing** | ⚙️ **Embedded Systems** | 🔬 **Research Hardware** |
| Op-amp signal chains · Filters | FreeRTOS · PlatformIO · C++ | Flexible PCBs · Wearable sensors |
| ESD protection · Decoupling | Bring-up · Validation · Debug | Medical device prototyping |
| JLCPCB fab · LCSC BOM | Python servers · WebSocket APIs | MEMS microphones · ADC front-ends |

---

### Workflow

```
requirements ──▶ schematic ──▶ PCB layout ──▶ fab (JLCPCB)
                                                    │
UI / API     ◀── server    ◀── firmware    ◀── bring-up
```

Every layer. No handoffs.

---

### Interfaces & Protocols

![MIPI CSI-2](https://img.shields.io/badge/MIPI%20CSI--2-00f0c8?style=flat-square)
![MIPI DSI](https://img.shields.io/badge/MIPI%20DSI-00f0c8?style=flat-square)
![I2S](https://img.shields.io/badge/I%C2%B2S-00f0c8?style=flat-square)
![I2C](https://img.shields.io/badge/I%C2%B2C-00f0c8?style=flat-square)
![SPI](https://img.shields.io/badge/SPI-00f0c8?style=flat-square)
![USB-C](https://img.shields.io/badge/USB--C-00f0c8?style=flat-square)

### Toolchain

![ESP32](https://img.shields.io/badge/ESP32-E03030?style=flat-square&logo=espressif&logoColor=white)
![C++](https://img.shields.io/badge/C%2B%2B-00599C?style=flat-square&logo=c%2B%2B&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![FreeRTOS](https://img.shields.io/badge/FreeRTOS-007ACC?style=flat-square)
![PlatformIO](https://img.shields.io/badge/PlatformIO-F5822A?style=flat-square&logo=platformio&logoColor=white)
![KiCad](https://img.shields.io/badge/KiCad-314CB0?style=flat-square)

---

### Featured

<a href="https://github.com/out-of-mana8/esp32-talking-agent">
  <img align="left" src="https://github-readme-stats.vercel.app/api/pin/?username=out-of-mana8&repo=esp32-talking-agent&theme=dark&bg_color=0f0f0f&border_color=1e1e1e&title_color=00f0c8&icon_color=00f0c8&text_color=aaaaaa" />
</a>

<br clear="left"/>

> Battery-powered ESP32-S3 · dual I²S mics · stereo Class-D amp · custom PCB  
> Whisper STT → Claude LLM → kokoro TTS · ~1.9s end-to-end latency

<div align="center">
*Studying ECE at Vanderbilt · avionics · medical · AI hardware*
</div>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>out-of-mana8</title>
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&family=Syne:wght@700;800&display=swap" rel="stylesheet"/>
<style>
  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    background: #0a0a0a;
    color: #aaa;
    font-family: 'JetBrains Mono', monospace;
    min-height: 100vh;
    display: flex;
    justify-content: center;
    padding: 3rem 1.5rem;
  }
  .wrap { width: 100%; max-width: 760px; }

  /* Header */
  .header { margin-bottom: 2rem; }
  .headline {
    font-family: 'Syne', sans-serif;
    font-size: 32px;
    font-weight: 800;
    letter-spacing: -0.02em;
    line-height: 1.15;
    color: #fff;
    margin-bottom: 10px;
  }
  .headline .accent { color: #00f0c8; }
  .sub { font-size: 12.5px; color: #555; line-height: 2; }
  .sub .hl { color: #00f0c8; }

  .divider { border: none; border-top: 0.5px solid #1c1c1c; margin: 1.5rem 0; }

  /* Terminal */
  .terminal {
    background: #050505;
    border-radius: 10px;
    padding: 1.1rem 1.4rem;
    margin-bottom: 1.75rem;
    border: 0.5px solid #1c1c1c;
  }
  .term-bar { display: flex; gap: 7px; margin-bottom: 16px; }
  .dot { width: 11px; height: 11px; border-radius: 50%; }
  .d-r { background: #ff5f57; } .d-y { background: #febc2e; } .d-g { background: #28c840; }
  .tl { font-size: 13px; line-height: 2.1; color: #3a3a3a; }
  .tl .p { color: #00f0c8; }
  .tl .v { color: #e5c07b; }
  .tl .w { color: #888; }
  .tl .dim { color: #2a2a2a; }
  .cursor {
    display: inline-block; width: 7px; height: 14px;
    background: #00f0c8; vertical-align: middle;
    animation: blink 1.1s step-end infinite;
  }
  @keyframes blink { 0%,100%{opacity:1} 50%{opacity:0} }

  /* Domain grid */
  .section-label {
    font-size: 10px; letter-spacing: 0.14em;
    text-transform: uppercase; color: #333;
    margin-bottom: 10px;
  }
  .domains {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
    margin-bottom: 1.75rem;
  }
  .domain {
    background: #080808;
    border: 0.5px solid #1c1c1c;
    border-radius: 9px;
    padding: 14px 16px;
  }
  .domain-head { display: flex; align-items: center; gap: 8px; margin-bottom: 10px; }
  .domain-icon { font-size: 15px; }
  .domain-title {
    font-size: 10.5px; font-weight: 700;
    color: #00f0c8; text-transform: uppercase; letter-spacing: 0.1em;
  }
  .domain-items { font-size: 11.5px; color: #444; line-height: 2.1; }
  .domain-items span { color: #777; }

  /* Workflow */
  .workflow {
    background: #050505;
    border: 0.5px solid #1c1c1c;
    border-radius: 9px;
    padding: 1.1rem 1.4rem;
    margin-bottom: 1.75rem;
    font-size: 12.5px;
    line-height: 2.1;
    color: #2e2e2e;
  }
  .workflow .node { color: #777; }
  .workflow .anode { color: #00f0c8; }
  .workflow .tagline {
    font-size: 11px; color: #333; margin-top: 8px;
    border-top: 0.5px solid #161616; padding-top: 10px;
    letter-spacing: 0.05em;
  }

  /* Chips */
  .interfaces { margin-bottom: 1.75rem; }
  .chip-row { display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 6px; }
  .chip {
    font-size: 11px; padding: 3px 11px; border-radius: 4px;
    border: 0.5px solid #00f0c8; color: #00f0c8; background: #061a15;
  }
  .chip-n {
    font-size: 11px; padding: 3px 11px; border-radius: 4px;
    border: 0.5px solid #222; color: #555; background: transparent;
  }

  /* Footer */
  .footer {
    display: flex; justify-content: space-between;
    align-items: center; margin-top: 1.75rem;
  }
  .footer-l { font-size: 11px; color: #333; display: flex; align-items: center; gap: 7px; }
  .footer-r { font-size: 11px; color: #00f0c8; }
  .pulse {
    width: 6px; height: 6px; border-radius: 50%;
    background: #00f0c8; flex-shrink: 0;
    animation: pulse 2s ease-in-out infinite;
  }
  @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:0.15} }

  /* Stats row */
  .stats { display: flex; gap: 12px; margin-bottom: 1.75rem; flex-wrap: wrap; }
  .stats img { border-radius: 8px; height: 145px; }
</style>
</head>
<body>
<div class="wrap">

  <div class="header">
    <div class="headline">
      Hardware Engineering Student<br>
      <span class="accent">·</span> Edge AI
      <span class="accent">·</span> Mixed-Signal
      <span class="accent">·</span> Custom PCB
    </div>
    <div class="sub" style="margin-top:12px;">
      Studying ECE at Vanderbilt — Building devices from <span class="hl">schematic to silicon</span> — analog signal chains, high-speed interfaces,<br>
      embedded firmware, and the full-stack infrastructure around them.<br>
      <span class="hl">Avionics · Medical · Audio · Vision · Environmental sensing.</span>
    </div>
  </div>

  <hr class="divider">

  <div class="terminal">
    <div class="term-bar">
      <div class="dot d-r"></div>
      <div class="dot d-y"></div>
      <div class="dot d-g"></div>
    </div>
    <div class="tl"><span class="p">$ </span><span style="color:#2a2a2a"># what I build</span></div>
    <div class="tl"><span class="p">$ </span>ls domains/</div>
    <div class="tl">
      <span class="v">edge-ai/</span>&nbsp;&nbsp;
      <span class="v">mixed-signal/</span>&nbsp;&nbsp;
      <span class="v">avionics/</span>&nbsp;&nbsp;
      <span class="v">medical/</span>
    </div>
    <div class="tl"><span class="p">$ </span>cat stack.txt</div>
    <div class="tl">
      <span class="w">schematic</span> <span class="dim">→</span>
      <span class="w">PCB layout</span> <span class="dim">→</span>
      <span class="w">fab</span> <span class="dim">→</span>
      <span class="w">bring-up</span> <span class="dim">→</span>
      <span class="w">firmware</span> <span class="dim">→</span>
      <span class="w">server</span> <span class="dim">→</span>
      <span class="w">UI</span>
    </div>
    <div class="tl"><span class="p">$ </span><span class="cursor"></span></div>
  </div>

  <div class="section-label">domains</div>
  <div class="domains">
    <div class="domain">
      <div class="domain-head">
        <div class="domain-icon">🎙</div>
        <div class="domain-title">Audio / Voice AI</div>
      </div>
      <div class="domain-items">
        <span>Full-duplex pipeline · AEC · VAD</span><br>
        <span>Custom I²S signal chains</span><br>
        <span>Edge STT → LLM → TTS</span><br>
        <span>ESP32-S3 · Class-D amp</span>
      </div>
    </div>
    <div class="domain">
      <div class="domain-head">
        <div class="domain-icon">📷</div>
        <div class="domain-title">Vision / Camera</div>
      </div>
      <div class="domain-items">
        <span>MIPI CSI-2 · IMX708 · DSI</span><br>
        <span>Custom ESP32-P4 board</span><br>
        <span>IMU · LiPo power management</span><br>
        <span>Full camera pipeline design</span>
      </div>
    </div>
    <div class="domain">
      <div class="domain-head">
        <div class="domain-icon">✈️</div>
        <div class="domain-title">Avionics / Aerospace</div>
      </div>
      <div class="domain-items">
        <span>EE validation · Zipline drones</span><br>
        <span>GPS RTK prototyping</span><br>
        <span>ESP32 mesh networking</span><br>
        <span>Ground support equipment</span>
      </div>
    </div>
    <div class="domain">
      <div class="domain-head">
        <div class="domain-icon">🧪</div>
        <div class="domain-title">Mixed-Signal / Sensing</div>
      </div>
      <div class="domain-items">
        <span>Op-amp chains · anti-alias filters</span><br>
        <span>Flexible PCBs · wearable sensors</span><br>
        <span>Medical device hardware</span><br>
        <span>Environmental monitoring</span>
      </div>
    </div>
  </div>

  <div class="section-label">workflow</div>
  <div class="workflow">
    <span class="anode">requirements</span>
    <span style="color:#1e1e1e"> ──▶ </span>
    <span class="node">schematic</span>
    <span style="color:#1e1e1e"> ──▶ </span>
    <span class="node">PCB layout</span>
    <span style="color:#1e1e1e"> ──▶ </span>
    <span class="node">JLCPCB fab</span>
    <br>
    <span style="color:#1e1e1e; padding-left: 20ch">│</span>
    <br>
    <span class="anode">UI / API</span>
    <span style="color:#1e1e1e">   ◀── </span>
    <span class="node">server</span>
    <span style="color:#1e1e1e">    ◀── </span>
    <span class="node">firmware</span>
    <span style="color:#1e1e1e">   ◀── </span>
    <span class="node">bring-up</span>
    <div class="tagline">Every layer. No handoffs.</div>
  </div>

  <div class="interfaces">
    <div class="section-label">high-speed interfaces</div>
    <div class="chip-row" style="margin-bottom:10px;">
      <div class="chip">MIPI CSI-2</div>
      <div class="chip">MIPI DSI</div>
      <div class="chip">I²S</div>
      <div class="chip">USB-C</div>
    </div>
    <div class="section-label" style="margin-top:12px;">toolchain</div>
    <div class="chip-row">
      <div class="chip-n">ESP32-S3 / P4</div>
      <div class="chip-n">C++</div>
      <div class="chip-n">Python</div>
      <div class="chip-n">FreeRTOS</div>
      <div class="chip-n">PlatformIO</div>
      <div class="chip-n">KiCad</div>
      <div class="chip-n">I²C</div>
      <div class="chip-n">SPI</div>
      <div class="chip-n">UART</div>
    </div>
  </div>

  <hr class="divider">

  <div class="section-label" style="margin-bottom:12px;">stats</div>
  <div class="stats">
    <img src="https://github-readme-stats.vercel.app/api?username=out-of-mana8&show_icons=true&theme=dark&bg_color=0f0f0f&border_color=1e1e1e&title_color=00f0c8&icon_color=00f0c8&text_color=aaaaaaa&hide_border=false&count_private=true"/>
    <img src="https://streak-stats.demolab.com?user=out-of-mana8&theme=dark&background=0f0f0f&border=1e1e1e&ring=00f0c8&fire=00d4b0&currStreakLabel=00f0c8&sideLabels=aaaaaa&dates=555555"/>
  </div>

  <hr class="divider">

  <div class="footer">
    <div class="footer-l">
      <div class="pulse"></div>
      Studying ECE @ Vanderbilt · avionics · medical · AI hardware
    </div>
    <div class="footer-r">out-of-mana8</div>
  </div>

</div>
</body>
</html>
