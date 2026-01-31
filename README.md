# Subdragon 🐉

A high-performance, multi-threaded subdomain discovery tool designed for speed and simplicity.

Subdragon allows you to perform fast subdomain fuzzing using customized wordlists, providing clean and color-coded output for better visibility during reconnaissance.

---

## 🚀 Features

* **Fast Scanning:** Powered by Python's `ThreadPoolExecutor` for concurrent requests.
* **Colorized Output:** Clear distinction between found subdomains and errors.
* **Easy Installation:** Supports `setup.py` for global system access.
* **Lightweight:** Minimal dependencies with maximum efficiency.

---

## 🛠️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/0xCr7ck3r/Subdragon.git
cd Subdragon

```

### 2. Install Globally

```bash
python3 -m venv venv
source venv/bin/activate
pip3 install .

```

> **Note:** If you are using Linux and encounter permission issues, use `pip3 install . --user` or run with `sudo`.

---

## 📖 Usage

```bash
subdragon -d example.com -w wordlist.txt -t 100

```

### Options:

| Flag | Description |
| --- | --- |
| `-d`, `--domain` | **Required:** The target domain (e.g., example.com) |
| `-w`, `--wordlist` | **Required:** Path to your subdomains wordlist |
| `-t`, `--threads` | Number of threads (default: 50) |
| `-o`, `--output` | Save discovered subdomains to a text file |

---

## 💡 Troubleshooting

If you get a `command not found` error after installation, make sure your local bin path is in your system's PATH. Add this to your `~/.bashrc` or `~/.zshrc`:

```bash
export PATH=$PATH:~/.local/bin

```

---

## 🛡️ Disclaimer

This tool is intended for **legal security testing and educational purposes only**. The author is not responsible for any misuse or damage caused by this tool. Use it only on domains you have explicit permission to test.

## 👤 Author

* **0xCr7ck3r** - [GitHub Profile](https://github.com/0xCr7ck3r)
