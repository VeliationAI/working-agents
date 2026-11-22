"""Download DoTA (Detection of Traffic Anomaly) dataset media.

Official sources (as of 2026-11):
  - Annotations / metadata / scripts: GitHub dataset/ folder (works)
  - Extracted frames (~55GB) Google Drive: DEAD (404)
  - Split zip folder Google Drive: DEAD (404)
  - YouTube source URLs in DoTA_urls.txt: all removed / unavailable
  - Community Baidu mirror: https://pan.baidu.com/s/1XF1IIT2eVFiM-Tr72qTHuw?pwd=1919
    (requires a Baidu account; password 1919)

This script:
  1) Ensures GitHub annotation package is present under data/raw/dota/
  2) Probes Drive + YouTube and reports status
  3) Optionally downloads CCD Crash-1500 dashcam clips (working Drive mirror)
     so RoadGuard notebooks have real accident video while DoTA frames stay blocked.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import zipfile
from pathlib import Path
from urllib.request import urlretrieve

ROOT = Path(__file__).resolve().parents[1]
DOTA = ROOT / "data" / "raw" / "dota"
CCD = ROOT / "data" / "raw" / "ccd"
GITHUB_BASE = (
    "https://raw.githubusercontent.com/MoonBlvd/"
    "Detection-of-Traffic-Anomaly/master/dataset"
)
ANNOT_ZIP_URL = (
    "https://github.com/MoonBlvd/Detection-of-Traffic-Anomaly/"
    "raw/master/dataset/DoTA_annotations.zip"
)
DEAD_DRIVE = {
    "frames_55gb": "1RQp4hOP9X7TW6S3_vbqZvFSkrbbFzrRj",
    "frames_split_folder": "1_WzhwZC2NIpzZIpX7YCvapq66rtBc67n",
    "broken_videos_folder": "1uSdyNu8XM_QV6y9r4tpxN7iNNNAgWy9P",
    "fol_features_folder": "1IVCedrlPg03Fsg4tqDA2cWYlcdrsKUsp",
}
BAIDU_MIRROR = "https://pan.baidu.com/s/1XF1IIT2eVFiM-Tr72qTHuw?pwd=1919"
CCD_CRASH_ZIP_ID = "1fmcwGhr8JT9YfLUrlcvuCZ3ychi2eyFP"
CCD_CRASH_TXT_ID = "13OgrD0-8cKG0X00MlA6JXr0G_JJmHYXg"


def ensure_dota_annotations() -> None:
    DOTA.mkdir(parents=True, exist_ok=True)
    zip_path = DOTA / "DoTA_annotations.zip"
    if not zip_path.exists():
        print("Downloading DoTA_annotations.zip ...")
        urlretrieve(ANNOT_ZIP_URL, zip_path)
    ann_dir = DOTA / "annotations" / "annotations"
    if not ann_dir.exists() or not any(ann_dir.glob("*.json")):
        print("Extracting annotations ...")
        with zipfile.ZipFile(zip_path) as zf:
            zf.extractall(DOTA / "annotations")
    for name in (
        "DoTA_urls.txt",
        "broken_urls.txt",
        "metadata_train.json",
        "metadata_val.json",
        "train_split.txt",
        "val_split.txt",
        "download_DoTA.py",
        "video2frames.py",
        "dota.py",
    ):
        dest = DOTA / name
        if dest.exists():
            continue
        try:
            urlretrieve(f"{GITHUB_BASE}/{name}", dest)
            print("Fetched", name)
        except Exception as exc:  # noqa: BLE001
            print("Skip", name, exc)


def probe_youtube(limit: int = 20) -> dict:
    urls_path = DOTA / "DoTA_urls.txt"
    if not urls_path.exists():
        return {"ok": 0, "fail": 0, "note": "DoTA_urls.txt missing"}
    urls = [u.strip() for u in urls_path.read_text(encoding="utf-8").splitlines() if u.strip()]
    urls = urls[:limit]
    ok = fail = 0
    yt = ROOT / ".venv" / "Scripts" / "yt-dlp.exe"
    bin_path = str(yt if yt.exists() else "yt-dlp")
    for url in urls:
        try:
            r = subprocess.run(
                [bin_path, "--skip-download", "--print", "%(id)s", "--no-warnings", url],
                capture_output=True,
                text=True,
                timeout=60,
                check=False,
            )
            if r.returncode == 0:
                ok += 1
            else:
                fail += 1
        except Exception:  # noqa: BLE001
            fail += 1
    return {"ok": ok, "fail": fail, "probed": len(urls)}


def download_ccd_crash(copy_n: int = 10) -> None:
    try:
        import gdown
    except ImportError as exc:
        raise SystemExit("Install gdown in the project venv first.") from exc

    videos = CCD / "videos"
    videos.mkdir(parents=True, exist_ok=True)
    zip_path = videos / "Crash-1500.zip"
    txt_path = videos / "Crash-1500.txt"
    if not zip_path.exists():
        print("Downloading CCD Crash-1500.zip (~793MB) ...")
        gdown.download(id=CCD_CRASH_ZIP_ID, output=str(zip_path), quiet=False, resume=True)
    if not txt_path.exists():
        gdown.download(id=CCD_CRASH_TXT_ID, output=str(txt_path), quiet=False, resume=True)

    extract_dir = videos / "Crash-1500_extract"
    if not extract_dir.exists() or not any(extract_dir.glob("*.mp4")):
        print("Extracting Crash-1500.zip ...")
        with zipfile.ZipFile(zip_path) as zf:
            zf.extractall(extract_dir)

    out = DOTA / "videos"
    out.mkdir(parents=True, exist_ok=True)
    mp4s = sorted(extract_dir.glob("*.mp4"))[:copy_n]
    for src in mp4s:
        dest = out / f"ccd_crash_{src.stem}.mp4"
        if not dest.exists():
            dest.write_bytes(src.read_bytes())
            print("Copied", dest.name)
    print(f"CCD clips ready under {out} ({len(list(out.glob('ccd_crash_*.mp4')))} files)")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--probe-youtube", type=int, default=0, help="Probe N DoTA YouTube URLs")
    parser.add_argument("--ccd", action="store_true", help="Download CCD crash videos as interim media")
    parser.add_argument("--copy-n", type=int, default=10, help="CCD clips to copy into dota/videos")
    args = parser.parse_args()

    ensure_dota_annotations()
    status = {
        "dota_annotations": True,
        "official_drive": "dead_404",
        "baidu_mirror": BAIDU_MIRROR,
        "dead_drive_ids": DEAD_DRIVE,
    }
    if args.probe_youtube:
        status["youtube_probe"] = probe_youtube(args.probe_youtube)
    if args.ccd:
        download_ccd_crash(args.copy_n)
    print(json.dumps(status, indent=2))
    print(
        "\nDoTA frame archive is not publicly reachable via Google Drive anymore.\n"
        f"Use Baidu (login required): {BAIDU_MIRROR}\n"
        "Or run: python scripts/download_dota_media.py --ccd"
    )


if __name__ == "__main__":
    main()
