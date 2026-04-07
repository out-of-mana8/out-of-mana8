OUTPUT = "profile-card.svg"

W   = 760
PAD = 36

PIPELINE_ROW1 = ["schematic", "PCB layout", "PCB fab",   "bring-up"]
PIPELINE_ROW2 = ["UI / API",  "server",     "firmware",  "validate"]

DOMAINS = [
    ("AUDIO",    "#00f0c8", [
        "full-duplex \xb7 AEC/VAD",
        "I\u00b2S signal chains",
        "edge STT\u2192LLM\u2192TTS",
    ], "ESP32-S3 \xb7 Class-D amp"),
    ("VISION",   "#00b896", [
        "MIPI CSI-2 \xb7 DSI",
        "IMX708 \xb7 ESP32-P4",
        "ISP \xb7 RAW10 \xb7 D-PHY",
    ], "custom SoC board"),
    ("AVIONICS", "#007a63", [
        "EE validation \xb7 Zipline",
        "GPS RTK prototyping",
        "ESP32 mesh networks",
    ], "Oshkosh AeroTech"),
    ("SENSING",  "#4d9e8c", [
        "INA \xb7 PGA \xb7 sigma-delta ADC",
        "SHT40 \xb7 SCD40 \xb7 OPT3001",
        "MEMS mic \xb7 anti-alias filter",
    ], "Stanford AI Lab"),
]

EXPERIENCES = [
    "Research @ Vanderbilt Miniature Robotics Lab",
    "Research @ Stanford Artificial Intelligence Lab",
    "EE Intern @ Zipline",
    "EE Intern @ Oshkosh AeroTech",
    "ASIC Intern @ Synaptics  \u2192  summer 2025",
]

SIGNAL = [
    ("analog:",  "op-amp \xb7 anti-alias \xb7 ESD"),
    ("digital:", "I\u00b2S \xb7 MIPI CSI-2 \xb7 SPI \xb7 I\u00b2C"),
    ("power:",   "LiPo \xb7 LDO \xb7 decoupling"),
]

# ── helpers ───────────────────────────────────────────────────────────────────

def t(x, y, s, size=13, fill="#8b949e", anchor="start", weight="normal", spacing=None):
    attrs  = f' font-weight="{weight}"' if weight != "normal" else ""
    attrs += f' letter-spacing="{spacing}"' if spacing else ""
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" text-anchor="{anchor}"{attrs}>{s}</text>'

def hr(y):
    return f'<line x1="{PAD}" y1="{y}" x2="{W-PAD}" y2="{y}" stroke="#21262d" stroke-width="0.5"/>'

def section_label(x, y, label):
    return t(x, y, label, size=10, fill="#30363d", spacing="2.5")

# ── pipeline ──────────────────────────────────────────────────────────────────

NODE_W = 150
NODE_H = 40

def node(x, y, label):
    cx = x + NODE_W // 2
    cy = y + NODE_H // 2 + 5
    return (
        f'<rect x="{x}" y="{y}" width="{NODE_W}" height="{NODE_H}" rx="5"'
        f' fill="#0d1117" stroke="#00f0c8" stroke-width="0.9"/>\n  '
        + t(cx, cy, label, size=12, fill="#00f0c8", anchor="middle")
    )

def rarrow(x1, x2, y):
    return (
        f'<line x1="{x1}" y1="{y}" x2="{x2-7}" y2="{y}" stroke="#21262d" stroke-width="1.2"/>\n  '
        f'<polygon points="{x2-7},{y-4} {x2},{y} {x2-7},{y+4}" fill="#21262d"/>'
    )

def larrow(x1, x2, y):
    return (
        f'<line x1="{x1}" y1="{y}" x2="{x2+7}" y2="{y}" stroke="#21262d" stroke-width="1.2"/>\n  '
        f'<polygon points="{x2+7},{y-4} {x2},{y} {x2+7},{y+4}" fill="#21262d"/>'
    )

def darrow(x, y1, y2):
    return (
        f'<line x1="{x}" y1="{y1}" x2="{x}" y2="{y2-7}" stroke="#21262d" stroke-width="1.2"/>\n  '
        f'<polygon points="{x-4},{y2-7} {x},{y2} {x+4},{y2-7}" fill="#21262d"/>'
    )

# ── domain cards ──────────────────────────────────────────────────────────────

CARD_H = 155

def domain_card(x, y, w, title, color, lines, sub=""):
    rows = "".join(
        f'\n  ' + t(x + 16, y + 50 + i * 22, line, size=13)
        for i, line in enumerate(lines)
    )
    sub_el = f'\n  ' + t(x + 16, y + 132, sub, size=11, fill="#30363d") if sub else ""
    return (
        f'<rect x="{x}" y="{y}" width="{w}" height="{CARD_H}" rx="8"'
        f' fill="#0d1117" stroke="#21262d" stroke-width="0.6"/>\n  '
        f'<rect x="{x}" y="{y}" width="{w}" height="3" fill="{color}"/>\n  '
        + t(x + 16, y + 24, title, size=11, fill=color, spacing="2")
        + rows + sub_el
    )

# ── main ──────────────────────────────────────────────────────────────────────

def svg():
    # pipeline
    n       = len(PIPELINE_ROW1)
    gap     = (W - 2 * PAD - n * NODE_W) // (n - 1)
    node_xs = [PAD + i * (NODE_W + gap) for i in range(n)]
    row1_y  = 130;  row1_bot = row1_y + NODE_H;  row1_cy = row1_y + NODE_H // 2
    row2_y  = 215;  row2_bot = row2_y + NODE_H;  row2_cy = row2_y + NODE_H // 2
    conn_x  = node_xs[-1] + NODE_W // 2

    nodes_r1  = "\n  ".join(node(x, row1_y, l) for x, l in zip(node_xs, PIPELINE_ROW1))
    arrows_r1 = "\n  ".join(rarrow(node_xs[i]+NODE_W, node_xs[i+1], row1_cy) for i in range(n-1))
    connector = darrow(conn_x, row1_bot, row2_y)
    nodes_r2  = "\n  ".join(node(x, row2_y, l) for x, l in zip(node_xs, PIPELINE_ROW2))
    arrows_r2 = "\n  ".join(larrow(node_xs[i+1], node_xs[i]+NODE_W, row2_cy) for i in range(n-1))

    # domain cards 2×2
    card_gap    = 16
    card_w      = (W - 2 * PAD - card_gap) // 2
    card_xs     = [PAD, PAD + card_w + card_gap]
    card_row1_y = 320
    card_row2_y = card_row1_y + CARD_H + 16

    cards = "\n  ".join(
        domain_card(card_xs[i % 2], card_row1_y if i < 2 else card_row2_y,
                    card_w, title, color, lines, sub)
        for i, (title, color, lines, sub) in enumerate(DOMAINS)
    )

    # HR positions (computed, no hardcoding)
    hr1 = 96
    hr2 = row2_bot + 28
    hr3 = card_row2_y + CARD_H + 24

    # experience section
    exp_label_y = hr3 + 30
    exp_row_y0  = exp_label_y + 28
    LINE        = 26

    exp_rows = [t(PAD + 20, exp_label_y, "experience:", size=13, fill="#00f0c8")]
    for i, entry in enumerate(EXPERIENCES):
        y = exp_row_y0 + i * LINE
        exp_rows.append(t(PAD + 30, y, "\u2023", size=11, fill="#30363d"))
        exp_rows.append(t(PAD + 46, y, entry, size=13, fill="#8b949e"))
    exp_section = "\n  ".join(exp_rows)

    # signal chain section
    sig_label_y = exp_row_y0 + len(EXPERIENCES) * LINE + 20
    sig_row_y0  = sig_label_y + 28

    sig_rows = [t(PAD + 20, sig_label_y, "signal_chain:", size=13, fill="#00f0c8")]
    for i, (k, v) in enumerate(SIGNAL):
        y = sig_row_y0 + i * LINE
        sig_rows.append(t(PAD + 30, y, k,  size=13, fill="#79c0ff"))
        sig_rows.append(t(PAD + 175, y, v, size=13, fill="#8b949e"))
    sig_section = "\n  ".join(sig_rows)

    # footer
    hr4    = sig_row_y0 + len(SIGNAL) * LINE + 16
    foot_y = hr4 + 28
    H      = foot_y + 28   # computed height

    return f'''<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}">
  <defs>
    <style>text {{ font-family: "JetBrains Mono", "Courier New", monospace; }}</style>
  </defs>
  <rect width="{W}" height="{H}" fill="#0d1117" rx="12"/>
  <rect width="{W}" height="3" fill="#00f0c8"/>

  <!-- header -->
  {t(PAD, 52, "out-of-mana8", size=30, fill="#e6edf3", weight="700", spacing="-0.5")}
  {t(PAD, 78, "ECE @ Vanderbilt  \xb7  Synaptics  \xb7  AI-optimized silicon", size=13, fill="#555e6b")}
  {hr(hr1)}

  <!-- pipeline -->
  {section_label(PAD, hr1 + 20, "PIPELINE")}
  {nodes_r1}
  {arrows_r1}
  {connector}
  {nodes_r2}
  {arrows_r2}
  {hr(hr2)}

  <!-- domains 2x2 -->
  {section_label(PAD, hr2 + 20, "DOMAINS")}
  {cards}
  {hr(hr3)}

  <!-- experience -->
  {exp_section}

  <!-- signal chain -->
  {sig_section}
  {hr(hr4)}

  <!-- footer -->
  {t(PAD, foot_y, "PlatformIO \xb7 KiCad \xb7 EasyEDA Pro \xb7 FreeRTOS \xb7 C++ \xb7 Python", size=11, fill="#30363d")}
  {t(W - PAD, foot_y, "schematic \u2192 silicon", size=11, fill="#00f0c8", anchor="end")}
</svg>'''


if __name__ == "__main__":
    with open(OUTPUT, "w", encoding="utf-8") as f:
        f.write(svg())
    print(f"{OUTPUT} written.")
