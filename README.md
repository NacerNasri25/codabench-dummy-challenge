# Codabench Dummy Challenge

This repository contains a minimal dummy Codabench challenge.
The goal is to understand the basic Codabench workflow before integrating the real benchmark evaluation code.

## Goal

This dummy challenge tests the complete benchmark workflow in a simple way:

1. A participant submits a prediction file.
2. The scoring program reads the prediction.
3. The scoring program reads the reference data.
4. A simple metric is computed.
5. The result is written to `scores.json`.

## Dummy Task

The task is to predict a single number.

The reference data contains the correct value:

```text
reference_data/ground_truth.txt
```

Example:

```text
10
```

The sample submission contains a predicted value:

```text
sample_result_submission/prediction.txt
```

Example:

```text
8
```

## Scoring Rule

The scoring program computes the absolute error between the ground truth and the prediction:

```text
error = abs(ground_truth - prediction)
```

The final score is computed as:

```text
score = max(0, 100 - error * 10)
```

Example:

```text
ground_truth = 10
prediction = 8
error = 2
score = 80
```

## Repository Structure

```text
codabench-dummy-challenge/
├── competition.yaml
├── Dockerfile
├── README.md
├── requirements.txt
├── reference_data/
│   └── ground_truth.txt
├── sample_result_submission/
│   └── prediction.txt
├── scoring_program/
│   ├── metadata.yaml
│   └── score.py
└── bundles/
    ├── scoring_program.zip
    ├── reference_data.zip
    └── sample_result_submission.zip
```

## Local Test

Run the scoring program locally:

```bash
python scoring_program/score.py
```

Expected output:

```text
score = 80.0
error = 2.0
ground_truth = 10.0
prediction = 8.0
```

The result is written to:

```text
scoring_output/scores.json
```

## Local Test with Explicit Paths

The scoring script also supports explicit input/output paths:

```bash
python scoring_program/score.py \
  --reference_file reference_data/ground_truth.txt \
  --prediction_file sample_result_submission/prediction.txt \
  --output_dir test_output
```

The result is written to:

```text
test_output/scores.json
```

## Docker Test

Build the Docker image:

```bash
docker build -t codabench-dummy-challenge .
```

Run the Docker image:

```bash
docker run --rm codabench-dummy-challenge
```

## Docker Test with Mounted Volumes

This simulates a more Codabench-like execution where input/output folders are mounted into the container:

```bash
mkdir -p docker_test_output

docker run --rm \
  -v "$(pwd)/reference_data:/app/reference_data" \
  -v "$(pwd)/sample_result_submission:/app/sample_result_submission" \
  -v "$(pwd)/docker_test_output:/app/scoring_output" \
  codabench-dummy-challenge
```

The result is written to:

```text
docker_test_output/scores.json
```

## Bundle Files

The current dummy bundle files are stored in:

```text
bundles/
```

They were created using:

```bash
mkdir -p bundles

zip -r bundles/scoring_program.zip scoring_program
zip -r bundles/reference_data.zip reference_data
zip -r bundles/sample_result_submission.zip sample_result_submission
```

## Current Status

The following parts have been tested successfully:

* Local scoring script
* `scores.json` generation
* Docker build
* Docker execution
* Docker execution with mounted folders
* Basic Codabench-style zip bundles

## Next Step

The next step is to define a minimal `competition.yaml` file for the dummy challenge and test whether the bundle can be uploaded or imported into Codabench.
