# Longest Common Subsequence (LCS) - Dynamic Programming Implementation
# Based on CLRS pseudocode (Ch. 15)

find_lcs <- function(v, w)   # run by passing string literals -- e.g., find_lcs("ACCCTG", "TACCCCGTTTG")
{
  v <- strsplit(v, "")[[1]]   # atomizes string into individual letters (character vector)
  w <- strsplit(w, "")[[1]]   # strsplit returns a list; [[1]] extracts the character vector
  n <- length(v)              # length of first sequence
  m <- length(w)              # length of second sequence
  # print(n)                    # lengths for reference when calling print_lcs()
  # print(m)
  
  s <- matrix(0, nrow=n+1, ncol=m+1)  # dynamic programming table: s[i,j] = LCS length of v[1..i-1] and w[1..j-1]
  b <- matrix(0, nrow=n+1, ncol=m+1)  # backtracking pointers: 1=up, 2=left, 3=diagonal
  
  for (i in 2:(n+1)) {
    for (j in 2:(m+1)) {
      s[i,j] <- max(s[i-1, j], s[i, j-1])
      if (v[i-1] == w[j-1]) {
        s[i,j] <- max(s[i,j], s[i-1, j-1] + 1)
      }
      if (s[i,j] == s[i-1, j])
        b[i,j] <- 1
      else if (s[i,j] == s[i, j-1])
        b[i,j] <- 2
      else
        b[i,j] <- 3
    }
  }
  return(list("s" = s, "b" = b, "vectorV" = v, "vectorW" = w, "n" = n, "m" = m))
}

# Print LCS by backtracking. Pass i = n+1, j = m+1 to print the full LCS.
# Example: x <- find_lcs("AAACGTA", "ACCGGTAATCGAA"); print_lcs(b=x$b, v=x$vectorV, 8, 14)
print_lcs <- function(b, v, i, j)
{
  if (i <= 1 || j <= 1)  # stop at first row or column
    return(invisible(NULL))
  if (b[i, j] == 3) {    # diagonal - match
    print_lcs(b, v, i - 1, j - 1)
    print(v[i - 1])
  } else {
    if (b[i, j] == 1)    # up
      print_lcs(b, v, i - 1, j)
    else                 # left
      print_lcs(b, v, i, j - 1)
  }
}

# Convenience function: returns LCS as a character string
# Example: get_lcs("AAACGTA", "ACCGGTAATCGAA")  # returns "AACGTA"
get_lcs <- function(v, w) {
  result <- find_lcs(v, w)
  capture_lcs <- function(b, v, i, j) {
    if (i <= 1 || j <= 1)
      return(character(0))
    if (b[i, j] == 3) {
      c(capture_lcs(b, v, i - 1, j - 1), v[i - 1])
    } else if (b[i, j] == 1) {
      capture_lcs(b, v, i - 1, j)
    } else {
      capture_lcs(b, v, i, j - 1)
    }
  }
  paste(capture_lcs(result$b, result$vectorV, result$n + 1, result$m + 1), collapse = "")
}
