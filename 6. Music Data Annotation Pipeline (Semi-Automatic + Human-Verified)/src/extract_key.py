import sys, glob, os, numpy as np, pandas as pd, librosa

MAJ = np.array([6.35,2.23,3.48,2.33,4.38,4.09,2.52,5.19,2.39,3.66,2.29,2.88])
MIN = np.array([6.33,2.68,3.52,5.38,2.60,3.53,2.54,4.75,3.98,2.69,3.34,3.17])
NOTE_NAMES = ["C","C#","D","Eb","E","F","F#","G","Ab","A","Bb","B"]

def estimate_key(y, sr):
    C = librosa.feature.chroma_cqt(y=y, sr=sr)
    chroma = np.mean(C, axis=1)
    chroma = chroma / (np.linalg.norm(chroma) + 1e-9)

    best, best_name, best_mode = -1, "", ""
    for i in range(12):
        maj = np.roll(MAJ, i); maj = maj / np.linalg.norm(maj)
        minr = np.roll(MIN, i); minr = minr / np.linalg.norm(minr)
        cmaj = float(np.dot(chroma, maj))
        cmin = float(np.dot(chroma, minr))
        if cmaj > best:
            best, best_name, best_mode = cmaj, NOTE_NAMES[i], "major"
        if cmin > best:
            best, best_name, best_mode = cmin, NOTE_NAMES[i], "minor"
    return f"{best_name} {best_mode}", max(0.0, min(1.0, (best+1)/2))

inp, out = sys.argv[1], sys.argv[2]
rows=[]
for p in glob.glob(os.path.join(inp, "*")):
    try:
        y, sr = librosa.load(p, sr=22050, mono=True)
        k, conf = estimate_key(y, sr)
        rows.append({"title": os.path.basename(p), "key_est": k, "confidence": round(conf,3)})
    except Exception as e:
        rows.append({"title": os.path.basename(p), "key_est": "", "confidence": "", "notes": f"ERR:{e}"})

pd.DataFrame(rows).to_csv(out, index=False)