import pandas as pd, os

# 1) Leggi il tuo schema (AI) e rinomina instruments -> instruments_manual
base = pd.read_csv("csv/schema_labels_v1_utf8.csv")
base = base.rename(columns={"instruments":"instruments_manual"})
if "source" not in base.columns: base["source"]="AI_generated"

# 2) Aggiungi MFCC AI
ai_mfcc = pd.read_csv("csv/ai_mfcc.csv")
ai = base.merge(ai_mfcc, on="title", how="left")

# 3) MAESTRO: rinomina instruments auto
mae_bpm = pd.read_csv("csv/maestro_auto_bpm.csv")
mae_key = pd.read_csv("csv/maestro_auto_key_instr.csv").rename(columns={"instruments":"instruments_auto"})
mae = mae_bpm.merge(mae_key, on="title", how="outer")
p = "csv/maestro_mfcc.csv"
if os.path.exists(p): mae = mae.merge(pd.read_csv(p), on="title", how="left")
mae["source"]="MAESTRO"

# 4) Colonna unificata (preferisci manuale, altrimenti auto)
for df in (ai, mae):
    if "instruments_manual" not in df: df["instruments_manual"]=""
    if "instruments_auto" not in df: df["instruments_auto"]=""
    df["instruments"] = df["instruments_manual"].where(df["instruments_manual"].ne(""), df["instruments_auto"])

# 5) Concat e salva
cols = sorted(set(ai.columns)|set(mae.columns))
out = pd.concat([ai.reindex(columns=cols), mae.reindex(columns=cols)], ignore_index=True)
out.to_csv("csv/auto_labels_extended.csv", index=False)
print("✅ saved csv/auto_labels_extended.csv")
