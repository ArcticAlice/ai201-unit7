# Provenance Guard

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first.**
>
> Once `python test.py` passes, in one terminal:
>
> ```bash
> python app.py
> ```
>
> and in another:
>
> ```bash
> curl -X POST http://127.0.0.1:5000/ping \
>   -H "Content-Type: application/json" \
>   -d '{"message": "hello"}'
> ```
>
> That's a web service. Something sent it text and it sent something back.
> Everything this unit is filling in the middle.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     Unit 7 asks for the first five sections. Unit 8 adds the five below.

     Everything is pasted as TEXT. A pasted curl response gets full credit;
     a picture of your terminal gets none.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 7 — THE BUILD ═══════════════════════ -->

## What This Does

Provenance Guard is a backend verification service that evaluates whether submitted text is likely human-written, AI-generated, or uncertain. When a text submission arrives, it proceeds through the following 7-step pipeline:

1. **Request Ingestion (`POST /submit`):** A client sends a `POST` request to `/submit` with a JSON body containing `text` (the body of writing) and `creator_id` (the author's identifier).
2. **Payload Parsing & Identity Generation:** Flask parses and validates the JSON payload. A unique `content_id` (UUID) is minted for the submission so it can be tracked, audited, and referenced in any subsequent appeal.
3. **Signal 1 — Model Evaluation (`detector.py`):** The text is passed to the local causal language model (GPT-2) to compute token perplexity. This measures how predictable the word choices are and outputs a normalized `model_score` from `0.0` (surprising / human-like) to `1.0` (highly predictable / AI-like).
4. **Signal 2 — Stylometric Analysis (`stylometry.py`):** The text is analyzed purely as text—measuring sentence length spread, vocabulary richness (type-token ratio), and punctuation density. This outputs a normalized `style_score` from `0.0` (high variation / human-like) to `1.0` (uniform / AI-like).
5. **Signal Combination (`scoring.py::combine_signals`):** The system combines `model_score` and `style_score` using a defined weighting and disagreement rule to produce a single continuous score and a preliminary categorical guess (`human` or `ai`).
6. **Confidence & Label Assignment (`scoring.py::score_to_label`):** The continuous score maps into one of three user-facing label bands: `high-confidence human`, `unsure`, or `high-confidence AI`. Ambiguous or borderline scores land in the `unsure` tier, avoiding false accusations against real writers.
7. **Audit Logging & Response Dispatch (`audit.py`):** The complete decision record—including timestamp, `content_id`, `creator_id`, individual signal scores, combined score, and assigned status (`accepted`)—is appended to `logs/audit.jsonl`. The endpoint responds with JSON containing `content_id`, `guess`, `confidence`, `label`, `model_score`, and `style_score`.



---

## Signals and Scoring

<!-- For each signal: what property it measures, why that might differ between
     human and AI writing, and WHAT IT CAN'T SEE.

     The blind spot is not optional. If you can't name it you don't understand
     the signal yet — and unit 8's attack set is built out of blind spots. -->

### Signal one — the model signal

**What it measures:** The AI model measures how predicatble the next word is based on the previous one. 

**Why that might differ between human and AI writing:** Since humans are more creative or 
at least use a larger scope of different phrases and words this causes the predictability to be low. While
on the hand an AI model tends to use more common phrases and words leading it to be more general.

**What it can't see:** The model can flag real humans who decided to write plainly. It could
give a high perplexity score for someone who wanted to write a sentence straight to the point. 
On the other hand if an AI was prompted to use vocabulary from a specific genre it could possibly 
score a low perplexity score.

### Signal two — the style signal

**What it measures:** Measure sentence structure of a body of text. For example puncation and sentence length.

**Why that might differ between human and AI writing:** Huamns use a variety of different puncuation and 
sentence length. While an AI will try to keep its sentences the same length and use the same strict puncuation 
a human wouldn't.

**What it can't see:** Someone can easily get AI generated text and then go into it and add randomness. For example
decided to split up sentences so their length vary, or add multiple typos. 

### The combining rule

**The rule:** A weighted linear combination of the model signal (perplexity) and the style signal (stylometry). When the signals disagree, the weighted average naturally pulls the combined score toward the center (the "unsure" band), avoiding aggressive misclassifications. We weight stylometry slightly higher than perplexity because common human phrases and conversational conventions (like answering "Thank you" with "You're welcome") have very low perplexity under an AI model; weighting style higher protects human authors who write plainly.

**The numbers:** 45% model signal (`WEIGHT_MODEL_SIGNAL = 0.45`) and 55% style signal (`WEIGHT_STYLE_SIGNAL = 0.55`).

**Where it lives:** `scoring.py::combine_signals`

**A case where my two signals split, and what my rule does with it:** Plain, everyday human writing (such as simple journal entries or daily recounts). The model signal flags it as AI-like (`model_score = 0.8296`) because the vocabulary is common and predictable. However, the style signal detects human structural variation (`style_score = 0.4502`). Blending at 45/55 produces a combined score of `0.6209`, placing the text safely in the `0.40 – 0.65` "unsure" band rather than falsely accusing the writer of cheating.

---

## Label Variants

| Label | Score range | The exact text a reader sees |
|---|---|---|
| high-confidence human | 0.00 – 0.40 | Based on the provided text, this was most likely written by a person. |
| unsure | 0.40 – 0.65 | We could not determine with confidence whether this was written by a person or AI. |
| high-confidence AI | 0.65 – 1.00 | Based on the provided text, this was most likely written by AI. |

**Why I worded the "unsure" one this way:**
It frames the uncertainty as a limitation of the verification system ("We could not determine with confidence") rather than an accusation against the author. This ensures honest reporting without alienating human writers whose work happens to score in the middle.

---

## Sample Run

**A submission**

```bash
$ curl -X POST http://127.0.0.1:5000/submit \
  -H "Content-Type: application/json" \
  -d '{"text": "The implementation of the proposed framework requires careful consideration of several key factors. First, it is important to note that the system must be able to handle a wide variety of different inputs. Additionally, the overall performance of the solution depends on a number of important variables.", "creator_id": "author_bob"}'
```

```json
{
  "confidence": 0.6737,
  "content_id": "683a7ae4-cb94-4fdd-af54-d68210ad6efa",
  "guess": "ai",
  "label": "Based on the provided text, this was most likely written by AI.",
  "model_score": 0.8864,
  "style_score": 0.4997
}
```

**An appeal**

```bash
$ curl -X POST http://127.0.0.1:5000/appeal \
  -H "Content-Type: application/json" \
  -d '{"content_id": "683a7ae4-cb94-4fdd-af54-d68210ad6efa", "reasoning": "I wrote this paragraph using formal academic phrasing for my engineering paper."}'
```

```json
{
  "content_id": "683a7ae4-cb94-4fdd-af54-d68210ad6efa",
  "message": "Appeal received and status updated to under_review.",
  "ok": true,
  "status": "under_review"
}
```

**What the log shows afterwards**

```bash
$ curl "http://127.0.0.1:5000/log?limit=3"
```

```json
{
  "count": 3,
  "entries": [
    {
      "combined_score": 0.6737,
      "content_id": "683a7ae4-cb94-4fdd-af54-d68210ad6efa",
      "creator_id": "author_bob",
      "guess": "ai",
      "label": "Based on the provided text, this was most likely written by AI.",
      "model_score": 0.8864,
      "status": "decided",
      "style_score": 0.4997,
      "timestamp": "2026-11-09T22:35:24+00:00"
    },
    {
      "combined_score": 0.6209,
      "content_id": "88a0326e-9f73-48d7-a200-dec8a30d87b7",
      "creator_id": "author_charlie",
      "guess": "unsure",
      "label": "We could not determine with confidence whether this was written by a person or AI.",
      "model_score": 0.8296,
      "status": "decided",
      "style_score": 0.4502,
      "timestamp": "2026-11-09T22:35:24+00:00"
    },
    {
      "content_id": "683a7ae4-cb94-4fdd-af54-d68210ad6efa",
      "creator_id": "author_bob",
      "event": "appeal",
      "reasoning": "I wrote this paragraph using formal academic phrasing for my engineering paper.",
      "status": "under_review",
      "timestamp": "2026-11-09T22:35:24+00:00"
    }
  ]
}
```

---

## How I Used AI

**Moment 1**

- *What I asked for:* Feedback on my initial 3 acceptance criteria for Milestone 2 regarding score thresholds, gibberish handling, and restricting appeals on high AI scores.
- *What came back:* Detailed critique explaining that setting thresholds in code is an implementation rule rather than an observable performance target, that "gibberish" is subjective and unmeasurable, and that barring appeals on high AI scores harms falsely accused writers. The AI recommended a full set of 5 testable criteria covering false positives, score spread, label coverage, appeal reliability, and bad input handling.
- *What I changed:* I updated `criteria.md` to use all 5 measurable criteria, establishing a strict 10% false-positive limit on my own writing, a 0.35 score spread between human and AI text, reachability of all three labels, and graceful 400 Bad Request handling for malformed input.

**Moment 2**

- *What I asked for:* Assistance in implementing the Python features across `stylometry.py`, `scoring.py`, and `app.py`, specifically computing sentence length spread, type-token ratio, punctuation density, combining the signals with custom weights, and implementing the `/submit` and `/appeal` routes.
- *What came back:* Python code providing statistical calculation of sentence variation (coefficient of variation), vocabulary richness, normalized 0–1 style scoring, the combining rule in `scoring.py`, and Flask route handlers with input validation and audit logging.
- *What I changed:* Configured the exact weights (45% model, 55% style) and threshold cutoffs (0.40 to 0.65 for unsure) in `config.py`, customized the user-facing label text to match the requested template, and verified that edge cases return 400 Bad Request.

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** 10 per minute, 100 per day

**Why those numbers and not others:**
A legitimate human writer revising essays or drafts submits a few times per hour, and at most 5–10 times per minute during rapid iterative edits. Conversely, an adversarial probing script attempting to map score thresholds and evasion patterns sends dozens or hundreds of automated requests. Capping requests at 10 per minute and 100 per day accommodates real authors while stopping automated boundary-probing scripts.

**What a caller counts as:**
A caller counts as `creator_id` when provided as a valid non-empty string in the JSON payload, falling back to the remote client IP address (`get_remote_address()`). This prevents multiple independent writers on a shared network (like a household or campus) from exhausting each other's quota, while anonymous or malformed requests are bound to their IP address.

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```
200 200 200 200 200 200 200 200 200 200 429 429 429 429 429
```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->



**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json

```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:



---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

```json

```

**Diagnoses**

<!-- For each miss AND each broken attack: the stage and the mechanism.

     Your service has five stages: the route, signal one, signal two, the
     combining rule, and the label mapping.

     Not a diagnosis:  "The evasion attacks got through."
     A diagnosis:      "Four evasion inputs got through. All four had typos
                        added to AI-generated text. My second signal measures
                        word variety, and typos raise word variety — so it read
                        them as more human. My combining rule weights that
                        signal at 0.6, so it dragged the whole score down."

     Look for a pattern. Five failures on one signal is one problem, not five. -->



---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->



**Did it help, and how do I know:**

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->



---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->



**The trade I'd make if this ran for real:**

<!-- Two sentences. Fewer wrong accusations means more AI text getting through.
     Say which way you'd go and WHO PAYS FOR IT. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 7

       [ ] criteria.md has five numbered criteria, each naming a target
       [ ] Each has a reason underneath
       [ ] POST /submit returns content_id, guess, confidence, label,
           model_score and style_score
       [ ] Two signals that measure DIFFERENT things, each with a named blind spot
       [ ] Three label variants, all reachable, written out in full
       [ ] POST /appeal changes status and writes to the log
       [ ] Signals and Scoring names scoring.py::combine_signals
       [ ] Sample Run: a submission AND an appeal, as pasted text
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 8

       [ ] Rate limiting on /submit, with your numbers justified
       [ ] The pasted run of status codes showing 429
       [ ] Audit log with all nine fields, recording rejections too
       [ ] The attack set run IN FULL, every input with an outcome
       [ ] Ten audit log entries pasted as text
       [ ] Five criteria across three trials
       [ ] A diagnosis for every miss and every broken attack — stage AND mechanism
       [ ] One improvement, with Attack Run — After
       [ ] What's Still Broken, including the production trade
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
