import click
from lib.fasta_utils import Fasta_stats
from Bio import SeqIO


@click.command()
@click.option('--input', required=True, type=click.File(mode='r'))
@click.option('--gc', required=False, default=False, is_flag=True, show_default=True, type=bool)
@click.option('--base-content', required=False, default=False, is_flag=True, show_default=True, type=bool)
@click.option('--reverse-complement', required=False, type=str)
@click.option('--complement', required=False, type=str)
@click.option('--translate', required=False, type=str)
@click.option('--transcribe', required=False, type=str)
def run(input, gc, base_content, reverse_complement, complement, translate, transcribe):
    # check fasta file has a sequence in it
    if not any(SeqIO.parse(input.name, "fasta")):
        raise TypeError("The fasta file you provided is not a valid fasta file")
    fasta_file=Fasta_stats(input)
    if gc:
        fasta_file.get_gc_content()
    elif base_content:
        fasta_file.get_base_content()
    elif reverse_complement:
        fasta_file.reverse_complement(reverse_complement)
    elif complement:
        fasta_file.complement(complement)
    elif translate:
        fasta_file.translate(translate)
    elif transcribe:
        fasta_file.transcribe(transcribe)


if __name__ == '__main__':
    run()


