from pathlib import Path


SUSPICIOUS_EXTENSIONS = {
    ".exe",
    ".scr",
    ".bat",
    ".cmd",
    ".vbs",
    ".vbe",
    ".js",
    ".jse",
    ".ps1",
    ".hta",
}


def analyze_file(file_path):
    path = Path(file_path)

    reasons = []
    score = 0

    extension = path.suffix.lower()

    # Suspicious executable/script extension
    if extension in SUSPICIOUS_EXTENSIONS:
        score += 40
        reasons.append(f"Suspicious file type: {extension}")

    # Double extension detection
    parts = path.name.lower().split(".")

    if len(parts) >= 3:
        suspicious_extensions = {
            ".exe",
            ".scr",
            ".bat",
            ".cmd",
            ".vbs",
            ".js",
        }

        if f".{parts[-1]}" in suspicious_extensions:
            score += 30
            reasons.append("Possible double-extension disguise")

    # Suspicious filename
    suspicious_names = {
        "autorun.inf",
        "autorun.exe",
    }

    if path.name.lower() in suspicious_names:
        score += 30
        reasons.append("Suspicious autorun-related filename")

    if score >= 70:
        risk = "HIGH"
    elif score >= 40:
        risk = "SUSPICIOUS"
    else:
        risk = "LOW"

    return {
        "file": str(path),
        "risk_score": score,
        "risk": risk,
        "reasons": reasons,
    }