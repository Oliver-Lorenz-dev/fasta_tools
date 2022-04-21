import pytest
from lib.fasta_utils import Fasta_stats


@pytest.fixture
def fasta_sequence():
    fasta_stats_instance = Fasta_stats("tests/test.fasta")
    return fasta_stats_instance


@pytest.fixture
def multi_fasta_sequence():
    fasta_stats_instance = Fasta_stats("tests/multi_test.fasta")
    return fasta_stats_instance


@pytest.fixture
def rev_comp(multi_fasta_sequence):
    multi_fasta_sequence.reverse_complement("tests/rev_comp_test.fasta")
    fasta_stats_reverse_comp_instance = Fasta_stats("tests/rev_comp_test.fasta")
    return fasta_stats_reverse_comp_instance


@pytest.fixture
def comp(multi_fasta_sequence):
    multi_fasta_sequence.complement("tests/comp_test.fasta")
    fasta_stats_reverse_comp_instance = Fasta_stats("tests/comp_test.fasta")
    return fasta_stats_reverse_comp_instance


@pytest.fixture
def translate(multi_fasta_sequence):
    multi_fasta_sequence.translate("tests/translated_test.fasta")
    fasta_stats_translated_instance = Fasta_stats("tests/translated_test.fasta")
    return fasta_stats_translated_instance


@pytest.fixture
def transcribe(multi_fasta_sequence):
    multi_fasta_sequence.transcribe("tests/transcribed_test.fasta")
    fasta_stats_translated_instance = Fasta_stats("tests/transcribed_test.fasta")
    return fasta_stats_translated_instance


def test_read_fasta(fasta_sequence):
    assert fasta_sequence.read_fasta_file() == "ATGCCATG"


def test_get_gc_content(fasta_sequence):
    gc_content = fasta_sequence.get_gc_content()
    assert gc_content == 50


def test_get_base_content(fasta_sequence):
    base_content = fasta_sequence.get_base_content()
    assert base_content == (25, 25, 25, 25)


def test_reverse_complement(rev_comp):
    assert rev_comp.read_fasta_file() == "TCGC"


def test_complement(comp):
    assert comp.read_fasta_file() == "CTCG"


def test_translate(translate):
    assert translate.read_fasta_file() == "XA"


def test_transcribe(transcribe):
    assert transcribe.read_fasta_file() == "GAGC"