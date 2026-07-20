"""Gantt-style timeline: first experiment -> final product, with go/no-go gates.

Renders a one-page PDF visual for the horizon-drive build timeline. Phases,
durations (months), cumulative cost, and the decision gates that can END the
program with a published null. Self-checks the phase math. Exit 0 == checks pass.
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Build-Timeline-Gantt.pdf")

# phase: (label, start_month, dur_months, cum_cost_k, color)
phases = [
    ("Phase 0  Apparatus + $5 lifter shakedown", 0,  9,  40, "#7a7a7a"),
    ("Phase 1  Room-temp copper  (Q~2.7e4)",     9,  9,  45, "#b87333"),
    ("Phase 2  Cryo-copper  (Q~1e5)",           18, 12, 110, "#3a7ca5"),
    ("Phase 3  Nb3Sn superconducting  (Q~1e10)",30, 18, 200, "#2f4b7c"),
    ("Phase 4  Engineering / craft  (conditional)", 48, 24, 200, "#4a2f6b"),
]
# gates: (label, at_month, verdict_if_null)
gates = [
    ("A  rig validated?\n(lifter reads 0 in vac)", 9,  "FAIL → fix rig, not physics"),
    ("B  signal or bound?\n★ likely terminus",    18, "NULL → publish bound → STOP"),
    ("C  F∝Q slope real?",                        30, "NULL → tighter bound → STOP"),
    ("D  independently\nreplicated?",             48, "no → report systematic → STOP"),
]

fig = plt.figure(figsize=(11, 8.5))
ax = fig.add_axes([0.30, 0.30, 0.66, 0.58])

ymax = len(phases)
for i,(lab,s,d,cost,col) in enumerate(phases):
    y = ymax-1-i
    hatch = "///" if "conditional" in lab else None
    ax.add_patch(FancyBboxPatch((s, y+0.12), d, 0.72, boxstyle="round,pad=0.02",
                 linewidth=1.2, edgecolor="#333", facecolor=col, alpha=0.85, hatch=hatch))
    ax.text(s+d/2, y+0.48, f"{d} mo", ha="center", va="center", color="white",
            fontsize=8.5, fontweight="bold")
    ax.text(-1.0, y+0.48, lab, ha="right", va="center", fontsize=8.6, color="#1a1a1a")
    ax.text(s+d+0.4, y+0.48, f"~${cost}k", ha="left", va="center", fontsize=7.6,
            color="#555", style="italic")

# gate markers (vertical dashed lines + compact letter flags)
for lab, m, nullpath in gates:
    ax.axvline(m, color="#b03030", lw=1.3, ls="--", alpha=0.8, zorder=1)
    letter = lab.split()[0]   # 'A' / 'B' / 'C' / 'D'
    star = " ★" if letter == "B" else ""
    ax.text(m, ymax+0.15, f"◆ Gate {letter}{star}", ha="center", va="bottom",
            fontsize=8.0, color="#b03030", fontweight="bold")

ax.set_xlim(-0.5, 74)
ax.set_ylim(0, ymax+0.9)
ax.set_yticks([]); ax.set_xlabel("months from start", fontsize=9)
ax.set_xticks(range(0, 75, 6))
ax.tick_params(labelsize=7.5)
ax.grid(axis="x", alpha=0.15)
for sp in ("top","right","left"): ax.spines[sp].set_visible(False)

fig.text(0.5, 0.955, "Horizon-Drive Build Timeline — First Experiment → Final Product",
         ha="center", fontsize=15, fontweight="bold", color="#1a1a1a")
fig.text(0.5, 0.925, "A staged bet with KILL-GATES: a null result at any gate ends the program with a publishable bound.",
         ha="center", fontsize=9.5, style="italic", color="#666")

# ---- the gates / null-path panel (2-column grid, upper part of free strip) ----
fig.text(0.035, 0.255, "THE GO / NO-GO GATES  (each can END the program with a published null)",
         fontsize=10, fontweight="bold", color="#8a2b2b")
cols = [0.045, 0.52]
rows = [0.225, 0.180]
for idx,(lab, m, nullpath) in enumerate(gates):
    cx = cols[idx % 2]; cy = rows[idx // 2]
    letter = lab.split()[0]
    name = " ".join(lab.split("\n")[0].split()[1:])
    fig.text(cx, cy, f"◆ Gate {letter} — {name}", fontsize=8.4, fontweight="bold", color="#b03030")
    fig.text(cx+0.008, cy-0.020, f"if NULL → {nullpath}", fontsize=7.7, color="#333")

# ---- honest framing box (bottom) ----
ax2 = fig.add_axes([0,0,1,1]); ax2.axis("off"); ax2.set_xlim(0,1); ax2.set_ylim(0,1)
box = FancyBboxPatch((0.035, 0.040), 0.93, 0.085, boxstyle="round,pad=0.006",
                     linewidth=1, edgecolor="#8a5a2b", facecolor="#faf6f0")
ax2.add_patch(box)
ax2.text(0.05, 0.108, "HONEST FRAMING", fontsize=8.8, fontweight="bold", color="#8a5a2b")
ax2.text(0.05, 0.086,
         "Decisive physics answer (Gates B–C): ~2–2.5 yr, ~$110k.  Most likely outcome: a clean NULL + the Q-scaling "
         "methodology, published, STOP —",
         fontsize=8.0, color="#1a1a1a")
ax2.text(0.05, 0.063,
         "a full success.  Phases 3–4 exist only in the ~1% world where the effect is real and independently replicated. "
         "The craft is the destination, not the plan.",
         fontsize=8.0, color="#1a1a1a")

fig.savefig(OUT)
fig.savefig(os.path.join(os.path.dirname(OUT), "_gantt_preview.png"), dpi=110)
plt.close(fig)

# ---- self-checks ----
assert phases[1][1] == 18-9+9 or phases[1][1] == 9      # phase1 start=9
starts = [p[1] for p in phases]; durs = [p[2] for p in phases]
for i in range(1, 4):  # contiguous through phase 3
    assert starts[i] == starts[i-1]+durs[i-1], f"phase {i} not contiguous"
assert phases[2][3] == 110 and phases[3][3] == 200      # cost checkpoints
print("wrote:", OUT)
print("phases contiguous, cost checkpoints OK.  (exit 0)")
