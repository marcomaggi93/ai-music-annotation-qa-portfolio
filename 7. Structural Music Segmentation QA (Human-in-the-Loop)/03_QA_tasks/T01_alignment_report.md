T01 — Auto vs Manual Alignment (Mini-QA Report)

Track ID: T01_ambient
Task: Structural Segmentation QA
Focus: Automatic vs Manual Boundary Alignment

Track Overview

Style: Cinematic ambient underscore

Duration: ~1:11

Structure (Manual): Intro → Main Section A → Build / Theme B → Outro

Manual annotation quality: High confidence, clear macro-structure

Automatic system: Novelty-based segmentation with fixed temporal constraints

Boundary-by-Boundary Analysis
Boundary 1 — 0.000 sec (Intro)

Auto: 0.000

Manual: 0.000

Status: ✅ Correct boundary

Error type: None

Analysis: Perfect alignment with manual intro onset.

Confidence (auto vs manual): 0.90 vs 0.80

Boundary 2 — 10.080 sec

Auto: 10.080

Manual: 3.450 (Intro → Main Section A)

Difference: +6.63 sec (very late)

Status: ❌ Missed boundary + false boundary

Error type: Missing + False boundary

Analysis:
The real section transition at 3.45 sec was missed entirely.
The automatic boundary at 10.08 sec falls inside Main Section A with no structural cue.

Confidence (auto vs manual): 0.50 vs 0.90

Boundary 3 — 20.149 sec

Auto: 20.149

Manual: within Main Section A (3.450 → 33.434)

Status: ❌ False boundary

Error type: False boundary

Analysis:
Boundary placed inside a stable section with no change in harmony, energy, or texture.

Confidence (auto vs manual): 0.50 vs 0.90

Boundary 4 — 30.261 sec

Auto: 30.261

Manual (next real): 33.434 (Build / Theme B)

Difference: −3.17 sec (early)

Status: ⚠️ Anticipated boundary

Error type: On-silence / early anticipation

Analysis:
Boundary captures a decay/reverb tail shortly before the real thematic transition.
No stable new section begins at this point.

Confidence (auto vs manual): 0.20 vs 0.85

Boundary 5 — 40.320 sec

Auto: 40.320

Manual: inside Build / Theme B (33.434 → 63.450)

Status: ❌ False boundary

Error type: False boundary

Analysis:
No harmonic, rhythmic, or functional event justifies a section split here.

Confidence (auto vs manual): 0.05 vs 0.85

Boundary 6 — 50.447 sec

Auto: 50.447

Manual: inside Build / Theme B

Status: ❌ False boundary

Error type: False boundary

Analysis:
Additional internal split of a continuous build section without musical motivation.

Confidence (auto vs manual): 0.05 vs 0.85

Boundary 7 — Missing boundary (Outro)

Auto: No boundary detected

Manual: 63.450 sec → Outro

Status: ❌ Missed boundary

Error type: Missing boundary

Analysis:
The transition to the Outro was completely missed by the system.

Confidence (auto vs manual): n/a vs 0.60

Summary Table
Error Type	Count
Correct	1
False Boundary	4
On-Silence / Early	1
Missing Boundary	3
QA Insights

The automatic system shows strong over-segmentation, producing multiple false boundaries inside stable sections.

Core structural transitions are systematically missed, indicating low structural awareness.

Boundaries appear at near-regular temporal intervals, suggesting a mathematically driven segmentation rather than musically informed detection.

Manual annotations reveal a clear, well-defined macro-structure that the automatic pipeline fails to capture.