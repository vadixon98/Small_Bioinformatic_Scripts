# Day-one image: Python 3.12 + your scripts (stdlib-oriented).
# R is not included; add a second stage or another Dockerfile later if you need it.

FROM python:3.12-slim

WORKDIR /app

# All top-level Python modules (dna.py imports aminoAcids, etc.)
COPY *.py ./

# Quick sanity check when you run the container with no extra args
CMD ["python3", "-c", "import dna; print(dna.reverseComplement('ATGC'))"]
