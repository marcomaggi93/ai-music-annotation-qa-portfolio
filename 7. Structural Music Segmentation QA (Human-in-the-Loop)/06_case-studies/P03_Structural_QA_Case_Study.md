From Auto to Gold Label — Structural QA Case Study (Track: P03)

Track type: Female pop ballad
Task: Structural segmentation QA (automatic vs manual gold standard)
Focus: Boundary validation, error analysis, confidence assessment, KPI evaluation

This case study documents a full human-in-the-loop QA workflow applied to a noisy automatic segmentation output, transforming it into a consistent gold-labeled structural dataset.Manual boundaries were produced following a standardized listening-based QA workflow (see manual_guideline.md).The automatic segmentation used in this project is intentionally based on a lightweight, baseline script relying on energy-based novelty detection and fixed temporal constraints.
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

## Automatic Segmentation Baseline (Initial Setup)

The initial segmentation was generated using a lightweight, signal-driven baseline based on energy and onset novelty detection, combined with fixed temporal constraints.

This approach relies on detecting sudden changes in onset strength and enforcing a minimum temporal gap between boundaries. While technically sound and computationally efficient, the resulting segmentation exhibited mathematically regular boundary placement and weak alignment with higher-level musical structure.

This baseline was intentionally used to highlight the limitations of purely signal-based segmentation methods when applied to complex musical forms such as vocal pop ballads. The goal was not to maximize automatic accuracy, but to create a controlled reference point against which manual QA corrections and pipeline improvement strategies could be evaluated.

1. Automatic vs Manual Boundaries
1.1 Automatic Boundaries (Model Output)
section_label	boundary_time_sec	issue_auto	confidence_auto
Section_01	0.000	ok	0.90
Section_02	10.229	false_boundary	0.10
Section_03	21.493	false_boundary	0.20
Section_04	31.861	false_boundary	0.05
Section_05	41.931	ok	0.90
Section_06	51.968	false_boundary	0.10
Section_07	62.421	false_boundary	0.10
Section_08	72.448	false_boundary	0.05
Section_09	84.309	false_boundary	0.05
Section_10	94.347	false_boundary	0.05
Section_11	104.352	false_boundary	0.05
Section_12	114.400	false_boundary	0.05
Section_13	124.821	false_boundary	0.05
Section_14	134.933	boundary_shift_early	0.60
Section_15	145.013	false_boundary	0.10
Section_16	155.157	false_boundary	0.05
Section_17	165.227	severe_boundary_shift_late	0.50
Section_18	175.232	false_boundary	0.05
Section_19	186.741	false_boundary	0.10
Section_20	197.045	false_boundary	0.10
Section_21	207.947	false_boundary	0.10
Section_22	218.389	false_boundary	0.10
Automatically Missing Boundaries

These manual boundaries were not detected within ±1.0 second by the model and were explicitly marked as missing:

manual_boundary_sec	issue	confidence_manual
14.421	missing_boundary	0.80
56.987	missing_boundary	0.80
92.614	missing_boundary	0.80
120.396	missing_boundary	0.80
164.116	missing_boundary	0.70
180.545	missing_boundary	0.80
212.898	missing_boundary	0.80

Observation:
The automatic model shows a strong tendency toward regular, near-periodic segmentation, producing micro-splits across stable vocal and harmonic passages rather than detecting musically meaningful form changes.

1.2 Manual Gold Boundaries (Human Reference)
section_label	boundary_time_sec	confidence_manual
Intro	0.000	0.90
Verse_1	14.421	0.80
Pre_Chorus_1	41.931	0.80
Chorus_1	56.987	0.80
Verse_2	92.614	0.80
Pre_Chorus_2	120.396	0.80
Chorus_2	135.353	0.80
Bridge	164.116	0.70
Final_Chorus	180.545	0.80
Outro	212.898	0.80
Key Misalignments (Chronological)

14.421 s — Verse_1 entry → missing

56.987 s — Chorus_1 entry → missing

92.614 s — Verse_2 entry → missing

120.396 s — Pre_Chorus_2 entry → missing

135.353 s — Chorus_2 entry → detected only as boundary_shift

164.116 s — Bridge entry → severe boundary shift

180.545 s — Final Chorus → missing

212.898 s — Outro → missing

2. Metadata Pack (Gold Labels)
section	instruments	mood	energy	function	confidence
Intro	Piano, Voice	intimate, heartfelt	low	intro	0.9
Verse_1	Piano, Voice	intimate, reflective	low	verse	0.8
Pre_Chorus_1	Piano, Voice	emotional, reflective	low_medium	pre_chorus	0.8
Chorus_1	Piano, Strings, Pads, Bass, Voice	emotionally intense	medium_high	chorus	0.8
Verse_2	Piano, Percussion, Pads, Bass, Voice	reflective	medium	verse	0.8
Pre_Chorus_2	Piano, Percussion, Pads, Bass	longing, emotional	medium	pre_chorus	0.8
Chorus_2	Full ensemble	passionate	high	chorus	0.8
Bridge	Full ensemble	introspective	medium_high	bridge	0.7
Final_Chorus	Piano, Voice	cathartic	low	final_chorus	0.8
Outro	Piano, Voice	intimate	low	outro	0.8
3. Errors & Fixes
False Boundaries

Numerous boundaries placed inside stable verses and choruses with no harmonic, thematic, or functional change.

Regular spacing suggests algorithmic over-segmentation rather than novelty-based detection.

Fix: All false boundaries were removed and merged into surrounding gold sections.

Missing Boundaries

Critical structural transitions (verse → chorus, chorus → verse, bridge entry, outro) were never detected.

Fix: Each missing transition was manually added as Section_missing and validated through musical listening.

Boundary Shifts

Boundary Shift (Early): Chorus_2 detected ~0.42 s early with a weak attack.

Severe Boundary Shift (Late): Bridge detected ~1.11 s late, truncating the downbeat.

Fix: Gold boundaries were placed at musically correct onsets, while auto boundaries were retained only for analysis.

4. KPI — Before vs After QA
Pre-QA (Automatic vs Gold)

Precision: 13.6%

Recall: 30%

Match rate: 30%

False boundaries: 18

Missed boundaries: 7

Avg confidence (auto): 0.20

Avg confidence (manual): 0.80

Interpretation:
Extremely high false-positive rate and poor alignment with pop song structure. The model detects time-based events rather than formal musical transitions.

Post-QA

Manual QA establishes a clean, consistent gold standard

Structure is now reliable for:

training datasets

model evaluation

human-in-the-loop pipelines

5. Confidence Strategy

confidence_auto: Often unreliable — moderate values assigned to meaningless splits.

confidence_manual: Based on musical clarity, functional change, and perceptual certainty.

confidence_final (conceptual):
Would correct auto scores using human judgment, stabilizing datasets for downstream AI tasks.

## Pipeline Improvement Proposal (Post-QA Insight)

The automatic segmentation errors observed in this case study suggest that the baseline approach, while robust at a signal-processing level, lacks musical awareness and structural priors. The following improvements would significantly enhance segmentation quality without requiring a complete redesign of the system.

### 1. Duration-Aware Expected Section Ranges

Instead of allowing the algorithm to generate an arbitrary number of boundaries, the total track duration can be used to define a plausible range of expected structural sections.

Examples:
- Pop songs (3–4 minutes): typically 6–10 macro boundaries (Intro, Verses, Pre-Choruses, Choruses, Bridge, Outro)
- Short cinematic or ambient tracks (1–2 minutes): typically 2–4 macro sections (Intro texture, Main texture, Variation/Build, Release)

This expected range can act as a soft prior, preventing excessive fragmentation and discouraging mathematically regular segmentation.

### 2. Removal of Fixed Temporal Constraints

The use of a fixed minimum gap between boundaries (e.g. a constant 10 seconds) effectively forces quasi-regular segmentation patterns.

A more adaptive solution is to derive the minimum gap dynamically from:
- track duration
- expected number of sections

For example, a 120-second cinematic track with an expected 4 sections would naturally imply a minimum gap of roughly 20–25 seconds.

### 3. Genre- and Form-Aware Structural Expectations

While the algorithm does not need to explicitly label sections, it can still leverage high-level expectations:
- Vocal pop tracks tend to follow Verse–Pre-Chorus–Chorus cycles
- Cinematic and ambient cues often follow ternary (A–B–A′) or developmental forms

This prevents structurally implausible outputs such as 20+ sections in a standard pop song.

### 4. Richer Novelty Detection Beyond Energy

Relying solely on onset strength captures rhythmic changes but misses important musical transitions.

Immediate gains could be achieved by combining novelty measures from:
- MFCC or Mel-band features (timbre and instrumentation changes)
- Chroma features (harmonic and tonal shifts)
- RMS energy (macro-dynamic changes)

A combined novelty curve would better reflect musically meaningful transitions.

### 5. Post-Processing and Structural Cleanup

Simple post-processing rules could substantially reduce noise:
- merge sections shorter than a minimum duration with the most similar neighboring section
- collapse boundaries occurring too close in time (“micro-splits”)
- enforce a maximum number of sections for a given duration range

### 6. Human-in-the-Loop Feedback Integration

The manual QA annotations produced in this project (false boundaries, missing boundaries, boundary shifts) can be used as feedback signals to tune:
- novelty thresholds
- minimum section duration
- boundary density per track segment

This enables iterative improvement using a small, high-quality gold dataset rather than large-scale retraining.