

rule quantify_taxa_megan:
    input:
        dmnd_m8 = config['align_reads_to_nr']['m8'],
        acc2tax = config['quantify_taxa_megan']['acc2tax']
    output:
        taxa = config['quantify_taxa_megan']['taxa']
    params:
        blast2lca = config['quantify_taxa_megan']['blast2lca'],
    resources:
        time=int(config['quantify_taxa_megan']['time']),
        n_gb_ram=int(config['quantify_taxa_megan']['ram'])
    run:
        cmd = ('{params.blast2lca} '
               '-i {input.dmnd_m8} '
               '-f DAA '
               '-m BlastX '
               '-a2t {input.acc2tax} '
               '-o {output.taxa} '
        )
        shell(cmd)