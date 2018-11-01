from Bio import SeqIO
import os, datetime

class AlignHandler():
	def mergeFastas(seqs_item_list, file_name):	# Aglomera los .fasta en un solo archivo (preparacion para clustalw)
		records = []
		seqs_paths = [item.data(35) for item in seqs_item_list]
		for path in seqs_paths:
			handle = open(path)
			new_record = SeqIO.read(handle, "fasta")
			records.append(new_record)

		result_name = None

		if file_name == "":	# Si no fue proporcionado un nombre
			now = datetime.datetime.now()
			result_name = "Aligment_"+now.strftime("%Y-%m-%d@%H:%M:%S") # Los archivos resultantes usaran este formato de nombre
		else:
			result_name = file_name # Si no, se respeta el nombre ingresado

		if not os.path.exists("data/aligments/"+result_name):	# Creando de manera segura un folder por alineamiento
			os.makedirs("data/aligments/"+result_name)
		SeqIO.write(records, "data/aligments/"+result_name+"/"+result_name+".fasta", "fasta")
		return ("data/aligments/"+result_name+"/", result_name)	# Retornando las rutas creadas

	def alignSeqs(merged_fasta_path, merged_fasta_name):	# Usando clustalw para alinear
		os.system("clustalw "+merged_fasta_path+merged_fasta_name+".fasta > " +merged_fasta_path+"clustalw.output")
		return(merged_fasta_path+"clustalw.output")	# Retornando la ruta del output