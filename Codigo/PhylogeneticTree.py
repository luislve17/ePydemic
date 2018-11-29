"""
## PhylogeneticTree ##
"""

from Bio import AlignIO
from Bio import Phylo
from Bio.Phylo.TreeConstruction import DistanceCalculator
from Bio.Phylo.TreeConstruction import DistanceTreeConstructor

import pylab
import os
import fnmatch

class PhylogeneticTree():
	def tree(aln_item):
		aln = [item.data(35) for item in aln_item]
		for path in aln:
			handle = open(path)

		alignment = AlignIO.read(handle,"clustal")
		calculator = DistanceCalculator('identity')	# Se calculan las distancias
		dm = calculator.get_distance(alignment)	# Se obtienen las distancias
		constructor = DistanceTreeConstructor(calculator)	
		upgma_tree = constructor.build_tree(alignment)	# Se construye el arbol filogenetico
		Phylo.draw(upgma_tree)		# Grafico del arbol filogenetico