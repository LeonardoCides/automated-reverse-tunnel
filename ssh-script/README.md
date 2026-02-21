# Remote SSH Auto-Fix & Tunneling Tool 🚀

This utility script is designed for remote administration of Linux and Windows machines. It ensures the local SSH server is active and establishes a secure reverse tunnel using **Serveo**, bypassing NAT and firewalls without manual router configuration.

## 🌟 Key Features
* **Service Self-Healing**: Automatically detects if the SSH service is down and attempts to start it (requires sudo/admin).
* **NAT Traversal**: Uses reverse tunneling to make the machine accessible from the internet even behind a CGNAT or strict firewall.
* **Instant Notifications**: Sends the connection details (Port, Host, and User) directly to your Telegram Bot.
* **Cross-Platform**: Support for both Linux (systemd) and Windows (PowerShell).

## 🛠️ Prerequisites
* Python 3.12.3
* OpenSSH Server installed on the host machine.
* A Telegram Bot (Token and Chat ID).

## 🚀 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/LeonardoCides/automated-reverse-tunnel
   cd automated-reverse-tunnel
   ```
2. **Install dependencies**
   ```bash
   pip install requests python-dotenv
   ```
   
3. **Configure environment variables:**
   * Create a .env file in the root directory:
     ```bash
     TELEGRAM_TOKEN=your_bot_token_here
      CHAT_ID=your_personal_chat_id
     ```
4. **Execute:**
     ```bash
   python3 main.py
     ```
