import argparse
import json
from pathlib import Path


def read_number(file_path: Path) -> float:
    """Read a single number from a text file."""
    with open(file_path, "r", encoding="utf-8") as file:
        return float(file.read().strip())


def compute_score(ground_truth: float, prediction: float) -> dict:
    """
    Compute a simple dummy score.

    A perfect prediction gives 100.
    A larger error gives a lower score.
    """
    error = abs(ground_truth - prediction)
    score = max(0.0, 100.0 - error * 10.0)

    return {
        "score": score,
        "error": error,
        "ground_truth": ground_truth,
        "prediction": prediction,
    }


def main():
    parser = argparse.ArgumentParser(description="Dummy Codabench scoring program")

    parser.add_argument(
        "--reference_file",
        type=str,
        default=None,
        help="Path to the ground-truth file.",
    )

    parser.add_argument(
        "--prediction_file",
        type=str,
        default=None,
        help="Path to the submitted prediction file.",
    )

    parser.add_argument(
        "--output_dir",
        type=str,
        default=None,
        help="Directory where scores.json will be written.",
    )

    args = parser.parse_args()

    project_root = Path(__file__).resolve().parents[1]

    reference_file = (
        Path(args.reference_file)
        if args.reference_file
        else project_root / "reference_data" / "ground_truth.txt"
    )

    prediction_file = (
        Path(args.prediction_file)
        if args.prediction_file
        else project_root / "sample_result_submission" / "prediction.txt"
    )

    output_dir = (
        Path(args.output_dir)
        if args.output_dir
        else project_root / "scoring_output"
    )

    output_dir.mkdir(parents=True, exist_ok=True)

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