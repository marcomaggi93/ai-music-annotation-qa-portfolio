T02 — Auto vs Manual Alignment (Mini-QA Report)

Track ID: T02_bright_momentum
Style: Corporate pop / motivational instrumental
Task: Structural Segmentation QA

Track Structure (Manual Reference)

Manual macro-structure:

Intro → Main Section A → Breakdown / Release → Main Section B

Manual annotations show clear section boundaries with consistent confidence scores.

Boundary-by-Boundary Analysis
Boundary 1 — 0.000 sec (Intro)

Auto: 0.000

Manual: 0.000

Status: ✅ Correct boundary

Error type: None

Analysis: Accurate detection of track onset.

Confidence (auto vs manual): 0.90 vs 0.60

Boundary 2 — 10.027 sec

Auto: 10.027

Manual: 22.511 (Intro → Main Section A)

Difference: +12.48 sec (late)

Status: ❌ False boundary

Error type: False boundary

Analysis: Boundary placed inside the Intro without any corresponding manual transition.

Confidence (auto vs manual): 0.10 vs 0.60

Boundary 3 — 20.043 sec (On Silence)

Auto: 20.043

Manual: no boundary

Status: ❌ False boundary

Error type: On-silence

Analysis: Boundary triggered by a non-structural silence or decay.

Confidence (auto vs manual): 0.10 vs 0.60

Boundary 4 — Missing boundary (Main Section A entry)

Auto: No boundary detected

Manual: 22.511 sec

Status: ❌ Missed boundary

Error type: Missing boundary

Analysis: Core structural transition was not detected within tolerance.

Confidence (auto vs manual): n/a vs 0.80

Boundaries 5–8 — 30.048 → 71.893 sec

Auto:

30.048

40.181

50.197

60.331

71.893

Manual: All inside Main Section A (22.511 → 62.509)

Status: ❌ False boundaries

Error type: False boundary (over-segmentation)

Analysis: Multiple internal splits without corresponding manual section changes.

Confidence (auto vs manual): 0.05–0.10 vs 0.80

Boundary 9 — 81.899 sec

Auto: 81.899

Manual: 82.512 (Breakdown → Main Section B)

Difference: −0.61 sec (early)

Status: ⚠️ Boundary shift (early)

Error type: Boundary shift

Analysis: Boundary detected in the correct functional area but slightly anticipated.

Confidence (auto vs manual): 0.70 vs 0.90

Boundary 10 — Missing boundary (Breakdown entry)

Auto: No boundary detected

Manual: 62.509 sec

Status: ❌ Missed boundary

Error type: Missing boundary

Analysis: Breakdown / release entry not identified by automatic system.

Confidence (auto vs manual): n/a vs 0.75

Summary Table
Error Type	Count
Correct	1
Boundary Shift	1
False Boundary	7
Missing Boundary	2
QA Insights

Automatic segmentation shows strong over-segmentation, with multiple false boundaries inside stable manual sections.

Two core structural transitions were missed.

Boundary density suggests time-driven splitting behavior rather than structure-aware segmentation.

Manual annotations provide a consistent and reliable macro-structural reference.