import sys, glob, librosa, pandas as pd, os
inp = sys.argv[1]; out = sys.argv[2]
rows=[]
for p in glob.glob(os.path.join(inp, "*")):
    try:
        y,sr = librosa.load(p, sr=44100, mono=True)
        tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
        rows.append({"title":os.path.basename(p),"bpm_est":round(float(tempo[0]),1)})

    except Exception as e:
        rows.append({"title":os.path.basename(p),"bpm_est":"","notes":f"ERR:{e}"})
pd.DataFrame(rows).to_csv(out, index=False)
