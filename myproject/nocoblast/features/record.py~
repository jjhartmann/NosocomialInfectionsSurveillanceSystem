"""
Module with biopython-like classes to keep & process results from blast analysis.
"""


class Hsp(object):
    """Store and process HSP object from blast local search.  """

    def __init__(self, *args, **kwargs):
        self.limit_length = 80

        self.align_length = kwargs['align_length']
        self.bits = round(kwargs['bits'], 1)
        self.expect = kwargs['expect']
        self.frame = kwargs['frame']
        self.gaps = kwargs['gaps']
        self.identities = kwargs['identities']
        self.match = kwargs['match']
        self.num_alignments = kwargs['num_alignments']
        self.positives = kwargs['positives']
        self.query = kwargs['query']
        self.query_end = kwargs['query_end']
        self.query_start = kwargs['query_start']
        self.sbjct = kwargs['sbjct']
        self.sbjct_end = kwargs['sbjct_end']
        self.sbjct_start = kwargs['sbjct_start']
        self.score = kwargs['score']
        self.strand = kwargs['strand']
        self.str = kwargs['str']

