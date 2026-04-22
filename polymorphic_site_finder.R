calc_segsites <- function(fn="bigcats")
{
  # Error handling: check if file exists
  if (!file.exists(fn)) {
    stop(paste("Error: File", fn, "does not exist"))
  }
  
  # Error handling: try to read the file
  tryCatch({
    dat <- read.table(file=fn, header=TRUE, stringsAsFactors=FALSE)
  }, error = function(e) {
    stop(paste("Error reading file", fn, ":", e$message))
  })
  
  # Error handling: check if 'seqs' column exists
  if (!"seqs" %in% colnames(dat)) {
    stop(paste("Error: Column 'seqs' not found in", fn))
  }
  
  dat$seqs <- as.character(dat$seqs)            # Convert the factor vector to character
  numseqs <- length(dat$seqs)                     # Determine the number of sequences
  
  # Error handling: check if we have sequences
  if (numseqs == 0) {
    stop("Error: No sequences found in file")
  }
  
  seqs <- vector("list", length = numseqs)        # Create a list to hold each sequence
  
  for (i in 1:numseqs) {
    seqs[i] <- strsplit(dat$seqs[i], "")         # Split each sequence into individual nucleotides
  }
  
  segsites <- 0                                  # Initialize segregating sites counter
  len <- length(seqs[[1]])                        # Get the length of the first sequence (assumes equal lengths)
  
  # Check for equal sequence lengths
  seq_lengths <- sapply(seqs, length)
  if (length(unique(seq_lengths)) > 1) {
    warning("Sequences have unequal lengths. Using minimum length.")
    len <- min(seq_lengths)
  }
  
  for (i in 1:len) {                             # Loop over each nucleotide position
    comparison <- seqs[[1]][i]                    # Use the nucleotide from the first sequence as the reference
    for (j in 2:numseqs) {                        # Loop over the remaining sequences
      if (seqs[[j]][i] != comparison) {           # Compare the nucleotide at position i in sequence j
        segsites <- segsites + 1                  # Increment counter if a difference is found
        break                                   # Stop checking further sequences for this position
      }
    }
  }
  
  return(segsites)
}


# Example usage (commented out - uncomment to run):
# result <- calc_segsites()
# print(result)
#
# # Alignment-based polymorphism detection example:
# # dat <- read.alignment("feliformia.aln", format = "clustal")
# # dat2 <- alignment2genind(dat) # creates genind object (adegenet)
# # poly_sites <- isPoly(dat2, by="loc") # returns a logical vector of polymorphic sites
# # print(paste("Number of polymorphic sites:", sum(poly_sites)))
# # print(paste("Total sites:", length(poly_sites)))
# # summary(dat2) 
