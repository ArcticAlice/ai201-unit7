# Attack run — after

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-11 20:24
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
  "content_id": "ab2ea1e2-f917-4fc3-8361-711b4359b08e",
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
  "content_id": "3b9122fb-2518-4778-aaa2-4c5dafd83b50",
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
  "content_id": "20bc8b30-b033-4bcd-8333-f693d7fc76d7",
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
  "content_id": "1c2d2063-bfd6-46be-b6c5-d0b9bc0db477",
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
  "content_id": "85d0dc9c-3971-4c01-b1d4-c196fd516520",
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
  "content_id": "d30c932c-932e-4737-9c1a-68265cc0d54e",
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
  "content_id": "ad0a1247-ac58-4489-88ae-51b3a7f3d916",
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
  "content_id": "63be6461-a9c2-465a-a402-e4a1fdfce83c",
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
  "content_id": "cb7b8d4c-819f-4e5a-af95-d2787b1677ce",
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
  "content_id": "d9ec6327-d3af-4308-aa67-9ddbc5a583b7",
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
  "content_id": "7d14f48e-2b3d-4d35-a81a-e0caf5f65bf1",
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
  "content_id": "7db7e1d4-8501-4f93-8f5b-f5afa0412862",
  "creator_id": "attacker_FP02",
  "guess": "unsure",
  "confidence": 0.6555,
  "model_score": 0.7387,
  "style_score": 0.5875,
  "label": "We could not determine with confidence whether this was written by a person or AI.",
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
  "content_id": "c0fac72c-27ca-42d9-ae92-3ab33cbb6e8a",
  "creator_id": "attacker_FP03",
  "guess": "unsure",
  "confidence": 0.6547,
  "model_score": 0.8051,
  "style_score": 0.5317,
  "label": "We could not determine with confidence whether this was written by a person or AI.",
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
  "content_id": "b5bb65ed-2642-4e60-8616-da73f86434ff",
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
  "content_id": "5a291f3a-e56f-4448-9840-9c97af1dfc1b",
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
  "content_id": "e038707b-19b9-4bbf-99e0-269b94b9c99e",
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
  "content_id": "19892020-9232-4379-a472-1a555ea6caa9",
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
  "content_id": "de03cd2d-10db-47e3-a194-3f2b733fa9f1",
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
  "content_id": "0d9ebe66-d4ef-49b3-b0cb-02508f789174",
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
  "content_id": "ae00c731-36f2-4ae6-a51a-dc4a1e631121",
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
  "content_id": "4fb724b2-3e14-4ede-b702-cb66c533cf91",
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
  "content_id": "250a7ba8-a68f-4f67-9018-aa8f9f4b2aa1",
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
  "content_id": "f4288813-b0d0-4ab7-97bb-cedb24e3180b",
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
  "content_id": "e11aebc0-193c-4a92-9383-64a2532c9657",
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
  "content_id": "87ed6ae0-d2cd-41c7-a9c8-9498ebb40719",
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
  "content_id": "baaa197c-cc21-4dc3-a8d7-5498e472f2a5",
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
  "content_id": "4df94c2f-e742-4a98-a4be-2a16fe087a8e",
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
  "content_id": "6106e5fa-0de0-4d99-b51e-9b12d5339325",
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
  "content_id": "c4f2cd42-35d9-417f-9022-3bdf2bbdde63",
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
  "content_id": "248a155f-539d-4282-84be-4653106860f9",
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
  "content_id": "622936a8-72d8-42c9-80d0-0102d1bd9cf9",
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
  "content_id": "296b8f8a-4cb5-4df7-bf14-c3ff11df42c9",
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
  "content_id": "230349b2-9347-42a8-a5eb-9dfbdae3ef16",
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
  "content_id": "aef04e0b-a45f-4bdd-91e8-9d44fa75ae47",
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
  "content_id": "e59e6b9a-7b8d-4f1a-88d3-b282da39231c",
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
  "content_id": "6295a41c-50b8-4e34-bb14-e8641905f9dc",
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
  "content_id": "b7bc6c9f-591e-41b4-8de3-f44245fac816",
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
  "content_id": "32ccb8c8-8987-4225-b73e-0bc5e01d5384",
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
  "content_id": "064dbde2-e2e4-4a44-8b9a-210317ecef0d",
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
  "content_id": "ec416e59-8cae-49ba-802b-6fedeb6c7fc8",
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
