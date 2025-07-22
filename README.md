# AI DevOps Copilot


🚀 N3x-Synth4r

The Swiss Army Knife CLI for Developers!
🧠 Explain commands, generate code, supercharge Git & Docker, get dev tips—all in a sleek, AI-powered terminal interface. Run entirely offline with Ollama or tap into online magic with OpenAI!
✨ Features

    🧠 Explain Commands: Instantly understand Linux/CLI/code commands (locally or via OpenAI).

    ⚡ AI Code Generation: Create scripts on demand—works offline (Ollama) or online (OpenAI).

    💻 System Info: Print detailed device/system information.

    💡 Dev Tips: Boost your skills with daily developer wisdom.

    🐳 Docker Controls: List, run, or stop containers and images.

    🔧 Git Automation: Status, add, commit, push, pull—right from the CLI!

    🌗 Offline & Online: Seamlessly switch between local (LLM/Ollama) or SaaS (OpenAI) modes.

#  🛠️ Installation

Clone & set up:

bash



git clone https://github.com/amandx36/AI-DEVOPS-COPILOT
cd N3xthar-Voryx
python -m venv .venv
source .venv/bin/activate        # On Windows: .venv\Scripts\activate
pip install -r requirements.txt




# 🦙 For Offline Mode (Ollama)

    Install Ollama

    Download a local model (for example: llama3):

    bash
    ollama pull llama3

    Start Ollama before starting the CLI!

# 🤖 For Online Mode (OpenAI)

    Get an OpenAI API Key

    Set it in your environment:

    bash
    export OPENAI_API_KEY=your-openai-api-key

# 🚦 Usage

bash
python copilot_ai.py

Interact via the epic CLI menu! Example session:

text
╔══════════════════════════════════════════════════╗
║           🌍 Select Operational Mode 🌐         ║
╠══════════════════════════════════════════════════╣
║  1️⃣  Online Mode    - Connect to the internet  ║
║  0️⃣  Offline Mode   - Stay local (no network)  ║
╚══════════════════════════════════════════════════╝
👉  Enter 1 for Online, or 0 for Offline: 1

╔════════════════════════════════════════════════════════════════════════╗
║                🚀 Choose Your Command Superpower! 🚀                 ║
╠════════════════════════════════════════════════════════════════════════╣
║ 🧠  explain            ➡️   Code/command explanations               ║
║ ⚡  generate           ➡️   Instantly generate code/files           ║
║ 💻  system_info        ➡️   Reveal system information               ║
║ 💡  dev_tips           ➡️   Get clutch dev tips                    ║
║ 🐳  docker_containers  ➡️   List Docker containers                  ║
║ 🖼️  docker_images      ➡️   List Docker images                      ║
║ 🚀  docker_run         ➡️   Launch a Docker container               ║
║ 🛑  docker_stop        ➡️   Stop a Docker container                 ║
║ 🔍  git_status         ➡️   Show Git working status                 ║
║ ➕  git_add            ➡️   Add files to Git staging area           ║
║ 💾  git_commit         ➡️   Commit changes to Git                   ║
║ ⤴️  git_push           ➡️   Push to remote repository               ║
║ ⤵️  git_pull           ➡️   Pull latest from remote                 ║
╚════════════════════════════════════════════════════════════════════════╝

Just type your choice and follow the prompts!
📦 Folders & Structure

text

N3xthar-Voryx/
├── main.py
├── Utility_functions/
│   ├── commands_explain_online.py
│   ├── commands_explain_offline.py
│   ├── response_generator_online.py
│   ├── response_generator_offline.py
│   ├── git_helper.py
│   ├── docker_helper.py
│   └── daily_tips.py
├── system_info.py
├── requirements.txt
└── ...

🐳 Docker Integration

Make sure Docker is installed and running.

    List containers/images

    Launch or stop containers
    All via this CLI!

🤝 Contributions

Pull requests & issues welcome!

    Open an issue for bugs or ideas

    Fork, create a branch, make improvements, and open a PR 🚀

👤 Author

Aman Deep (N3xthar-Voryx)
GitHub - LinkedIn
📄 License

MIT License

💡 Pro tip: Star this repo if you like it!

Happy hacking! 🦾

    Copy, share, and rule your terminal life!



































#


# PACKAGES  I USED  

| Package           | Purpose                                                      |
| ----------------- | ------------------------------------------------------------ |
| **openai**        | Allows your code to talk to ChatGPT                          |
| **python-dotenv** | Loads secrets (like your API key) from `.env` into your code |



 # MY CLI LOOK LIKE THIS (USED THIS SKELTON WITH THE HELP OF TYPER )

 ai-devops-copilot
 ├── git
 │    └── commit
 │    └── undo
 │
 ├── docker
 │    └── list
 │    └── stop
 │
 ├── linux
 │    └── explain
 │    └── generate
 │
 └── ai
      └── suggest
      └── tips



# till now how to use it 

python main.py set-mode 1
python main.py explain "ls -a"


✅ First set mode (online = 1, offline = 0)
✅ Then run any command (here, explain)



🔷 2. What is SDK structure?
✅ SDK = Software Development Kit

    It is a package/library provided by a service (like OpenAI) to make it easier for developers to use their API.


✅ SDK structure refers to how classes, functions, and methods are organised inside the SDK to access different functionalities. 

All the modern api use this format 

# Design of the open ai for the call for the different purpose !! 
| **Functionality**   | **Method**                             |
| ------------------- | -------------------------------------- |
| Chat completions    | `client.chat.completions.create()`     |
| Image generation    | `client.images.generate()`             |
| Audio transcription | `client.audio.transcriptions.create()` |
| Embeddings          | `client.embeddings.create()`           |







# API PART OF KNOWLEDGE BROOO 

If you change "role" to anything else (e.g., "speaker") or "user" to "person", the API will throw an error, because it does not recognise it.


| **Key**     | **Required?** | **Allowed values**                  |
| ----------- | ------------- | ----------------------------------- |
| `"role"`    | ✅ Required    | `"system"`, `"user"`, `"assistant"` |
| `"content"` | ✅ Required    | Your text message                   |



🔷 1. Why do we write response.choices[0].message.content?

analogy 02 
response
 └── choices (branch) [list]
       └── [0] (first leaf)
            └── message (sub-branch)
                 └── content (final fruit 🍎)

output of the api form openai !! 

✅ Because the response returned by OpenAI is structured like this:
{
  "id": "...",
  "object": "chat.completion",
  "created": ...,
  "model": "gpt-4o",
  
  "choices": [    <-- ✅ This is a list of choices (outputs). By default, it has 1 item at index [0].
    {
      "index": 0,   <-- ✅ This is the index = 0 (first output).

      "message": {  <-- ✅ This is the 'message' key containing AI's reply.
        "role": "assistant",  
        "content": "Here is your AI-generated answer..."  
        // ✅ 'content' is the **actual text answer** generated by ChatGPT.
      },

      "finish_reason": "stop"
    }
  ],

  "usage": {...}
}


