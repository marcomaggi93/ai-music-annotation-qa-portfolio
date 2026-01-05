import sys, glob, os
import librosa, numpy as np, pandas as pd

inp, out = sys.argv[1], sys.argv[2]
rows=[]
for f in glob.glob(os.path.join(inp, "*")):
    try:
        y, sr = librosa.load(f, sr=None, mono=True)
        mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
        m = np.mean(mfcc, axis=1)
        row = {"title": os.path.basename(f)}
        for i in range(13):
            row[f"mfcc_{i+1}"] = float(m[i])
        rows.append(row)
    except Exception as e:
        rows.append({"title": os.path.basename(f), "error": str(e)})
pd.DataFrame(rows).to_csv(out, index=False)
print("✅ MFCC saved to", out)
