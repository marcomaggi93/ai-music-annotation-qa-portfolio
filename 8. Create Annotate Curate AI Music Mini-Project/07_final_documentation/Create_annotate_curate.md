Create • Annotate • Curate

A Practical Workflow for Music AI Evaluation and Training

1. Introduction

This document presents a practical, production-oriented workflow for working with music AI systems, focused on generation, annotation, evaluation, and prompt optimization.
The methodology is designed to mirror real-world tasks required in roles such as Music AI Trainer, Prompt Engineer, Music Data Annotator, and Audio QA Specialist.

Rather than treating AI-generated music as a black box, this workflow emphasizes critical listening, structural awareness, and human-in-the-loop evaluation. Each step is grounded in musical analysis (harmony, texture, form, rhythm) and translated into formats that are usable by AI teams: structured metadata, section labels, evaluation criteria, and prompt QA documentation.

The workflow is articulated in three core phases:

Create: controlled music generation through technically precise prompts

Annotate: manual structural and harmonic analysis, with dataset-ready labeling

Curate: qualitative evaluation, prompt refinement, and documentation for training and QA purposes

The case studies included combine instrumental underscore and song-based pop/R&B material, reflecting two of the most common domains used in contemporary music AI datasets.
All outputs are documented in English, using formats compatible with professional portfolios and industry workflows.

The goal is not only to obtain musically convincing results, but to demonstrate methodological rigor, analytical clarity, and repeatability—key qualities expected when collaborating with AI research, product, or content teams.

2. Creation Phase (Prompt Design)

In this project we used two AI music-generation platforms: ElevenLabs Music (for the instrumental track) and Suno v5 (for the vocal future R&B/alternative pop track).

ElevenLabs Music offers precise control over instrumentation, structure, tempo and style, ideal for cinematic / underscore instrumental pieces.

Suno v5 excels at vocal songs: thanks to its advanced “custom mode + manual lyrics” it delivers convincing voice realism, solid structure management and good mixing — particularly effective when a lead vocal is required. 
ElevenLabs Music — Prompt Design Principles

.For Glass Echoes in Motion (instrumental underscore), prompts were structured in this order:

Genre & Style
(e.g. modern neo-classical minimalism, cinematic underscore)

Mood & Emotional Character
(contemplative, hypnotic, emotionally restrained)

Instrumentation
Explicitly defined sound sources (felt piano, muted strings, ambient pads)

Tempo & Key
Numerical BPM and tonal center (≈90 BPM, A minor)

Vocal Information
Clearly specified as instrumental only

Structure
High-level formal flow (sparse intro → evolving pulse → soft release)

Constraints
Negative prompts to avoid unwanted artifacts
(no heavy percussion, no dramatic hits, no EDM elements)

Duration
Provided as a target range, refined later inside the interface

Prompts were kept concise (≈150–250 characters), technical rather than narrative, and focused on musical attributes rather than imagery.

-Glass Echoes in Motion (the created track) is a short modern neo-classical minimalist instrumental underscore built around a felt-piano ostinato, soft sustained strings, and warm ambient pads.
The track unfolds as a gradual textural crescendo in A minor, maintaining a contemplative and hypnotic mood, with restrained dynamics and no heavy percussion, making it suitable for cinematic underscore use and music-AI evaluation tasks.

.Suno v5 (Custom Mode) — Prompt Design Principles

For Stay in the Blue Light (future R&B / alternative pop song), Custom Mode was used, separating responsibilities between fields:

Style → sound, genre, instrumentation, production, mix

Lyrics → full manual lyrics with structural tags
([Intro], [Verse], [Pre-Chorus], [Chorus], etc.)

The Style prompt followed this structure:

Genre & Subgenre
(future R&B, alternative pop)

Instrumentation & Voice
(warm Rhodes, clean sub-bass, airy pads, soft synth plucks; female vocal)

Technical Parameters
(78 BPM, E♭ minor, 4/4, vocal-forward clean mix)

Negative Prompts / Constraints
(no EDM risers, no rock drums, no distortion)

Advanced options were explicitly set to control output behavior:

Vocal Gender: Female

Lyrics Mode: Manual

Weirdness: controlled (≈20%)

Style Influence: high (≈80%)

This separation allows precise control over form, groove, and vocal delivery, while reducing ambiguity in section handling and model interpretation. The Style prompt is written in telegraphic form, using commas and semicolons, and kept between 80–250 characters for best adherence.

The created track (Stay in the Blue Light) is a future R&B / alternative pop song cue with intimate female lead vocals, vocal-forward mix, and minimal modern production. The track follows a clear contemporary pop/R&B form, supported by warm Rhodes, clean sub-bass, pads, soft synth plucks, and light trap-lite drums. Mood is intimate, sensual, and nocturnal, with controlled dynamics and emotional restraint, suitable for vocal QA and structural evaluation datasets.

3. Manual Structural Annotation

Manual structural annotation focuses on formal section changes, not on micro-events or local texture details.
The goal is to identify musically meaningful boundaries that reflect how a human listener perceives form, using both critical listening and waveform inspection.

-Annotation principles

Only structural sections are labeled, such as:

Intro

Section A (main idea)

Section A1 (variation / development)

Section B (new idea or contrast)

Bridge / middle section

Build-up / Climax

Outro

Minor changes (single instrument entries, small dynamic swells, brief harmonic color shifts) are not labeled as separate sections, but are used only as cues to locate real boundaries.

For short AI-generated tracks (≈ 1:30–2:00), the optimal level of detail is:

2–5 sections total

Typically 3–4 sections provide the best balance for QA and portfolio use

.Methodology

-Critical listening (primary method)

While listening, section boundaries are identified when one or more of the following persist over time:

Harmonic change (new loop, new chord set, modal shift)

Entry or removal of core instrumental layers

Change of melodic material or clear variation

Sustained change in energy or density

Change of rhythmic character or groove

A boundary is confirmed only when the change is structural, not momentary.

- Audacity support (visual + technical)

Audacity is used as a support tool, not as the main decision-maker.

The waveform is inspected to identify:

denser vs thinner energy blocks

pauses or transitions

changes in amplitude and texture continuity

Labels are placed using Ctrl + B, adjusted by ear, and exported as CSV.

Listening always has priority; the waveform serves to refine timing precision.

- Example: Stay in the Blue Light — Manual Section Labels
section_label,start_sec,end_sec,confidence_manual
Soft Ambient Intro,0,13.266010,0.8
Intro/Vocal,13.266010,25.734835,0.8
Verse 1,25.734835,50.684478,0.8
Pre-Chorus 1,50.684478,63.138314,0.7
Chorus 1,63.138314,88.061865,0.8
Verse 2,88.061865,113.008953,0.8
Pre-Chorus 2,113.008953,125.461902,0.7
Chorus 2,125.461902,150.449738,0.8
Bridge,150.449738,176.902650,0.7
Final Chorus,176.902650,203.386316,0.7
Outro,203.386316,214.879979,0.7

.Summary

Listening defines structure: musical perception comes first.

Audacity refines boundaries: visual confirmation and precise timing.

The resulting labels are human-interpretable, consistent, and suitable for:

Music AI training

QA evaluation

Professional portfolio presentation

4. Metadata & Evaluation

- Section-level metadata (compiled for each section)

The following metadata was compiled section by section, not at track level, in order to support professional QA, training, and evaluation workflows :
title,section,genre,source_model,duration,instruments,mood,energy,function,confidence_manual,usage_context,notes.

Example :
 - Glass Echoes in Motion,Intro,Modern neo-classical minimalism,ElevenLabs Music,01:29,Felt piano,restrained / contemplative,very low (1–2/10),tonal establishment and minimal pulse introduction,0.9,Background underscore for film/TV scenes, documentaries, branded content,Muted strings are barely perceptible; harmony remains constant while textural density gradually evolves.
- Glass Echoes in Motion,Section A,Modern neo-classical minimalism,ElevenLabs Music,01:29,Felt piano + soft strings + pads,calm / reflective,low (2–3/10),initial textural expansion and modal color reinforcement,0.8,Background underscore for film/TV scenes, documentaries, branded content,Muted strings could interact more actively with the piano; harmonic loop remains unchanged.

.Terminology clarification (brief)

Mood: perceived emotional character of the section (e.g. contemplative, calm, intense), independent from tempo or loudness.

Energy: perceived intensity level based on density, register, rhythm, and dynamics (not emotional impact).

Function: structural role of the section within the form (e.g. establishment, development, climax, release).

5. Criteria Evaluation Framework (used for both tracks)

Structural Coherence
Evaluates whether the form is logical, readable, and well-connected (e.g. Intro → A → B → Climax).

Harmonic Clarity
Measures how clearly the tonal center and harmonic language are defined and consistently maintained.

Timbral Consistency
Assesses coherence of instruments, sound design, and mix across sections, without arbitrary changes.

Dynamic Progression
Evaluates how energy evolves over time (growth, contrast, release), even without harmonic changes.

Model Reliability
Measures how accurately the AI model follows the prompt in terms of style, mood, structure, instruments, and constraints.

6. Prompt QA & Iteration

This phase documents how prompt quality was evaluated and iteratively improved based on musical, structural, and timbral outcomes.
The goal is not to rewrite prompts blindly, but to identify mismatches between intent and output, understand their causes, and apply targeted, platform-readable adjustments.

Track A — Glass Echoes in Motion

Model: ElevenLabs Music
Type: Instrumental — Modern Neo-Classical Minimalism

Issue
Muted strings are barely perceptible, resulting in a piano-dominant texture with limited timbral interaction.

Cause
Although muted strings were listed in the prompt, their prominence and continuity were not explicitly specified, leading the model to prioritize felt piano and pads.

Prompt Adjustment (conceptual)
Increase specificity on string audibility and persistence (e.g. explicitly stating sustained muted strings across sections, not background-only).

Expected Outcome
Clearer timbral balance and dialogue between piano and strings, while preserving the minimalist aesthetic and gradual textural evolution.

Track B — Stay in the Blue Light

Model: Suno v5 (Custom Mode — Style + Manual Lyrics)
Type: Future R&B / Alternative Pop

Issue
The Outro is partially rendered as an extension of the Final Chorus. Additional issues include limited contrast in the Bridge, minimal melodic micro-variation, and weak perceptual presence of airy pads.

Cause
The Style prompt does not sufficiently differentiate Outro texture and energy from the Chorus.
Bridge contrast and melodic variation are under-specified, and airy pads are mentioned but not emphasized relative to low-register harmonic layers.

Prompt Adjustment (conceptual)
Refine the Style prompt using concise, telegraphic instructions to:

distinguish the Outro via reduced drums and atmospheric decay,

introduce slight Bridge contrast (percussive or harmonic),

encourage subtle Rhodes/synth micro-variations,

reinforce audible airy pads alongside the sub-layer.

Expected Outcome
Improved sectional clarity, a more engaging Bridge, audible timbral variation, and a clearly separated Outro with smoother structural closure.

7. Human-in-the-Loop Perspective

This workflow adopts a human-in-the-loop approach, where AI generation is continuously guided, evaluated, and refined through expert musical judgment rather than treated as an autonomous creative process.

Human listening and musical analysis play a central role at every stage:

in defining musically meaningful prompts,

in performing manual structural annotation beyond what automatic segmentation can reliably detect,

in evaluating harmonic clarity, timbral balance, and dynamic progression using domain-specific criteria.

The human role is particularly critical in identifying model misinterpretations (e.g., chorus/outro merging, under-emphasized instruments, overly uniform textures) and translating these observations into prompt-level adjustments that the model can actually interpret and execute.

This iterative loop — generate → listen → analyze → adjust → regenerate — ensures that AI outputs remain musically coherent, structurally readable, and aligned with professional production standards. Rather than replacing musical expertise, the AI system becomes a collaborative tool, with the human acting as supervisor, evaluator, and final decision-maker.

8. Conclusion

This project demonstrates a complete, professional workflow for AI music evaluation and training, combining musical expertise with prompt engineering and QA skills.

.Competencies Demonstrated

Advanced prompt design for multiple AI music platforms

Manual structural annotation and boundary validation

Harmonic, timbral, and dynamic analysis

AI output evaluation using standardized criteria

Iterative prompt refinement based on QA feedback

.Suitable Roles

Music AI Trainer / Annotator

Music QA Specialist

Prompt Designer / Prompt Engineer (music domain)


AI Music Evaluator / Content Curator
