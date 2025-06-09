# 🥕 parsnip

**parsnip** is a lightweight CLI tool for extracting parameter names from JavaScript files. It scans for parameters used in API requests, including in query strings, request bodies, and structured objects (`params`, `data`, etc.).

This is especially useful for reconnaissance, reverse engineering frontend APIs, or generating wordlists for tools like [`paraminer`](https://portswigger.net/bappstore/17d2949a985c4b7ca092728dba871943).

---

## 🚀 Purpose

JavaScript files often reveal hidden API parameter names that aren't documented or accessible via static analysis. `parsnip` helps you find:

- Query parameters (`?param=value&key=value`)
- Parameters in `params: {}` and `data: {}` blocks
- Parameters in `JSON.stringify({ ... })` payloads

Use these discovered parameters to fuzz or brute-force API inputs more intelligently.

---

## ⚠️ Note on False Positives

Since JavaScript is dynamic and loosely structured, `parsnip` may extract unrelated object keys or values that resemble parameter names. A quick manual review is recommended before using the list in automated tooling.

---

## 📦 Usage

### 1. Create a list of JavaScript URLs (e.g., using gau, waybackurls, hakrawler, etc.)

```bash
python3 parsnip.py -i jsurls.txt >> paramswordlist.txt

```

### 2. Pass the output to paraminer or similar tools:
<img width="1165" alt="Screenshot 2025-06-09 at 19 52 54" src="https://github.com/user-attachments/assets/1b67df16-0ac3-4c2a-903b-06cd0c7262d7" />


<img width="1167" alt="Screenshot 2025-06-09 at 19 52 38" src="https://github.com/user-attachments/assets/ff9132e0-bbb0-4774-aa98-bd133036dd7e" />


###  Happy hacking! 🥕
