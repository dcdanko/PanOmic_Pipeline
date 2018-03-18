

rule align_reads_to_nr:
    input:
        reads1 = getOriginResultFiles(config, 'filter_human_dna', 'nonhuman_read1'),
        reads2 = getOriginResultFiles(config, 'filter_human_dna', 'nonhuman_read2'),
        dmnd_db = config['align_reads_to_nr']['dmnd']['filepath']
    output:
        m8 = config['align_reads_to_nr']['m8']
    threads: int(config['align_reads_to_nr']['dmnd']['threads'])
    params:
        dmnd = config['diamond']['exc']['filepath'],
        bsize=int(config['align_reads_to_nr']['dmnd']['block_size']),
    resources:
        time=int(config['align_reads_to_nr']['dmnd']['time']),
        n_gb_ram=int(config['align_reads_to_nr']['dmnd']['ram'])
    run:
        cmd = ('{params.dmnd} blastx '
               '--threads {threads} '
               '-d {input.dmnd_db} '
               '-q {input.reads1} '
               '--block-size {params.bsize} '
               '> {output.m8} ') 
        shell(cmd)