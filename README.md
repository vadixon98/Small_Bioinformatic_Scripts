<div align="center">

# Small Bioinformatic Scripts

**R and Python utilities for sequence analysis and common bioinformatics tasks**

[![R](https://img.shields.io/badge/R-3.6+-blue?logo=r)](https://www.r-project.org/)
[![Python](https://img.shields.io/badge/Python-3.8+-green?logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

</div>

---

## Overview

This repository is a set of **R** and **Python** scripts for working with sequence data, including:

- **Polymorphic site detection** in sequence alignments
- **Alignment-based polymorphism** analysis
- **Sequence processing** and manipulation
- **ORF detection** and open reading frame analysis
- **Motif scoring** and pattern matching

These are **teaching and small-workflow** scripts, not a maintained library or pipeline framework.

---

## Requirements

### R

* **R** 3.6 or later
* CRAN packages:
  - `seqinr` — read alignment files
  - `adegenet` — `alignment2genind` and `isPoly`

**Installation**

```r
install.packages(c("seqinr", "adegenet"))
```

### Python

* **Python** 3.8 or later (most scripts use the standard library only)

---

## Quick start

### R

```r
# Segregating-site helper and comments for alignment-based workflow
source("polymorphic_site_finder.R")

# Count segregating sites
n_segsites <- calc_segsites("bigcats")
print(n_segsites)
```

### Python

Run these from the repository root (or add it to `PYTHONPATH`) so modules like `dna` resolve.

```python
from dna import reverseComplement, codingStrandToAA
from orf import longestORF

dna_seq = "ATGCGATCG"
rev_comp = reverseComplement(dna_seq)
```

### Docker (Python)

The repository includes a `Dockerfile` that packages the top-level Python modules in a **Python 3.12** image. **R is not included** in that image; use a local R install or extend the image if you need the R scripts.

From the repository root, build and run:

```bash
docker build -t small-bioinformatic-scripts .
docker run --rm small-bioinformatic-scripts
```

The default container command runs a short import check (`dna.reverseComplement`). Override the command to run another script or an interactive shell, for example:

```bash
docker run --rm -it small-bioinformatic-scripts python3 -c "from orf import longestORF; print(longestORF('ATGTAATAG'))"
```

Rebuild the image after you change any `*.py` files at the repo root, since they are copied into the image at build time.

---

## Scripts

### R

#### 1. `calc_segsites(fn = "bigcats")` — `polymorphic_site_finder.R`

Counts segregating (polymorphic) sites in a tab-delimited file of sequences.

**Behavior**

- Reads tab-delimited sequence files
- Compares sequences position by position
- Returns the number of sites where any sequence differs from the first (reference) sequence

**Input**

- Table with a header column named `seqs`
- All sequences the same length

**Workflow**

1. Read the table into `dat`
2. Split each sequence into characters
3. For each column, compare all sequences to the first row
4. Increment the count when any value differs from the reference at that position

**Output:** Integer count of segregating sites.

**Example**

```r
n_segsites <- calc_segsites()
print(n_segsites)

n_segsites2 <- calc_segsites("my_sequences.txt")
```

---

#### 2. Alignment-based polymorphism

Uses `seqinr` and `adegenet` to read a multiple sequence alignment and mark polymorphic loci.

**Input:** Clustal alignment (e.g. `feliformia.aln`)

**Steps**

1. **Read alignment**
   ```r
   dat <- read.alignment("feliformia.aln", format = "clustal")
   ```

2. **Convert to `genind`**
   ```r
   dat2 <- alignment2genind(dat)
   ```

3. **Polymorphic sites**
   ```r
   poly_flags <- isPoly(dat2, by = "loc")
   ```
   `poly_flags` is logical: `TRUE` = polymorphic locus.

4. **Summarize**
   ```r
   n_poly <- sum(poly_flags)
   print(n_poly)
   summary(dat2)
   ```

**Full example**

```r
alignment_data <- read.alignment("feliformia.aln", format = "clustal")
genind_obj <- alignment2genind(alignment_data)
poly_sites <- isPoly(genind_obj, by = "loc")

cat("Number of polymorphic loci:", sum(poly_sites), "\n")
cat("Total loci:", length(poly_sites), "\n")
```

---

#### 3. `Find_LCS.r` — longest common subsequence

Classical LCS (dynamic programming, CLRS-style) for two strings, useful for comparing sequences at the character level.

- `find_lcs(v, w)` — Builds DP and backtrack tables; returns `s`, `b`, and parsed vectors. Prints lengths of `v` and `w`.
- `print_lcs(b, v, i, j)` — Prints one LCS by backtracking from `i, j` (e.g. `n+1`, `m+1` for full result).
- `get_lcs(v, w)` — Returns the LCS as a single string (e.g. `get_lcs("AAACGTA", "ACCGGTAATCGAA")`).

---

### Python

#### Core utilities

| Script | Functions | Description |
|--------|-----------|-------------|
| **`aminoAcids.py`** | (data: `aa`, `codons`) | One-letter amino acid order and codon groups for the standard code |
| **`count.py`** | `count(letter, string)` | Counts occurrences of a character in a string |
| **`dna.py`** | `compBase(N)`, `reverse(s)`, `reverseComplement(DNA)`, `amino(codon)`, `codingStrandToAA(DNA)` | DNA utilities and translation |
| **`load.py`** | `loadSeq(fileName)` | Loads a single-entry FASTA and returns the sequence string |

#### DNA

**`dna.py`** — see the table above; implementation details and edge cases are in the module source.

#### ORF detection

**`orf.py`**

- `restOfORF(DNA)` — ORF from first `ATG` to first in-frame stop
- `oneFrame(DNA)` — ORFs in the first reading frame
- `longestORF(DNA)` — Longest ORF across frames

**`elif.py`**

- `ORFadviser(dna)` — Checks ORF structure (start, stop, length multiple of 3)
- `friendly(greeting)` — Simple interactive helper (demo / CLI-style responses)

#### Sequence processing

**`looping.py`**

- `countLength(dnaList, length)` — How many strings have a given length
- `getLength(DNAlist, length)` — Strings of a given length
- `factorial(n)` — Factorial

#### Sequence screening

**`seq_screener.py`**

- `t_finder(list)` — Count strings with at least two `t` characters
- `GC_maker(list)` — GC counts per string
- `GC_rich(list)` — GC-rich strings (≥ 55%)
- `string_start(seq)` — Possible start codon positions
- `list_start(list)` — Apply `string_start` to a list
- `seq_analyzer(list)` — Run the above and print summaries

#### Motif scoring

**`motif_scoring.py`**

- `load_motif_profile(path)` — Read a motif scoring matrix
- `load_dna_sequence(path)` — Load and concatenate a FASTA sequence
- `reverse_complement(seq)` — Reverse complement
- `score_window(window, profile)` — Score a window against the profile
- `main()` — CLI: scan forward and reverse strands, print scores

---

## Directory structure

Create `data/` and `results/` locally if you use the example paths in the notes above. They are not always committed.

```
Small_Bioinformatic_Scripts/
│
├── data/                        # Example inputs (e.g. bigcats, feliformia.aln), optional
│   ├── bigcats
│   └── feliformia.aln
│
├── results/                     # Output summaries and plots, optional
│
├── polymorphic_site_finder.R    # calc_segsites; alignment workflow comments (see Quick start)
├── Find_LCS.r                   # LCS (DP)
│
├── aminoAcids.py
├── count.py
├── dna.py
├── elif.py
├── looping.py
├── load.py
├── orf.py
├── seq_screener.py
├── motif_scoring.py
│
├── Dockerfile                   # Python 3.12 image for *.py scripts
└── README.md
```

---

## Contributing

Contributions are welcome via issues and pull requests. A larger backlog of possible fixes lives in [IMPROVEMENTS.md](IMPROVEMENTS.md). Suggestions that fit the scope of the repo include:

- Visualizations of segregating sites
- Support for more alignment formats (e.g. FASTA, PHYLIP)
- Minor allele frequency and related population summaries
- Bug fixes, tests, and documentation

---

## License

This project is released under the **MIT License**. See [LICENSE](LICENSE) for the full text.

---

<div align="center">

**Small utilities for teaching, coursework, and light sequence workflows.**

</div>
