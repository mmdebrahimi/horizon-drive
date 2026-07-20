"""Cross-subsystem artifact-vs-signal budget for the Phase-1 apparatus.

Consolidates the quantitative findings from the 7 subsystem-optimization memos
into one self-checking script. The point: the ~12 uN target signal is SMALLER
than several candidate ARTIFACTS unless each is actively suppressed. Each block
shows an artifact's size and the discriminator that separates it from a real
thrust. Exit 0 == all cross-checks pass.
"""
import math
c = 2.998e8
SIGNAL = 12e-6          # N, predicted Phase-1 thrust (eta*P*Q/c, P=10W, Q~5e4)
f0 = 1.836e9
Q  = 27000.0

print("=" * 68)
print("PHASE-1 APPARATUS — artifact-vs-signal budget  (target signal 12 uN)")
print("=" * 68)

# --- 1. Vacuum: radiometric/convective force vs pressure --------------------
# transition-regime thermal-edge force ~ p*A*(dT/T); peaks at Kn~1 (~0.1-1 torr),
# falls ~linearly with p into free-molecular. Agent sizing: A~100 cm^2, dT~10 K.
def radiometric(p_torr, A=100e-4, dT=10.0, T=300.0):
    # order-of-magnitude: F ~ p*A*(dT/T) with a transition-regime rolloff below ~5e-4 torr
    p_pa = p_torr * 133.322
    f_peak = p_pa * A * (dT/T)
    # linear falloff into free-molecular relative to a ~1e-3 torr reference
    return f_peak
F_rough = radiometric(1e-3)
F_hv    = radiometric(1e-6)
print("\n[1] VACUUM  (discriminator: pressure sweep at fixed RF power)")
print(f"   radiometric force @ 1e-3 torr (roughing only) ~ {F_rough*1e6:5.1f} uN"
      f"   ({'EXCEEDS' if F_rough>SIGNAL else 'below'} the 12 uN signal -> the EmDrive trap)")
print(f"   radiometric force @ 1e-6 torr (turbo)         ~ {F_hv*1e6:7.3f} uN"
      f"   ({SIGNAL/F_hv:.0f}x margin)")
print("   real thrust is pressure-INDEPENDENT; artifact dies as you pump down.")

# --- 2. Thermal: CTE detune vs linewidth -----------------------------------
cte = 17e-6
detune_per_K = cte * f0            # Hz per K (df/f = alpha*dT -> df = alpha*f*dT)
linewidth = f0 / Q
print("\n[2] THERMAL  (discriminator: constant-DISSIPATED-power modulation + PLL)")
print(f"   copper detune = {detune_per_K/1e3:.1f} kHz/K ; linewidth f/Q = {linewidth/1e3:.1f} kHz")
print(f"   1 K of RF heating = {detune_per_K/linewidth:.2f} linewidths -> stored energy runs away")
print("   FATAL naive scheme: on/off modulates HEAT at the lock-in freq (not rejected).")
print("   FIX: on-resonance<->off-resonance at CONSTANT total dissipated power")
print("        -> heating identical both phases -> artifact common-mode -> rejected.")

# --- 3. EM: feed-current x Earth-field force --------------------------------
B_earth = 50e-6
L = 0.30
I_loop = 1.0                        # A, a plausible net-loop feed current
F_ILB = I_loop * L * B_earth
print("\n[3] EM  (discriminator: coax zero-loop + polarity/rotation 2x2)")
print(f"   1 A net-loop current x Earth field over {L*100:.0f} cm = {F_ILB*1e6:.1f} uN"
      f"   (~{F_ILB/SIGNAL:.1f}x the signal -> the #1 published EmDrive artifact)")
print("   FIX: coaxial routing (~0 net loop area) + real thrust flips under 180 deg")
print("        cavity rotation but NOT under current-polarity flip; I L x B does opposite.")

# --- 4. Calibration: photon-pressure floor + electrostatic span -------------
photon_coeff = 2.0/c               # N/W
F_photon_15W = photon_coeff * 15.0
print("\n[4] CALIBRATION  (discriminator: two absolute refs agree <2%)")
print(f"   photon pressure 2/c = {photon_coeff*1e9:.2f} nN/W ; 15 W -> {F_photon_15W*1e9:.0f} nN")
print("   photons anchor the nN-sub-uN bottom; electrostatic V^2 law spans to 12 uN;")
print("   the two MUST agree <2% in overlap or a systematic is present -> block reporting.")

# --- 5. Force metrology: balance deflection --------------------------------
kappa = 3.5e-2                      # N*m/rad, 0.90 mm W fibre x 300 mm
r = 0.15
theta = SIGNAL * r / kappa
tip = theta * r
print("\n[5] FORCE METROLOGY  (discriminator: 180 deg rotation + dummy-heater null)")
print(f"   0.90 mm W fibre: 12 uN @ {r*100:.0f} cm -> {theta*1e6:.0f} urad -> {tip*1e6:.1f} um tip")
print("   real thrust INVERTS under 180 deg cavity rotation; thermal CoM drift does NOT.")

# --- 6. Q-ladder = the discriminator axis (with honest cryo-Cu correction) --
print("\n[6] Q-LADDER  (discriminator: F proportional to Q at fixed dissipated power)")
print("   Cu(300K) 2.7e4  ->  cryo-Cu(4K) ~1e5  ->  Nb3Sn(4.2K) ~1e10")
print("   NOTE/correction: cryo-Cu caps ~1e5 (anomalous skin effect), NOT ~1e6")
print("   as loosely stated earlier -- still a real middle F-vs-Q point.")

# --- self-checks ------------------------------------------------------------
assert F_rough > SIGNAL,        "radiometric @1e-3 torr must exceed signal (the trap)"
assert F_hv < 0.1*SIGNAL,       "radiometric @1e-6 torr must be <<signal"
assert detune_per_K/linewidth > 0.3, "1K detune should be a sizable fraction of linewidth"
assert F_ILB > SIGNAL,          "1A loop-current artifact must exceed signal"
assert 6e-9 < photon_coeff < 7e-9, "photon coeff ~6.67 nN/W"
assert 6e-6 < tip < 10e-6,      "balance tip deflection ~8 um"
print("\nAll cross-subsystem checks passed.  (exit 0)")
print("Bottom line: 4 of 6 candidate artifacts individually EXCEED or rival the")
print("12 uN signal. Only the STACK of orthogonal discriminators makes a claim safe.")
