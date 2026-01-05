# How I Detect Structural Boundaries in Music  
*(Manual QA Workflow – Human-in-the-Loop)*

This document summarizes my practical workflow for detecting, validating, and refining structural boundaries in music, combining automatic novelty detection, critical listening, metadata, and confidence scoring.
The automatic segmentation used in this project is intentionally based on a lightweight, baseline script relying on energy-based novelty detection and fixed temporal constraints.
This code is not presented as a production-ready segmentation system, but as a deliberately simple starting point designed to:

- expose the limitations of purely signal-driven segmentation,
- generate realistic segmentation noise (over-segmentation, false positives, timing shifts),
- clearly demonstrate the value of manual QA, musical expertise, and human-in-the-loop correction.

The goal of this project is not to showcase advanced programming skills, but to demonstrate professional competence in:

- structural listening and musical judgment,
- boundary validation and confidence assessment,
- error analysis and QA reporting,
- pipeline reasoning and improvement proposals.

Based on the observed failure modes, a set of pipeline improvement proposals is provided, showing how this baseline could be refined using genre awareness, adaptive thresholds, post-processing logic, and feedback from manual QA.

This reflects a real-world scenario in which automatic systems are iteratively improved through expert human review rather than replaced by fully engineered solutions.


---

## 1. Input & Folder Structure

I work inside a consistent project structure:

- `00_audio/` → input audio files (WAV/MP3) to annotate  
- `01_segmentation_auto/` → CSV files from automatic segmentation  
- `02_manual_section_labels/` → manual section labels (from Audacity)  
- `03_QA_tasks/` → alignment files, error classification, 30-min challenges  
- `04_metadata_sections/` → per-section metadata CSVs  
- `05_final_QA/` → quality metrics, KPI macro, feedback logs  
- `06_case_studies/` → in-depth structural QA case studies (e.g., P03)  
- `07_methodology/` → guidelines and workflow docs (this file, boundary rules, manual segmentation guideline)
- edge_cases_log.md
- notes.md
- run_segmentation.py

Tools used:

- **Audacity** → listening + labeling boundaries  
- **VS Code** → editing CSV/MD files  
- **Python + librosa** → automatic segmentation (baseline script)

---

## 2. Novelty Detection (Automatic Baseline)

I start with a **lightweight novelty-based baseline** using `run_segmentation.py`:

- Compute an **onset-based energy curve** (`librosa.onset.onset_strength`)  
- Derive a **novelty function** (frame-to-frame changes)  
- Apply a **data-driven threshold** (mean + k·std) to select candidate boundaries  
- Enforce:
  - minimum gap between boundaries (`MIN_GAP_SEC`)
  - minimum section duration (`MIN_SECTION_SEC`)
- Add start (0.0) and end (track duration) as section limits  
- Save output as CSV in `01_segmentation_auto/` with columns:  
  `section_label;start_sec;end_sec`

This automatic baseline is intentionally simple and “signal-driven”: it produces mathematically regular boundaries and helps reveal the gap between pure DSP and true musical structure.

---

## 3. Critical Listening & Manual Boundary Detection

The **primary source of truth** is my ear.

### 3.1. Listening pass (musical criteria)

While listening, I mark potential boundaries where I hear **stable changes** such as:

- Harmonic change (new progression, modulation, cadence)  
- Instrumentation change (drums/bass/pads/strings/vocals entering or dropping)  
- Thematic/melodic change or clear variation  
- Energy/dynamic shift (sustained build or release)  
- Tempo, groove, or rhythmic character change that stays consistent over time  

Only **true structural changes** are labelled (Intro, Verse, Chorus, Bridge, Build, Outro, etc.), not every small production detail.

### 3.2. Audacity support (visual + labels)

In **Audacity** I:

1. Import the audio from `00_audio/`  
2. Zoom into the waveform and look for:
   - denser blocks (higher energy)
   - thinner blocks (lower energy)
   - gaps or near-silence
   - visible pattern changes  
3. Use `Ctrl + B` to drop **label points** at candidate boundaries  
4. Add quick notes in the label text (e.g., “new theme”, “drums in”, “build starts”, doubts)  
5. Export labels as `.txt` into `02_manual_section_labels/`  
6. Use those exported times and notes as the basis for my **manual section CSVs**, then I delete the temporary `.txt` files once the CSVs are created.

---

## 4. Section Naming & Manual Sections CSV

From the Audacity labels and listening notes, I build for each track a CSV in  
`02_manual_section_labels/`, e.g. `T01_sections_manual.csv`, with:

```text
section_label;start_sec;end_sec;confidence_manual
section_label → short, musically meaningful names
(e.g., Intro, Main_Section_A, Build_Theme_B, Climax, Outro, Verse_1, Pre_Chorus_1, Chorus_2, Bridge, Final_Chorus)

start_sec, end_sec → refined from Audacity labels

confidence_manual → my structural certainty, based on listening and the global confidence scale

This is my gold structural grid for each track.

## 5. Metadata Pack per Section

For each track, I create a section-level metadata file inside  
`04_metadata_sections/` (e.g. `P03_section_metadata.csv`).

Each row represents a **manual (gold) section**, not a boundary.

**Schema:**
section;start_sec;end_sec;instruments;mood;energy;function;confidence_manual

- instruments → dominant sound sources in the section  
- mood → concise emotional descriptors  
- energy → low / medium / high (or combined: low-medium, medium-high)  
- function → musical role (intro, verse, chorus, bridge, build, outro, etc.)  
- confidence_manual → structural certainty based on listening  

This metadata layer makes the segmentation musically interpretable, showing not just *where* sections start, but *what they represent*.

---

## 6. Automatic Boundary QA & Confidence Scoring

Automatic segmentation results (stored in `01_segmentation_auto/`) are reviewed and extended at **boundary level**, not section level.

**Schema:**
section_label;start_sec;end_sec;issue_auto;confidence_auto;boundary_time_sec

For each automatic boundary, I assign:

### Boundary Issue Types
- ok  
- boundary_shift_early  
- boundary_shift_late  
- boundary_shift_severe  
- false_boundary  
- on_silence  
- too_close  

### Confidence Scoring (confidence_auto)

Confidence values are assigned using a fixed professional scale and reflect:

1. Temporal distance (Δt) from the correct manual boundary  
2. Attack quality (play test at the exact boundary time)  
3. Musical correlation with the true structural transition  

Confidence scores follow the definitions provided in  
**“Guideline — Boundary Validation & Confidence Assessment (Professional Version)”**.

### Section Missing

If no automatic boundary occurs within ±1.0 s of a correct manual boundary,  
a Section_missing row is explicitly added with:

- issue_auto = missing_boundary  

This ensures that **false negatives** are explicitly tracked and auditable.

---

## 7. Automatic vs Manual Alignment & Error Classification

For selected tracks (e.g. T01, T02, T03) I perform detailed QA inside  
`03_QA-tasks/`.

### 7.1 Boundary-Level Alignment (Markdown)

File example:  
`T01_auto_manual_alignment.md`

For each relevant boundary, I document:

- automatic boundary time  
- closest manual boundary time  
- temporal difference (Δt)  
- alignment status (correct / early / late / false / missing)  
- confidence_auto vs confidence_manual  
- short explanatory analysis  

This provides transparent, human-auditable QA evidence.

---

### 7.2 Error Classification (CSV)

File example:  
`T01_error_classification.csv`

**Schema:**
Error_Type;Description;Affected_Boundaries;Notes;Confidence_diff

Typical error categories include:

- over-segmentation  
- under-segmentation  
- boundary_shift  
- false_boundary  
- correct_boundary  

Confidence_diff highlights cases of over- or under-confidence  
(confidence_auto − confidence_manual).

I also perform time-limited QA challenges (e.g. 30-minute review tasks) to simulate real annotation workflows.

---

## 8. KPI Macro & Quality Metrics

All aggregated metrics are stored in `05_final_QA/`.

### 8.1 Quality Metrics (Per Track)

**Schema:**
track_id;n_auto_sections;n_manual_sections;match_percent_boundaries;false_boundaries;missed_boundaries;avg_confidence_auto;avg_confidence_manual;notes

These metrics summarize:

- segmentation granularity  
- proportion of correctly matched boundaries  
- false positives and false negatives  
- confidence behavior of the automatic system  

---

### 8.2 KPI Macro (Precision & Recall)

**Schema:**
track_id;precision;recall;notes

Using standard information retrieval definitions at boundary level:

- Precision (AUTO) = TP / (TP + FP)  
- Recall (MANUAL) = TP / (TP + FN)  

Precision reflects automatic reliability,  
Recall reflects sensitivity to real musical structure.

---

## 9. Feedback Logs & Case Studies

### 9.1 Feedback Logs (2–3 Tracks)

Stored in `05_final_QA/` as Markdown files.

For each track, the following fields are compiled:

- Problem  
- Fix (QA intervention)  
- Expected structure  
- Final assessment  
- Confidence score (global judgment confidence)  

This format mirrors professional QA feedback used in industry annotation pipelines.

---

### 9.2 Case Study (Portfolio-Ready)

Stored in `06_case_studies/`.

Example title:  
**“From Auto to Gold Label — Structural QA Case Study (Track: P03)”**

Structure:

1. Automatic vs Manual Boundaries  
2. Metadata Pack  
3. Errors & Fixes  
4. KPI — Before vs After QA  
5. Confidence Strategy  
6. Pipeline Improvement Proposal (Post-QA Insight)  

Each case study documents the complete transformation from raw automatic segmentation to a musically validated gold standard.

---

## 10. Human-in-the-Loop Pipeline Summary

The overall workflow follows a human-in-the-loop QA model:

1. Automatic baseline segmentation using novelty detection  
2. Expert listening-based structural analysis  
3. Manual boundary placement and section definition  
4. Metadata enrichment (musical function, mood, energy)  
5. Boundary-level QA with confidence scoring  
6. KPI evaluation (precision, recall, quality metrics)  
7. Feedback-driven pipeline improvement  

This workflow demonstrates how automatic segmentation systems can be reliably integrated with expert musical judgment to produce production-ready structural annotations.