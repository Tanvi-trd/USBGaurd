# USBGuard

**USBGuard** is a lightweight Python-based USB security scanner designed to identify potentially suspicious files on removable storage devices.

The project performs static file analysis by calculating **SHA-256 cryptographic hashes** and applying **heuristic security rules** to detect suspicious file characteristics such as executable extensions, double extensions, and autorun-related filenames.

>  USBGuard is an educational security screening tool, not a replacement for a full antivirus or endpoint protection solution.

---

##  Features

-  Recursive scanning of USB/removable-drive files
-  SHA-256 hash generation
-  Heuristic suspicious-file detection
-  Detection of suspicious executable/script extensions
-  Double-extension detection
-  Autorun-related filename detection
-  Risk scoring system
-  LOW /  SUSPICIOUS /  HIGH risk classification
- Lightweight and built using Python's standard library

---

##  How It Works

```text
USB Drive
    │
    ▼
User provides USB path
    │
    ▼
Directory Scanner
    │
    ▼
File Enumeration
    │
    ├───────────────┐
    ▼               ▼
SHA-256         Heuristic
Hashing         Analysis
    │               │
    └───────┬───────┘
            ▼
       Risk Scoring
            │
      ┌─────┼─────┐
      ▼     ▼     ▼
     LOW  SUSPICIOUS  HIGH

```
⚠️ Disclaimer

USBGuard is developed for educational and authorized security testing purposes only.
Do not use this tool to inspect systems, removable drives, or files without appropriate authorization.
USBGuard does not guarantee malware detection and should not be used as a replacement for professional antivirus or endpoint security software.


👩‍💻 Author
Tanvi R. Devadiga
Computer Science & Engineering Student
Cybersecurity| Network Security| and Ethical Hacking.
