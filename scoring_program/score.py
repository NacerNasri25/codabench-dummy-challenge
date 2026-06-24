import json
from pathlib import Path


def find_file(possible_paths):
    """Return the first existing file from a list of possible paths."""
    for path in possible_paths:
        path = Path(path)
        if path.exists():
            return path
    raise FileNotFoundError(
        "None of the expected files were found:\n"
        + "\n".join(str(p) for p in possible_paths)
    )


def read_number(file_path: Path) -> float:
    """Read a single number from a text file."""
    with open(file_path, "r", encoding="utf-8") as file:
        return float(file.read().strip())


def compute_score(ground_truth: float, prediction: float) -> dict:
    """Compute a simple dummy score."""
    error = abs(ground_truth - prediction)
    score = max(0.0, 100.0 - error * 10.0)

    return {
        "score": score,
        "error": error,
        "ground_truth": ground_truth,
        "prediction": prediction,
    }


def main():
    project_root = Path(__file__).resolve().parents[1]

    reference_file = find_file(
        [
            project_root / "reference_data" / "ground_truth.txt",
            project_root / "ground_truth.txt",
            "/app/input/ref/ground_truth.txt",
            "/app/input/ref/reference_data/ground_truth.txt",
            "/app/reference_data/ground_truth.txt",
        ]
    )

    prediction_file = find_file(
        [
            project_root / "sample_result_submission" / "prediction.txt",
            project_root / "prediction.txt",
            "/app/input/res/prediction.txt",
            "/app/input/res/sample_result_submission/prediction.txt",
            "/app/sample_result_submission/prediction.txt",
        ]
    )

    output_dir_candidates = [
        Path("/app/output"),
        Path("/app/output/res"),
        project_root / "scoring_output",
    ]

    output_dir = None
    for candidate in output_dir_candidates:
        try:
            candidate.mkdir(parents=True, exist_ok=True)
            output_dir = candidate
            break
        except PermissionError:
            continue

    if output_dir is None:
        raise RuntimeError("No writable output directory found.")

    ground_truth = read_number(reference_file)
    prediction = read_number(prediction_file)

    scores = compute_score(ground_truth, prediction)

    scores_file = output_dir / "scores.json"

    with open(scores_file, "w", encoding="utf-8") as file:
        json.dump(scores, file, indent=4)

    print(f"Reference file: {reference_file}")
    print(f"Prediction file: {prediction_file}")
    print(f"Scores written to: {scores_file}")
    print(scores)


if __name__ == "__main__":
    main()