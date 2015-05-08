import argparse
from BigQueryGenomicsQC import GenomicsQC

def RunQC(verbose= False, sample_level=False, variant_level=False, client_secrets=None, project_number=None,
          dataset=None, variant_table=None, expanded_table=None):

    qc = GenomicsQC(verbose=verbose, client_secrets=client_secrets, project_number=project_number, dataset=dataset,
                    variant_table=variant_table, expanded_table=expanded_table)

    if sample_level is True:
        qc.sample_qc()
    if variant_level is True:
        qc.variant_qc()

def parse_command_line():
    parser = argparse.ArgumentParser(
        description = 'This script runs qc queries on genomics data stored in BigQuery.  Failing samples and variants'
                      'will be removed from the variantset.  Sample level qc and variant level qc can be run at the '
                      'same time.  See config.py to set dataset and table names.')

    parser.add_argument("--sample_qc", action='store_true', default=False,
                                help="Run sample level qc.")
    parser.add_argument("--variant_qc", action='store_true', default=False,
                                help="Run variant level qc.")
    parser.add_argument("--variant_table", default=None,
                                help="OPTIONAL. Variant table to query. Defaults to value in config.py")
    parser.add_argument("--expanded_table", default=None,
                                help="OPTIONAL. Expanded variant table to query. Defaults to value in config.py")
    parser.add_argument("--project_number", default=None,
                                help="OPTIONAL. Google Cloud project number. Defaults to value in config.py")
    parser.add_argument("--dataset", default=None,
                                help="OPTIONAL. Variant store dataset. Defaults to value in config.py")
    parser.add_argument("--client_secrets", default=None,
                                help="OPTIONAL. client_secrets.json. Defaults to value in config.py")
    parser.add_argument("--verbose", action='store_true', default=False,
                                help="OPTIONAL. Logs will be very detailed. Kind of noise regardless thanks to Google"
                                     "API Client.")

    options = parser.parse_args()
    if options.sample_qc is False and options.variant_qc is False:
        print "Exiting, no qc specified.\nSpecify sample qc, variant qc, or both.\n--sample_qc and/or --variant_qc"
        exit(0)
    return options

if __name__ == "__main__":
    options = parse_command_line()
    RunQC(sample_level=options.sample_qc, variant_level=options.variant_qc, verbose=options.verbose,
          client_secrets=options.client_secrets, project_number=options.project_number, dataset=options.dataset,
          variant_table=options.variant_table, expanded_table=options.expanded_table)