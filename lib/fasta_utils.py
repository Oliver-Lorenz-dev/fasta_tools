from Bio import SeqIO
from Bio.SeqUtils import GC
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq


class Fasta_stats:

    def __init__(self, fasta_file):
        self.fasta_file = fasta_file

    def read_fasta_file(self):
        seq = ""
        for record in SeqIO.parse(self.fasta_file, "fasta"):
            seq += record.seq
        return seq

    def get_gc_content(self):
        seq = self.read_fasta_file()
        gc_content = GC(seq)
        print(f"GC content: {gc_content}")
        return gc_content

    def get_base_content(self):
        seq = self.read_fasta_file()
        seq_length = len(seq)
        percent_a = ((seq.count("A") / seq_length) * 100)
        percent_c = ((seq.count("C") / seq_length) * 100)
        percent_g = ((seq.count("G") / seq_length) * 100)
        percent_t = ((seq.count("T") / seq_length) * 100)
        print(f"Base \t Percentage \n A \t {percent_a} \n C \t {percent_c} \n G \t {percent_g} \n T \t {percent_t}")
        return percent_a, percent_c, percent_g, percent_t

    def make_rc_record_rev_comp(self, record):
        return SeqRecord(seq=record.seq.reverse_complement(),
                         id=record.id,
                         description="reverse complement")

    def reverse_complement(self, outfile):
        records = map(self.make_rc_record_rev_comp, SeqIO.parse(self.fasta_file, "fasta"))
        SeqIO.write(records, outfile, "fasta")
        return records

    def make_rc_record_comp(self, record):
        return SeqRecord(seq=record.seq.complement(),
                         id=record.id,
                         description="complement")

    def complement(self, outfile):
        records = map(self.make_rc_record_comp, SeqIO.parse(self.fasta_file, "fasta"))
        SeqIO.write(records, outfile, "fasta")
        return records

    def make_rc_record_translate(self, record):
        seq = record.seq
        remainder = len(seq) % 3
        if remainder != 0:
            seq = seq + Seq('N' * (3 - remainder))
        return SeqRecord(seq.translate(),
                         id=record.id,
                         description="translation")

    def translate(self, outfile):
        records = map(self.make_rc_record_translate, SeqIO.parse(self.fasta_file, "fasta"))
        SeqIO.write(records, outfile, "fasta")
        return records

    def make_rc_record_transcribe(self, record):
        return SeqRecord(seq=record.seq.transcribe(),
                         id=record.id,
                         description="transcribe")

    def transcribe(self, outfile):
        records = map(self.make_rc_record_transcribe, SeqIO.parse(self.fasta_file, "fasta"))
        SeqIO.write(records, outfile, "fasta")
        return records
