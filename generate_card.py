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
        "compute \xb7 EE validation",
        "signal \xb7 power integrity",
        "GPS RTK \xb7 mesh networks",
    ], "Zipline \xb7 Oshkosh AeroTech"),
    ("SENSING",  "#4d9e8c", [
        "EMG \xb7 ECG signal acquisition",
        "INA \xb7 PGA \xb7 sigma-delta ADC",
        "flex bioelectronics \xb7 MEMS",
    ], "Research"),
]

# colour palette
C_BG     = "#0d1117"
C_CARD   = "#161b22"
C_BORDER = "#30363d"
C_ARROW  = "#4e6070"
C_TEXT   = "#c9d1d9"
C_ACCENT = "#00f0c8"

MONO_W = 0.601   # JetBrains Mono: char width / font-size ratio

# ── helpers ───────────────────────────────────────────────────────────────────

def t(x, y, s, size=14, fill=C_TEXT, anchor="start", weight="normal", spacing=None):
    attrs  = f' font-weight="{weight}"' if weight != "normal" else ""
    attrs += f' letter-spacing="{spacing}"' if spacing else ""
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" text-anchor="{anchor}"{attrs}>{s}</text>'

def hr(y):
    return f'<line x1="{PAD}" y1="{y}" x2="{W-PAD}" y2="{y}" stroke="{C_BORDER}" stroke-width="0.5"/>'

def pill(x, y, text, size, fill, bg, px=10, py=4, spacing=0):
    """Text with a colored background pill. x is the LEFT EDGE of the rect."""
    ls_gap = (len(text) - 1) * spacing
    w  = round(len(text) * size * MONO_W + ls_gap + px * 2)
    h  = round(size * 1.15 + py * 2)
    ry = round(y - size * 0.82 - py)
    ls = str(spacing) if spacing else None
    return (
        f'<rect x="{x}" y="{ry}" width="{w}" height="{h}" rx="5" fill="{bg}"/>\n  '
        + t(x + px, y, text, size=size, fill=fill, spacing=ls),
        w   # return total width so caller can chain pills
    )

def section_pill(x, y, label):
    svg, _ = pill(x, y, label, size=13, fill=C_ACCENT, bg="#0e2820", px=10, py=4, spacing=3)
    return svg

# ── pipeline ──────────────────────────────────────────────────────────────────

NODE_W = 150
NODE_H = 42

def node(x, y, label):
    cx = x + NODE_W // 2
    cy = y + NODE_H // 2 + 5
    return (
        f'<rect x="{x}" y="{y}" width="{NODE_W}" height="{NODE_H}" rx="5"'
        f' fill="{C_BG}" stroke="{C_ACCENT}" stroke-width="0.9"/>\n  '
        + t(cx, cy, label, size=14, fill=C_ACCENT, anchor="middle")
    )

def rarrow(x1, x2, y):
    return (
        f'<line x1="{x1}" y1="{y}" x2="{x2-8}" y2="{y}" stroke="{C_ARROW}" stroke-width="1.8"/>\n  '
        f'<polygon points="{x2-8},{y-5} {x2},{y} {x2-8},{y+5}" fill="{C_ARROW}"/>'
    )

def larrow(x1, x2, y):
    return (
        f'<line x1="{x1}" y1="{y}" x2="{x2+8}" y2="{y}" stroke="{C_ARROW}" stroke-width="1.8"/>\n  '
        f'<polygon points="{x2+8},{y-5} {x2},{y} {x2+8},{y+5}" fill="{C_ARROW}"/>'
    )

def darrow(x, y1, y2):
    return (
        f'<line x1="{x}" y1="{y1}" x2="{x}" y2="{y2-8}" stroke="{C_ARROW}" stroke-width="1.8"/>\n  '
        f'<polygon points="{x-5},{y2-8} {x},{y2} {x+5},{y2-8}" fill="{C_ARROW}"/>'
    )

# ── domain cards ──────────────────────────────────────────────────────────────

CARD_H = 162

def domain_card(x, y, w, title, color, lines, sub=""):
    rows = "".join(
        f'\n  ' + t(x + 10, y + 54 + i * 24, line, size=14, fill=C_TEXT)
        for i, line in enumerate(lines)
    )
    sub_el = f'\n  ' + t(x + 10, y + 140, sub, size=13, fill="#8b949e") if sub else ""
    return (
        f'<rect x="{x}" y="{y}" width="{w}" height="{CARD_H}" rx="8"'
        f' fill="{C_CARD}" stroke="{C_BORDER}" stroke-width="0.6"/>\n  '
        f'<rect x="{x}" y="{y}" width="{w}" height="3" fill="{color}"/>\n  '
        + t(x + 10, y + 26, title, size=13, fill=color, spacing="2")
        + rows + sub_el
    )

# ── main ──────────────────────────────────────────────────────────────────────

def svg():
    # pipeline
    n       = len(PIPELINE_ROW1)
    gap     = (W - 2 * PAD - n * NODE_W) // (n - 1)
    node_xs = [PAD + i * (NODE_W + gap) for i in range(n)]
    row1_y  = 132;  row1_bot = row1_y + NODE_H;  row1_cy = row1_y + NODE_H // 2
    row2_y  = 220;  row2_bot = row2_y + NODE_H;  row2_cy = row2_y + NODE_H // 2
    conn_x  = node_xs[-1] + NODE_W // 2

    nodes_r1  = "\n  ".join(node(x, row1_y, l) for x, l in zip(node_xs, PIPELINE_ROW1))
    arrows_r1 = "\n  ".join(rarrow(node_xs[i]+NODE_W, node_xs[i+1], row1_cy) for i in range(n-1))
    connector = darrow(conn_x, row1_bot, row2_y)
    nodes_r2  = "\n  ".join(node(x, row2_y, l) for x, l in zip(node_xs, PIPELINE_ROW2))
    arrows_r2 = "\n  ".join(larrow(node_xs[i+1], node_xs[i]+NODE_W, row2_cy) for i in range(n-1))

    # HR positions
    hr1 = 98
    hr2 = row2_bot + 48


    # domain cards 2×2
    card_gap    = 16
    card_w      = (W - 2 * PAD - card_gap) // 2
    card_xs     = [PAD, PAD + card_w + card_gap]
    card_row1_y = hr2 + 52
    card_row2_y = card_row1_y + CARD_H + 16
    hr3         = card_row2_y + CARD_H + 28

    cards = "\n  ".join(
        domain_card(card_xs[i % 2], card_row1_y if i < 2 else card_row2_y,
                    card_w, title, color, lines, sub)
        for i, (title, color, lines, sub) in enumerate(DOMAINS)
    )

    # header subtitle — two badge pills
    hb1_svg, hb1_w = pill(PAD, 80, "ECE @ Vanderbilt", size=14, fill=C_TEXT, bg="#1a2540", px=10, py=4)
    hb2_svg, _     = pill(PAD + hb1_w + 10, 80, "ASIC @ Synaptics", size=14, fill=C_TEXT, bg="#1a2540", px=10, py=4)

    # footer
    foot_y = hr3 + 40
    H      = foot_y + 30

    return f'''<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}">
  <defs>
    <style>text {{ font-family: "JetBrains Mono", "Courier New", monospace; }}</style>
  </defs>
  <rect width="{W}" height="{H}" fill="{C_BG}" rx="12"/>
  <rect width="{W}" height="3" fill="{C_ACCENT}"/>

  <!-- header -->
  {t(PAD, 54, "Tausif Samin", size=30, fill="#e6edf3", weight="700", spacing="-0.5")}
  {hb1_svg}
  {hb2_svg}
  {hr(hr1)}

  <!-- pipeline -->
  {section_pill(PAD, hr1 + 22, "PIPELINE")}
  {nodes_r1}
  {arrows_r1}
  {connector}
  {nodes_r2}
  {arrows_r2}
  {hr(hr2)}

  <!-- domains 2x2 -->
  {section_pill(PAD, hr2 + 22, "DOMAINS")}
  {cards}
  {hr(hr3)}

  <!-- footer -->
  {t(PAD, foot_y, "PlatformIO \xb7 KiCad \xb7 EasyEDA Pro \xb7 FreeRTOS \xb7 C++ \xb7 Python", size=12, fill="#8b949e")}
  {t(W - PAD, foot_y, "schematic \u2192 silicon", size=12, fill=C_ACCENT, anchor="end")}
</svg>'''


if __name__ == "__main__":
    with open(OUTPUT, "w", encoding="utf-8") as f:
        f.write(svg())
    print(f"{OUTPUT} written.")
