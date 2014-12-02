import os
from mock import Mock
import msmseeder.initproject
import msmseeder.integration_test_utils
import msmseeder.tests.utils


def test_loopmodel_KC1D_HUMAN_D0_4KB8_D():
    with msmseeder.integration_test_utils.integration_test_context(project_data='templates_observed'):
        template = Mock()
        template.templateid = 'KC1D_HUMAN_D0_4KB8_D'
        template.chainid = 'D'
        template.resolved_seq = 'LRVGNRYRLGRKIGDIYLGTDIAAGEEVAIKLECPQLHIESKIYKMMQGGVGIPTIRWCGAEGDYNVMVMELLGPSLEDLFNFCSRKFSLKTVLLLADQMISRIEYIHSKNFIHRDVKPDNFLMGLGKKGNLVYIIDFGLAKKYRDAQHIPYRENKNLTGTARYASINTHLGIEQSRRDDLESLGYVLMYFNLGSLPWQGLKAATKRQKYERISEKKMSTPIEVLCKGYPSEFATYLNFCRSLRFDDKPDYSYLRQLFRNLFHRQGFSYDYVFDWNML'
        template.full_seq = 'LRVGNRYRLGRKIGSGSFGDIYLGTDIAAGEEVAIKLECVKTKHPQLHIESKIYKMMQGGVGIPTIRWCGAEGDYNVMVMELLGPSLEDLFNFCSRKFSLKTVLLLADQMISRIEYIHSKNFIHRDVKPDNFLMGLGKKGNLVYIIDFGLAKKYRDARTHQHIPYRENKNLTGTARYASINTHLGIEQSRRDDLESLGYVLMYFNLGSLPWQGLKAATKRQKYERISEKKMSTPIEVLCKGYPSEFATYLNFCRSLRFDDKPDYSYLRQLFRNLFHRQGFSYDYVFDWNMLKFGASRAADDAERERRDREERLRH'

        missing_residues = msmseeder.initproject.pdbfix_template(template)
        msmseeder.initproject.loopmodel_template(template, missing_residues)

        assert os.path.exists(os.path.join('templates', 'structures-modeled-loops', 'KC1D_HUMAN_D0_4KB8_D-loopmodeled.pdb'))


def test_loopmodel_KC1D_HUMAN_D0_4HNF_A():
    with msmseeder.integration_test_utils.integration_test_context(project_data='templates_observed'):
        template = Mock()
        template.templateid = 'KC1D_HUMAN_D0_4HNF_A'
        template.chainid = 'A'
        template.resolved_seq = 'LRVGNRYRLGRKIGSGSFGDIYLGTDIAAGEEVAIKLECVKPQLHIESKIYKMMQGGVGIPTIRWCGAEGDYNVMVMELLGPSLEDLFNFCSRKFSLKTVLLLADQMISRIEYIHSKNFIHRDVKPDNFLMGLGKKGNLVYIIDFGLAKKYRDARTHQHIPYRENKNLTGTARYASINTHLGIEQSRRDDLESLGYVLMYFNLGSLPWQGLKAATKRQKYERISEKKMSTPIEVLCKGYPSEFATYLNFCRSLRFDDKPDYSYLRQLFRNLFHRQGFSYDYVFDWNMLK'
        template.full_seq = 'MELRVGNRYRLGRKIGSGSFGDIYLGTDIAAGEEVAIKLECVKTKHPQLHIESKIYKMMQGGVGIPTIRWCGAEGDYNVMVMELLGPSLEDLFNFCSRKFSLKTVLLLADQMISRIEYIHSKNFIHRDVKPDNFLMGLGKKGNLVYIIDFGLAKKYRDARTHQHIPYRENKNLTGTARYASINTHLGIEQSRRDDLESLGYVLMYFNLGSLPWQGLKAATKRQKYERISEKKMSTPIEVLCKGYPSEFATYLNFCRSLRFDDKPDYSYLRQLFRNLFHRQGFSYDYVFDWNMLK'

        missing_residues = msmseeder.initproject.pdbfix_template(template)
        msmseeder.initproject.loopmodel_template(template, missing_residues)

        assert os.path.exists(os.path.join('templates', 'structures-modeled-loops', 'KC1D_HUMAN_D0_4HNF_A-loopmodeled.pdb'))


@msmseeder.tests.utils.expected_failure
def test_loopmodel_KC1D_HUMAN_D0_3UZP_A():
    with msmseeder.integration_test_utils.integration_test_context(project_data='templates_observed'):
        template = Mock()
        template.templateid = 'KC1D_HUMAN_D0_3UZP_A'
        template.chainid = 'A'
        template.resolved_seq = 'LRVGNRYRLGRKIGSGSFGDIYLGTDIAAGEEVAIKLECVKTKHPQLHIESKIYKMMQGGVGIPTIRWCGAEGDYNVMVMELLGPSLEDLFNFCSRKFSLKTVLLLADQMISRIEYIHSKNFIHRDVKPDNFLMGLGKKGNLVYIIDFGLAKKYRDARTHQHIPYRENKNLTGTARYASINTHLGIEQSRRDDLESLGYVLMYFNLGSLPWQGLKAATKRQKYERISEKKMSTPIEVLCKGYPSEFATYLNFCRSLRFDDKPDYSYLRQLFRNLFHRQGFSYDYVFDWNMLK'
        template.full_seq = 'MELRVGNRYRLGRKIGSGSFGDIYLGTDIAAGEEVAIKLECVKTKHPQLHIESKIYKMMQGGVGIPTIRWCGAEGDYNVMVMELLGPSLEDLFNFCSRKFSLKTVLLLADQMISRIEYIHSKNFIHRDVKPDNFLMGLGKKGNLVYIIDFGLAKKYRDARTHQHIPYRENKNLTGTARYASINTHLGIEQSRRDDLESLGYVLMYFNLGSLPWQGLKAATKRQKYERISEKKMSTPIEVLCKGYPSEFATYLNFCRSLRFDDKPDYSYLRQLFRNLFHRQGFSYDYVFDWNMLK'

        missing_residues = msmseeder.initproject.pdbfix_template(template)
        msmseeder.initproject.loopmodel_template(template, missing_residues)

        assert os.path.exists(os.path.join('templates', 'structures-modeled-loops', 'KC1D_HUMAN_D0_3UZP_A-loopmodeled.pdb'))


def test_loopmodel_ZAP70_HUMAN_D0_1U59_A():
    with msmseeder.integration_test_utils.integration_test_context(project_data='templates_observed'):
        template = Mock()
        template.templateid = 'ZAP70_HUMAN_D0_1U59_A'
        template.chainid = 'A'
        template.resolved_seq = 'KKLFLKRDNLLIADIELGCGNFGSVRQGVYRKQIDVAIKVLKQGTEKADTEEMMREAQIMHQLDNPYIVRLIGVCQAEALMLVMEMAGGGPLHKFLVGKREEIPVSNVAELLHQVSMGMKYLEEKNFVHRDLAARNVLLVNRHYAKISDFGLSKALGADDSYYTARSAGKWPLKWYAPECINFRKFSSRSDVWSYGVTMWEALSYGQKPYKKMKGPEVMAFIEQGKRMECPPECPPELYALMSDCWIYKWEDRPDFLTVEQRMRACYYSLASKVEG'
        template.full_seq = 'DKKLFLKRDNLLIADIELGCGNFGSVRQGVYRMRKKQIDVAIKVLKQGTEKADTEEMMREAQIMHQLDNPYIVRLIGVCQAEALMLVMEMAGGGPLHKFLVGKREEIPVSNVAELLHQVSMGMKYLEEKNFVHRDLAARNVLLVNRHYAKISDFGLSKALGADDSYYTARSAGKWPLKWYAPECINFRKFSSRSDVWSYGVTMWEALSYGQKPYKKMKGPEVMAFIEQGKRMECPPECPPELYALMSDCWIYKWEDRPDFLTVEQRMRACYYSLASKVEG'

        missing_residues = msmseeder.initproject.pdbfix_template(template)
        msmseeder.initproject.loopmodel_template(template, missing_residues)

        assert os.path.exists(os.path.join('templates', 'structures-modeled-loops', 'ZAP70_HUMAN_D0_1U59_A-loopmodeled.pdb'))