#!/usr/bin/env python3

from __future__ import annotations

import csv
import json
import shutil
from pathlib import Path

WORKSPACE_ROOT = Path(__file__).resolve().parents[2]
PRIVATE_REPO = WORKSPACE_ROOT / "euclid_qso_repo"
PUBLIC_REPO = Path(__file__).resolve().parents[1]

PRIVATE_SAMPLE_JSON = PRIVATE_REPO / "data" / "euclid-published-sample.json"
PRIVATE_COMPARISON_JSON = PRIVATE_REPO / "data" / "other-quasar-sample.json"
PRIVATE_SKY_MAP_JSON = PRIVATE_REPO / "data" / "sky-map-overlays.json"
PRIVATE_SITE_DATA_JS = PRIVATE_REPO / "assets" / "site-data.js"
PRIVATE_CUTOUT_DIR = PRIVATE_REPO / "assets" / "generated" / "cutouts"
PRIVATE_SPECTRUM_DIR = PRIVATE_REPO / "assets" / "generated" / "spectra"

PUBLIC_SAMPLE_JSON = PUBLIC_REPO / "data" / "euclid-published-sample.json"
PUBLIC_COMPARISON_JSON = PUBLIC_REPO / "data" / "other-quasar-sample.json"
PUBLIC_SKY_MAP_JSON = PUBLIC_REPO / "data" / "sky-map-overlays.json"
PUBLIC_SAMPLE_JS = PUBLIC_REPO / "assets" / "published-sample.js"
PUBLIC_SKY_MAP_JS = PUBLIC_REPO / "assets" / "sky-map-overlays.js"
PUBLIC_SITE_DATA_JS = PUBLIC_REPO / "assets" / "site-data.js"
PUBLIC_CSV = PUBLIC_REPO / "downloads" / "euclid-published-sample.csv"
PUBLIC_CUTOUT_DIR = PUBLIC_REPO / "assets" / "generated" / "cutouts"
PUBLIC_SPECTRUM_DIR = PUBLIC_REPO / "assets" / "generated" / "spectra"

# Published values from Yang et al. (2026), Table A.3.
PUBLISHED_VALUES = {
    "J1729+6410": (7.77, -25.05, 22.02),
    "J1253+7054": (7.69, -24.06, 22.97),
    "J1012+6630": (7.61, -23.98, 23.00),
    "J0522-5127": (7.50, -24.75, 22.17),
    "J1355+7000": (7.45, -25.01, 21.89),
    "J1445+7143": (7.36, -24.10, 22.78),
    "J1418+6949": (7.35, -24.00, 22.88),
    "J1631+6259": (7.33, -24.69, 22.19),
    "J0412-5639": (7.17, -24.41, 22.42),
    "J1340+6747": (7.05, -23.67, 23.12),
    "J1722+5741": (7.01, -23.93, 22.84),
    "J1614+4528": (7.00, -23.80, 22.97),
    "J0933+7427": (6.96, -24.98, 21.77),
    "J1555+5152": (6.95, -24.53, 22.22),
    "J0502-3849": (6.90, -25.46, 21.27),
    "J0526-4609": (6.89, -25.19, 21.54),
    "J0250-5317": (6.86, -25.17, 21.55),
    "J1707+6502": (6.84, -24.46, 22.25),
    "J1543+4718": (6.84, -24.35, 22.36),
    "J0252-4125": (6.83, -25.32, 21.39),
    "J1434+6857": (6.82, -23.67, 23.04),
    "J1505+7734": (6.72, -24.52, 22.06),
    "J1537+5829": (6.68, -24.10, 22.58),
    "J0443-5332": (6.67, -24.45, 22.22),
    "J0451-3426": (6.65, -24.57, 22.10),
    "J1155+7046": (6.65, -23.84, 22.83),
    "J0446-5700": (6.64, -24.19, 22.48),
    "J0916+6836": (6.64, -24.94, 21.73),
    "J1811+6145": (6.63, -24.60, 22.07),
    "J1732+6016": (6.61, -25.37, 21.30),
    "J0315-6844": (6.60, -25.42, 21.26),
}

PUBLISHED_SUPPLEMENTS = [
    {
        "id": "J0502-3849",
        "name": "J0502-3849",
        "ra": "75.670542",
        "dec": "-38.818361",
        "instrument": "FIRE",
        "group": "Published",
        "paperIds": [],
    }
]


def load_json(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8"))


def save_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def prepare_public_sample(
    private_sample: list[dict[str, object]],
) -> tuple[list[dict[str, object]], dict[str, str]]:
    public_sample: list[dict[str, object]] = []
    name_map: dict[str, str] = {}

    source_sample = list(private_sample)
    existing_ids = {str(row["id"]) for row in source_sample}
    source_sample.extend(
        row for row in PUBLISHED_SUPPLEMENTS if str(row["id"]) not in existing_ids
    )

    for row in source_sample:
        identifier = str(row["id"])
        redshift, muv, jmag = PUBLISHED_VALUES[identifier]
        name_map[identifier] = identifier

        public_sample.append(
            {
                "id": identifier,
                "name": str(row.get("name", identifier)),
                "ra": str(row["ra"]),
                "dec": str(row["dec"]),
                "redshift": redshift,
                "muv": muv,
                "jmag": jmag,
                "group": row.get("group", "Published"),
                "instrument": row.get("instrument", "Unknown"),
                "publication": "Yang et al. (2026)",
                "summary": "Published Euclid high-redshift quasar from Yang et al. (2026).",
                "paperIds": row.get("paperIds", []),
                "cutoutPreview": f"assets/generated/cutouts/{identifier}.png",
                "spectrumPreview": f"assets/generated/spectra/{identifier}.png",
                "cutoutPath": "",
                "spectrumPath": "",
            }
        )

    public_sample.sort(
        key=lambda item: (float(item["redshift"]), str(item["name"]))
    )
    return public_sample, name_map


def sanitize_sky_map(private_sky_map: dict[str, object]) -> dict[str, object]:
    payload = dict(private_sky_map)
    payload["footprintSource"] = "Sanitized public demo"
    return payload


def sanitize_site_data(name_map: dict[str, str]) -> None:
    site_data_text = PRIVATE_SITE_DATA_JS.read_text(encoding="utf-8")

    for original_name, fake_name in name_map.items():
        site_data_text = site_data_text.replace(f'"{original_name}"', f'"{fake_name}"')

    PUBLIC_SITE_DATA_JS.write_text(site_data_text, encoding="utf-8")


def write_public_sample_bundle(
    sample: list[dict[str, object]],
    comparison_sample: list[dict[str, object]],
) -> None:
    PUBLIC_SAMPLE_JS.write_text(
        "window.EuclidPublishedSample = "
        + json.dumps(sample, indent=2)
        + ";\nwindow.EuclidComparisonSample = "
        + json.dumps(comparison_sample, indent=2)
        + ";\n",
        encoding="utf-8",
    )


def write_public_sky_map_bundle(sky_map_payload: dict[str, object]) -> None:
    PUBLIC_SKY_MAP_JS.write_text(
        "window.EuclidSkyMapOverlays = "
        + json.dumps(sky_map_payload, separators=(",", ":"))
        + ";\n",
        encoding="utf-8",
    )


def write_public_csv(sample: list[dict[str, object]]) -> None:
    PUBLIC_CSV.parent.mkdir(parents=True, exist_ok=True)
    with PUBLIC_CSV.open("w", newline="", encoding="utf-8") as handle:
        fieldnames = ["name", "ra", "dec", "redshift", "muv", "jmag", "instrument", "publication"]
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()

        for row in sample:
            writer.writerow({field: row[field] for field in fieldnames})


def copy_preview_assets(sample: list[dict[str, object]]) -> None:
    PUBLIC_CUTOUT_DIR.mkdir(parents=True, exist_ok=True)
    PUBLIC_SPECTRUM_DIR.mkdir(parents=True, exist_ok=True)

    for row in sample:
        identifier = str(row["id"])
        source_cutout = PRIVATE_CUTOUT_DIR / f"{identifier}.png"
        source_spectrum = PRIVATE_SPECTRUM_DIR / f"{identifier}.png"

        if not source_cutout.is_file():
            raise FileNotFoundError(f"Missing cutout preview: {source_cutout}")
        if not source_spectrum.is_file():
            raise FileNotFoundError(f"Missing spectrum preview: {source_spectrum}")

        shutil.copy2(source_cutout, PUBLIC_CUTOUT_DIR / source_cutout.name)
        shutil.copy2(source_spectrum, PUBLIC_SPECTRUM_DIR / source_spectrum.name)


def main() -> None:
    private_sample = load_json(PRIVATE_SAMPLE_JSON)
    comparison_sample = load_json(PRIVATE_COMPARISON_JSON)
    private_sky_map = load_json(PRIVATE_SKY_MAP_JSON)

    if not isinstance(private_sample, list):
        raise ValueError("Expected private sample JSON to contain a list.")
    if not isinstance(comparison_sample, list):
        raise ValueError("Expected private comparison JSON to contain a list.")
    if not isinstance(private_sky_map, dict):
        raise ValueError("Expected private sky map JSON to contain an object.")

    public_sample, name_map = prepare_public_sample(private_sample)
    public_sky_map = sanitize_sky_map(private_sky_map)

    save_json(PUBLIC_SAMPLE_JSON, public_sample)
    save_json(PUBLIC_COMPARISON_JSON, comparison_sample)
    save_json(PUBLIC_SKY_MAP_JSON, public_sky_map)
    write_public_sample_bundle(public_sample, comparison_sample)
    write_public_sky_map_bundle(public_sky_map)
    sanitize_site_data(name_map)
    write_public_csv(public_sample)
    copy_preview_assets(public_sample)

    print(f"Wrote {len(public_sample)} real public quasars with scrubbed file paths.")
    print(f"Wrote {len(comparison_sample)} comparison quasars.")
    print("Wrote scrubbed sky-map overlays and real cutout/spectrum preview images.")


if __name__ == "__main__":
    main()
