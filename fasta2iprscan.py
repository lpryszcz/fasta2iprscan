#!/usr/bin/env python
"""Process scan proteins from fasta using online interpro scan
USAGE: cat proteins.fa | src/fasta2iprscan.py
"""

import os, sys
from Bio import SeqIO
from datetime import datetime
#from iprscan_soappy import * #serviceRun, getResult

def iprscan_soap(fasta, email, title="", verbose=1):
	"""
	"""
	params = {}
	params['sequence'] = fasta
	params['nocrc']    = 0
	params['goterms']  = 1
	# Add the other options (if defined)
	#if options.appl:
	#    params['appl'] = {'string':options.appl}
	# Submit the job
	jobid = serviceRun(email, title, params)
	#sleep
	time.sleep(3)
	getResult(jobid)

t0     = datetime.now()
email  = "lpryszcz@crg.es"
outdir = "out"
#create outdir	
if not os.path.isdir(outdir):
	os.makedirs(outdir)
#process fasta seqs
for i, r in enumerate(SeqIO.parse(sys.stdin, 'fasta'), 1):
	#get fpath
	fpath = os.path.join(outdir, r.id, r.id+".fa")
	if os.path.isfile(fpath):
		continue
	sys.stdout.write("[%s] %s %s\n" % (datetime.ctime(datetime.now()), i, r.id))
	#irpscan_soap(r.format('fasta'))
	#get subdir and store single fasta
	if not os.path.isdir(os.path.dirname(fpath)):
		os.makedirs(os.path.dirname(fpath))
	out = open(fpath, 'w'); out.write(r.format('fasta')); out.close()
	#submit job
	cmd = "src/iprscan_soappy.py --goterms --email %s --outfile %s %s" % (email, fpath, fpath)#; print cmd
	os.system(cmd)

print "#Elapsed time: %s" % (datetime.now()-t0,)
