#!/usr/bin/env python3
"""Upload Pencil2D binaries to GitLab Generic Package Registry."""

import argparse
import os
import sys
from pathlib import Path
from urllib.parse import quote

import requests

# Hardcode the token here, or leave empty to fall back to the environment variable
GITLAB_ACCESS_TOKEN = ""

GITLAB_PROJECT = "chchwy%2Fpencil2d"  # URL-encoded "chchwy/pencil2d"
GITLAB_API_URL = f"https://gitlab.com/api/v4/projects/{GITLAB_PROJECT}/packages/generic"
PACKAGE_NAME = "pencil2d"

FILES = [
    "pencil2d-win32-{version}.zip",
    "pencil2d-win64-{version}.zip",
    "pencil2d-winxp-{version}.zip",
    "pencil2d-mac-{version}.dmg",
    "pencil2d-mac-legacy-{version}.dmg",
    "pencil2d-linux-i386-{version}.AppImage",
    "pencil2d-linux-amd64-{version}.AppImage",
]


def get_token():
    token = GITLAB_ACCESS_TOKEN or os.environ.get("GITLAB_ACCESS_TOKEN", "")
    if not token:
        print("Error: No access token found.")
        print("Either set GITLAB_ACCESS_TOKEN in the script or as an environment variable.")
        sys.exit(1)
    return token


def upload_file(token, version, filepath):
    """Upload a single file to GitLab Generic Package Registry.

    PUT /projects/:id/packages/generic/:package_name/:package_version/:file_name
    """
    filename = filepath.name
    url = f"{GITLAB_API_URL}/{PACKAGE_NAME}/{version}/{quote(filename)}"
    headers = {"PRIVATE-TOKEN": token}

    file_size = filepath.stat().st_size
    print(f"Uploading {filename} ({file_size / (1024*1024):.1f} MB)... ", end="", flush=True)

    with open(filepath, "rb") as f:
        resp = requests.put(url, headers=headers, data=f)

    if resp.status_code == 201:
        print("OK")
        return True
    else:
        print(f"FAILED (HTTP {resp.status_code})")
        print(f"  Response: {resp.text}")
        return False


def main():
    parser = argparse.ArgumentParser(description="Upload Pencil2D binaries to GitLab Package Registry.")
    parser.add_argument("version", help="Release version (e.g. 0.7.0)")
    args = parser.parse_args()

    version = args.version
    token = get_token()
    script_dir = Path(__file__).resolve().parent

    # Check which files exist
    file_paths = []
    for template in FILES:
        filename = template.format(version=version)
        filepath = script_dir / filename
        if filepath.is_file():
            file_paths.append(filepath)
        else:
            print(f"Warning: {filename} not found, skipping.")

    if not file_paths:
        print("Error: No files found to upload.")
        sys.exit(1)

    print(f"Uploading {len(file_paths)} file(s) to GitLab Package Registry ({version})...")
    print()

    failed = []
    for filepath in file_paths:
        if not upload_file(token, version, filepath):
            failed.append(filepath.name)

    print()
    if failed:
        print(f"Failed to upload {len(failed)} file(s): {', '.join(failed)}")
        sys.exit(1)
    else:
        print("All files uploaded successfully.")


if __name__ == "__main__":
    main()
