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

**Moment 3**

- *What I asked for:* Assistance in setting up rate limiting and rejection audit logging, executing the full 56-attack red team test suite, automating three-trial evaluation runs in `run_eval.py`, diagnosing the pipeline mechanisms behind evasion and false-positive failures, and analyzing trade-offs between widening thresholds versus adjusting input validation.
- *What came back:* Structured testing workflows executing `run_attacks.py` and `run_eval.py`, root-cause analysis pinpointing how stylometric heuristics and model predictability collapsed score spreads and caused false positives on formal prose, and quantitative evaluation of widening `AI_THRESHOLD` to 0.67.
- *What I changed:* Enabled rate limiting at 10/min and 100/day with audit rejection logging, executed before-and-after attack runs, populated `scenarios.py` with 10 authentic author samples, diagnosed all five stages, raised `AI_THRESHOLD` to 0.67 to protect innocent human writers, and documented all findings and trade-offs.

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

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `33df15c7-8dc1-4c51-a9ef-39bd2e34e5d8` | human | 0.361 | BROKE |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `0ec67d69-d3eb-4717-a879-f3fdcc6746ec` | human | 0.345 | BROKE |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `d5ccec58-de56-4f07-9eef-fe641408f337` | unsure | 0.448 | BROKE |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `e82a0724-a95a-423e-b831-3109dd5a2100` | unsure | 0.549 | BROKE |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `bc83136b-e182-46b4-96a9-8f5d6eb804ce` | human | 0.216 | BROKE |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `cef9d6d8-c0ba-48df-925c-7df7d4532864` | human | 0.367 | BROKE |
| EV07 | evasion | signal two: padding with punctuation | 200 | `47e7e6a6-76bc-45d6-a5c6-e2c7da24cee2` | unsure | 0.551 | BROKE |
| EV08 | evasion | signal one: text below the token window | 200 | `6f244533-5f4c-469c-9eba-4d85ab8166a6` | human | 0.384 | BROKE |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `8759c07d-6823-4ff0-ae32-0814d582fa97` | unsure | 0.452 | BROKE |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `78b7e050-daf0-4e7a-8ec0-c587007c510f` | ai | 0.836 | HELD |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `bc8942ff-3671-418b-87b9-42434b0f2de4` | unsure | 0.512 | HELD |
| FP02 | false_positive | human writing in a formal register | 200 | `9692dc5d-3bc6-4eb0-a635-7a9c155e6598` | ai | 0.655 | BROKE |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `b2065942-ea42-4d32-b6c9-0a8749e8d282` | ai | 0.655 | BROKE |
| FP04 | false_positive | a student essay written to a rubric | 200 | `d39d25e4-b2a4-4a71-ac55-31fa38899819` | unsure | 0.605 | HELD |
| FP05 | false_positive | technical documentation written by a person | 200 | `16496eef-8cdb-4b3e-ac14-672dce6fea9b` | ai | 0.717 | BROKE |
| FP06 | false_positive | a person imitating a formal template | 200 | `2d94151f-5ebe-469f-b124-23a951a5603f` | unsure | 0.597 | HELD |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `41f1207b-26b9-4a5a-8d94-3e0499ce086d` | unsure | 0.643 | HELD |
| FP08 | false_positive | very short genuine human submission | 200 | `feee0c71-d107-4f87-9437-94690d314d7b` | human | 0.360 | HELD |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `44b6cca4-aa8a-45a1-b600-fb018a69ed95` | human | 0.333 | HELD |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `67d109fa-7b04-408f-9669-b2be63e5d676` | human | 0.188 | HELD |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `9faa3c1a-31c9-40f6-922e-8b402a0b5d83` | unsure | 0.478 | HELD |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `67631e91-97ea-4775-a782-ea7a8c908fe2` | human | 0.368 | HELD |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `a91a5b24-0451-462a-bace-4a040c4e1156` | human | 0.378 | HELD |
| PI06 | prompt_injection | instruction plus real human text | 200 | `96251dc3-a45d-4a82-a60f-cd3abed4962e` | unsure | 0.492 | HELD |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — | HELD |
| MF02 | malformed | text is a single character | 400 | `—` | — | — | HELD |
| MF03 | malformed | text is control characters | 200 | `b839141b-1e4e-41d0-a095-63c5ca4513d3` | human | 0.275 | BROKE |
| MF04 | malformed | text is only punctuation | 200 | `a2a7ad99-9850-4a50-8cb4-ef6a5a2e30b0` | human | 0.280 | BROKE |
| MF05 | malformed | text is a very long single word | 200 | `232d3788-7111-42eb-8fd3-5892c5aac510` | ai | 0.724 | BROKE |
| MF06 | malformed | text is emoji only | 200 | `09e37341-3bb7-495e-8274-f7dbf5f465c2` | ai | 0.724 | BROKE |
| MF07 | malformed | text is right-to-left script | 200 | `5d6d0e31-2dab-47e0-80a3-088d04cf60c5` | ai | 0.683 | HELD |
| MF08 | malformed | text is 60,000 characters | 200 | `bd590e31-d93a-4dd6-af93-5795f0655f8a` | ai | 0.812 | HELD |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — | HELD |
| RQ02 | malformed | no creator_id | 400 | `—` | — | — | HELD |
| RQ03 | malformed | text is a number | 400 | `—` | — | — | HELD |
| RQ04 | malformed | text is a list | 400 | `—` | — | — | HELD |
| RQ05 | malformed | text is null | 400 | `—` | — | — | HELD |
| RQ06 | malformed | creator_id is an object | 400 | `—` | — | — | HELD |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — | HELD |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — | HELD |
| RQ09 | malformed | body is empty | 400 | `—` | — | — | HELD |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — | HELD |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | `—` | — | — | HELD |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — | HELD |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `2736840f-fff8-4e40-895a-d8af42316614` | human | 0.398 | HELD |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `2608c49c-ce61-483d-b03d-855a9ea8db17` | human | 0.398 | HELD |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `06d9ecc3-5641-4109-a33b-ad70b16d0cb2` | human | 0.398 | HELD |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `ac74896c-7c08-49f8-bd68-7cd0096585ca` | human | 0.398 | HELD |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `58e0f28c-474f-4e60-8f91-977f44c45695` | human | 0.398 | HELD |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `bc8aa6de-f6c1-44fe-8d60-7a14fa3eb601` | human | 0.398 | HELD |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c5388bf1-b184-4a88-adbf-449053ecf22a` | human | 0.398 | HELD |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `15dbb70e-f352-4704-bb94-a61d4856044f` | human | 0.398 | HELD |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `67d3f576-cfaf-47f5-8a8a-accf9c376512` | human | 0.398 | HELD |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `f5bfe06a-502f-4dfd-804b-7edaec72e7e4` | human | 0.398 | HELD |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |

**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json
[
  {
    "timestamp": "2026-11-12T00:49:39+00:00",
    "content_id": "9692dc5d-3bc6-4eb0-a635-7a9c155e6598",
    "creator_id": "attacker_FP02",
    "guess": "ai",
    "model_score": 0.7387,
    "style_score": 0.5875,
    "combined_score": 0.6555,
    "label": "Based on the provided text, this was most likely written by AI.",
    "status": "decided"
  },
  {
    "timestamp": "2026-11-12T00:49:40+00:00",
    "content_id": "b2065942-ea42-4d32-b6c9-0a8749e8d282",
    "creator_id": "attacker_FP03",
    "guess": "ai",
    "model_score": 0.8051,
    "style_score": 0.5317,
    "combined_score": 0.6547,
    "label": "Based on the provided text, this was most likely written by AI.",
    "status": "decided"
  },
  {
    "timestamp": "2026-11-12T00:49:40+00:00",
    "content_id": "16496eef-8cdb-4b3e-ac14-672dce6fea9b",
    "creator_id": "attacker_FP05",
    "guess": "ai",
    "model_score": 0.8005,
    "style_score": 0.6478,
    "combined_score": 0.7165,
    "label": "Based on the provided text, this was most likely written by AI.",
    "status": "decided"
  },
  {
    "timestamp": "2026-11-12T00:49:37+00:00",
    "content_id": "33df15c7-8dc1-4c51-a9ef-39bd2e34e5d8",
    "creator_id": "attacker_EV01",
    "guess": "human",
    "model_score": 0.1635,
    "style_score": 0.5224,
    "combined_score": 0.3609,
    "label": "Based on the provided text, this was most likely written by a person.",
    "status": "decided"
  },
  {
    "timestamp": "2026-11-12T00:49:37+00:00",
    "content_id": "0ec67d69-d3eb-4717-a879-f3fdcc6746ec",
    "creator_id": "attacker_EV02",
    "guess": "human",
    "model_score": 0.5943,
    "style_score": 0.1413,
    "combined_score": 0.3452,
    "label": "Based on the provided text, this was most likely written by a person.",
    "status": "decided"
  },
  {
    "timestamp": "2026-11-12T00:49:38+00:00",
    "content_id": "cef9d6d8-c0ba-48df-925c-7df7d4532864",
    "creator_id": "attacker_EV06",
    "guess": "human",
    "model_score": 0.5727,
    "style_score": 0.1994,
    "combined_score": 0.3674,
    "label": "Based on the provided text, this was most likely written by a person.",
    "status": "decided"
  },
  {
    "timestamp": "2026-11-12T00:49:44+00:00",
    "content_id": "b839141b-1e4e-41d0-a095-63c5ca4513d3",
    "creator_id": "attacker_MF03",
    "guess": "human",
    "model_score": 0.0,
    "style_score": 0.5,
    "combined_score": 0.275,
    "label": "Based on the provided text, this was most likely written by a person.",
    "status": "decided"
  },
  {
    "timestamp": "2026-11-12T00:49:39+00:00",
    "content_id": "78b7e050-daf0-4e7a-8ec0-c587007c510f",
    "creator_id": "attacker_EV10",
    "guess": "ai",
    "model_score": 0.9792,
    "style_score": 0.7186,
    "combined_score": 0.8359,
    "label": "Based on the provided text, this was most likely written by AI.",
    "status": "decided"
  },
  {
    "timestamp": "2026-11-12T00:43:24+00:00",
    "creator_id": "test_bad",
    "event": "rejected",
    "status": "rejected",
    "reason": "empty_or_non_string_text"
  },
  {
    "timestamp": "2026-11-12T00:43:54+00:00",
    "creator_id": "flood_tester",
    "event": "rejected",
    "status": "rejected",
    "reason": "rate_limited",
    "limit": "10 per 1 minute"
  }
]
```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:

The worst failure was **FP03** (`attacker_FP03`), which submitted writing from a non-native English speaker writing carefully. The system assigned a combined score of `0.6547` (with `model_score = 0.8051` and `style_score = 0.5317`), crossing our `0.65` threshold and returning: "Based on the provided text, this was most likely written by AI."

Explaining this to an authentic writer who took great care to write clear, grammatically conventional sentences would be indefensible: they were accused of dishonesty simply because their straightforward vocabulary looked predictable to GPT-2, and their structured punctuation produced average stylometric variance.



---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. My own writing flagged as AI | ≤ 1 of 10 | 0/10 | 0/10 | 0/10 | MET |
| 2. Score spread between AI and human | ≥ 0.35 | 0.1207 | 0.1207 | 0.1207 | MISSED |
| 3. All three labels reachable | 3 of 3 | 3/3 | 3/3 | 3/3 | MET |
| 4. Appeal updates status to under_review | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 5. Malformed requests return 400 Bad Request | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

Produced by `run_eval.py::main`:

```json
{
  "criterion_1_my_own_writing": [
    {
      "status": 200,
      "guess": "unsure",
      "confidence": 0.4794,
      "model_score": 0.5332,
      "style_score": 0.4353,
      "label": "We could not determine with confidence whether this was written by a person or AI.",
      "sent": "Social responsibility should be an important consideration to business"
    },
    {
      "status": 200,
      "guess": "human",
      "confidence": 0.3996,
      "model_score": 0.5199,
      "style_score": 0.3011,
      "label": "Based on the provided text, this was most likely written by a person.",
      "sent": "John Lewis and the large number of people who committed sit-ins displa"
    },
    {
      "status": 200,
      "guess": "unsure",
      "confidence": 0.4666,
      "model_score": 0.6196,
      "style_score": 0.3414,
      "label": "We could not determine with confidence whether this was written by a person or AI.",
      "sent": "In the 1900s, a patient\u2019s pain wasn\u2019t given much thought to. Doctors p"
    },
    {
      "status": 200,
      "guess": "unsure",
      "confidence": 0.4758,
      "model_score": 0.8381,
      "style_score": 0.1793,
      "label": "We could not determine with confidence whether this was written by a person or AI.",
      "sent": "Bacteria are one of the three domains of life. They play a key role in"
    },
    {
      "status": 200,
      "guess": "unsure",
      "confidence": 0.5696,
      "model_score": 0.7097,
      "style_score": 0.4549,
      "label": "We could not determine with confidence whether this was written by a person or AI.",
      "sent": "I would gather up as much evidence to show that I did not go through w"
    },
    {
      "status": 200,
      "guess": "unsure",
      "confidence": 0.5138,
      "model_score": 0.4824,
      "style_score": 0.5394,
      "label": "We could not determine with confidence whether this was written by a person or AI.",
      "sent": "It\u2019s morning and I\u2019m helping set up stock for the day. I hear the mark"
    },
    {
      "status": 200,
      "guess": "unsure",
      "confidence": 0.4239,
      "model_score": 0.5826,
      "style_score": 0.294,
      "label": "We could not determine with confidence whether this was written by a person or AI.",
      "sent": "Three days. That\u2019s the absurd amount of time I spent attempting to bui"
    },
    {
      "status": 200,
      "guess": "unsure",
      "confidence": 0.5892,
      "model_score": 0.5226,
      "style_score": 0.6437,
      "label": "We could not determine with confidence whether this was written by a person or AI.",
      "sent": "The physical transition is when he leaves his home to go live with unc"
    },
    {
      "status": 200,
      "guess": "unsure",
      "confidence": 0.5043,
      "model_score": 0.3259,
      "style_score": 0.6502,
      "label": "We could not determine with confidence whether this was written by a person or AI.",
      "sent": "I think the line Samuel 16:12 (KJV) becomes distorted into showing Dav"
    },
    {
      "status": 200,
      "guess": "unsure",
      "confidence": 0.5128,
      "model_score": 0.4971,
      "style_score": 0.5256,
      "label": "We could not determine with confidence whether this was written by a person or AI.",
      "sent": "The colosseum was packed to the brink. Spectators cheered as the first"
    }
  ],
  "criterion_2_score_spread": [
    {
      "status": 200,
      "guess": "unsure",
      "confidence": 0.5309,
      "model_score": 0.5869,
      "style_score": 0.485,
      "label": "We could not determine with confidence whether this was written by a person or AI.",
      "sent": "Artificial intelligence is transforming modern society across various "
    },
    {
      "status": 200,
      "guess": "unsure",
      "confidence": 0.5241,
      "model_score": 0.5592,
      "style_score": 0.4953,
      "label": "We could not determine with confidence whether this was written by a person or AI.",
      "sent": "In today's digital landscape, effective communication plays a crucial "
    },
    {
      "status": 200,
      "guess": "unsure",
      "confidence": 0.6173,
      "model_score": 0.7138,
      "style_score": 0.5384,
      "label": "We could not determine with confidence whether this was written by a person or AI.",
      "sent": "The implementation of sustainable energy systems represents a fundamen"
    },
    {
      "status": 200,
      "guess": "unsure",
      "confidence": 0.5406,
      "model_score": 0.5279,
      "style_score": 0.5509,
      "label": "We could not determine with confidence whether this was written by a person or AI.",
      "sent": "Data analysis has become an indispensable component of contemporary de"
    },
    {
      "status": 200,
      "guess": "unsure",
      "confidence": 0.4993,
      "model_score": 0.5112,
      "style_score": 0.4896,
      "label": "We could not determine with confidence whether this was written by a person or AI.",
      "sent": "Urban planning in modern metropolitan regions necessitates balanced ap"
    },
    {
      "status": 200,
      "guess": "unsure",
      "confidence": 0.4483,
      "model_score": 0.4873,
      "style_score": 0.4164,
      "label": "We could not determine with confidence whether this was written by a person or AI.",
      "sent": "It\u2019s morning and I\u2019m helping set up stock for the day. I hear the mark"
    },
    {
      "status": 200,
      "guess": "human",
      "confidence": 0.3303,
      "model_score": 0.5874,
      "style_score": 0.12,
      "label": "Based on the provided text, this was most likely written by a person.",
      "sent": "Three days. That\u2019s the absurd amount of time I spent attempting to bui"
    },
    {
      "status": 200,
      "guess": "unsure",
      "confidence": 0.4556,
      "model_score": 0.4244,
      "style_score": 0.4811,
      "label": "We could not determine with confidence whether this was written by a person or AI.",
      "sent": "The colosseum was packed to the brink. Spectators cheered as the first"
    },
    {
      "status": 200,
      "guess": "unsure",
      "confidence": 0.5875,
      "model_score": 0.5606,
      "style_score": 0.6095,
      "label": "We could not determine with confidence whether this was written by a person or AI.",
      "sent": "I was walking down the gravel road behind the old barn when the storm "
    },
    {
      "status": 200,
      "guess": "human",
      "confidence": 0.2869,
      "model_score": 0.4432,
      "style_score": 0.159,
      "label": "Based on the provided text, this was most likely written by a person.",
      "sent": "My grandmother always kept an old rusted biscuit tin on the top shelf "
    }
  ],
  "criterion_3_label_coverage": [
    {
      "status": 200,
      "guess": "human",
      "confidence": 0.3563,
      "model_score": 0.5064,
      "style_score": 0.2335,
      "label": "Based on the provided text, this was most likely written by a person.",
      "sent": "John Lewis and the large number of people who committed sit-ins displa"
    },
    {
      "status": 200,
      "guess": "unsure",
      "confidence": 0.4771,
      "model_score": 0.5314,
      "style_score": 0.4327,
      "label": "We could not determine with confidence whether this was written by a person or AI.",
      "sent": "Social responsibility should be an important consideration to business"
    },
    {
      "status": 200,
      "guess": "ai",
      "confidence": 0.6737,
      "model_score": 0.8864,
      "style_score": 0.4997,
      "label": "Based on the provided text, this was most likely written by AI.",
      "sent": "The implementation of the proposed framework requires careful consider"
    }
  ],
  "criterion_4_appeal_path": [
    {
      "status": 200,
      "content_id": "a32ed18e-e37b-4edd-bc8f-de1cec9cbff4",
      "appeal_status": "under_review",
      "ok": true,
      "message": "Appeal received and status updated to under_review.",
      "sent": "appeal: I drafted this historical overview myself using primary sour"
    },
    {
      "status": 200,
      "content_id": "36cbbe78-033f-4276-8c3c-e1b443154a1c",
      "appeal_status": "under_review",
      "ok": true,
      "message": "Appeal received and status updated to under_review.",
      "sent": "appeal: I authored this technical explanation for my team's document"
    },
    {
      "status": 200,
      "content_id": "07022c66-8d74-41dd-a453-b345920f3755",
      "appeal_status": "under_review",
      "ok": true,
      "message": "Appeal received and status updated to under_review.",
      "sent": "appeal: This is a creative personal memoir recounting my own family "
    },
    {
      "status": 200,
      "content_id": "5000d176-b17d-45c8-b8df-820cfaccc102",
      "appeal_status": "under_review",
      "ok": true,
      "message": "Appeal received and status updated to under_review.",
      "sent": "appeal: This analysis was composed independently for a university li"
    },
    {
      "status": 200,
      "content_id": "808ff789-ef36-4695-b22a-d56e59c9dc80",
      "appeal_status": "under_review",
      "ok": true,
      "message": "Appeal received and status updated to under_review.",
      "sent": "appeal: I wrote this reflection based on corporate ethics case studi"
    }
  ],
  "criterion_5_bad_input": [
    {
      "status": 400,
      "guess": null,
      "confidence": null,
      "model_score": null,
      "style_score": null,
      "label": null,
      "sent": "(empty text)"
    },
    {
      "status": 400,
      "guess": null,
      "confidence": null,
      "model_score": null,
      "style_score": null,
      "label": null,
      "sent": "{\"creator_id\": \"eval_bad_missing\"}"
    },
    {
      "status": 400,
      "guess": null,
      "confidence": null,
      "model_score": null,
      "style_score": null,
      "label": null,
      "sent": "{\"text\": null, \"creator_id\": \"eval_bad_null\"}"
    },
    {
      "status": 400,
      "guess": null,
      "confidence": null,
      "model_score": null,
      "style_score": null,
      "label": null,
      "sent": "word word word word word word word word word word word word word word "
    },
    {
      "status": 400,
      "guess": null,
      "confidence": null,
      "model_score": null,
      "style_score": null,
      "label": null,
      "sent": "   \n\t  "
    }
  ]
}
```

**Diagnoses**

### Criteria Misses

#### Criterion 2: Score Spread Collapsed (Target: ≥ 0.35, Actual: 0.1207 across all 3 trials) — MISSED
- **Stage:** Combining rule (`scoring.py::combine_signals`) and Signal 2 (`stylometry.py`).
- **Mechanism:** Stylometry was weighted at 55% (`WEIGHT_STYLE_SIGNAL = 0.55`). For standard narrative and explanatory prose, stylometric indicators (sentence length variation, punctuation density, type-token ratio) cluster tightly in the 0.30–0.55 range for both human and AI text. Simultaneously, GPT-2 token perplexity (`model_score`) for fluent modern AI text produced scores around 0.55–0.72 rather than reaching near 1.0. Blending these signals with a 45/55 linear average compressed the overall score distribution into a narrow mid-tier band (0.35–0.65). Consequently, the AI average (0.5424) and human average (0.4217) separated by only 0.1207, falling well short of the 0.35 target.

---

### Broken Attacks by Stage and Mechanism

#### 1. False Positives: `FP02`, `FP03`, `FP05` Flagged as High-Confidence AI
- **Stage:** Label mapping (`config.py::AI_THRESHOLD`) and Signal 1 (`detector.py`).
- **Mechanism:** Formal human prose (`FP02`, score 0.6555), careful non-native English writing (`FP03`, score 0.6547), and technical documentation (`FP05`, score 0.7165) all exhibited high model predictability (`model_score = 0.74` to `0.81`). GPT-2 assigns low perplexity to standard grammatical syntax and common technical vocabulary. Because `AI_THRESHOLD` was set at `0.65`, `FP02` and `FP03` crossed the cutoff by less than 0.006, falsely labeling real human writing as AI-generated.

#### 2. Evasions: `EV01`–`EV09` Escaped Detection
- **Stage:** Signal 2 (`stylometry.py`) and Combining rule (`scoring.py`).
- **Mechanism:**
  - In `EV01`, injected typos inflated unique word counts (type-token ratio), causing Signal 2 to interpret misspelled tokens as rich human vocabulary (`style_score = 0.5224`), which pulled the combined score to 0.3609 (`human`).
  - In `EV02` and `EV06`, artificially breaking sentences or combining one very long sentence with one very short sentence artificially inflated sentence length variance. Signal 2 generated very low style scores (`0.1413` and `0.1994`). Because Signal 2 carries 55% weight, this dragged the combined score directly into the `human` band (`0.345` and `0.367`).
  - In `EV03`, `EV04`, `EV07`, and `EV09`, inserting quotations, rare words, excessive punctuation, or a human opening paragraph raised perplexity and stylometric spread just enough to land in the 0.44–0.55 `unsure` band.
  - **Pattern:** Signal 2 is vulnerable to superficial text formatting hacks (typos, sentence fragmentation, punctuation padding) that attackers use to spoof human stylometric variation without affecting AI semantics.

#### 3. Malformed Inputs: `MF03`, `MF04`, `MF05`, `MF06` Accepted as 200 OK
- **Stage:** Route input validation (`app.py::submit`).
- **Mechanism:** Input guards only verified that `text` was a non-empty string under 50,000 words. `MF03` (control characters) and `MF04` (punctuation-only text) satisfied the non-empty check despite containing zero human words. GPT-2 returned a default score of 0.0 or minimal perplexity, and stylometry defaulted to 0.5, classifying non-text junk as `human` (scores 0.275 and 0.280) rather than rejecting it with an HTTP 400 Bad Request. Similarly, `MF05` (a single massive word) and `MF06` (emoji-only text) proceeded through the scoring pipeline instead of being caught as invalid prose.



---

## The Improvement

**What I changed:**
Raised `AI_THRESHOLD` from `0.65` to `0.67` in `config.py`, widening the `unsure` band from `0.40 – 0.65` to `0.40 – 0.67`.

**Which diagnosis pointed at it:**
The false-positive diagnosis on attacks `FP02` (formal human writing, score `0.6555`) and `FP03` (careful non-native English writing, score `0.6547`). Both authentic human submissions had narrowly crossed the original `0.65` threshold by less than `0.006`, triggering false accusations of AI generation.

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `ab2ea1e2-f917-4fc3-8361-711b4359b08e` | human | 0.361 | BROKE |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `3b9122fb-2518-4778-aaa2-4c5dafd83b50` | human | 0.345 | BROKE |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `20bc8b30-b033-4bcd-8333-f693d7fc76d7` | unsure | 0.448 | BROKE |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `1c2d2063-bfd6-46be-b6c5-d0b9bc0db477` | unsure | 0.549 | BROKE |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `85d0dc9c-3971-4c01-b1d4-c196fd516520` | human | 0.216 | BROKE |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `d30c932c-932e-4737-9c1a-68265cc0d54e` | human | 0.367 | BROKE |
| EV07 | evasion | signal two: padding with punctuation | 200 | `ad0a1247-ac58-4489-88ae-51b3a7f3d916` | unsure | 0.551 | BROKE |
| EV08 | evasion | signal one: text below the token window | 200 | `63be6461-a9c2-465a-a402-e4a1fdfce83c` | human | 0.384 | BROKE |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `cb7b8d4c-819f-4e5a-af95-d2787b1677ce` | unsure | 0.452 | BROKE |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `d9ec6327-d3af-4308-aa67-9ddbc5a583b7` | ai | 0.836 | HELD |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `7d14f48e-2b3d-4d35-a81a-e0caf5f65bf1` | unsure | 0.512 | HELD |
| FP02 | false_positive | human writing in a formal register | 200 | `7db7e1d4-8501-4f93-8f5b-f5afa0412862` | unsure | 0.655 | HELD |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `c0fac72c-27ca-42d9-ae92-3ab33cbb6e8a` | unsure | 0.655 | HELD |
| FP04 | false_positive | a student essay written to a rubric | 200 | `b5bb65ed-2642-4e60-8616-da73f86434ff` | unsure | 0.605 | HELD |
| FP05 | false_positive | technical documentation written by a person | 200 | `5a291f3a-e56f-4448-9840-9c97af1dfc1b` | ai | 0.717 | BROKE |
| FP06 | false_positive | a person imitating a formal template | 200 | `e038707b-19b9-4bbf-99e0-269b94b9c99e` | unsure | 0.597 | HELD |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `19892020-9232-4379-a472-1a555ea6caa9` | unsure | 0.643 | HELD |
| FP08 | false_positive | very short genuine human submission | 200 | `de03cd2d-10db-47e3-a194-3f2b733fa9f1` | human | 0.360 | HELD |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `0d9ebe66-d4ef-49b3-b0cb-02508f789174` | human | 0.333 | HELD |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `ae00c731-36f2-4ae6-a51a-dc4a1e631121` | human | 0.188 | HELD |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `4fb724b2-3e14-4ede-b702-cb66c533cf91` | unsure | 0.478 | HELD |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `250a7ba8-a68f-4f67-9018-aa8f9f4b2aa1` | human | 0.368 | HELD |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `f4288813-b0d0-4ab7-97bb-cedb24e3180b` | human | 0.378 | HELD |
| PI06 | prompt_injection | instruction plus real human text | 200 | `e11aebc0-193c-4a92-9383-64a2532c9657` | unsure | 0.492 | HELD |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — | HELD |
| MF02 | malformed | text is a single character | 400 | `—` | — | — | HELD |
| MF03 | malformed | text is control characters | 200 | `87ed6ae0-d2cd-41c7-a9c8-9498ebb40719` | human | 0.275 | BROKE |
| MF04 | malformed | text is only punctuation | 200 | `baaa197c-cc21-4dc3-a8d7-5498e472f2a5` | human | 0.280 | BROKE |
| MF05 | malformed | text is a very long single word | 200 | `4df94c2f-e742-4a98-a4be-2a16fe087a8e` | ai | 0.724 | BROKE |
| MF06 | malformed | text is emoji only | 200 | `6106e5fa-0de0-4d99-b51e-9b12d5339325` | ai | 0.724 | BROKE |
| MF07 | malformed | text is right-to-left script | 200 | `c4f2cd42-35d9-417f-9022-3bdf2bbdde63` | ai | 0.683 | HELD |
| MF08 | malformed | text is 60,000 characters | 200 | `248a155f-539d-4282-84be-4653106860f9` | ai | 0.812 | HELD |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — | HELD |
| RQ02 | malformed | no creator_id | 400 | `—` | — | — | HELD |
| RQ03 | malformed | text is a number | 400 | `—` | — | — | HELD |
| RQ04 | malformed | text is a list | 400 | `—` | — | — | HELD |
| RQ05 | malformed | text is null | 400 | `—` | — | — | HELD |
| RQ06 | malformed | creator_id is an object | 400 | `—` | — | — | HELD |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — | HELD |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — | HELD |
| RQ09 | malformed | body is empty | 400 | `—` | — | — | HELD |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — | HELD |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | `—` | — | — | HELD |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — | HELD |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `622936a8-72d8-42c9-80d0-0102d1bd9cf9` | human | 0.398 | HELD |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `296b8f8a-4cb5-4df7-bf14-c3ff11df42c9` | human | 0.398 | HELD |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `230349b2-9347-42a8-a5eb-9dfbdae3ef16` | human | 0.398 | HELD |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `aef04e0b-a45f-4bdd-91e8-9d44fa75ae47` | human | 0.398 | HELD |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `e59e6b9a-7b8d-4f1a-88d3-b282da39231c` | human | 0.398 | HELD |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `6295a41c-50b8-4e34-bb14-e8641905f9dc` | human | 0.398 | HELD |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `b7bc6c9f-591e-41b4-8de3-f44245fac816` | human | 0.398 | HELD |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `32ccb8c8-8987-4225-b73e-0bc5e01d5384` | human | 0.398 | HELD |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `064dbde2-e2e4-4a44-8b9a-210317ecef0d` | human | 0.398 | HELD |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `ec416e59-8cae-49ba-802b-6fedeb6c7fc8` | human | 0.398 | HELD |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |

**Did it help, and how do I know:**
Yes, it helped where it mattered most: protecting real writers. In the initial attack run, both `FP02` and `FP03` were mislabeled as `high-confidence AI` (BROKE). After raising `AI_THRESHOLD` to `0.67`, both fell safely into the `unsure` band (scores `0.655` < `0.67`), converting both outcomes to HELD. Crucially, high-confidence AI text like `EV10` (`0.836`) still cleared the threshold and was flagged as AI (HELD), and Criterion 3 confirmed all three labels remained reachable (3 of 3). The trade-off is that any borderline AI text scoring between 0.65 and 0.67 now lands in `unsure` rather than being caught outright.



---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->

### Remaining Attacks Still Getting Through
1. **Technical Documentation False Positive (`FP05`):**
   - *Status:* Human-written technical documentation scored `0.7165`, remaining above the `0.67` threshold and misclassified as AI.
   - *What I'd do:* Implement domain-aware preprocessing or custom thresholding for technical/academic text, which naturally exhibits lower perplexity and rigid terminology.
   - *Why I stopped:* Raising `AI_THRESHOLD` beyond 0.72 would cause virtually all conversational AI text to escape into the unsure band, neutralizing the detector without training a domain-specific model.

2. **Adversarial Evasions (`EV01`–`EV09`):**
   - *Status:* AI text with injected typos, manipulated sentence length variance, quotation padding, or prepended human introductions still evade classification as `ai`, landing in `human` or `unsure`.
   - *What I'd do:* Add an input-sanitization step that spell-checks and normalizes typos before stylometric analysis, combined with sliding-window chunk evaluation to prevent human introductory paragraphs from masking trailing AI content.
   - *Why I stopped:* Course guidelines restrict Unit 8 to a single measured improvement to isolate causal variables.

3. **Non-Prose Malformed Payloads (`MF03`, `MF04`, `MF05`, `MF06`):**
   - *Status:* Control characters (`MF03`) and punctuation-only strings (`MF04`) return 200 OK and score as `human` (scores `0.275` and `0.280`), while giant single words (`MF05`) and emoji-only text (`MF06`) score as `ai`.
   - *What I'd do:* Add regex-based token validation in `app.py::submit` to reject any payload lacking at least three standard natural language words with HTTP 400 Bad Request.
   - *Why I stopped:* Prioritized fixing false accusations against real human authors (`FP02`, `FP03`) as the single allowed change.

### Remaining Criteria Missed
1. **Criterion 2 (Score Spread Between AI and Human Text):**
   - *Status:* Average AI score (`0.5424`) and human score (`0.4217`) differed by only `0.1207`, missing the `≥ 0.35` target.
   - *What I'd do:* Replace the raw linear weighting in `scoring.py::combine_signals` with non-linear sigmoid score scaling and rebalance feature weights so model and stylometry distributions amplify score divergence on clear-cut samples.
   - *Why I stopped:* Adhered to the single-change rule for Milestone 5.

**The trade I'd make if this ran for real:**

In production, I would prioritize writer protection by keeping false-positive accusations as close to zero as possible, aggressively expanding the "unsure" band and routing flagged drafts to human reviewers. The platform pays for this trade by accepting increased human moderation overhead and acknowledging that subtle AI assistance will occasionally go unflagged, which is far better than wrongly accusing and permanently alienating honest creators.



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
