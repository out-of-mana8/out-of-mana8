OUTPUT = "profile-card.svg"

W = 760
H = 490

DOMAINS = [
    ("AUDIO",    "#00f0c8", ["full-duplex · AEC/VAD", "I\u00b2S signal chains", "edge STT\u2192LLM\u2192TTS"], "ESP32-S3 · Class-D amp"),
    ("VISION",   "#00b896", ["MIPI CSI-2 · DSI", "IMX708 · ESP32-P4", "IMU · LiPo power"],                   "custom SoC board"),
    ("AVIONICS", "#007a63", ["EE validation · Zipline", "GPS RTK prototyping", "ESP32 mesh networks"],         "Oshkosh AeroTech"),
    ("SENSING",  "#4d9e8c", ["op-amp · anti-alias", "flex PCB · wearable", "medical · env. monitor"],         "Stanford AI Lab"),
]

PIPELINE = ["schematic", "PCB layout", "JLCPCB fab", "bring-up", "firmware", "UI / API"]

SIGNAL = [
    ("analog:",  "op-amp \xb7 anti-alias filter \xb7 ESD protection"),
    ("digital:", "I\u00b2S \xb7 MIPI CSI-2 \xb7 MIPI DSI \xb7 SPI \xb7 I\u00b2C \xb7 UART \xb7 USB-C"),
    ("power:",   "LiPo \xb7 LDO \xb7 decoupling \xb7 ESD \xb7 power sequencing"),
]

PAD = 36   # left/right margin


def hr(y):
    return f'<line x1="{PAD}" y1="{y}" x2="{W - PAD}" y2="{y}" stroke="#21262d" stroke-width="0.5"/>'


def text(x, y, s, size=12, fill="#8b949e", anchor="start", weight="normal", spacing=None):
    ls = f' letter-spacing="{spacing}"' if spacing else ""
    fw = f' font-weight="{weight}"' if weight != "normal" else ""
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" text-anchor="{anchor}"{fw}{ls}>{s}</text>'


def pipeline_node(x, y, label, w=92, h=30, accent=False):
    stroke = "#00f0c8" if accent else "#21262d"
    color  = "#00f0c8" if accent else "#8b949e"
    cx = x + w // 2
    return (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="5"'
        f' fill="#0d1117" stroke="{stroke}" stroke-width="0.8"/>\n  '
        + text(cx, y + 20, label, size=11, fill=color, anchor="middle")
    )


def pipeline_arrow(x1, x2, y):
    mid = (x1 + x2) // 2
    return (
        f'<line x1="{x1}" y1="{y}" x2="{x2 - 7}" y2="{y}" stroke="#21262d" stroke-width="1"/>\n  '
        f'<polygon points="{x2-7},{y-4} {x2},{y} {x2-7},{y+4}" fill="#21262d"/>'
    )


def domain_card(x, y, w, title, color, lines, sub=""):
    h = 116
    rows = "".join(
        f'\n  ' + text(x + 14, y + 38 + i * 20, line, size=11)
        for i, line in enumerate(lines)
    )
    sub_el = f'\n  ' + text(x + 14, y + 102, sub, size=10, fill="#30363d") if sub else ""
    bar    = f'<rect x="{x}" y="{y}" width="{w}" height="3" fill="{color}"/>'
    box    = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="7" fill="#0d1117" stroke="#21262d" stroke-width="0.5"/>'
    ttl    = text(x + 14, y + 20, title, size=10, fill=color, spacing="2")
    return f'{box}\n  {bar}\n  {ttl}{rows}{sub_el}'


def kv_row(x, y, key, value):
    return (
        text(x, y, key, size=11, fill="#79c0ff")
        + "\n  "
        + text(x + 82, y, value, size=11)
    )


def svg():
    # ── layout constants ──────────────────────────────────────
    node_w   = 92
    node_gap = 18          # gap between nodes (for arrow)
    n        = len(PIPELINE)
    total_nw = n * node_w + (n - 1) * node_gap
    node_x0  = (W - total_nw) // 2   # center the pipeline
    node_xs  = [node_x0 + i * (node_w + node_gap) for i in range(n)]
    node_y   = 144
    node_cy  = node_y + 15            # vertical center of nodes

    card_gap = 12
    n_cards  = len(DOMAINS)
    card_w   = (W - 2 * PAD - (n_cards - 1) * card_gap) // n_cards
    card_xs  = [PAD + i * (card_w + card_gap) for i in range(n_cards)]
    card_y   = 210

    sig_y0   = 370
    sig_gap  = 24

    # ── build elements ────────────────────────────────────────
    nodes = "\n  ".join(
        pipeline_node(x, node_y, label, w=node_w, accent=(i == 0 or i == n - 1))
        for i, (x, label) in enumerate(zip(node_xs, PIPELINE))
    )
    arrows = "\n  ".join(
        pipeline_arrow(node_xs[i] + node_w, node_xs[i + 1], node_cy)
        for i in range(n - 1)
    )
    cards = "\n  ".join(
        domain_card(x, card_y, card_w, title, color, lines, sub)
        for x, (title, color, lines, sub) in zip(card_xs, DOMAINS)
    )
    signal = "\n  ".join(
        kv_row(PAD, sig_y0 + i * sig_gap, k, v)
        for i, (k, v) in enumerate(SIGNAL)
    )

    hr1 = node_y - 16
    hr2 = card_y - 16
    hr3 = card_y + 116 + 16
    hr4 = sig_y0 + len(SIGNAL) * sig_gap + 4
    foot_y = hr4 + 26

    return f'''<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}">
  <defs>
    <style>text {{ font-family: "JetBrains Mono", "Courier New", monospace; }}</style>
  </defs>

  <rect width="{W}" height="{H}" fill="#0d1117" rx="12"/>
  <rect width="{W}" height="3" fill="#00f0c8"/>

  <!-- header -->
  {text(PAD, 50, "HARDWARE ENGINEER", size=11, fill="#555e6b", spacing="2.5")}
  {text(PAD, 82, "out-of-mana8", size=26, fill="#e6edf3", weight="700", spacing="-0.5")}
  {text(PAD, 104, "ECE @ Vanderbilt University \xb7 Synaptics \xb7 AI-optimized silicon", size=12, fill="#8b949e")}

  {hr(hr1)}

  <!-- pipeline -->
  {nodes}
  {arrows}

  {hr(hr2)}

  <!-- domain cards -->
  {cards}

  {hr(hr3)}

  <!-- signal chain -->
  {text(PAD, sig_y0 - 16, "SIGNAL CHAIN", size=10, fill="#30363d", spacing="2")}
  {signal}

  {hr(hr4)}

  <!-- footer -->
  {text(PAD, foot_y, "PlatformIO \xb7 KiCad \xb7 EasyEDA Pro \xb7 FreeRTOS \xb7 C++ \xb7 Python \xb7 JLCPCB", size=10, fill="#30363d")}
  {text(W - PAD, foot_y, "schematic \u2192 silicon", size=10, fill="#00f0c8", anchor="end")}

</svg>'''


if __name__ == "__main__":
    with open(OUTPUT, "w", encoding="utf-8") as f:
        f.write(svg())
    print(f"{OUTPUT} written.")
