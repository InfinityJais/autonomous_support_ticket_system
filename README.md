# 🤖 Autonomous Support Ticket System

##  Project Overview
The **Autonomous Support Ticket System** is an AI-powered application built using CrewAI.  
It automatically analyzes, routes, and responds to user support tickets (like password resets or leave balance queries) using LLM agents.
---
## ✨ Features

- 🔄 **Ticket Routing** – Detects the type of issue and assigns it to the right AI agent.
- 🔑 **Password Reset Agent** – Handles password reset requests.
- 📊 **Leave Balance Agent** – Retrieves and reports user leave balances.
- 🧑‍💻 **Customizable Tasks & Agents** – Easily extend the system with your own agents.
- ⚡ **Command-Line Interface (CLI)** – Run support tickets directly from terminal.

---

## 📂 Project Structure

```
autonomous_support_ticket_system/
│
├── src/
│ └── autonomous_support_ticket_system/
│ ├── main.py 
│ ├── crew.py 
| └── config/
│    ├── tasks.ymal # Task configs
│    ├── agents.yaml # Agent configs
├── pyproject.toml # Project configuration & dependencies
├── README.md # Documentation
└── .env # API keys (ignored in git)
```

---
## 🚀 Getting Started

### Prerequisites

List any software or dependencies a user needs to have installed.

   * Python 3.10
   * `uv` 
   * Git

### Installation


1.  Clone the repository:
    ```bash
    git clone https://github.com/your-username/autonomous-support-ticket-system.
    ```
2.  Navigate to the project directory:
    ```bash
    cd autonomous-support-ticket-system
    ```
3.  Create vertual envirment:
    ```bash
    uv venv --python=3.10
    ```
4.  Activate vertual enveirement:
    ```bash
    .venv\Scripts\activate  #Windows
    ```
    ```bash
    source .venv/bin/activate  #Mac/Linux
    ```
5.  Install the required libraries:
    ```bash
    uv sync
    ```
5.  Run FastAPI server:
    ```bash
    python main.py run "Password Reset Issue" "I forgot my password, please reset." "user@example.com"
    ```

---

## 🎯 output


Agent:PasswordResetAgent\
Final Answer: \
Dear user, \
We have received your request regarding account access and have initiated the password reset process for your account associated with 
the username 'user@example.com'. A password reset link has been sent to your registered email address. Please check your inbox, and if you 
do not see it shortly, also check your spam or junk folder.\
Here are the steps to complete your password reset:  
1. **Open the Email**: Locate the email with the subject line "Password Reset Request" from our support team.
2. **Click the Reset Link**: Click on the link provided in the email. This link is unique to your account and is secure.  
3. **Create a New Password**: You will be directed to a secure page where you can enter a new password. When creating your new password, 
please follow these security best practices: 
- Use at least 12 characters, combining uppercase letters, lowercase letters, numbers, and special symbols.
- Avoid using easily guessable information, such as your name or birthday.
- Consider using a passphrase, which can be easier to remember and harder to crack.  
4. **Confirm Your New Password**: Enter your new password again to confirm it. 
5. **Log In**: Once your password has been successfully reset, you can log in to your account using your new password.
6. **Enable Two-Factor Authentication (optional but recommended)**: For added security, consider enabling two-factor authentication  
(2FA) in your account settings once you regain access. This provides an extra layer of protection. 

If you encounter any issues during this process or do not receive the password reset email, \
please don’t hesitate to reach out for further assistance. 
                                    
Thank you for your attention to account security, and we hope you regain access to your account promptly.
 
Best regards,  
[Your Support Team]

---
## RAG Pipeline (Retrieval-Augmented Generation)
To make responses more accurate and context-aware, this system integrates a RAG pipeline.
This allows agents to search external knowledge sources (e.g., HR policies, IT documentation, or PDFs) before generating answers.\
🔹 How it works
1. Knowledge Ingestion
- Upload documents (PDF, TXT, Markdown, etc.).
- Split into chunks and create embeddings using Hugging Face models.
- Store in a vector database (Chroma/FAISS).

2. Query Processing
- When a ticket is created, the system retrieves relevant chunks from the vector DB.
- These are passed to the LLM as additional context.

3. Answer Generation
- The LLM combines the user query + retrieved context to give a more precise answer.

### Instead of only relying on the LLM’s memory, the system will:

- Search HR documentation in the vector DB.
- Retrieve the employee leave balance info.
- Respond with an accurate, knowledge-grounded answer.


## 📜 License
This project is licensed under the MIT License - see the `LICENSE` file for details.
