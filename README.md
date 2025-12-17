<div align="center">

# 🧬 Small Bioinformatic Scripts

**A collection of powerful R and Python utilities for sequence analysis and bioinformatics**

[![R](https://img.shields.io/badge/R-3.6+-blue?logo=r)](https://www.r-project.org/)
[![Python](https://img.shields.io/badge/Python-3.x-green?logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Bioinformatics](https://img.shields.io/badge/Bioinformatics-Sequence%20Analysis-purple)](https://github.com)

</div>

---

## 📋 Overview

This repository contains a curated collection of **R** and **Python** utilities designed for sequence analysis, including:

- 🔍 **Polymorphic site detection** in sequence alignments
- 📊 **Alignment-based polymorphism** analysis
- 🧪 **Sequence processing** and manipulation tools
- 🎯 **ORF detection** and analysis
- 🧮 **Motif scoring** and pattern matching

---

## ⚙️ Requirements

### R Dependencies

* **R** (version 3.6 or higher)
* Required CRAN packages:
  - 📦 `seqinr` - for reading alignment files
  - 📦 `adegenet` - for `alignment2genind` and `isPoly` functions

**Installation:**

```r
install.packages(c("seqinr", "adegenet"))
```

### Python Dependencies

* **Python** 3.x (standard library only for most scripts)

---

## 🚀 Quick Start

### R Scripts

```r
# Source the main analysis script
source("polymorphism_analysis.R")

# Count segregating sites
n_segsites <- calc_segsites("bigcats")
print(n_segsites)
```

### Python Scripts

```python
# Import and use utilities
from dna import reverseComplement, codingStrandToAA
from orf import longestORF

# Example usage
dna_seq = "ATGCGATCG"
rev_comp = reverseComplement(dna_seq)
```

---

## 📚 Scripts Overview

### 🔬 R Scripts

#### 1. `calc_segsites(fn = "bigcats")`

Counts segregating (polymorphic) sites in a tab-delimited file of sequences.

**Features:**
- ✅ Reads tab-delimited sequence files
- ✅ Compares sequences position-by-position
- ✅ Returns total count of polymorphic sites

**Input Format:**
- File with header containing a column named `seqs`
- Each entry is a sequence string of equal length

**Workflow:**
1. 📥 Reads the table into `dat`
2. 🔪 Splits each sequence into individual characters
3. 🔄 Iterates over each position, comparing all sequences to the first as reference
4. ➕ Increments count when any sequence differs from reference at that site

**Output:** Returns the total number of segregating sites (integer)

**Example:**

```r
# Count sites in default file
n_segsites <- calc_segsites()
print(n_segsites)

# Or specify a different filename
n_segsites2 <- calc_segsites("my_sequences.txt")
```

---

#### 2. Alignment-based Polymorphism Detection

Leverages `seqinr` and `adegenet` to read a multiple sequence alignment and flag polymorphic loci.

**Input:** Clustal-format alignment file (e.g., `feliformia.aln`)

**Workflow:**

1. **📖 Read alignment:**
   ```r
   dat <- read.alignment("feliformia.aln", format = "clustal")
   ```

2. **🔄 Convert to genind object:**
   ```r
   dat2 <- alignment2genind(dat)
   ```

3. **🔍 Identify polymorphic sites:**
   ```r
   poly_flags <- isPoly(dat2, by = "loc")
   ```
   `poly_flags` is a logical vector where `TRUE` indicates a polymorphic site.

4. **📊 Summarize:**
   ```r
   n_poly <- sum(poly_flags)
   print(n_poly)
   summary(dat2)
   ```

**Complete Example:**

```r
# Read and analyze alignment
alignment_data <- read.alignment("feliformia.aln", format = "clustal")
genind_obj <- alignment2genind(alignment_data)
poly_sites <- isPoly(genind_obj, by = "loc")

cat("Number of polymorphic loci:", sum(poly_sites), "\n")
cat("Total loci:", length(poly_sites), "\n")
```

---

### 🐍 Python Scripts

#### 📊 Core Utilities

| Script | Functions | Description |
|--------|-----------|-------------|
| **`count.py``** | `count(letter, string)` | Counts occurrences of a letter in a string |
| **`dna.py`** | `compBase(N)`, `reverse(s)`, `reverseComplement(DNA)`, `amino(codon)`, `codingStrandToAA(DNA)` | DNA sequence manipulation and translation |
| **`load.py`** | `loadSeq(fileName)` | Loads a single-entry FASTA and returns the sequence string |

#### 🧬 DNA Analysis

**`dna.py`** - Comprehensive DNA sequence utilities:

- `compBase(N)` - Returns the complementary DNA base
- `reverse(s)` - Reverses a string
- `reverseComplement(DNA)` - Returns the reverse complement of a DNA string
- `amino(codon)` - Translates a codon to its amino acid
- `codingStrandToAA(DNA)` - Converts a DNA coding strand to an amino acid sequence

#### 🎯 ORF Detection

**`orf.py`** - Open Reading Frame analysis:

- `restOfORF(DNA)` - Returns ORF from the first 'ATG' to the first in-frame stop
- `oneFrame(DNA)` - Finds all ORFs in the first reading frame
- `longestORF(DNA)` - Identifies the longest ORF across all frames

**`elif.py`** - ORF validation:

- `ORFadviser(dna)` - Checks if a DNA string is a valid ORF (start codon, stop codon, length multiple of 3)
- `friendly(greeting)` - Responds to greetings or questions

#### 🔄 Sequence Processing

**`looping.py`** - List and sequence operations:

- `countLength(dnaList, length)` - Counts strings of a given length in a list
- `getLength(DNAlist, length)` - Returns list of strings matching a specified length
- `factorial(n)` - Computes `n!`

#### 🔍 Sequence Screening

**`seq_screener.py`** - Comprehensive sequence analysis:

- `t_finder(list)` - Counts strings with ≥2 't's
- `GC_maker(list)` - Computes GC counts for each string
- `GC_rich(list)` - Identifies GC-rich strings (≥55%)
- `string_start(seq)` - Finds potential start codon positions
- `list_start(list)` - Applies `string_start` to a list
- `seq_analyzer(list)` - Runs all above analyses and prints summaries

#### 🎨 Motif Scoring

**`motif_scoring.py`** - Motif pattern matching:

- `load_motif_profile(path)` - Reads a motif scoring matrix
- `load_dna_sequence(path)` - Loads and concatenates a FASTA sequence
- `reverse_complement(seq)` - Computes the reverse complement
- `score_window(window, profile)` - Scores a window against the motif profile
- `main()` - CLI entrypoint to scan a sequence (forward and reverse) and output scores

---

## 📁 Directory Structure

```
Small_Bioinformatic_Scripts/
│
├── 📂 data/                      # Input files (e.g., bigcats, feliformia.aln)
│   ├── bigcats                   # Tab-delimited sequence file
│   └── feliformia.aln            # Clustal alignment file
│
├── 📂 results/                   # Output summaries and plots
│
├── 📜 polymorphism_analysis.R    # Main R script with analysis functions
│
├── 🐍 Python Scripts/
│   ├── count.py
│   ├── dna.py
│   ├── elif.py
│   ├── looping.py
│   ├── load.py
│   ├── seq_screener.py
│   ├── orf.py
│   └── motif_scoring.py
│
└── 📄 README.md                  # This file
```

---

## 🤝 Contributing

We welcome contributions! Feel free to fork the repository and submit pull requests for:

- ✨ Add visualization of segregating sites
- 📈 Support additional alignment formats (FASTA, PHYLIP)
- 🧮 Integrate minor allele frequency calculations
- 🐛 Bug fixes and improvements
- 📝 Documentation enhancements

---

## 📄 License

This project is licensed under the **MIT License**. See the LICENSE file for details.

---

<div align="center">

**Made with ❤️ for the bioinformatics community**

⭐ Star this repo if you find it useful!

</div>
