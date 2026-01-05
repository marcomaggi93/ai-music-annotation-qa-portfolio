import sys
import os
import librosa
import numpy as np
import pandas as pd

HOP_LENGTH = 512
MIN_GAP_SEC = 10.0   # distanza minima tra due confini
MIN_SECTION_SEC = 8.0  # durata minima di una sezione


def segment_track(audio_path: str) -> pd.DataFrame:
    # Carica audio (wav/mp3)
    y, sr = librosa.load(audio_path, sr=None, mono=True)
    duration = librosa.get_duration(y=y, sr=sr)

    # Novelty basata su variazioni di energia/onset
    onset_env = librosa.onset.onset_strength(y=y, sr=sr, hop_length=HOP_LENGTH)
    novelty = np.abs(np.diff(onset_env, prepend=onset_env[0]))

    # Soglia automatica: media + 1 * std
    thr = np.mean(novelty) + 1.0 * np.std(novelty)
    candidate_frames = np.where(novelty >= thr)[0]

    # Converte in tempi
    candidate_times = librosa.frames_to_time(
        candidate_frames, sr=sr, hop_length=HOP_LENGTH
    )

    # Filtra per distanza minima tra confini
    boundaries = []
    last_time = 0.0
    for t in candidate_times:
        if t - last_time >= MIN_GAP_SEC and t >= MIN_SECTION_SEC and t <= duration - MIN_SECTION_SEC:
            boundaries.append(t)
            last_time = t

    # Aggiungi inizio e fine brano
    boundaries = [0.0] + boundaries + [duration]

    # Se per qualche motivo rimangono solo 0 e duration, va bene: un’unica sezione
    sections = []
    for i in range(len(boundaries) - 1):
        start = float(boundaries[i])
        end = float(boundaries[i + 1])
        if end - start < MIN_SECTION_SEC and len(boundaries) > 2:
            # Skippa sezioni troppo corte (tranne caso singola sezione)
            continue
        label = f"Section_{i+1:02d}"
        sections.append(
            {
                "section_label": label,
                "start_sec": start,
                "end_sec": end,
            }
        )

    # Se abbiamo skippato tutto per qualche motivo, rimetti una sezione unica
    if not sections:
        sections.append(
            {"section_label": "Section_01", "start_sec": 0.0, "end_sec": float(duration)}
        )

    return pd.DataFrame(sections)


def main():
    if len(sys.argv) < 2:
        print("Usage: python run_segmentation.py path/to/audio.wav")
        sys.exit(1)

    audio_path = sys.argv[1]
    if not os.path.exists(audio_path):
        print(f"File not found: {audio_path}")
        sys.exit(1)

    df = segment_track(audio_path)

    base = os.path.splitext(os.path.basename(audio_path))[0]
    out_dir = "01_segmentation_auto"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, f"{base}_sections_auto.csv")

    df.to_csv(out_path, index=False)
    print(f"Saved: {out_path}")


if __name__ == "__main__":
    main()