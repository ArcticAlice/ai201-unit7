# Attack run — before

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-11 19:49
- Auto-marked BROKE (5xx, crash, no response): **0**
- Left for you to judge: **56**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

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

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 0 | 20 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "33df15c7-8dc1-4c51-a9ef-39bd2e34e5d8",
  "creator_id": "attacker_EV01",
  "guess": "human",
  "confidence": 0.3609,
  "model_score": 0.1635,
  "style_score": 0.5224,
  "label": "Based on the provided text, this was most likely written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "0ec67d69-d3eb-4717-a879-f3fdcc6746ec",
  "creator_id": "attacker_EV02",
  "guess": "human",
  "confidence": 0.3452,
  "model_score": 0.5943,
  "style_score": 0.1413,
  "label": "Based on the provided text, this was most likely written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "d5ccec58-de56-4f07-9eef-fe641408f337",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.4483,
  "model_score": 0.6662,
  "style_score": 0.2701,
  "label": "We could not determine with confidence whether this was written by a person or AI.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "e82a0724-a95a-423e-b831-3109dd5a2100",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.5491,
  "model_score": 0.6114,
  "style_score": 0.4982,
  "label": "We could not determine with confidence whether this was written by a person or AI.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "bc83136b-e182-46b4-96a9-8f5d6eb804ce",
  "creator_id": "attacker_EV05",
  "guess": "human",
  "confidence": 0.2165,
  "model_score": 0.3212,
  "style_score": 0.1309,
  "label": "Based on the provided text, this was most likely written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "cef9d6d8-c0ba-48df-925c-7df7d4532864",
  "creator_id": "attacker_EV06",
  "guess": "human",
  "confidence": 0.3674,
  "model_score": 0.5727,
  "style_score": 0.1994,
  "label": "Based on the provided text, this was most likely written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "47e7e6a6-76bc-45d6-a5c6-e2c7da24cee2",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.5514,
  "model_score": 0.5862,
  "style_score": 0.523,
  "label": "We could not determine with confidence whether this was written by a person or AI.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "6f244533-5f4c-469c-9eba-4d85ab8166a6",
  "creator_id": "attacker_EV08",
  "guess": "human",
  "confidence": 0.3842,
  "model_score": 0.2452,
  "style_score": 0.498,
  "label": "Based on the provided text, this was most likely written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "8759c07d-6823-4ff0-ae32-0814d582fa97",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.4521,
  "model_score": 0.7042,
  "style_score": 0.2459,
  "label": "We could not determine with confidence whether this was written by a person or AI.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "78b7e050-daf0-4e7a-8ec0-c587007c510f",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.8359,
  "model_score": 0.9792,
  "style_score": 0.7186,
  "label": "Based on the provided text, this was most likely written by AI.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "bc8942ff-3671-418b-87b9-42434b0f2de4",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.512,
  "model_score": 0.6175,
  "style_score": 0.4256,
  "label": "We could not determine with confidence whether this was written by a person or AI.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "9692dc5d-3bc6-4eb0-a635-7a9c155e6598",
  "creator_id": "attacker_FP02",
  "guess": "ai",
  "confidence": 0.6555,
  "model_score": 0.7387,
  "style_score": 0.5875,
  "label": "Based on the provided text, this was most likely written by AI.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "b2065942-ea42-4d32-b6c9-0a8749e8d282",
  "creator_id": "attacker_FP03",
  "guess": "ai",
  "confidence": 0.6547,
  "model_score": 0.8051,
  "style_score": 0.5317,
  "label": "Based on the provided text, this was most likely written by AI.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "d39d25e4-b2a4-4a71-ac55-31fa38899819",
  "creator_id": "attacker_FP04",
  "guess": "unsure",
  "confidence": 0.605,
  "model_score": 0.8329,
  "style_score": 0.4185,
  "label": "We could not determine with confidence whether this was written by a person or AI.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "16496eef-8cdb-4b3e-ac14-672dce6fea9b",
  "creator_id": "attacker_FP05",
  "guess": "ai",
  "confidence": 0.7165,
  "model_score": 0.8005,
  "style_score": 0.6478,
  "label": "Based on the provided text, this was most likely written by AI.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "2d94151f-5ebe-469f-b124-23a951a5603f",
  "creator_id": "attacker_FP06",
  "guess": "unsure",
  "confidence": 0.5972,
  "model_score": 0.8814,
  "style_score": 0.3646,
  "label": "We could not determine with confidence whether this was written by a person or AI.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "41f1207b-26b9-4a5a-8d94-3e0499ce086d",
  "creator_id": "attacker_FP07",
  "guess": "unsure",
  "confidence": 0.6433,
  "model_score": 0.8816,
  "style_score": 0.4483,
  "label": "We could not determine with confidence whether this was written by a person or AI.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "feee0c71-d107-4f87-9437-94690d314d7b",
  "creator_id": "attacker_FP08",
  "guess": "human",
  "confidence": 0.3599,
  "model_score": 0.3223,
  "style_score": 0.3907,
  "label": "Based on the provided text, this was most likely written by a person.",
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "44b6cca4-aa8a-45a1-b600-fb018a69ed95",
  "creator_id": "attacker_PI01",
  "guess": "human",
  "confidence": 0.3328,
  "model_score": 0.4625,
  "style_score": 0.2266,
  "label": "Based on the provided text, this was most likely written by a person.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "67d109fa-7b04-408f-9669-b2be63e5d676",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.1883,
  "model_score": 0.2044,
  "style_score": 0.1752,
  "label": "Based on the provided text, this was most likely written by a person.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "9faa3c1a-31c9-40f6-922e-8b402a0b5d83",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.4777,
  "model_score": 0.5943,
  "style_score": 0.3823,
  "label": "We could not determine with confidence whether this was written by a person or AI.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "67631e91-97ea-4775-a782-ea7a8c908fe2",
  "creator_id": "attacker_PI04",
  "guess": "human",
  "confidence": 0.3678,
  "model_score": 0.4998,
  "style_score": 0.2598,
  "label": "Based on the provided text, this was most likely written by a person.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "a91a5b24-0451-462a-bace-4a040c4e1156",
  "creator_id": "attacker_PI05",
  "guess": "human",
  "confidence": 0.3779,
  "model_score": 0.6401,
  "style_score": 0.1633,
  "label": "Based on the provided text, this was most likely written by a person.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "96251dc3-a45d-4a82-a60f-cd3abed4962e",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.4916,
  "model_score": 0.5583,
  "style_score": 0.4371,
  "label": "We could not determine with confidence whether this was written by a person or AI.",
  "error": null,
  "verdict": ""
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 200,
  "content_id": "b839141b-1e4e-41d0-a095-63c5ca4513d3",
  "creator_id": "attacker_MF03",
  "guess": "human",
  "confidence": 0.275,
  "model_score": 0.0,
  "style_score": 0.5,
  "label": "Based on the provided text, this was most likely written by a person.",
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 200,
  "content_id": "a2a7ad99-9850-4a50-8cb4-ef6a5a2e30b0",
  "creator_id": "attacker_MF04",
  "guess": "human",
  "confidence": 0.28,
  "model_score": 0.0112,
  "style_score": 0.5,
  "label": "Based on the provided text, this was most likely written by a person.",
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 200,
  "content_id": "232d3788-7111-42eb-8fd3-5892c5aac510",
  "creator_id": "attacker_MF05",
  "guess": "ai",
  "confidence": 0.7239,
  "model_score": 0.9976,
  "style_score": 0.5,
  "label": "Based on the provided text, this was most likely written by AI.",
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 200,
  "content_id": "09e37341-3bb7-495e-8274-f7dbf5f465c2",
  "creator_id": "attacker_MF06",
  "guess": "ai",
  "confidence": 0.7236,
  "model_score": 0.9969,
  "style_score": 0.5,
  "label": "Based on the provided text, this was most likely written by AI.",
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 200,
  "content_id": "5d6d0e31-2dab-47e0-80a3-088d04cf60c5",
  "creator_id": "attacker_MF07",
  "guess": "ai",
  "confidence": 0.6829,
  "model_score": 0.9064,
  "style_score": 0.5,
  "label": "Based on the provided text, this was most likely written by AI.",
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 200,
  "content_id": "bd590e31-d93a-4dd6-af93-5795f0655f8a",
  "creator_id": "attacker_MF08",
  "guess": "ai",
  "confidence": 0.812,
  "model_score": 0.9876,
  "style_score": 0.6683,
  "label": "Based on the provided text, this was most likely written by AI.",
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 400,
  "content_id": null,
  "creator_id": {
    "id": "x"
  },
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "2736840f-fff8-4e40-895a-d8af42316614",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3979,
  "model_score": 0.0287,
  "style_score": 0.7,
  "label": "Based on the provided text, this was most likely written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "2608c49c-ce61-483d-b03d-855a9ea8db17",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3979,
  "model_score": 0.0287,
  "style_score": 0.7,
  "label": "Based on the provided text, this was most likely written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "06d9ecc3-5641-4109-a33b-ad70b16d0cb2",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3979,
  "model_score": 0.0287,
  "style_score": 0.7,
  "label": "Based on the provided text, this was most likely written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "ac74896c-7c08-49f8-bd68-7cd0096585ca",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3979,
  "model_score": 0.0287,
  "style_score": 0.7,
  "label": "Based on the provided text, this was most likely written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "58e0f28c-474f-4e60-8f91-977f44c45695",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3979,
  "model_score": 0.0287,
  "style_score": 0.7,
  "label": "Based on the provided text, this was most likely written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 200,
  "content_id": "bc8aa6de-f6c1-44fe-8d60-7a14fa3eb601",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3979,
  "model_score": 0.0287,
  "style_score": 0.7,
  "label": "Based on the provided text, this was most likely written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 200,
  "content_id": "c5388bf1-b184-4a88-adbf-449053ecf22a",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3979,
  "model_score": 0.0287,
  "style_score": 0.7,
  "label": "Based on the provided text, this was most likely written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 200,
  "content_id": "15dbb70e-f352-4704-bb94-a61d4856044f",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3979,
  "model_score": 0.0287,
  "style_score": 0.7,
  "label": "Based on the provided text, this was most likely written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 200,
  "content_id": "67d3f576-cfaf-47f5-8a8a-accf9c376512",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3979,
  "model_score": 0.0287,
  "style_score": 0.7,
  "label": "Based on the provided text, this was most likely written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 200,
  "content_id": "f5bfe06a-502f-4dfd-804b-7edaec72e7e4",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3979,
  "model_score": 0.0287,
  "style_score": 0.7,
  "label": "Based on the provided text, this was most likely written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```
