from pathlib import Path

from scanner.hasher import calculate_sha256
from scanner.analyzer import analyze_file


def scan_directory(directory):
    directory = Path(directory)

    if not directory.exists():
        print("Directory does not exist.")
        return

    if not directory.is_dir():
        print("The provided path is not a directory.")
        return

    print("\nUSBGuard")
    print("=" * 60)
    print(f"Scanning: {directory}")
    print("=" * 60)

    files_scanned = 0

    for file_path in directory.rglob("*"):

        if not file_path.is_file():
            continue

        files_scanned += 1

        analysis = analyze_file(file_path)
        file_hash = calculate_sha256(file_path)

        print("\nFile:", file_path)
        print("SHA-256:", file_hash)
        print("Risk:", analysis["risk"])
        print("Score:", analysis["risk_score"])

        if analysis["reasons"]:
            print("Reasons:")

            for reason in analysis["reasons"]:
                print(" -", reason)

    print("\n" + "=" * 60)
    print(f"Files scanned: {files_scanned}")
    print("=" * 60)


if __name__ == "__main__":

    directory = input("Enter USB drive path (example E:\\): ")

    scan_directory(directory)