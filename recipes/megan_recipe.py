from packagemega import BaseRecipe, SourceFile, ConstructedFile


class MeganRecipe(BaseRecipe):
    '''
    Recipe for uniref90 with diamond index
    '''

    def __init__(self):
        super(MeganRecipe, self).__init__()
        self.acc2taxa = SourceFile(self.repo, "prot_acc2tax-May2017.abin")
        self.blast2lca = ConstructedFile(self.repo, "blast2lca")

    def name(self):
        return 'megan'

    def fileTypes(self):
        return ['megan_table']

    def resultSchema(self):
        return {
            'acc2taxa': 'megan_table',
            'blast2lca': 'megan_table'
        }

    def makeRecipe(self):
        self.acc2taxa.resolve()
        self.repo.saveFiles(self,
                            'acc2taxa',
                            self.acc2taxa.filepath())
        self.blast2lca.resolve()
        self.repo.saveFiles(self,
                            'blast2lca',
                            self.blast2lca.filepath())
