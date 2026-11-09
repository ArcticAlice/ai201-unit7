# Acceptance criteria — Provenance Guard

Five criteria that say what "working" means for this service, written in unit 7
**before** you built it.

**All five are yours.** None are given.

An acceptance criterion names a number or something plainly observable. *"The
detector is accurate"* is an opinion — and perfect AI detection isn't possible
anyway, so it's an opinion about something nobody can deliver. *"Of 10 pieces I
wrote myself, at most 1 is labelled high-confidence AI"* is a criterion.

Under each, write a sentence or two on **why that target**. *"I allow at most 1
false positive in 10 because on a writing site a wrong accusation costs more
than a missed detection"* is a real answer.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## Pick numbers you can defend

**Cover at least three of these five areas.** They're prompts, not a form.

| Area | A question it could answer |
|---|---|
| False positives | How often may a human's writing get called AI? |
| Score spread | How far apart should clearly-AI and clearly-human text score? |
| Label coverage | Is every one of your three labels actually reachable? |
| The appeal path | Does an appeal always change status and always get recorded? |
| Bad input | What happens when `text` is missing, empty, or enormous? |

Two things worth knowing before you pick numbers:

- **The expensive mistake is one-sided.** Missing some AI text costs the site a
  little. Accusing a real writer costs that person a lot. A criterion that
  treats both errors as equally bad is describing a system nobody would ship.
- **Unit 8 tests across three trials, and the target has to hold across all
  three.** Your first signal runs a model, so identical input can score
  differently twice. A target of "at most 1 in 10" against trials of 2, 1, 2 is
  a **miss**.

---
## 1.

Across 10 distinct samples of writing that I authored myself, at most 1 is labeled as "high-confidence AI" (score >= 0.65).

**Why this target:**

On a publishing platform, false accusations cause immediate reputational harm to writers and erode trust in the platform. A 10% maximum false-positive ceiling prioritizes writer protection by pushing questionable human writing into either the "human" or "unsure" bands.

---

## 2.

The average combined score for 5 clearly AI-generated samples and 5 clearly human-authored samples must differ by at least 0.35.

**Why this target:**

A detector is useless if its score distribution collapses into a narrow clump. A spread of at least 0.35 proves the two signals (perplexity and stylometry) are actively distinguishing between synthetic and organic text.

---

## 3.

Across a calibration suite containing pure human text, pure AI text, and hybrid/borderline text, all three user-facing labels ("high-confidence human", "unsure", and "high-confidence AI") are each produced at least once.

**Why this target:**

Ensures that thresholds in `config.py` leave sufficient room for every label to be reachable in practice, avoiding dead zones or an unreachable "unsure" category.

---

## 4.

For 100% of appeal requests submitted to `POST /appeal` referencing an existing `content_id`, the submission status in `logs/audit.jsonl` is updated to `under_review` and a confirmation response is returned.

**Why this target:**

The appeal system is the sole safety net for falsely accused writers. It must be completely reliable, deterministic, and never fail silently or drop a writer's appeal.

---

## 5.

100% of malformed requests (empty text, missing "text" key, null body, or payloads over 50,000 words) return an HTTP 400 Bad Request error with a JSON error explanation, without causing a 500 crash or unhandled exception.

**Why this target:**

Backend services in production encounter garbage inputs and malicious payloads. The service must validate input boundaries gracefully rather than crashing the Python process.



---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 8 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

         ## 2. Uncertain cases land in the unsure band

         The system handles uncertain cases well.

         **Why this target:** ...

         > **Revised in unit 8:** Text I judged borderline scores between
         > 0.4 and 0.6 in at least 4 of 5 cases.
         >
         > **Why revised:** "well" gave me nothing to check. I couldn't
         > reach a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "At most 1 of 10 of my own pieces flagged as AI" → "at most 3
            of 10", because 1 of 10 turned out to be hard.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->
