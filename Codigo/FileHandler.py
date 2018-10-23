class FileHandler():
	def loadEpyFile(file_path):
		data = {}
		file_content = open(file_path).read().split('\n')
		fields = ['family','genre','species_sci', 'species', 'group', 'route_img', 'desc', 'fasta']
		for field, item in zip(fields, file_content):
			data[field] = item.split(":")[1]
		return(data)