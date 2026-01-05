T03 — Auto vs Manual Alignment (Mini-QA Report)

Track ID: T03_chill_pulse
Style: Chill EDM / electronic pop
Task: Structural Segmentation QA

Track Structure (Manual Reference)

Manual macro-structure:

Intro → Build → Main Section → Outro

Manual boundaries are clearly defined and supported by consistent confidence scores.

Boundary-by-Boundary Analysis
Boundary 1 — 0.000 sec (Intro)

Auto: 0.000

Manual: 0.000

Status: ✅ Correct boundary

Error type: None

Analysis: Accurate detection of track start.

Confidence (auto vs manual): 0.90 vs 0.60

Boundary 2 — 10.229 sec (Build entry)

Auto: 10.229

Manual: 10.874

Difference: −0.64 sec (early)

Status: ⚠️ Boundary shift (early)

Error type: Boundary shift

Analysis: Boundary placed in the correct functional region but slightly anticipated.

Confidence (auto vs manual): 0.60 vs 0.60

Boundary 3 — 20.267 sec (Main Section entry)

Auto: 20.267

Manual: 21.309

Difference: −1.04 sec (too early)

Status: ❌ Severe boundary shift

Error type: Severe boundary shift

Analysis: Boundary detected near the real transition but outside the ±1s tolerance window.

Confidence (auto vs manual): 0.50 vs 0.75

Boundary 4 — Missing boundary (Main Section entry)

Auto: No valid boundary within tolerance

Manual: 21.309 sec

Status: ❌ Missed boundary

Error type: Missing boundary

Analysis: Correct boundary had to be manually added due to severe timing misalignment.

Confidence (auto vs manual): n/a vs 0.75

Boundaries 5–7 — 30.293 → 50.507 sec

Auto:

30.293

40.406

50.507

Manual: All inside Main Section (21.309 → 52.626)

Status: ❌ False boundaries

Error type: False boundary

Analysis: Internal splits with no corresponding manual section boundaries.

Confidence (auto vs manual): 0.05–0.10 vs 0.75

Boundary 8 — Missing boundary (Outro entry)

Auto: No boundary detected

Manual: 52.626 sec

Status: ❌ Missed boundary

Error type: Missing boundary

Analysis: Transition to final section not captured by the automatic model.

Confidence (auto vs manual): n/a vs 0.80

Summary Table
Error Type	Count
Correct	1
Boundary Shift	1
Severe Boundary Shift	1
False Boundary	3
Missing Boundary	2
QA Insights

Automatic segmentation partially captures early macro-structure but degrades after the first section.

Model shows timing sensitivity issues, with early anticipation of key transitions.

Multiple false boundaries indicate over-segmentation inside stable sections.

Manual QA restores a coherent and formally consistent structure suitable for metadata and training data.