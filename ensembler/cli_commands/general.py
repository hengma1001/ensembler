helpstring_header = """\
Ensembler
"""

ensembler_helpstring = """\
Usage:
  ensembler -h | --help
  ensembler init [-h | --help] [--project_dir <dir>]
  ensembler gather_targets [-h | --help] [--gather_from <method>] [--query <query>] [--dbapi_uri <uri>] [--uniprot_domain_regex <regex>]
  ensembler gather_templates [-h | --help] [--gather_from <method>] [--query <query>] [--dbapi_uri <uri>] [--uniprot_domain_regex <regex>] [--chainids <chainids>] [--structure_paths <path>]
  ensembler loopmodel [-h | --help] [--templates <templates>] [--overwrite_structures] [-v | --verbose]
  ensembler align [-h | --help] [--targets <targets>] [--targetsfile <targetsfile>] [--templates <templates>] [-v | --verbose]
  ensembler build_models [-h | --help] [--targets <target>] [--targetsfile <targetsfile>] [--templates <template>] [-v | --verbose]
  ensembler cluster [-h | --help] [--targets <target>] [--targetsfile <targetsfile>] [-v | --verbose]
  ensembler refine_implicit [-h | --help] [--targets <target>] [--targetsfile <targetsfile>] [--templates <template>] [--gpupn <gpupn>] [--openmm_platform <platform>] [--simlength <simlength>] [-v | --verbose]
  ensembler solvate [-h | --help] [--targets <target>] [--targetsfile <targetsfile>] [--templates <template>] [-v | --verbose]
  ensembler refine_explicit [-h | --help] [--targets <target>] [--targetsfile <targetsfile>] [--templates <template>] [--gpupn <gpupn>] [--openmm_platform <platform>] [--simlength <simlength>] [-v | --verbose]
  ensembler package_models [-h | --help] [--package_for <choice>] [--targets <target>] [--targetsfile <targetsfile>] [--nFAHclones <n>] [--archiveFAHproject]
  ensembler testrun_pipeline [-h | --help]
  ensembler quickmodel [-h | --help] [--targetid <id>] [--templateids <ids>] [--target_uniprot_entry_name <entry_name>] [--uniprot_domain_regex <regex>] [--template_pdbids <pdbids>] [--template_chainids <chainids>] [--template_seqid_cutoff <cutoff>] [--no-loopmodel] [--package_for_fah] [--nfahclones <nfahclones>]

Commands:
  init                          Initialize a new Ensembler project
  gather_targets                Gather targets

General options:
  -h --help                     Print command line help
"""

gather_from_helpstring = """\
  --gather_from <method>            Choose a source from which to gather data. {targetexplorer|uniprot} [default: targetexplorer]
                                      - "targetexplorer": An existing TargetExplorer database, specified via the --dbapi_uri argument.

                                      - "uniprot": UniProt (www.uniprot.org). Requires a user-defined query
                                      string, plus an optional regex string for further filtering.
"""