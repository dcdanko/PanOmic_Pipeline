from moduleultra.pipeline_config_utils import *
from packagemega import Repo as PMRepo
from packagemega.mini_language import processOperand
from sys import stderr

pipeDir = fromPipelineDir('')
pmrepo = PMRepo.loadRepo()


def scriptDir(fpath):
    dname = pipeDir + '/scripts/'
    return dname + fpath


def pmegaDB(operand):
    try:
        res = processOperand(pmrepo, operand, stringify=True)
    except KeyError:
        stderr.write('[packagemega] {} not found.\n'.format(operand))
        res = ''
    return res

def which(tool):
    cmd = 'which {}'.format(tool)
    return resolveCmd(cmd)


config = {
    'bt2': {
        'exc': {
            'filepath': which('bowtie2'),
            'version': resolveCmd('bowtie2 --version')
        }
    },
    'diamond': {
        'exc': {
            'filepath': which('diamond'),
            'version': resolveCmd('diamond --version')
        }
    },
    'align_reads_to_nr': {
        'fasta_db': {'filepath': pmegaDB('nr_protein.fasta.0')},
        'dmnd': {
            'filepath': pmegaDB('nr_protein.dmnd.0'),
            'threads': 6,
            'time': 2,
            'ram': 6,
            'block_size': 6
        }
    },
    'quantify_taxa_megan': {
        'acc2taxa': pmegaDB('megan.acc2taxa.0'),
        'blast2lca': pmegaDB('megan.blast2lca.0'),
        'time': 10,
        'ram': 10
    }
}
