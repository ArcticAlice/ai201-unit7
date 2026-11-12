"""
What your test runs. ← UNIT 8, MILESTONE 3

Each of your five criteria needs something run against it. A criterion about
false positives needs your own writing. One about label coverage needs inputs
across the score range. One about the appeal path needs a real content_id.
"""

SCENARIOS = [
    {
        "name": "my own writing",
        "criterion": 1,
        "texts": [
            "Social responsibility should be an important consideration to business because with the corporate power they possess they are able to greatly influence social goals. Businesses already play large roles in the way laws are shaped. With any large company it is almost a guarantee that they have spent some amount of money lobbying for or against a bill. These bills may not fall into social issues but this doesn’t point away from the fact that businesses play a greater role in society than just simply providing a service or good. Many businesses have audiences that are in the tens of millions of people.",
            "John Lewis and the large number of people who committed sit-ins displayed three stakeholder powers: economic power, informational power, and political power. The economic power was shown at first when businesses started to suffer financially through the sit-ins. This led to the effect of businesses saying they needed a moratorium so they could put together a proposal (Lewis & Aydin, p. 97). This proposal did not happen but it was showing that the sit-ins were having an effect on establishments. Economic power is further shown when the boycott of multiple businesses happens.",
            "In the 1900s, a patient’s pain wasn’t given much thought to. Doctors prioritized what they could see. This, of course, led to a lack of treatments and care for patients experiencing extreme pain. This problem is what opened the market to pain medication and what ultimately led to Purdue Pharma creating an Opioid crisis that spanned across several decades here in America. In a brief description, this opioid crisis involved patients who were legally prescribed an unethical amount of opioids. Many of these patients developed addictions, causing them to lose their jobs, relationships, and their lives.",
            "Bacteria are one of the three domains of life. They play a key role in the environment and in organisms. Bacteria have a few similarities with eukaryotic cells, for example having a cell membrane, cytoplasm and ribosomes. While in both cells ribosomes are responsible for protein synthesis, the actual size of them can differ between eukaryotes and bacteria. In bacteria the ribosomes are smaller, because of this some antibiotics are created to specifically target these smaller ribosomes as a way to destroy the bacteria (Mukhtar, T. A., & Wright, G. D. 2005).",
            "I would gather up as much evidence to show that I did not go through with what the company was asking. I would also find a way to record what the company asked of me. Afterwards I would just quit. I would probably not say anything or report anything because convicting the company itself would take many years. I would also lose my own time by being investigated and possibly accused and I would believe I would have a hard time finding a job afterwards. I would not feel protected by the Whistle Blower Protection Act because there have been numerous cases in America where the whistleblower has still been prosecuted, for example Edward Snowden.",
            "It’s morning and I’m helping set up stock for the day. I hear the market teeming with people early in the morning. My dad’s in a rush hopping to set up shop early. When we’re finally done, my dad opens up the door, takes his place by the merchandise, and my mom stands near the counter. Minutes go by and people start to walk in. Dad makes conversation with a buyer, while mom haggles the price of a pottery set with another. After a bit dad pauses his conversation; that’s when I notice a man entering.",
            "Three days. That’s the absurd amount of time I spent attempting to build a simple AI Tic-tac-toe player. You might notice the word attempting, and that’s because even after hours of programming I still couldn’t get it to work in time for the project deadline. Now it wasn’t a genuine AI like chatgpt, only a program following a simple algorithm. It was supposed to be a small part of the entire project, but it ended up taking the most time.",
            "The physical transition is when he leaves his home to go live with uncle. The spiritual transition is where his character is built from deceiving his brother to being deceived by his uncle. The word land is supposed to represent home or the birthplace of that person. The message is repeated because the writer wanted to show how important it was for Jacob to return to his homeland.",
            "I think the line Samuel 16:12 (KJV) becomes distorted into showing David as charismatic or the life of a party. The bible verse describes him as ruddy and has a beautiful countenance and this translates into “strength of a tiger” and “dances like two of him” into the song. In the song everybody wants to be him or they want to dance with him because everybody wants to be the most popular person at a party",
            "The colosseum was packed to the brink. Spectators cheered as the first event went on. A lion was pitted against three gladiators. The lion manages to tear into one of them with its claws. I wince seeing the blood drip down the lion’s paw and gladiator. The gladiator drops down and doesn’t move."
        ],
    },
    {
        "name": "score spread",
        "criterion": 2,
        "texts": [
            # 5 AI-generated samples
            "Artificial intelligence is transforming modern society across various domains. It is important to note that machine learning algorithms process large datasets to detect patterns. Furthermore, these technological developments offer significant benefits for efficiency and productivity. In conclusion, the integration of computational tools will continue to shape future industry standards.",
            "In today's digital landscape, effective communication plays a crucial role in professional success. It is essential to consider the multifaceted nature of interpersonal collaboration. Moreover, adopting structured workflows facilitates better outcomes across diverse teams. Ultimately, organizations must implement comprehensive strategies to foster innovation and maintain sustainable development.",
            "The implementation of sustainable energy systems represents a fundamental challenge for contemporary engineering. First, solar and wind power provide viable alternatives to traditional fossil fuels. Additionally, energy storage technologies have improved substantially in recent decades. Consequently, transitioning to renewable power grids is vital for minimizing environmental degradation.",
            "Data analysis has become an indispensable component of contemporary decision-making processes. Organizations utilize statistical methodologies to extract valuable insights from complex information repositories. Furthermore, predictive modeling allows enterprises to anticipate customer preferences with greater precision. Therefore, data literacy constitutes a prerequisite for achieving operational excellence.",
            "Urban planning in modern metropolitan regions necessitates balanced approaches to infrastructure development. It is widely acknowledged that public transportation networks reduce traffic congestion and carbon emissions. Additionally, green urban spaces enhance civic well-being and promote environmental sustainability. In summary, holistic urban strategies ensure resilient community growth.",
            # 5 human-authored samples
            "It’s morning and I’m helping set up stock for the day. I hear the market teeming with people early in the morning. My dad’s in a rush hopping to set up shop early. When we’re finally done, my dad opens up the door, takes his place by the merchandise, and my mom stands near the counter.",
            "Three days. That’s the absurd amount of time I spent attempting to build a simple AI Tic-tac-toe player. You might notice the word attempting, and that’s because even after hours of programming I still couldn’t get it to work in time for the project deadline.",
            "The colosseum was packed to the brink. Spectators cheered as the first event went on. A lion was pitted against three gladiators. The lion manages to tear into one of them with its claws. I wince seeing the blood drip down the lion’s paw and gladiator.",
            "I was walking down the gravel road behind the old barn when the storm hit out of nowhere. Hail the size of marbles started bouncing off the metal roof, sounding like a machine gun. I ducked into the shed just as the power lines started whining in the wind.",
            "My grandmother always kept an old rusted biscuit tin on the top shelf of her pantry. Inside wasn't cookies at all, but decades of yellowed receipts, silver buttons, faded black-and-white photos of cousins nobody remembers, and a single silver key to a lock that no longer exists."
        ],
    },
    {
        "name": "label coverage",
        "criterion": 3,
        "texts": [
            # High-confidence human (< 0.40)
            "John Lewis and the large number of people who committed sit-ins displayed three stakeholder powers: economic power, informational power, and political power. The economic power was shown at first when businesses started to suffer financially through the sit-ins. This led to the effect of businesses saying they needed a moratorium so they could put together a proposal (Lewis & Aydin, p. 97). This proposal did not happen but it was showing that the sit-ins were having an effect on establishments.",
            # Unsure (0.40 - 0.65)
            "Social responsibility should be an important consideration to business because with the corporate power they possess they are able to greatly influence social goals. Businesses already play large roles in the way laws are shaped. With any large company it is almost a guarantee that they have spent some amount of money lobbying for or against a bill.",
            # High-confidence AI (> 0.65)
            "The implementation of the proposed framework requires careful consideration of several key factors. First, it is important to note that the system must be able to handle a wide variety of different inputs. Additionally, the overall performance of the solution depends on a number of important variables."
        ],
    },
    {
        "name": "appeal path",
        "criterion": 4,
        "appeals": [
            {
                "submission_text": "This draft was written for an undergraduate history symposium regarding civil rights demonstrations in the mid-twentieth century.",
                "reasoning": "I drafted this historical overview myself using primary source documents."
            },
            {
                "submission_text": "Technical documentation summarizing relational database indexing strategies and B-tree search complexity.",
                "reasoning": "I authored this technical explanation for my team's documentation."
            },
            {
                "submission_text": "Personal narrative regarding childhood experiences during summer visits to rural agriculture markets.",
                "reasoning": "This is a creative personal memoir recounting my own family memories."
            },
            {
                "submission_text": "Comparative literature essay evaluating biblical allegories and character transformations in ancient folklore.",
                "reasoning": "This analysis was composed independently for a university literature seminar."
            },
            {
                "submission_text": "A brief reflection on ethics and corporate compliance policies within modern technology companies.",
                "reasoning": "I wrote this reflection based on corporate ethics case studies discussed in class."
            }
        ],
    },
    {
        "name": "bad input",
        "criterion": 5,
        "bodies": [
            {"text": "", "creator_id": "eval_bad_empty"},
            {"creator_id": "eval_bad_missing"},
            {"text": None, "creator_id": "eval_bad_null"},
            {"text": "word " * 50001, "creator_id": "eval_bad_huge"},
            {"text": "   \n\t  ", "creator_id": "eval_bad_whitespace"},
        ],
    },
]


def validate() -> list[str]:
    """
    Complain about anything malformed, before a long run rather than during.
    """
    problems = []
    for i, scenario in enumerate(SCENARIOS, 1):
        if not scenario.get("name"):
            problems.append(f"scenario {i} has no name")

        texts = scenario.get("texts")
        bodies = scenario.get("bodies")
        appeals = scenario.get("appeals")

        present = sum(1 for x in (texts, bodies, appeals) if x is not None)
        if present > 1:
            problems.append(
                f"scenario {i} ('{scenario.get('name')}') has multiple data sources — pick one of texts, bodies, or appeals"
            )
            continue
        if present == 0:
            problems.append(f"scenario {i} has no texts, bodies, or appeals")
            continue

        if appeals:
            for j, app_item in enumerate(appeals, 1):
                if not isinstance(app_item, dict) or "submission_text" not in app_item or "reasoning" not in app_item:
                    problems.append(
                        f"scenario {i}, appeal {j} must be a dict with submission_text and reasoning"
                    )
            continue

        if bodies:
            for j, body in enumerate(bodies, 1):
                if not isinstance(body, dict):
                    problems.append(
                        f"scenario {i}, body {j} is not a dict — bodies are whole "
                        f"request bodies, like {{'text': '', 'creator_id': 'x'}}"
                    )
            continue

        for j, text in enumerate(texts, 1):
            if not str(text).strip():
                problems.append(
                    f"scenario {i}, text {j} is empty — if an empty submission is what "
                    f"you're testing, use 'bodies' instead of 'texts'"
                )
            elif str(text).startswith("REPLACE ME"):
                problems.append(
                    f"scenario {i} ('{scenario.get('name')}'), text {j} is still "
                    f"the placeholder"
                )
    return problems
