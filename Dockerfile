# Day-one image: Python 3.12 + your scripts (stdlib-oriented).
# R is not included; add a second stage or another Dockerfile later if you need it.
#
# Next steps for fuller containerization:
# - Add requirements.txt (or pyproject.toml) if you introduce non-stdlib deps; COPY + pip install -r in this file.
# - Run as non-root: create a user, COPY --chown, USER before CMD (matches many cluster/Kubernetes policies).
# - Multi-stage: optional builder stage if you later compile wheels or pin tools; final stage stays slim.
# - R workflows: separate Dockerfile.r or rocker/r-ver base + install.packages(c("seqinr", "adegenet")).
# - docker-compose.yml: services for CLI runs with volumes ./data:/data for inputs and reproducible one-liners.
# - Optional: HEALTHCHECK only if you add a long-running service (not needed for one-shot script containers).

FROM python:3.12-slim

WORKDIR /app

# All top-level Python modules (dna.py imports aminoAcids, etc.)
COPY *.py ./

# Quick sanity check when you run the container with no extra args
CMD ["python3", "-c", "import dna; print(dna.reverseComplement('ATGC'))"]
