# Demo Python ML/AI Modules

This repository appears to be a school/practice repository for learning Python data
science, machine learning, and AI fundamentals. It contains lesson-style scripts,
a neural-network class from a notebook exercise, a small Transformer tokenization
demo, and an added importable Python package with unit-tested versions of the
most reusable concepts.

The original files are mostly exploratory scripts: they generate random data,
print intermediate values, plot charts, train small models, or demonstrate
library APIs. That is useful for assignments and notebooks, but it is not ideal
for automated unit testing because many files execute work at import time, open
plots, require local datasets, or rely on optional external downloads. To satisfy
the repository requirement that it contain unit-tested code, the reusable
concepts have been extracted into `src/ml_ai_modules/` and covered with pytest.

## What This Repository Does

At a high level, this repo demonstrates:

- Basic statistics: mean, median, mode, standard deviation, variance,
  percentiles, moments, covariance, and correlation.
- Probability: conditional probability and simulated purchase behavior.
- Data visualization: Matplotlib, Seaborn, histograms, scatter plots, bar charts,
  and statistical distributions.
- Regression: linear regression, polynomial regression, multiple regression, and
  train/test evaluation.
- Classification: decision trees, random forests, naive Bayes, support-vector
  machines, k-nearest neighbors, and XGBoost.
- Clustering and dimensionality reduction: k-means clustering and principal
  component analysis.
- Recommender-system ideas: item similarity and item-based collaborative
  filtering.
- Reinforcement learning setup: an OpenAI Gym Taxi environment example.
- Neural-network fundamentals: a simple feed-forward neural-network class with
  sigmoid activation and backpropagation.
- Transformer tokenization: a GPT-2 tokenizer/model loading example using the
  Hugging Face `transformers` package.

## Repository Layout

```text
.
├── .github/
│   ├── dependabot.yml
│   └── workflows/ci.yml
├── neural-network-template/
│   ├── neuralNetworkClass.py
│   ├── neuralNetworkNot.ipynb
│   └── nn-test-interface.py
├── python-exercises/
│   ├── PastHires.csv
│   ├── sample.csv
│   └── *.py lesson scripts
├── src/ml_ai_modules/
│   ├── probability.py
│   ├── regression.py
│   ├── similarity.py
│   └── statistics.py
├── tests/
├── transformers/tokenization.py
├── pyproject.toml
└── requirements-dev.txt
```

## Original Exercise Scripts

The `python-exercises/` directory contains the original assignment/practice
files. Most of them are intended to be run as scripts rather than imported as a
library.

| File | Purpose |
| --- | --- |
| `conditional-probabilty.py` | Simulates age-decade purchases and demonstrates conditional probability. |
| `mean-median-mode.py` | Shows how outliers affect mean vs. median. |
| `standard-dev-var.py` | Demonstrates standard deviation and variance. |
| `percentile.py` | Demonstrates percentile calculations. |
| `moments.py` | Explores distribution moments such as mean, variance, skew, and kurtosis. |
| `distributions.py` | Plots uniform, normal, exponential, binomial, and Poisson distributions. |
| `covariance-correlation.py` | Implements covariance/correlation helpers and compares them to NumPy. |
| `linear-regression.py` | Fits a simple linear regression with SciPy and plots the fitted line. |
| `poynomial-regression.py` | Demonstrates polynomial regression and curve fitting. |
| `mulitple-regressions.py` | Demonstrates multiple regression with tabular data. |
| `train-test.py` | Splits data into train/test sets and compares fit quality. |
| `decision-trees.py` | Uses `PastHires.csv` to train a decision tree and random forest. |
| `k-nearest-neighbors.py` | Demonstrates KNN classification. |
| `support-vector-machines.py` | Demonstrates SVM classification. |
| `xg-boosting.py` | Demonstrates gradient boosting with XGBoost. |
| `k-means-clustering.py` | Demonstrates unsupervised clustering. |
| `principle-comp-analysis.py` | Demonstrates principal component analysis. |
| `pandas-sample.py` | Demonstrates Pandas CSV/dataframe operations with `sample.csv`. |
| `generate-fake-data.py` | Generates synthetic data for examples. |
| `matplotlib-intro.py` | Introductory Matplotlib plotting exercise. |
| `matplotlib-other-plots.py` | Additional Matplotlib chart types. |
| `seaborn-plots.py` | Seaborn visualization examples. |
| `finding-similiar-items.py` | Item similarity exercise. |
| `item-based-collab-filtering.py` | Item-based collaborative filtering using MovieLens-style data. |
| `naive-bayes-span-classifier.py` | Naive Bayes spam classifier using local `emails/` data. |
| `q-learning.py` | Sets up the OpenAI Gym Taxi environment for reinforcement learning. |

Some scripts reference datasets that are intentionally ignored by git:

- `emails/`
- `ml-100k/`

Those are likely local course datasets. The checked-in tests do not require them.

## Tested Code

The tested package lives in `src/ml_ai_modules/`.

| Module | Tested behavior |
| --- | --- |
| `statistics.py` | Mean, median, mode, percentile, de-meaning, and sample covariance. |
| `probability.py` | Conditional probability and deterministic age-purchase simulation. |
| `regression.py` | Ordered train/test splitting and polynomial regression R-squared scoring. |
| `similarity.py` | Genre/popularity item distance and nearest-neighbor lookup. |

The test suite also directly loads and tests
`neural-network-template/neuralNetworkClass.py` to verify:

- constructor state and generated weight matrix shapes;
- getter/setter behavior;
- query output shape and sigmoid output range;
- training updates both weight matrices.

## Setup

Create and activate a virtual environment, then install the development
dependencies:

```bash
python -m venv .venv
python -m pip install -r requirements-dev.txt
```

The `requirements-dev.txt` file installs the local package in editable mode and
includes pytest, coverage support, Ruff, Bandit, and pip-audit.

## Unit Tests

Run the unit tests with coverage:

```bash
python -m pytest
```

Pytest is configured in `pyproject.toml` to:

- discover tests from `tests/`;
- include `src/` on the Python path;
- measure coverage for `src/ml_ai_modules/` and
  `neural-network-template/`;
- omit the interactive `nn-test-interface.py` demo from coverage;
- fail the run if total coverage drops below 90%.

Current local result:

```text
36 passed
Total coverage: 98.28%
```

## Quality and Security Commands

Run the same local quality and security checks used by CI:

```bash
python -m ruff check src tests neural-network-template/neuralNetworkClass.py
python -m bandit -r src neural-network-template -x neural-network-template/nn-test-interface.py
python -m pip_audit -r requirements-dev.txt
```

Notes:

- Ruff checks the importable/tested code and tests. The old lesson scripts are
  intentionally excluded from the quality gate because they are classroom-style
  one-off scripts with plotting, wildcard imports, top-level execution, and
  optional local datasets.
- Bandit scans the source package and neural-network class. The deterministic
  random-number generator in `probability.py` is marked `# nosec B311` because it
  is a reproducible lesson simulation, not security or cryptographic code.
- `pip-audit` checks Python dependencies for known vulnerabilities.

## GitHub Actions Pipeline

The workflow is defined in `.github/workflows/ci.yml` and runs on every push and
pull request.

### Unit Tests

The `unit-tests` job:

1. checks out the repository;
2. installs Python 3.12;
3. installs `requirements-dev.txt`;
4. runs `python -m pytest`;
5. enforces the 90% coverage floor from `pyproject.toml`.

### Code Scanning: Quality

The `quality-scan` job:

1. installs the development dependencies;
2. runs Ruff against the tested/importable code paths;
3. writes Ruff results as SARIF;
4. uploads the SARIF file with `github/codeql-action/upload-sarif`.

This makes quality findings visible in GitHub's code scanning UI when code
scanning is available for the repository.

### Code Scanning: Security

The pipeline has multiple security layers:

- `security-scan` runs Bandit against the Python source and neural-network class.
- `security-scan` runs `pip-audit` against `requirements-dev.txt`.
- `codeql` runs GitHub CodeQL analysis for Python.
- `dependency-review` runs GitHub's dependency review action on pull requests.

CodeQL provides the native GitHub code-scanning security integration. Bandit and
pip-audit provide fast Python-specific security gates in the normal Actions log.

### Dependabot

The `.github/dependabot.yml` file enables weekly update checks for:

- Python dependencies in the repository root;
- GitHub Actions versions.

This helps keep CI actions and Python tooling current without manually checking
for updates.

## GitHub Security Features Used

The workflow uses free GitHub-native features that are appropriate for this
repository:

- CodeQL code scanning for Python:
  <https://docs.github.com/en/code-security/code-scanning/introduction-to-code-scanning/about-code-scanning-with-codeql>
- SARIF upload for third-party analysis results:
  <https://docs.github.com/en/code-security/code-scanning/integrating-with-code-scanning/uploading-a-sarif-file-to-github>
- Dependency Review Action:
  <https://github.com/actions/dependency-review-action>
- Dependabot version updates:
  <https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/about-dependabot-version-updates>

## Working With the Original Scripts

The original lesson scripts can still be run directly, but many require extra
libraries or datasets that are not part of the unit-test dependency set. For
example:

- plotting scripts require Matplotlib and sometimes Seaborn;
- model scripts may require Pandas, scikit-learn, XGBoost, or Gym;
- NLP examples may require local `emails/` data;
- recommender examples may require MovieLens `ml-100k/` data;
- `transformers/tokenization.py` requires Hugging Face `transformers`, PyTorch,
  and network/cache access for GPT-2 model files.

For reproducible automation, prefer adding reusable logic to `src/ml_ai_modules/`
and covering it with tests in `tests/`.
