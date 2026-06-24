# Tutorial

This page explains how to submit to the dummy Codabench challenge.

## 1. Goal of the Challenge

The goal of this dummy challenge is to test the Codabench workflow.

A participant submits a number, and the scoring program compares it with the reference value.

## 2. Submission Format

The submission must be a ZIP file containing one file:

```text
prediction.txt
3. Creating the Submission ZIP

The expected submission ZIP is:

sample_result_submission.zip

It should contain:

prediction.txt

Important: prediction.txt should be directly inside the ZIP file, not inside an extra folder.

Correct:

sample_result_submission.zip
└── prediction.txt

Wrong:

sample_result_submission.zip
└── sample_result_submission/
    └── prediction.txt
4. Scoring

The scoring program compares the submitted prediction with the reference value.

error = abs(ground_truth - prediction)
score = max(0, 100 - error * 10)

Example:

ground_truth = 10
prediction = 8
error = 2
score = 80
5. Results

The leaderboard shows the numerical score.

The scoring program also writes a detailed HTML result file to test whether Codabench can display additional outputs beyond numbers.

This can later be adapted for the real benchmark, for example to show:

qualitative examples
images
visualizations
detailed per-sample results



```text