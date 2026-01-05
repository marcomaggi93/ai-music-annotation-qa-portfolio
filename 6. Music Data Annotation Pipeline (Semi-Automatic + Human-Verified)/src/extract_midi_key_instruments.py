import sys, glob, os, pandas as pd
import music21 as m21

def get_instruments(score):
    names = []
    for p in score.parts:
        nm = p.partName or ""
        ins = getattr(p, 'instrument', None)
        if ins and getattr(ins, 'instrumentName', None):
            nm = ins.instrumentName
        if not nm:
            nm = ins.bestName() if ins else ""
        if nm: names.append(nm)
    if not names:
        # fallback: piano if single-staff typical MIDI
        if len(score.parts) <= 2: names = ["Piano"]
    # dedup, clean
    return ", ".join(sorted({n.strip() for n in names if n}))

def analyze_file(path):
    s = m21.converter.parse(path)
    k = s.analyze('key').name
    inst = get_instruments(s)
    return k, inst

inp = sys.argv[1]  # folder with .mid/.midi
out = sys.argv[2]  # output csv

rows = []
for f in glob.glob(os.path.join(inp, "*")):
    if not f.lower().endswith((".mid", ".midi", ".xml", ".musicxml")):
        continue
    try:
        key, instruments = analyze_file(f)
        rows.append({"title": os.path.basename(f), "key_est": key, "instruments": instruments})
    except Exception as e:
        rows.append({"title": os.path.basename(f), "key_est": "", "instruments": "", "notes": f"ERR:{e}"})

pd.DataFrame(rows).to_csv(out, index=False)
print(f"✅ Saved {out} with {len(rows)} rows")
