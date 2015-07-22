"""
Module with forms to myblast search and validation functions.
"""

from django import forms
import tempfile

from Bio import SeqIO
from Bio.Alphabet.IUPAC import IUPACAmbiguousDNA
from Bio.Alphabet.IUPAC import IUPACProtein

import settings as blast_settings

ALLOWED_NUCL = set(IUPACAmbiguousDNA.letters)
ALLOWED_AMINOACIDS = set(IUPACProtein.letters)
# forms styling provided from css
BLAST_FORM_ATTRS = {'class': 'myblast_input_seq_form'}
BLAST_FORM_INPUTTEXT_ATTRS = {'class': 'myblast_input_textfield_form'}

# scoring Matrix sets
MATRIX_LIST = ['BLOSUM45', 'BLOSUM62', 'BLOSUM80', 'PAM30', 'PAM70']
MATRIX_CHOICE_LIST = list((x, x,) for x in MATRIX_LIST)
MATRIX_DEFAULT = 'BLOSUM62'

# e-value sets
EVALUE_LIST = [1, 0.001, 1e-5, 1e-6, 1e-10, 1e-30, 1e-50, 1e-100]
EVALUE_CHOICE_LIST = list((x, str(x),) for x in list(EVALUE_LIST))
EVALUE_BLAST_DEFAULT = 0.001


class BlastForm(forms.Form):
    """Form used for blast+ search following validation input sequence.  """

    sequence_in_form = forms.CharField(widget=forms.Textarea(blast_settings.BLAST_FORM_ATTRS), label="sequence")
    evalue_in_form = forms.ChoiceField(widget=forms.Select, choices=blast_settings.EVALUE_CHOICE_LIST, label="e-value")
    word_size_in_form = forms.CharField(widget=forms.TextInput(blast_settings.BLAST_FORM_INPUTTEXT_ATTRS),
                                        initial=blast_settings.BLASTN_DEFAULT_INT_WORD_SIZE, label="word size")
    search_sensitivity_in_form = forms.ChoiceField(widget=forms.Select, choices=blast_settings.NUCLEOTIDE_SEARCH_SENSITIVE_CHOICE,
                                                   label="sensitivity")
    blast_nucl_in_form = forms.ChoiceField(widget=forms.Select, choices=blast_settings.BLAST_DB_NUCL_CHOICE, label="Database")
    validate_word_size(word_size_in_form, blast_settings.BLASTN_MIN_INT_WORD_SIZE, blast_settings.BLASTN_MAX_INT_WORD_SIZE,
                                  blast_settings.BLASTN_WORD_SIZE_ERROR)

    def clean_sequence_in_form(self):
        word_size_in_form = self.cleaned_data['word_size_in_form']

        return(word_size_in_form)

    def clean_word_size_in_form(self):
        sequence_in_form = self.cleaned_data['sequence_in_form']

        return validate_sequence(sequence_in_form, sequence_is_as_nucleotide=True)
       

