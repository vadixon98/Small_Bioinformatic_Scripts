find_lcs <- function(v, w)   # run by passing string literals of the sequences -- e.g., find_lcs("ACCCTG", "TACCCCGTTTG")
{
  v <- strsplit(v, "")[[1]]   # atomizes string into individual letters -- i.e., a single, character vector instead of the list of length one returned by strsplit()
  w <- strsplit(w, "")[[1]]   # look up (?strsplit) if you're not sure what the second argument should be
  v <- as.vector(v[[1]]) 
  w <- as.vector(w[[1]])
  n <- length(...)  # length of first sequence
  m <- length(...)   # length of second sequence
  print (n)   # so that you know the true lengths of input strings v and w for calling function print_lcs()
  print(m)
  s <- matrix(0, nrow=n+1, ncol=m+1)  # s is the dynamic programming table (p. 175)
                                      # setting all cells to zero eliminates need for pseudocode lines 1-4 of LCS (p. 176)
                                      # the extra (+1) column and row make room for the additional "0" indices
                                      # our goal is to update the matrix such that the number in cell [i,j] is the length of the LCS from point [0,0] to [i,j]
  b <- matrix(0, nrow=n+1, ncol=m+1)  # b is the matrix of bactracing pointers
                                      # BACKTRACING POINTERS: 1 to represent up arrow, 2 for left arrow, and 3 for diagonal arrow
  for (i in 2:(n+1)){       # indexing differently than in the pseudocode (p.176, LCS)  because R is 1-based while the pseudocode assumes 0-based indexing
                            # if the parentheses are not placed around n+1, the loop bounds become 3 through n+1 instead of 2 through n+1
                            # because 2:n+1 is interpreted as add 1 to BOTH of the loop bounds: 2 and n  become 3 and n+1
    for (j in 2:(...)) {
      s[...] <- max(s[i-1,j], s[... , ...])
      if (v[i-1] == w[j-1]) {
        s[i,j] <- max(s[i,j], (s[i-1, j-1] + 1))
      }
      if(s[i,j] == s[i-1,j]) 
        b[i,j] <- 1
      else if(s[i,j] == s[i,j-1])
        b[i,j] <- 2
      else
        b[i,j] <- 3
    }
  }
  return(list("s"=s,"b"=b, "vectorV"=v))   
}

print_lcs <- function(b, v, i, j) # i and j are the lengths of the two strings, v and w, if you're looking for the overall LCS
                                  # HOWEVER, YOU MUST enter one more than the length of each string
                                  # e.g., IF len(v) = 10 and len(w) = 14, you should pass 11 and 15 to i and j, respectively
  
                                  # FINALLY, if you saved the list returned by find_lcs() to object x -- for example: x <- find_lcs("AAACGTA", "ACCGGTAATCGAA"), 
                                  # THEN you would call this function as print_lcs(b=x$b, v=x$vectorV, 7, 14) 
{
  if (...)  # stop if current cell [i,j] is in first row or column
    return()
  if (b[i,j]==3) { #diagonal
    print_lcs(... , ... , ... , ...)
    print(v[i-1])
  } else {
    if (b[i,j]==1) { #up
      print_lcs(b,v, ... , ...)
    } else { #left 
      print_lcs(b,v, ... , ...)
    }
  }  
}