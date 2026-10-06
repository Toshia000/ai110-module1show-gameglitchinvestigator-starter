# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error | Suspected Code Location |
|-------|-------------------|-----------------|------------------------|-------------------------|
| Guessed 64 | Hint to go lower | Hint to go higher | None | `app.by`
| Pressed enter | Submit guess | Nothing happened | None | `app.by`
| Changed difficulty to easy | More attempts | Less attempts | None | `app.by`

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.

---

- For this project I used Claude AI agent
- One suggestion that was correct was a move of a function from the `app.py` to `logic_utils.py`. I verified the result by comparing `app.py` before refactor and `logic_utils.py` after refactor
- One example of a suggestion I rejected is when I asked AI to fix the bug when the easier difficulties had less attempts that harder difficulties. The suggestion for the fix was correct, it was very simple. I asked AI to generate test. I was expecting a simple test like other tests in `test_game_logic.py`, but instead Claude suggested importing additional modules and the test itself was too complicated. I asked Claude several times to make test more simple without using any other modules, but Claude said it was not possible, so I rejected the suggestion and tested the bug fix myself in the browser.

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
