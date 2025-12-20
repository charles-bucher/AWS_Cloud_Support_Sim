import os

# Files smaller than this (in bytes) will be considered placeholders
PLACEHOLDER_SIZE_THRESHOLD = 100

def scan_repo(base_path):
    all_files = []
    placeholders = []

    for root, dirs, files in os.walk(base_path):
        for file in files:
            file_path = os.path.join(root, file)
            all_files.append(file_path)
            if os.path.getsize(file_path) < PLACEHOLDER_SIZE_THRESHOLD:
                placeholders.append(file_path)

    return all_files, placeholders

if __name__ == "__main__":
    base_repo_path = os.path.dirname(os.path.abspath(__file__))  # assumes script is in repo root
    all_files, placeholders = scan_repo(base_repo_path)

    print("\n===== Repo Scan Report =====\n")
    print(f"Total files found: {len(all_files)}\n")

    if placeholders:
        print(f"⚠️ Placeholder / tiny files ({len(placeholders)}):")
        for f in placeholders:
            print(f"   - {f}")
    else:
        print("✅ No placeholder files detected.")

    print("\nAll files scanned successfully.\n")
