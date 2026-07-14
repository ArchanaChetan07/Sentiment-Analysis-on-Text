# Lexicon Sentiment Analysis on Lyrics & Twitter

### ADS 509 Module 6 assignment scoring song and tweet sentiment with polarity lexicons.

[![GitHub](https://img.shields.io/badge/repo-Sentiment-Analysis-on-Text-181717?logo=github)](https://github.com/ArchanaChetan07/Sentiment-Analysis-on-Text)
[![Language](https://img.shields.io/badge/language-Jupyter%20Notebook-3572A5)](https://github.com/ArchanaChetan07/Sentiment-Analysis-on-Text)
[![License](https://img.shields.io/badge/license-See%20repository-yellow)](https://github.com/ArchanaChetan07/Sentiment-Analysis-on-Text)
[![CI](https://img.shields.io/badge/CI-GitHub%20Actions-2088FF?logo=githubactions&logoColor=white)](https://github.com/ArchanaChetan07/Sentiment-Analysis-on-Text/actions)

---

## Overview

Score sentiment of artist lyrics and Twitter corpora using positive/negative and tidytext lexicons.

Sentiment Assignment.ipynb loads lyrics/twitter folders plus positive-words.txt, negative-words.txt, tidytext_sentiments.txt; sums word polarity scores per song; compares top/bottom songs.

Completed course assignment notebook pattern with bundled lexicons (external corpora paths often local).

This repository is maintained as **production-minded portfolio work**: clear architecture, automated checks where present, and metrics that are **traceable to committed artifacts** (never invented).

---

## Architecture

Lyrics + Twitter files + lexicons â†’ tokenize words â†’ sum polarity â†’ rank songs / analyze tweets â†’ plots.

```mermaid
flowchart LR
  L[Lyrics/Twitter] --> S[Sentiment Assignment.ipynb]
  X[positive/negative/tidytext lexicons] --> S
  S --> R[Song scores + rankings]
```

```mermaid
sequenceDiagram
  participant U as User/Client
  participant S as Service/Pipeline
  participant E as Eval/Tools
  U->>S: request / job
  S->>E: execute
  E-->>S: results
  S-->>U: report / response
```

---

## Results & repository facts

> Only values found in code, configs, tests, or generated reports are listed. Absence of a clinical/ML accuracy number means it was **not** published in-repo.

| Metric | Value | Source |
|---|---|---|
| Tracked repository files | **8** | `git tree` |
| Notebook cells | **24** | `Sentiment Assignment.ipynb` |
| Tracked files | **8** | `git tree` |
| Python modules | **1** | `git tree` |
| Test-related paths | **1** | `git tree` |
| CI workflows | **Yes** | `.github/workflows` |
| Docker present | **No** | `repo root` |

```mermaid
%%{init: {'theme':'base'}}%%
pie showData title Language composition (bytes)
    "Jupyter Notebook" : 99
    "Python" : 1
```

---

## Key features

- Manual lexicon scoring (+1/-1)
- Bundled positive/negative/tidytext lexicons
- Song-level ranking examples in notebook

---

## Tech stack

| Layer | Technology |
|---|---|
| nlp | Lexicon sentiment |
| nlp | NLTK |
| data | pandas |
| viz | matplotlib/seaborn |
| ci | GitHub Actions |

---

## Skills demonstrated

Jupyter Notebook · p · a · n · d · s · CI/CD · testing · automation

Keyword surface: **Python · Jupyter Notebook · machine-learning · CI/CD · testing · API · Docker · automation · data-science · software-engineering · system-design · observability · LLM · cloud**

---

## Project structure

```text
Sentiment-Analysis-on-Text/
â”œâ”€â”€ Sentiment Assignment.ipynb
â”œâ”€â”€ positive-words.txt
â”œâ”€â”€ negative-words.txt
â”œâ”€â”€ tidytext_sentiments.txt
â”œâ”€â”€ requirements.txt
â””â”€â”€ tests/
```

---

## Installation & usage

```bash
git clone https://github.com/ArchanaChetan07/Sentiment-Analysis-on-Text.git
cd Sentiment-Analysis-on-Text
pip install -r requirements.txt
jupyter notebook "Sentiment Assignment.ipynb"
```

---

## How it works

After pointing data_location at lyrics/twitter folders, the notebook builds a sentiment dictionary from lexicons and scores each song by summing word polarities, then answers comparative questions.

---

## Future improvements

- Make data_location relative / ship sample subset
- Export summary tables as CSV artifacts

---

## License

See repository.

---

<p align="center">
  <b>Lexicon Sentiment Analysis on Lyrics & Twitter</b><br/>
  <a href="https://github.com/ArchanaChetan07/Sentiment-Analysis-on-Text">github.com/ArchanaChetan07/Sentiment-Analysis-on-Text</a>
</p>
