# AI Customer Support Bot — Product Documentation (Flask, SQLite, Gemini API, In-Context Learning)

This documentation guides AI agents and developers to build an AI-powered customer support bot using **Flask**, **SQLite**, **Gemini API** (Google Generative AI), and **in-context learning** (no vector databases). The workflow is simple: each query sends the full FAQ and session history to the LLM for context-aware answers and graceful escalation.

---

## Table of Contents

- [AI Customer Support Bot — Product Documentation (Flask, SQLite, Gemini API, In-Context Learning)](#ai-customer-support-bot--product-documentation-flask-sqlite-gemini-api-in-context-learning)
  - [Table of Contents](#table-of-contents)
  - [Project Overview](#project-overview)
  - [Design \& Technology Choices](#design--technology-choices)
  - [Folder Structure](#folder-structure)
  - [Step-by-Step Implementation Plan](#step-by-step-implementation-plan)
    - [1. Initialization](#1-initialization)
    - [2. Database Setup](#2-database-setup)
    - [3. FAQ Document](#3-faq-document)
    - [4. Flask API Endpoint](#4-flask-api-endpoint)
    - [5. Conversation Handling Workflow](#5-conversation-handling-workflow)
    - [6. Return to User](#6-return-to-user)
  - [API Contract](#api-contract)
  - [LLM Prompt Design](#llm-prompt-design)
  - [Escalation Workflow](#escalation-workflow)
  - [Deliverables](#deliverables)
  - [Best Practices \& Error Minimization](#best-practices--error-minimization)

---

## Project Overview

**Goal:** Build an AI-powered customer support bot that answers user queries strictly based on a provided FAQ document. If the answer is not in the FAQ, the bot will escalate to a human agent.

**Constraints:**

- Use only free or open-source tools.
- Avoid vector DBs and retrieval-augmented methods.
- Keep logic simple and transparent.

---

## Design & Technology Choices

| Layer        | Tool/Framework                    | Rationale                          |
| ------------ | --------------------------------- | ---------------------------------- |
| Backend API  | Flask (Python)                    | Lightweight, fast, familiar        |
| Database     | SQLite                            | File-based, zero setup, simple     |
| LLM          | Gemini API (Google Generative AI) | Powerful, easy to integrate        |
| FAQ Storage  | faqs.txt                          | Easy to edit, load, version        |
| Core Logic   | In-context learning               | Full FAQ & history in every prompt |
| API Endpoint | /chat (POST)                      | Single, simple REST endpoint       |

---

## Folder Structure

```
/app.py              # Flask backend and core logic
/faqs.txt            # All FAQs and answers in plain text
/requirements.txt    # Python dependencies
/README.md           # Setup and usage documentation
/demo.mp4            # Demo video (optional deliverable)
```

---

## Step-by-Step Implementation Plan

### 1. Initialization

- **Create Files:**
  - `app.py` — Main Flask app
  - `faqs.txt` — FAQs (one per line: Q: ... A: ...)
  - `requirements.txt` — `flask`, `google-generativeai`, `sqlite3` (standard lib)
- **Version Control:**
  - Initialize a GitHub repository, commit the above files.

### 2. Database Setup

- Use SQLite (no server needed).
- Table: `conversations`
  - `session_id TEXT PRIMARY KEY`
  - `history TEXT`
- In `app.py`, create logic to initialize the DB if it doesn't exist.

### 3. FAQ Document

- Store all FAQs in `faqs.txt` with clear formatting.

  ```
  Q: What is your return policy?
  A: You can return products within 30 days of purchase.

  Q: Do you ship internationally?
  A: Yes, we ship to over 50 countries worldwide.
  ```

- Load the contents of `faqs.txt` into a string variable at app startup.

### 4. Flask API Endpoint

- Define a single endpoint:
  - `POST /chat`
    - **Request:** `{"session_id": "...", "query": "..."}`
    - **Response:** `{"response": "..."}`

### 5. Conversation Handling Workflow

1. **Receive Request:**
   - Accept JSON payload: `session_id`, `query`
2. **Fetch History:**
   - If `session_id` exists, retrieve `history`;
   - Else, start new history (empty).
3. **Construct Gemini API Prompt:**
   - System instruction:
     > "You are a customer support bot. Answer the user's query based ONLY on the provided FAQs. If the answer isn't in the FAQs, respond with the exact phrase 'ESCALATE'."
   - Append entire `faqs.txt` content.
   - Append conversation history.
   - Append the new user query.
4. **Call Gemini API:**
   - Use the official `google-generativeai` Python client to send the full prompt.
5. **Process Response:**
   - If response is `"ESCALATE"`:
     - Reply: "I can't answer that question. I will escalate this to a human agent."
     - _(Optional)_: Make a second Gemini API call to summarize the conversation for the agent.
   - Else: Return Gemini's answer.
6. **Update History:**
   - Append the latest user query and bot response to the session's history.
   - Save updated history back to the DB.

### 6. Return to User

- Send the bot's final response as JSON:
  ```json
  { "response": "..." }
  ```

---

## API Contract

**Endpoint:**  
`POST /chat`

**Request Example:**

```json
{
  "session_id": "abcd1234",
  "query": "Do you ship to Canada?"
}
```

**Response Example:**

```json
{
  "response": "Yes, we ship to over 50 countries worldwide."
}
```

Or, if not found in FAQs:

```json
{
  "response": "I can't answer that question. I will escalate this to a human agent."
}
```

---

## LLM Prompt Design

**Structure:**

```
System Instruction:
"You are a customer support bot. Answer the user's query based ONLY on the provided FAQs. If the answer isn't in the FAQs, respond with the exact phrase 'ESCALATE'."

FAQs:
[contents of faqs.txt]

Conversation History:
[user: ...]
[bot: ...]
...

New User Query:
[user: ...]
```

---

## Escalation Workflow

- If Gemini's answer is `"ESCALATE"`:
  1. Respond to user with escalation message.
  2. _(Optional)_: Summarize history with a second Gemini API call for human agent handoff.

---

## Deliverables

- **Push to GitHub:**
  - `app.py`, `faqs.txt`, `requirements.txt`
- **Documentation:**
  - `README.md` with:
    - Setup instructions (pip install, Gemini API key, run Flask app)
    - Endpoint description and examples
    - Prompt design and escalation logic
- **Demo Video:**
  - Use Postman or curl to show:
    - Successful FAQ match
    - Escalation trigger

---

## Best Practices & Error Minimization

- Handle all errors and input validation in Flask routes.
- Always check for session existence before reading/updating history.
- Use clear, atomic commits in Git.
- Ensure prompt formatting is consistent to avoid LLM confusion.
- Document any changes or customizations in `README.md`.
- Test the API with at least three scenarios:
  1. FAQ match
  2. Escalation
  3. Session continuity (history)

---

**By following this plan, any AI or developer can build, understand, and extend the AI Customer Support Bot quickly and accurately using Gemini API.**
