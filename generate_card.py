SVG_WIDTH = 740
SVG_HEIGHT = 420

def svg():
    return f'''<svg viewBox="0 0 {SVG_WIDTH} {SVG_HEIGHT}" xmlns="http://www.w3.org/2000/svg" width="{SVG_WIDTH}" height="{SVG_HEIGHT}">
  <defs>
    <style>
      text {{ font-family: "JetBrains Mono", "Courier New", monospace; }}
    </style>
  </defs>

  <!-- background -->
  <rect width="{SVG_WIDTH}" height="{SVG_HEIGHT}" fill="#0d1117" rx="12"/>

  <!-- top accent bar -->
  <rect width="{SVG_WIDTH}" height="2" fill="#00f0c8"/>

  <!-- ── HEADER ─────────────────────────────────────────────── -->
  <text x="32" y="44" font-size="11" fill="#8b949e" letter-spacing="2">HARDWARE ENGINEER</text>
  <text x="32" y="72" font-size="22" font-weight="700" fill="#e6edf3" letter-spacing="-0.5">out-of-mana8</text>
  <text x="32" y="92" font-size="11" fill="#8b949e">ECE @ Vanderbilt University · Synaptics · AI-optimized silicon</text>

  <line x1="32" y1="108" x2="708" y2="108" stroke="#21262d" stroke-width="0.5"/>

  <!-- ── PIPELINE FLOW ──────────────────────────────────────── -->
  {pipeline_node(32,  124, "schematic", accent=True)}
  {pipeline_node(148, 124, "PCB layout")}
  {pipeline_node(264, 124, "JLCPCB fab")}
  {pipeline_node(380, 124, "bring-up")}
  {pipeline_node(496, 124, "firmware")}
  {pipeline_node(612, 124, "UI / API", accent=True)}

  {pipeline_arrow(122, 148)}
  {pipeline_arrow(238, 264)}
  {pipeline_arrow(354, 380)}
  {pipeline_arrow(470, 496)}
  {pipeline_arrow(586, 612)}

  <line x1="32" y1="168" x2="708" y2="168" stroke="#21262d" stroke-width="0.5"/>

  <!-- ── DOMAIN CARDS ───────────────────────────────────────── -->
  {domain_card(32,  180, 158, "AUDIO",    "#00f0c8", [
      "full-duplex · AEC/VAD",
      "I\u00b2S signal chains",
      "edge STT\u2192LLM\u2192TTS",
  ], sub="ESP32-S3 · Class-D amp")}

  {domain_card(200, 180, 158, "VISION",   "#00b896", [
      "MIPI CSI-2 · DSI",
      "IMX708 · ESP32-P4",
      "IMU · LiPo power",
  ], sub="custom SoC board")}

  {domain_card(368, 180, 158, "AVIONICS", "#007a63", [
      "EE validation · Zipline",
      "GPS RTK prototyping",
      "ESP32 mesh networks",
  ], sub="Oshkosh AeroTech")}

  {domain_card(536, 180, 172, "SENSING",  "#4d9e8c", [
      "op-amp · anti-alias",
      "flex PCB · wearable",
      "medical · env. monitor",
  ], sub="Stanford AI Lab")}

  <line x1="32" y1="284" x2="708" y2="284" stroke="#21262d" stroke-width="0.5"/>

  <!-- ── SIGNAL CHAIN ───────────────────────────────────────── -->
  <text x="32" y="306" font-size="9" fill="#30363d" letter-spacing="2">SIGNAL CHAIN</text>

  {kv_row(32, 326, "analog:",  "op-amp · anti-alias filter · ESD protection")}
  {kv_row(32, 344, "digital:", "I\u00b2S · MIPI CSI-2 · MIPI DSI · SPI · I\u00b2C · UART · USB-C")}
  {kv_row(32, 362, "power:",   "LiPo · LDO · decoupling · ESD · power sequencing")}

  <line x1="32" y1="378" x2="708" y2="378" stroke="#21262d" stroke-width="0.5"/>

  <!-- ── FOOTER ─────────────────────────────────────────────── -->
  <text x="32"  y="400" font-size="10" fill="#30363d">PlatformIO · KiCad · EasyEDA Pro · FreeRTOS · C++ · Python · JLCPCB</text>
  <text x="708" y="400" font-size="10" fill="#00f0c8" text-anchor="end">schematic \u2192 silicon</text>

</svg>'''


def pipeline_node(x, y, label, accent=False):
    color = "#00f0c8" if accent else "#21262d"
    text_color = "#00f0c8" if accent else "#8b949e"
    cx = x + 45
    return f'''<rect x="{x}" y="{y}" width="90" height="26" rx="4" fill="#0d1117" stroke="{color}" stroke-width="0.75"/>
  <text x="{cx}" y="{y + 17}" font-size="10" fill="{text_color}" text-anchor="middle">{label}</text>'''


def pipeline_arrow(x1, x2):
    y = 137
    return f'''<line x1="{x1}" y1="{y}" x2="{x2 - 8}" y2="{y}" stroke="#21262d" stroke-width="1"/>
  <polygon points="{x2 - 8},{y - 4} {x2},{y} {x2 - 8},{y + 4}" fill="#21262d"/>'''


def domain_card(x, y, w, title, color, lines, sub=""):
    h = 88
    rows = ""
    for i, line in enumerate(lines):
        rows += f'\n  <text x="{x + 12}" y="{y + 30 + i * 16}" font-size="10" fill="#8b949e">{line}</text>'
    sub_el = ""
    if sub:
        sub_el = f'\n  <text x="{x + 12}" y="{y + 79}" font-size="9" fill="#30363d">{sub}</text>'
    return f'''<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="#0d1117" stroke="#21262d" stroke-width="0.5"/>
  <rect x="{x}" y="{y}" width="{w}" height="3" fill="{color}"/>
  <text x="{x + 12}" y="{y + 16}" font-size="9" fill="{color}" letter-spacing="1.5">{title}</text>{rows}{sub_el}'''


def kv_row(x, y, key, value):
    return f'''<text x="{x}"       y="{y}" font-size="10" fill="#79c0ff">{key}</text>
  <text x="{x + 78}" y="{y}" font-size="10" fill="#8b949e">{value}</text>'''


if __name__ == "__main__":
    output = svg()
    with open("profile-card.svg", "w", encoding="utf-8") as f:
        f.write(output)
    print("profile-card.svg written.")
