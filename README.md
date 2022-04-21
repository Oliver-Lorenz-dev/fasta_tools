## Fasta toolkit

A small toolkit I made to test out some new python libraries

###Usage
`python fasta_tools.py <option>`

###Options
```--input <fasta_file> [required]```

```--gc Display GC content [optional]```

```--base-content Display percentage base content [optional]```

```--reverse-complement <output_file> Generate reverse complement of input file [optional]```

```--complement <output_file> Generate complement of input file [optional]```

```--translate <output_file> Generate translation of input file [optional]```

```--transcribe <output_file> Generate transcription of input file [optional]```

```--help Display this help message and exit the program```

### Additional information
This program was made to take in a DNA sequence in the form of a FASTA file as input.

This program only allows the use of one option at a time (TODO: allow multiple options at the same time)