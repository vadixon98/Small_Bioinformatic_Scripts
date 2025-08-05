# Small Bioinformatic Scripts

A collection of small R and Python utilities for sequence analysis, including polymorphic site detection, alignment-based polymorphism, and various sequence and text processing scripts.

---

## Requirements

* **R** (version 3.6 or higher)
* CRAN packages:

  * `seqinr` (for reading alignment files)
  * `adegenet` (for `alignment2genind` and `isPoly` functions)

Ensure these packages are installed before running the scripts:

```r
install.packages(c("seqinr", "adegenet"))
```

---

## Scripts Overview

All functionality can be placed into a single R script (e.g., `polymorphism_analysis.R`), or sourced interactively.

### 1. `calc_segsites(fn = "bigcats")`

Counts segregating (polymorphic) sites in a tab-delimited file of sequences.

* **Input**: A file (default `bigcats`) with header and a column named `seqs`, where each entry is a sequence string of equal length.
* **Behavior**:

  1. Reads the table into `dat`.
  2. Splits each sequence into individual characters.
  3. Iterates over each position, comparing all sequences to the first as reference.
  4. Increments count when any sequence differs from reference at that site.
* **Output**: Returns the total number of segregating sites (integer).

**Usage example**:

```r
# In R:
source("polymorphism_analysis.R")
# Count sites in default file:
n_segsites <- calc_segsites()
print(n_segsites)
# Or specify a different filename:
n_segsites2 <- calc_segsites("my_sequences.txt")
```

### 2. Alignment-based Polymorphism Detection

Leverages `seqinr` and `adegenet` to read a multiple sequence alignment and flag polymorphic loci.

* **Input**: A Clustal-format alignment file (e.g., `feliformia.aln`).
* **Workflow**:

  1. **Read alignment**:

     ```r
     ```

dat <- read.alignment("feliformia.aln", format = "clustal")

````
  2. **Convert to genind object**:
     ```r
dat2 <- alignment2genind(dat)
````

3. **Identify polymorphic sites**:

   ```r
   ```

poly\_flags <- isPoly(dat2, by = "loc")

````
     `poly_flags` is a logical vector where `TRUE` indicates a polymorphic site.
  4. **Summarize**:
     ```r
n_poly <- sum(poly_flags)
print(n_poly)
summary(dat2)
````

**Usage example**:

```r
# Assuming script is sourced or in R console:
source("polymorphism_analysis.R")  # defines helper functions
# Read and analyze alignment:
alignment_data <- read.alignment("feliformia.aln", format = "clustal")
genind_obj <- alignment2genind(alignment_data)
poly_sites <- isPoly(genind_obj, by = "loc")
cat("Number of polymorphic loci:", sum(poly_sites), "\n")
cat("Total loci:", length(poly_sites), "\n")
```

---

## Python Scripts Overview

In addition to R routines, this project includes the following Python utilities for sequence and text processing:

* **count.py**: `count(letter, string)` counts occurrences of `letter` in a given `string`. fileciteturn5file0
* **dna.py**:

  * `compBase(N)`: returns the complementary DNA base.
  * `reverse(s)`: reverses a string.
  * `reverseComplement(DNA)`: returns the reverse complement of a DNA string.
  * `amino(codon)`: translates a codon to its amino acid.
  * `codingStrandToAA(DNA)`: converts a DNA coding strand to an amino acid sequence. fileciteturn5file1turn5file3
* **elif.py**:

  * `ORFadviser(dna)`: checks if a DNA string is a valid ORF (start codon, stop codon, length multiple of 3).
  * `friendly(greeting)`: responds to greetings or questions. fileciteturn5file2
* **looping.py**:

  * `countLength(dnaList, length)`: counts strings of a given length in a list.
  * `getLength(DNAlist, length)`: returns list of strings matching a specified length.
  * `factorial(n)`: computes `n!`. fileciteturn5file4
* **load.py**: `loadSeq(fileName)` loads a single-entry FASTA and returns the sequence string. fileciteturn5file5
* **seq\_screener.py**:

  * `t_finder(list)`: counts strings with ≥2 't's.
  * `GC_maker(list)`: computes GC counts for each string.
  * `GC_rich(list)`: identifies GC-rich strings (≥55%).
  * `string_start(seq)`: finds potential start codon positions.
  * `list_start(list)`: applies `string_start` to a list.
  * `seq_analyzer(list)`: runs all above analyses and prints summaries. fileciteturn5file6
* **orf.py**:

  * `restOfORF(DNA)`: returns ORF from the first 'ATG' to the first in-frame stop.
  * `oneFrame(DNA)`: finds all ORFs in the first reading frame.
  * `longestORF(DNA)`: identifies the longest ORF across all frames. fileciteturn5file8
* **motif\_scoring.py**:

  * `load_motif_profile(path)`: reads a motif scoring matrix.
  * `load_dna_sequence(path)`: loads and concatenates a FASTA sequence.
  * `reverse_complement(seq)`: computes the reverse complement.
  * `score_window(window, profile)`: scores a window against the motif profile.
  * `main()`: CLI entrypoint to scan a sequence (forward and reverse) and output scores. fileciteturn5file9

---

## Directory Structure

```
├── data/                   # (Optional) input files, e.g., bigcats, feliformia.aln
├── polymorphism_analysis.R # R script with analysis functions
└── results/                # (Optional) output summaries or plots
```

---

## Contributing

Feel free to fork the repository and submit pull requests to:

* Add visualization of segregating sites
* Support additional alignment formats (FASTA, PHYLIP)
* Integrate minor allele frequency calculations

---

## License

This code is released under the MIT License. Include a copy of the license when distributing.
