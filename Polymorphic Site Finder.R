calc_segsites <- function(fn="bigcats")
{
  dat <- read.table(file=fn, header=T)
  dat$seqs <- as.character(dat$seqs)            # Convert the factor vector to character
  numseqs <- length(dat$seqs)                     # Determine the number of sequences
  seqs <- vector("list", length = numseqs)        # Create a list to hold each sequence
  
  for (i in 1:numseqs) {
    seqs[i] <- strsplit(dat$seqs[i], "")         # Split each sequence into individual nucleotides
  }
  
  segsites <- 0                                  # Initialize segregating sites counter
  len <- length(seqs[[1]])                        # Get the length of the first sequence (assumes equal lengths)
  
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


calc_segsites() 
dat <- read.alignment("feliformia.aln", format = "clustal")
dat2 <- alignment2genind(dat) # creates genind object (adegenet)
isPoly(dat2, by="loc") # returns a logical vector of polymorphic sites
length(isPoly(dat2, by="loc")) 
summary(dat2) 
