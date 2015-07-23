from django.db import models


# Create your models here.

# adapted from http://www.djangosnippets.org/snippets/494/
# using UN country and 3 char code list from http://unstats.un.org/unsd/methods/m49/m49alpha.htm
# correct as of 17th October 2008


COUNTRIES = (
    ('AFG', 'Afghanistan'),
    ('ALA', 'Aland Islands'),
    ('ALB', 'Albania'),
    ('DZA', 'Algeria'),
    ('ASM', 'American Samoa'),
    ('AND', 'Andorra'),
    ('AGO', 'Angola'),
    ('AIA', 'Anguilla'),
    ('ATG', 'Antigua and Barbuda'),
    ('ARG', 'Argentina'),
    ('ARM', 'Armenia'),
    ('ABW', 'Aruba'),
    ('AUS', 'Australia'),
    ('AUT', 'Austria'),
    ('AZE', 'Azerbaijan'),
    ('BHS', 'Bahamas'),
    ('BHR', 'Bahrain'),
    ('BGD', 'Bangladesh'),
    ('BRB', 'Barbados'),
    ('BLR', 'Belarus'),
    ('BEL', 'Belgium'),
    ('BLZ', 'Belize'),
    ('BEN', 'Benin'),
    ('BMU', 'Bermuda'),
    ('BTN', 'Bhutan'),
    ('BOL', 'Bolivia'),
    ('BIH', 'Bosnia and Herzegovina'),
    ('BWA', 'Botswana'),
    ('BRA', 'Brazil'),
    ('VGB', 'British Virgin Islands'),
    ('BRN', 'Brunei Darussalam'),
    ('BGR', 'Bulgaria'),
    ('BFA', 'Burkina Faso'),
    ('BDI', 'Burundi'),
    ('KHM', 'Cambodia'),
    ('CMR', 'Cameroon'),
    ('CAN', 'Canada'),
    ('CPV', 'Cape Verde'),
    ('CYM', 'Cayman Islands'),
    ('CAF', 'Central African Republic'),
    ('TCD', 'Chad'),
    ('CIL', 'Channel Islands'),
    ('CHL', 'Chile'),
    ('CHN', 'China'),
    ('HKG', 'China - Hong Kong'),
    ('MAC', 'China - Macao'),
    ('COL', 'Colombia'),
    ('COM', 'Comoros'),
    ('COG', 'Congo'),
    ('COK', 'Cook Islands'),
    ('CRI', 'Costa Rica'),
    ('CIV', 'Cote d\'Ivoire'),
    ('HRV', 'Croatia'),
    ('CUB', 'Cuba'),
    ('CYP', 'Cyprus'),
    ('CZE', 'Czech Republic'),
    ('PRK', 'Democratic People\'s Republic of Korea'),
    ('COD', 'Democratic Republic of the Congo'),
    ('DNK', 'Denmark'),
    ('DJI', 'Djibouti'),
    ('DMA', 'Dominica'),
    ('DOM', 'Dominican Republic'),
    ('ECU', 'Ecuador'),
    ('EGY', 'Egypt'),
    ('SLV', 'El Salvador'),
    ('GNQ', 'Equatorial Guinea'),
    ('ERI', 'Eritrea'),
    ('EST', 'Estonia'),
    ('ETH', 'Ethiopia'),
    ('FRO', 'Faeroe Islands'),
    ('FLK', 'Falkland Islands (Malvinas)'),
    ('FJI', 'Fiji'),
    ('FIN', 'Finland'),
    ('FRA', 'France'),
    ('GUF', 'French Guiana'),
    ('PYF', 'French Polynesia'),
    ('GAB', 'Gabon'),
    ('GMB', 'Gambia'),
    ('GEO', 'Georgia'),
    ('DEU', 'Germany'),
    ('GHA', 'Ghana'),
    ('GIB', 'Gibraltar'),
    ('GRC', 'Greece'),
    ('GRL', 'Greenland'),
    ('GRD', 'Grenada'),
    ('GLP', 'Guadeloupe'),
    ('GUM', 'Guam'),
    ('GTM', 'Guatemala'),
    ('GGY', 'Guernsey'),
    ('GIN', 'Guinea'),
    ('GNB', 'Guinea-Bissau'),
    ('GUY', 'Guyana'),
    ('HTI', 'Haiti'),
    ('VAT', 'Holy See (Vatican City)'),
    ('HND', 'Honduras'),
    ('HUN', 'Hungary'),
    ('ISL', 'Iceland'),
    ('IND', 'India'),
    ('IDN', 'Indonesia'),
    ('IRN', 'Iran'),
    ('IRQ', 'Iraq'),
    ('IRL', 'Ireland'),
    ('IMN', 'Isle of Man'),
    ('ISR', 'Israel'),
    ('ITA', 'Italy'),
    ('JAM', 'Jamaica'),
    ('JPN', 'Japan'),
    ('JEY', 'Jersey'),
    ('JOR', 'Jordan'),
    ('KAZ', 'Kazakhstan'),
    ('KEN', 'Kenya'),
    ('KIR', 'Kiribati'),
    ('KWT', 'Kuwait'),
    ('KGZ', 'Kyrgyzstan'),
    ('LAO', 'Lao People\'s Democratic Republic'),
    ('LVA', 'Latvia'),
    ('LBN', 'Lebanon'),
    ('LSO', 'Lesotho'),
    ('LBR', 'Liberia'),
    ('LBY', 'Libyan Arab Jamahiriya'),
    ('LIE', 'Liechtenstein'),
    ('LTU', 'Lithuania'),
    ('LUX', 'Luxembourg'),
    ('MKD', 'Macedonia'),
    ('MDG', 'Madagascar'),
    ('MWI', 'Malawi'),
    ('MYS', 'Malaysia'),
    ('MDV', 'Maldives'),
    ('MLI', 'Mali'),
    ('MLT', 'Malta'),
    ('MHL', 'Marshall Islands'),
    ('MTQ', 'Martinique'),
    ('MRT', 'Mauritania'),
    ('MUS', 'Mauritius'),
    ('MYT', 'Mayotte'),
    ('MEX', 'Mexico'),
    ('FSM', 'Micronesia, Federated States of'),
    ('MCO', 'Monaco'),
    ('MNG', 'Mongolia'),
    ('MNE', 'Montenegro'),
    ('MSR', 'Montserrat'),
    ('MAR', 'Morocco'),
    ('MOZ', 'Mozambique'),
    ('MMR', 'Myanmar'),
    ('NAM', 'Namibia'),
    ('NRU', 'Nauru'),
    ('NPL', 'Nepal'),
    ('NLD', 'Netherlands'),
    ('ANT', 'Netherlands Antilles'),
    ('NCL', 'New Caledonia'),
    ('NZL', 'New Zealand'),
    ('NIC', 'Nicaragua'),
    ('NER', 'Niger'),
    ('NGA', 'Nigeria'),
    ('NIU', 'Niue'),
    ('NFK', 'Norfolk Island'),
    ('MNP', 'Northern Mariana Islands'),
    ('NOR', 'Norway'),
    ('PSE', 'Occupied Palestinian Territory'),
    ('OMN', 'Oman'),
    ('PAK', 'Pakistan'),
    ('PLW', 'Palau'),
    ('PAN', 'Panama'),
    ('PNG', 'Papua New Guinea'),
    ('PRY', 'Paraguay'),
    ('PER', 'Peru'),
    ('PHL', 'Philippines'),
    ('PCN', 'Pitcairn'),
    ('POL', 'Poland'),
    ('PRT', 'Portugal'),
    ('PRI', 'Puerto Rico'),
    ('QAT', 'Qatar'),
    ('KOR', 'Republic of Korea'),
    ('MDA', 'Republic of Moldova'),
    ('REU', 'Reunion'),
    ('ROU', 'Romania'),
    ('RUS', 'Russian Federation'),
    ('RWA', 'Rwanda'),
    ('BLM', 'Saint-Barthelemy'),
    ('SHN', 'Saint Helena'),
    ('KNA', 'Saint Kitts and Nevis'),
    ('LCA', 'Saint Lucia'),
    ('MAF', 'Saint-Martin (French part)'),
    ('SPM', 'Saint Pierre and Miquelon'),
    ('VCT', 'Saint Vincent and the Grenadines'),
    ('WSM', 'Samoa'),
    ('SMR', 'San Marino'),
    ('STP', 'Sao Tome and Principe'),
    ('SAU', 'Saudi Arabia'),
    ('SEN', 'Senegal'),
    ('SRB', 'Serbia'),
    ('SYC', 'Seychelles'),
    ('SLE', 'Sierra Leone'),
    ('SGP', 'Singapore'),
    ('SVK', 'Slovakia'),
    ('SVN', 'Slovenia'),
    ('SLB', 'Solomon Islands'),
    ('SOM', 'Somalia'),
    ('ZAF', 'South Africa'),
    ('ESP', 'Spain'),
    ('LKA', 'Sri Lanka'),
    ('SDN', 'Sudan'),
    ('SUR', 'Suriname'),
    ('SJM', 'Svalbard and Jan Mayen Islands'),
    ('SWZ', 'Swaziland'),
    ('SWE', 'Sweden'),
    ('CHE', 'Switzerland'),
    ('SYR', 'Syrian Arab Republic'),
    ('TJK', 'Tajikistan'),
    ('THA', 'Thailand'),
    ('TLS', 'Timor-Leste'),
    ('TGO', 'Togo'),
    ('TKL', 'Tokelau'),
    ('TON', 'Tonga'),
    ('TTO', 'Trinidad and Tobago'),
    ('TUN', 'Tunisia'),
    ('TUR', 'Turkey'),
    ('TKM', 'Turkmenistan'),
    ('TCA', 'Turks and Caicos Islands'),
    ('TUV', 'Tuvalu'),
    ('UGA', 'Uganda'),
    ('UKR', 'Ukraine'),
    ('ARE', 'United Arab Emirates'),
    ('GBR', 'United Kingdom'),
    ('TZA', 'United Republic of Tanzania'),
    ('USA', 'USA'),
    ('VIR', 'United States Virgin Islands'),
    ('URY', 'Uruguay'),
    ('UZB', 'Uzbekistan'),
    ('VUT', 'Vanuatu'),
    ('VEN', 'Venezuela (Bolivarian Republic of)'),
    ('VNM', 'Viet Nam'),
    ('WLF', 'Wallis and Futuna Islands'),
    ('ESH', 'Western Sahara'),
    ('YEM', 'Yemen'),
    ('ZMB', 'Zambia'),
    ('ZWE', 'Zimbabwe'),
)

SEGMENTS = (
    ('1', '1 PB2'),
    ('2', '2 PB1'),
    ('3', '3 PA'),
    ('4', '4 HA'),
    ('5', '5 NP'),
    ('6', '6 NA'),
    ('7', '7 M'),
    ('8', '8 NS'),
)


class CountryField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 3)
        kwargs.setdefault('choices', COUNTRIES)

        super(CountryField, self).__init__(*args, **kwargs)

    def get_internal_type(self):
        return "CharField"


# Table for influenza_na
class Influenza_NA(models.Model):
    genbank_accession_number = models.CharField(max_length=10, null=False, primary_key=True)
    host = models.CharField(max_length=10, null=True)
    genomesegment_or_proteinname = models.CharField(max_length=10, null=True)
    subtype = models.CharField(max_length=10, null=True)
    country = CountryField(verbose_name="Country", help_text="Origin of viral strain.", null=True)
    date_discovered = models.DateField(null=True)
    sequence_length = models.IntegerField(null=True)
    virus_name = models.CharField(max_length=30, null=True)
    age = models.FloatField(null=True)
    gender = models.CharField(max_length=2, null=True)  # change to list....
    completeness = models.CharField(max_length=2, null=True)


# Table for the Influenza AA
class Influenza_AA(models.Model):
    genbank_accession_number = models.CharField(max_length=10, null=False, primary_key=True)
    host = models.CharField(max_length=10, null=True)
    genomesegment_or_proteinname = models.CharField(max_length=10, null=True)
    subtype = models.CharField(max_length=10, null=True)
    country = CountryField(verbose_name="Country", help_text="Origin of viral strain.", null=True)
    date_discovered = models.DateField(null=True)
    sequence_length = models.IntegerField(null=True)
    virus_name = models.CharField(max_length=30, null=True)
    age = models.FloatField(null=True)
    gender = models.CharField(max_length=2, null=True)  # change to list....
    completeness = models.CharField(max_length=2, null=True)


class Influenza_FNA(models.Model):
    genbank_na_accnum = models.OneToOneField(Influenza_NA, primary_key=True, null=False)
    fasta_nucleotide_description = models.CharField(max_length=30)


class Influenza_FAA(models.Model):
    genbank_na_accnum = models.OneToOneField(Influenza_AA, primary_key=True, null=False)
    fasta_protein_description = models.CharField(max_length=30)
