<div align="center">

# Small Bioinformatic Scripts

**R and Python utilities for sequence analysis and common bioinformatics tasks**

[![R](https://img.shields.io/badge/R-3.6+-blue?logo=r)](https://www.r-project.org/)
[![Python](https://img.shields.io/badge/Python-3.x-green?logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Bioinformatics](https://img.shields.io/badge/Bioinformatics-Sequence%20Analysis-purple)](https://github.com)

</div>

---

## Overview

This repository is a set of **R** and **Python** scripts for working with sequence data, including:

- **Polymorphic site detection** in sequence alignments
- **Alignment-based polymorphism** analysis
- **Sequence processing** and manipulation
- **ORF detection** and open reading frame analysis
- **Motif scoring** and pattern matching

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

* **Python** 3.x (most scripts use the standard library only)

---

## Quick start

### R

```r
# Source the main analysis script
source("polymorphism_analysis.R")

# Count segregating sites
n_segsites <- calc_segsites("bigcats")
print(n_segsites)
```

### Python

```python
from dna import reverseComplement, codingStrandToAA
from orf import longestORF

dna_seq = "ATGCGATCG"
rev_comp = reverseComplement(dna_seq)
```

---

## Scripts

### R

#### 1. `calc_segsites(fn = "bigcats")`

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

### Python

#### Core utilities

| Script | Functions | Description |
|--------|-----------|-------------|
| **`count.py`** | `count(letter, string)` | Counts occurrences of a character in a string |
| **`dna.py`** | `compBase(N)`, `reverse(s)`, `reverseComplement(DNA)`, `amino(codon)`, `codingStrandToAA(DNA)` | DNA utilities and translation |
| **`load.py`** | `loadSeq(fileName)` | Loads a single-entry FASTA and returns the sequence string |

#### DNA

**`dna.py`**

- `compBase(N)` — Complementary base
- `reverse(s)` — String reversal
- `reverseComplement(DNA)` — Reverse complement
- `amino(codon)` — Codon to amino acid
- `codingStrandToAA(DNA)` — Coding strand to amino acid sequence

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

```
Small_Bioinformatic_Scripts/
│
├── data/                       # Example inputs (e.g. bigcats, feliformia.aln)
│   ├── bigcats
│   └── feliformia.aln
│
├── results/                    # Outputs, summaries, figures
│
├── Find_LCS.r
├── Polymorphic Site Finder.R
├── polymorphism_analysis.R     # Referenced in Quick start; add or rename to match your layout
│
├── aminoAcids.py
├── count.py
├── dna.py
├── elif.py
├── looping.py
├── load.py
├── seq_screener.py
├── orf.py
├── motif_scoring.py
│
└── README.md
```

---

## Contributing

Contributions are welcome via issues and pull requests. Suggestions that fit the scope of the repo include:

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
