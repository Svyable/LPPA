# Legacy Leia image candidates — upload landing folder

This folder contains **unapproved source references**, not print-ready pages or publicly approved artwork.

To import existing Leia PNGs through GitHub:

1. Open this directory in the GitHub web interface.
2. Choose **Add file → Upload files** and drag in the *individual PNG files* (extract any ZIP first).
3. Select **Create a new branch for this commit and start a pull request** (or commit to main if working alone).
4. Keep original filenames and avoid replacing existing images.
5. After upload, update `../candidate-assets.json` and `../ASSET-AUDIT.md` with actual image paths, dimensions, provenance, review status and scene affinities.

Only record `binary_state: imported` after confirming a PNG is really committed to this repository. Never label a candidate as print-ready or use it on the public website without the appropriate approval.

There are filename collisions in the old library (for example, some `image-gen-*.png` names refer to unrelated technical diagrams). Check the image **visually**, not only its filename.
