# Claude Code Setup and Claude API Python Example

This project demonstrates a simple setup for using **Claude Code locally** and making a **Python API call to Claude** using the Anthropic Python library.

It was created while learning how to use Claude Code and the Anthropic API to interact with Claude models from a local development environment.

The repository contains a minimal Python script that sends a prompt to Claude and prints the response.

---

# What This Project Demonstrates

This project shows how to:

- Install **Claude Code locally**
- Set up a local development environment
- Call the **Claude API from Python**
- Send a prompt to a Claude model
- Receive and print the model response

It serves as a simple learning example for developers who want to start integrating Claude into their applications.

---

# Prerequisites

Before running the project, make sure you have the following installed:

- Python 3
- Git
- Claude Code (optional but recommended)

You may optionally use an **Anthropic API key** if you want to test real responses from Claude.

---

# Installing Claude Code

Claude Code allows developers to interact with Claude directly from the terminal and integrate it into local workflows.

Install Claude Code using one of the following commands.

### MacOS (Homebrew)

```bash
brew install --cask claude-code
```

### MacOS / Linux / WSL

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

### Windows (CMD)

```bash
curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd
```

After installation, run:

```bash
claude
```

The first time you run the command, you will be prompted to authenticate.

---

# Using the Anthropic API (Optional)

The Python script in this repository uses the **Anthropic Python library** to call the Claude API.

If you want to test the script with a real Claude model, you will need an API key.

You can generate one here:

https://console.anthropic.com/settings/keys

If you do not provide an API key, the project can still be studied as an example of how Claude API requests are structured.

---

# Install Python Dependencies

Install the Anthropic Python SDK:

```bash
pip install anthropic
```

This library provides an easy interface for interacting with Claude models.

---

# Running the Script

Run the script using:

```bash
python test_claude_api.py
```

The script sends a prompt to Claude and prints the response in the terminal.

---

# Example Code

```python
import anthropic

client = anthropic.Anthropic(
    api_key="YOUR_API_KEY"
)

response = client.messages.create(
    model="claude-3-haiku-20240307",
    max_tokens=200,
    messages=[
        {"role": "user", "content": "Say hello and confirm the Claude API is working."}
    ]
)

for block in response.content:
    print(block.text)
```

---

# What the Code Does

1. Imports the **Anthropic Python library**
2. Creates a **Claude client**
3. Sends a prompt to the Claude model
4. Receives the model response
5. Prints the generated output in the terminal

This demonstrates the basic workflow for interacting with Claude programmatically.

---

# Claude Model Used

This example uses the model:

```
claude-3-haiku-20240307
```

This model is designed for **fast and lightweight responses**, making it suitable for quick testing and experimentation.

---

# Project Structure

```
claude_api_test
│
├── test_claude_api.py
├── README.md
└── LICENSE
```

---

# Purpose of This Project

This project was created as a learning exercise to understand:

- How to install and use Claude Code
- How to call Claude models from Python
- Basic API authentication and request handling
- How LLM APIs work in real development workflows

---

# License

This project is licensed under the **MIT License**.