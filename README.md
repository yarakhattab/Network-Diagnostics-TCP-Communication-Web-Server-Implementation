
---

# 🌐 ENCS3320 - Computer Networks Project

## 📖 About the Project
This repository showcases the first project completed for the **Computer Networks (ENCS3320)** course at **Birzeit University**. The project is divided into three distinct sections, each designed to deepen understanding of core networking concepts and practical implementations:

1. **Network Analysis Tools** – Utilizing diagnostic utilities and Wireshark for inspection.
2. **TCP-Based Server-Client Model** – Verifying student IDs and executing system-level actions.
3. **Web Server Design** – Serving static resources and handling different HTTP request types.

---

## ⚙️ Project Components

### 🔍 Part 1: Network Tools Exploration
- Conducted network tests (ping, tracert, nslookup) on `www.cornell.edu`.
- Used **Wireshark** to examine DNS communications.
- Gained insight into how basic tools reveal underlying network behavior.

### 🔗 Part 2: Client-Server TCP Application
- **Port:** 9955  
- Developed using **Python sockets**.
- The server:
  - Accepts and validates student ID input.
  - If valid, notifies client of a screen lock and delays for 10 seconds before executing it.
  - Sends error feedback if ID is invalid.

### 🌐 Part 3: Lightweight Web Server
- **Port:** 9966  
- Handles:
  - Static content requests (HTML, CSS, PNG, JPG).
  - Redirections for endpoints like `/cr`, `/so`, and `/rt`.
  - Proper HTTP responses (200, 404, etc.).
- Supports access via both **desktop and mobile clients**.

---


## 💻 Setup & Requirements

- **Python** – Required for TCP and web server components  
- **Wireshark** – For packet analysis and DNS monitoring  
- Basic understanding of networking concepts and HTTP behavior

---

## 👩‍💻 Contributors

- **Saja Asfour**  
  🎓 Computer Engineering – Birzeit University  
  🔗 [GitHub: SajaAsfour](https://github.com/SajaAsfour)

- **Shahd Shreteh**  
  🎓 Computer Engineering – Birzeit University  
  🔗 [GitHub: ShahdShreteh](https://github.com/ShahdShreteh)

- **Rawand Bawatneh**  
  🎓 Computer Engineering – Birzeit University  
  🔗 [GitHub: rawandbawatneh](https://github.com/rawandbawatneh)

---

## 📘 License
This project is intended for academic learning. Feel free to explore and use the contents, but please provide appropriate attribution. 😊

---

Let me know if you'd like a downloadable version or a version formatted specifically for GitHub Markdown.
