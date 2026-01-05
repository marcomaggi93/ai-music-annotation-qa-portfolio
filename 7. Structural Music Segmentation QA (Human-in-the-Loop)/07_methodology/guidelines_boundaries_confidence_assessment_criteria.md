⭐ Guideline — Boundary Validation & Confidence Assessment
Professional Version — Integrated & Updated

This document defines the criteria used for automatic boundary validation, manual structural annotation, and confidence score assignment in music structural segmentation and Audio QA tasks.
All rules below are applied consistently across the dataset.

––––––––––––––––––––

Boundary Validation — Issue Types & Rules


1.1 OK (Correct Boundary)

A boundary is labelled ok when:
• The automatic boundary is placed within ±0.25 seconds of the correct manual boundary
• The start of the new section is musically clear
• The attack is clean and aligned (downbeat / phrase start)

This represents a correct structural alignment.

––––––––––––––––––––

1.2 Boundary Shift (Early / Late)

A boundary is labelled boundary_shift when:
• The automatic boundary occurs before (early) or after (late) the correct manual boundary
• The boundary is placed within ±1.0 second of the correct manual boundary
• The boundary still represents the same structural transition

Boundary shift types:
• boundary_shift_early
• boundary_shift_late

IMPORTANT:
A boundary_shift does NOT generate a Section Missing.
The section transition has been detected, but with imperfect timing.

––––––––––––––––––––

1.3 Severe Boundary Shift (Out-of-Range but Correlated)

A boundary is labelled boundary_shift_severe when:
• The automatic boundary is placed beyond ±1.0 second
• The boundary is still musically correlated with the same section transition
• The model anticipates or delays the transition too much

In this case, the manual boundary MUST be added as Section Missing, because the correct boundary was not captured within the ±1.0s window.
Timing alone does not define a false boundary. A severe boundary shift may still represent a valid structural transition if musical correlation is clearly identifiable.

––––––––––––––––––––

1.4 False Boundary

A boundary is labelled false_boundary when:
• The automatic boundary is placed more than ±2.0 seconds from any relevant manual boundary
• AND/OR it does not represent any real structural transition

Typical causes:
• non-functional musical moments
• random or misleading detection points

False boundaries receive very low confidence scores.

––––––––––––––––––––

1.5 On Silence

A boundary is labelled on_silence when the model splits on:
• short silences
• reverb tails
• micro-gaps between phrases
• phrase-ending decrescendos
• breaths or non-structural pauses

If no harmonic, rhythmic, thematic, instrumental, or functional change occurs, the boundary must be tagged on_silence.

An on_silence boundary never covers a real manual boundary.
If it is placed outside ±1.0 second of the manual boundary, the manual boundary must be marked as Section Missing.
An on_silence boundary is considered musically false by nature, even if it is temporally close to a manual boundary.

––––––––––––––––––––

1.6 Too Close (Over-Segmentation / Micro-Splits)

A boundary is labelled too_close when:
• Two automatic boundaries appear within a very short time window (typically <3–4 seconds)
• No real section change occurs between them
• The audio remains in the same theme, harmony, instrumentation, and energy

Detection method:
• Inspect boundary_time_sec for consecutive rows
• If the second boundary introduces no new structural function, mark it as too_close

The musically meaningful boundary may remain ok or boundary_shift.

––––––––––––––––––––
2. Section Missing (Manual Boundary Not Detected)
––––––––––––––––––––

Definition (Final)

A Section Missing is added ONLY when:
• No automatic boundary exists within ±1.0 second of the correct manual boundary

Rules:
• Do NOT add Section Missing if a boundary_shift (≤ ±1.0s) exists
• DO add Section Missing if the automatic boundary is:
– boundary_shift_severe
– false_boundary
– on_silence outside ±1.0s
– completely absent

A Section Missing represents a missing boundary, NOT a missing musical section. Example: if a correct manual boundary occurs at 30.0 s and the closest automatic boundary is placed at 31.2 s, this case is treated as a severe boundary shift and the manual boundary is added as Section Missing.

––––––––––––––––––––
3. Manual Boundary Placement — Musical Criteria
––––––––––––––––––––

A manual boundary should be placed when one or more of the following occur:
• harmonic change (new chords, modulation, cadence)
• instrumentation change (entry/exit of drums, bass, pads, etc.)
• thematic or melodic change
• energy shift (build → drop, breakdown → full)
• rhythmic change (new groove, stop-time, reset)
• dynamic change (dense → sparse, piano → forte)
• tempo or meter change

Waveform cues (Audacity):
• thick waveform = higher energy
• thin waveform = lower energy
• visible gaps = possible non-structural events

A valid boundary must introduce a stable new section, not a short fill or transition artifact.

Typical structure for short AI-generated music (1:00–1:30):
• 2–5 sections total
• usually 3–4 for pop / corporate / EDM
• avoid micro-fragmentation

––––––––––––––––––––
4. Confidence Assessment — Principles
––––––––––––––––––––

-General Definition of Confidence Scores

Confidence scores express how reliable and trustworthy a boundary placement is from a structural and musical perspective.
They do not measure correctness alone, but the degree of certainty that the boundary meaningfully represents a real section transition.

Confidence values must always be consistent, repeatable, and justified by musical listening, not by guesswork.

Manual boundary confidence reflects musical certainty only, whereas automatic boundary confidence reflects both timing accuracy and musical correlation.

-General Confidence Ranges (Global Rule)

The following confidence ranges apply across all boundary types:

• 0.80 – 0.95 → High Confidence
Clear, convincing structural boundary.
Strong musical cues and reliable placement.

• 0.60 – 0.75 → Medium Confidence
Valid boundary with some uncertainty.
Structurally meaningful but not striking.

• 0.40 – 0.55 → Low Confidence
Weak or ambiguous boundary.
Musically correlated but imprecise or problematic.

• 0.10 – 0.30 → Very Low Confidence / Almost None
Boundary is likely incorrect, non-structural, or caused by artifacts
(silence, reverb tail, micro-events, noise).

These ranges provide a global interpretative framework.
Specific confidence values within each range are determined using the detailed criteria for each boundary type (distance, attack quality, musical correlation).

––––––––––––––––––––

4.1 Main Criteria (Priority Order)

Confidence scores are based on:

Temporal distance (Δt)

Attack quality (play test)
– clean attack / downbeat → higher confidence
– cut or dirty attack → lower confidence

Musical correlation with the true transition

––––––––––––––––––––

4.2 Confidence — Boundary Shift (Early / Late)

General range: 0.40 – 0.80

Valid boundary_shift:
• Δt ≈ 0.30–0.50 s, high correlation → 0.70–0.80
• Δt ≈ 0.50–0.90 s, clear correlation → 0.60–0.70
• Δt ≈ 0.90–1.00 s, weak correlation → 0.55–0.60

Severe boundary_shift:
• Δt ≈ 1.1–1.5 s, same transition → 0.45–0.55
• Δt ≈ 1.5–2.0 s, weakly correlated → 0.40–0.45

For boundary_shift and boundary_shift_severe, confidence scores must be assigned based on the following primary criteria, in strict priority order:

-Confidence Assessment Criteria

Temporal Distance (Δt)
The farther the automatic boundary is from the correct manual boundary, the lower the confidence.

Attack Quality (Play Test)
Press Play exactly at the automatic boundary time:

• Clean attack / clear downbeat / clear phrase start → increase confidence
• Dirty attack / cut sound / truncated tail / awkward entry → decrease confidence

The attack test is mandatory and may override purely temporal considerations when the musical perception clearly improves or worsens the boundary validity.

High confidence values may also apply to boundary_shift cases when musical correlation is strong, even if temporal alignment is not perfect. Below 0.40, the boundary tends to be a false boundary.

––––––––––––––––––––

4.3 Confidence — On Silence

Professional confidence range:
0.10 – 0.30

• micro-pause / breath → 0.25–0.30
• decrescendo / tail → 0.20–0.25
• random silence split → 0.10–0.15

––––––––––––––––––––

4.4 Confidence — False Boundary

Very low confidence:
• downbeat but incorrect → ~0.20
• weak beat / levare, incorrect → 0.10–0.15
• random or off-grid → 0.05–0.10

––––––––––––––––––––
5. Summary Thresholds (Definitive)
––––––––––––––––––––

• ≤ ±0.25 s → ok
• ≤ ±1.0 s → boundary_shift (NOT missing)
• > ±1.0 s → boundary_shift_severe (ADD Section Missing)
• > ±2.0 s → false_boundary
• on_silence → confidence 0.10–0.30

––––––––––––––––––––
6. Final Note
––––––––––––––––––––

Boundary issues are classified using explicit temporal thresholds and musical validation.
Confidence scores reflect timing accuracy, musical correlation, and attack quality.
All criteria are applied consistently across the dataset.