# Claude Script

## Run Of Show
- 0-4 min: warm opening, purpose, chat prompt
- 4-10 min: basics, tokens, limitations
- 10-18 min: prompt warmup
- 18-27 min: documents and examples
- 27-34 min: models, effort, Projects, Skills
- 34-42 min: demo / follow-along
- 42-50 min: safety, ethics, Q&A, close

## Slide 1 - Opening
Good morning, everyone. Since this is July 1st and we are heading into a lighter holiday week, I am going to keep this practical. The goal today is not to turn everyone into an AI expert. The goal is to leave with a few Claude habits you can actually use.

Quick chat question before we start: what is one task you would gladly make less manual? A report summary, document Q&A, meeting notes, chart cleanup, variance wording, anything like that.

Cues:
- Keep it relaxed.
- Read 2-3 chat responses.
- Set expectation: short slides and a few follow-alongs.

## Slide 2 - Agenda
Here is the agenda. We will start with the basics, then move into prompting and a few follow-along examples. After that we will cover documents, model choices, reusable workflows, and the data rules to keep in mind.

Cues:
- Invite people to follow along.
- Remind them not to use CUI or sensitive data.

## Slide 3 - Use Cases
The best way to think about Claude is as a strong drafting and thinking partner. It can help you get from rough material to a cleaner starting point. For a lot of our work, that means summaries, report wording, document Q&A, meeting notes, and first-pass analysis. It is especially helpful when you give it the source material and tell it what kind of output you need.

Cues:
- Say first draft, not final answer.
- Connect examples to what people wrote in chat.

## Slide 4 - Limitations
Claude can be very helpful, but it is not the decision-maker. It can sound confident and still miss context, misread a number, or make a claim that needs checking. The simple habit is this: use Claude to draft, structure, and challenge the work. Use your own review for facts, risk, policy, and final wording.

Cues:
- Answer safety concerns early.
- Keep it calm and matter-of-fact.

## Slide 5 - LLM Basics
Claude is a large language model. For our purposes, the important part is simple: it works from the context you provide. Anthropic calls the context window the model's working memory. Tokens are the pieces of text Claude reads and writes. So when you paste a lot of material or ask for a long answer, you are asking Claude to process more tokens.

Cues:
- Use the meeting packet analogy.
- Do not get technical unless asked.

## Slide 6 - Tokenomics
Tokenomics is just a practical way of saying that Claude has to read and write tokens. If you hand it a large packet, ask for a long answer, use a stronger model, and ask for deep effort, you should expect more usage. For day-to-day work, the habit is not to starve Claude of context. The habit is to give the right context and ask for the output you actually need.

Cues:
- Explain cost without dwelling on API pricing.
- Mention admins may have usage analytics depending on plan setup.

## Slide 7 - Data Rules
Before we get into prompts, this is the most important slide. For Claude Commercial, the simple rule is: __ proprietary data only if internal policy allows it. Do not put CUI into Claude Commercial. Do not use classified, export-controlled, customer-restricted, privileged, or sensitive personal data unless that use is explicitly approved. And even when the data is allowed, Claude output is still a draft. We check it before it goes anywhere important.

Cues:
- Pause here.
- Say that __ policy is the authority.
- Do not invite exceptions in the live session.

## Slide 8 - Settings
A quick settings recommendation: if Claude asks what best describes your work, choose Finance, Business, Operations, or the closest option available. For style, I would use Concise. Anthropic says styles can change Claude's tone and structure, and Concise is meant for shorter, more direct responses.

For Instructions, use something like the block on this slide. It tells Claude to keep the writing business-ready, separate facts from assumptions, cite source text when working from documents, ask questions when needed, and avoid making up numbers.

For memory import from ChatGPT Enterprise, use the same data boundary: __ proprietary only, if internal policy allows. I would still not tell people to import everything. The safer guidance is to import only a reviewed, cleaned set of preferences, writing style notes, and general work habits. Do not import CUI, customer-sensitive details, program context, export-controlled information, or anything that would not be approved for Claude Commercial.

Cues:
- Do not over-explain settings.
- Memory import is optional and should be curated.
- Point out that this helps defaults, but prompts still matter.

## Slide 9 - Prompting
Anthropic's guidance is very practical: be clear and direct. I like to think about four pieces: role, task, context, and output. Claude is like a smart new teammate. If you say "help with this," it may guess correctly, but it may not. If you explain the audience, the task, the source material, and the format you want, the answer usually gets much better.

Cues:
- Use the new teammate analogy.
- Tell them this is the core habit.

## Slide 10 - Prompt Practice
Let's try this in Claude. First, type the rough prompt: "Summarize this variance." You can use a made-up sentence if you do not have safe sample data. Then try the better version on the right. The point is not that the second prompt is long. The point is that it tells Claude the audience, the output, the tone, and what to do with uncertainty.

Cues:
- Give them 2-3 minutes.
- Ask: what improved?
- Reinforce: specific beats vague.

## Slide 11 - Variance Example
For variance-style work, Claude is helpful when it has the facts and when you ask it to separate facts from questions. I would not ask Claude to invent the reason for a variance. I would give it the numbers and known drivers, then ask it to draft language and identify what still needs follow-up. That keeps the human review where it belongs.

Cues:
- Keep this broad.
- Emphasize facts vs questions.

## Slide 12 - Document Q&A
Claude is very good at helping with documents, but document Q&A should be grounded. My favorite pattern is ask, cite, verify. Ask a narrow question. Require Claude to quote the source text first. Then verify the answer before using it. If you have an approved, non-CUI sample document, you can try the prompt on the slide now.

Cues:
- Give them 3 minutes if time allows.
- Repeat: approved non-CUI only.

## Slide 13 - Models
The simple model guidance is this: Haiku is fast and lighter, Sonnet is the everyday workhorse, and Opus is for the hardest work. Most people should start with Sonnet unless they have a reason to do something else. Move up when the work is complex enough to justify it. Move down when the task is simple and speed matters.

Cues:
- Keep it practical.
- Do not over-index on model names.

## Slide 14 - Effort Levels
Effort is one of the easier concepts. Think of it like choosing a quick skim, a normal review, or a deep dive. Higher effort can improve difficult work, but it can also take longer and use more capacity. It is not automatically better for every task. For simple work, lower effort may be exactly right.

Cues:
- Use the skim/review/deep dive analogy.
- Mention higher effort is not magic.

## Slide 15 - Projects & Skills
Projects and Skills are where Claude starts becoming more repeatable. A Project is useful when you have a recurring area of work with reference materials or standing instructions. A Skill is useful when there is a repeatable task you want Claude to do in a consistent way. For example, a business narrative helper could enforce a standard structure: known facts, open questions, risks, and clean executive wording.

Cues:
- Do not go too deep.
- Set up the demo.

## Slide 16 - Tool Comparison
A fair way to say it is that these tools overlap. Claude is especially useful for long-context work, careful drafting, and reusable Projects and Skills. ChatGPT is a broad general assistant. Copilot is closest to the Microsoft 365 flow. The right tool depends on the work, the data rules, and where the source material lives.

Cues:
- Avoid absolute claims.
- Tie back to approved use.

## Slide 17 - Next Steps
The main takeaway is simple: Claude can help you get to a better first draft faster. It can help structure work, summarize documents, clean up wording, and create better follow-up questions. It does not replace your judgment. Keep the data rules in mind, verify the facts, and use it where it saves time without creating risk.

If you try one thing before the long weekend, make it small: improve one prompt, ask Claude to question your assumptions, or use it to summarize an approved document. That is enough to start building the habit.

Cues:
- Close warmly.
- Leave time for questions.
- Point to appendix if sharing the deck afterward.

## Likely Q&A
- Can I upload __ proprietary data? Only if internal policy allows. Use the least sensitive useful data.
- Can I upload CUI? No. Do not put CUI into Claude Commercial.
- Does Claude train on our data? Use the approved Enterprise guidance for your tenant. Do not assume consumer rules apply.
- Who can see my chats or files? Follow __ admin and retention guidance.
- How do I know if Claude made something up? Ask for sources, quotes, assumptions, and check the underlying material.
- Can Claude summarize PDFs or contracts? Yes, when the document is approved for use. Ask it to cite the source text.
- Can Claude work with Excel and PowerPoint? Yes, depending on enabled features. Still review formulas, numbers, and formatting.
- When should I use Opus vs Sonnet? Sonnet for most work. Opus for the hardest, highest-value work.
- Does higher effort always mean better? No. It helps hard tasks, but simple tasks may not need it.
- Can I use output in a customer deliverable? Only after review and only if the data and use case are allowed.

## Sources
- Anthropic Academy / Claude 101: https://anthropic.skilljar.com/
- Claude for work: https://www.anthropic.com/learn/claude-for-work
- Prompting best practices: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
- Reduce hallucinations: https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations
- Glossary: https://platform.claude.com/docs/en/about-claude/glossary
- Effort: https://platform.claude.com/docs/en/build-with-claude/effort
- Projects: https://claude.com/resources/tutorials/intro-to-projects
- Skills: https://support.claude.com/en/articles/12512176-what-are-skills
