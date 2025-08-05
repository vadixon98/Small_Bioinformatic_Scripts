import sys
import csv
from pathlib import Path


def load_motif_profile(path):
    matrix = []
    with open(path) as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            parts = line.split()
            try:
                row = [float(x) for x in parts]
            except ValueError:
                sys.exit(f"Error: Non-numeric value on line {line_num} of {path}")
            matrix.append(row)
    if len(matrix) != 4:
        sys.exit(f"Error: Expected 4 rows in motif profile, found {len(matrix)}")
    lengths = {len(r) for r in matrix}
    if len(lengths) != 1:
        sys.exit("Error: Inconsistent column counts in motif profile rows.")
    return matrix


def load_dna_sequence(path):
    seq_parts = []
    with open(path) as f:
        for line in f:
            if line.startswith('>'):
                continue
            seq_parts.append(line.strip())
    sequence = ''.join(seq_parts).upper()
    if not sequence:
        sys.exit(f"Error: No sequence data found in {path}")
    return sequence


def reverse_complement(seq):
    comp = str.maketrans('ACGTacgt', 'TGCAtgca')
    return seq.translate(comp)[::-1]


def score_window(window, profile):
    base2idx = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    score = 0.0
    for i, base in enumerate(window):
        idx = base2idx.get(base)
        if idx is None:
            continue
        score += profile[idx][i]
    return score


def main():
    # Accept 2 or 3 positional arguments (motif, sequence, optional output)
    if len(sys.argv) not in (3, 4):
        print("Usage: python motif_scoring.py <motif_profile.txt> <dna_sequence.txt> [<output.tsv>]")
        sys.exit(1)

    motif_path = Path(sys.argv[1])
    seq_path   = Path(sys.argv[2])
    out_path   = Path(sys.argv[3]) if len(sys.argv) == 4 else None

    # Load data
    profile  = load_motif_profile(motif_path)
    sequence = load_dna_sequence(seq_path)
    motif_len = len(profile[0])
    seq_len   = len(sequence)

    print(f"Scanning sequence of length {seq_len} with motif length {motif_len}...")

    # Prepare output handle
    out_fh = open(out_path, 'w', newline='') if out_path else sys.stdout
    writer = csv.writer(out_fh, delimiter='\t')
    writer.writerow(["position", "score_forward", "score_reverse", "score_best"])

    # Scan windows
    for pos in range(seq_len - motif_len + 1):
        window = sequence[pos:pos + motif_len]
        sf = score_window(window, profile)
        rcw = reverse_complement(window)
        sr = score_window(rcw, profile)
        sb = max(sf, sr)
        writer.writerow([pos, f"{sf:.4f}", f"{sr:.4f}", f"{sb:.4f}"])

    if out_path:
        out_fh.close()
        print(f"Results written to {out_path}")

if __name__ == '__main__':
    main()

