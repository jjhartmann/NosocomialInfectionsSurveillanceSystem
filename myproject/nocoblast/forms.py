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


class BlastForm(forms.Form):
    """Form used for blast+ search following validation input sequence.  """

    sequence_in_form = forms.CharField(widget=forms.Textarea(blast_settings.BLAST_FORM_ATTRS), label="sequence")
    evalue_in_form = forms.ChoiceField(widget=forms.Select, choices=blast_settings.EVALUE_CHOICE_LIST, label="e-value")
    word_size_in_form = forms.CharField(widget=forms.TextInput(blast_settings.BLAST_FORM_INPUTTEXT_ATTRS),
                                        initial=blast_settings.BLASTN_DEFAULT_INT_WORD_SIZE, label="word size")
    search_sensitivity_in_form = forms.ChoiceField(widget=forms.Select, choices=blast_settings.NUCLEOTIDE_SEARCH_SENSITIVE_CHOICE,
                                                   label="sensitivity")
    blast_nucl_in_form = forms.ChoiceField(widget=forms.Select, choices=blast_settings.BLAST_DB_NUCL_CHOICE, label="Database")


    def clean_sequence_in_form(self):
        sequence_in_form = self.cleaned_data['sequence_in_form']

        return validate_sequence(sequence_in_form, sequence_is_as_nucleotide=True)

    def clean_word_size_in_form(self):
        word_size_in_form = self.cleaned_data['word_size_in_form']

        return validate_word_size(word_size_in_form, blast_settings.BLASTN_MIN_INT_WORD_SIZE, blast_settings.BLASTN_MAX_INT_WORD_SIZE,
                                  blast_settings.BLASTN_WORD_SIZE_ERROR)


class TBlastnForm(forms.Form):
    """Form used for blast+ search following validation input sequence.  """

    sequence_in_form = forms.CharField(widget=forms.Textarea(blast_settings.BLAST_FORM_ATTRS), label="sequence")
    evalue_in_form = forms.ChoiceField(widget=forms.Select, choices=blast_settings.EVALUE_CHOICE_LIST, label="e-value")
    matrix_in_form = forms.ChoiceField(widget=forms.Select, choices=blast_settings.MATRIX_CHOICE_LIST, initial=blast_settings.MATRIX_DEFAULT,                                       label="matrix")
    word_size_in_form = forms.CharField(widget=forms.TextInput(blast_settings.BLAST_FORM_INPUTTEXT_ATTRS),
                                        initial=blast_settings.TBLASTN_DEFAULT_INT_WORD_SIZE, label="word size")
    search_sensitivity_in_form = forms.ChoiceField(widget=forms.Select, choices=blast_settings.PROTEIN_SEARCH_SENSITIVE_CHOICE, label="sensitivity")
    blast_nucl_in_form = forms.ChoiceField(widget=forms.Select, choices=blast_settings.BLAST_DB_NUCL_CHOICE, label="Database")

    def clean_sequence_in_form(self):
        sequence_in_form = self.cleaned_data['sequence_in_form']
        return validate_sequence(sequence_in_form, sequence_is_as_nucleotide=False)

    def clean_word_size_in_form(self):
        word_size_in_form = self.cleaned_data['word_size_in_form']
        return validate_word_size(word_size_in_form, blast_settings.TBLASTN_MIN_INT_WORD_SIZE, blast_settings.TBLASTN_MAX_INT_WORD_SIZE,
                                  blast_settings.TBLASTN_WORD_SIZE_ERROR)
