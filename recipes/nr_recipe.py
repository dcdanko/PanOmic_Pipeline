from packagemega import BaseRecipe, SourceFile, ConstructedFile


class NRProteinRecipe(BaseRecipe):
    '''
    Recipe for uniref90 with diamond index
    '''

    def __init__(self):
        super(NRProteinRecipe, self).__init__()
        self.fasta = SourceFile(self.repo, "nr.faa.gz")
        self.dmnd = ConstructedFile(self.repo, "nr.dmnd")

    def name(self):
        return 'nr_protein'

    def fileTypes(self):
        return ['gz_fasta_aa', 'dmnd-db']

    def resultSchema(self):
        return {
            'fasta': 'gz_fasta_aa',
            'dmnd': 'dmnd-db'
        }

    def makeRecipe(self):
        self.fasta.resolve()
        self.repo.saveFiles(self,
                            'fasta',
                            self.fasta.filepath())
        self.dmnd.resolve()
        self.repo.saveFiles(self,
                            'dmnd',
                            self.dmnd.filepath())
