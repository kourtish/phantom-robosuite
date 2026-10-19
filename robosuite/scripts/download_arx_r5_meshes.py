"""
Download the ARX R5 meshes used by the ARXR5 robot and ARXR5Gripper models.

The meshes come from ARX's official CAD export (ARXroboticsX/ARX_Model, R5/R5a) and are not
redistributed with robosuite. Run once after installation:

    python robosuite/scripts/download_arx_r5_meshes.py
"""
import os
import urllib.request

# Pinned ARX_Model commit for reproducibility
ARX_MODEL_COMMIT = "74386441845f12af4da203843b6400951d6c5530"
BASE_URL = f"https://raw.githubusercontent.com/ARXroboticsX/ARX_Model/{ARX_MODEL_COMMIT}/R5/R5a/meshes"

ASSETS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "models", "assets")
TARGETS = {
    os.path.join(ASSETS_DIR, "robots", "arx_r5", "meshes"): ["base_link", "link1", "link2", "link3", "link4", "link5", "link6"],
    os.path.join(ASSETS_DIR, "grippers", "meshes", "arx_r5_gripper"): ["link7", "link8"],
}


def main():
    for out_dir, names in TARGETS.items():
        os.makedirs(out_dir, exist_ok=True)
        for name in names:
            out_path = os.path.join(out_dir, f"{name}.STL")
            if os.path.exists(out_path):
                print(f"exists, skipping: {out_path}")
                continue
            urllib.request.urlretrieve(f"{BASE_URL}/{name}.STL", out_path)
            print(f"downloaded: {out_path}")


if __name__ == "__main__":
    main()
