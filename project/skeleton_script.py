import os
import subprocess	

if __name__=="__main__":

	inlist_project_file = open("inlist_project", "r")
	inlist_project_lines = inlist_project_file.readlines()
	inlist_project_file.close()
	

	#iterating through solar masses from 2 to 10
	for n in range(2, 3):
	
		for i in range(len(inlist_project_lines)):
			if inlist_project_lines[i][4:16]=="initial_mass":
				inlist_project_lines[i] = "    initial_mass = " + str(n) + "\n"
	
		inlist_project_file = open("inlist_project", "w")
		inlist_project_file.writelines(inlist_project_lines)
		inlist_project_file.close()
		
		command = "./rn"
		process = subprocess.Popen(command)
		process.wait()
		print(process.returncode)
	
		data_file_name = str(n) + "MSun_He_star.data"
		data_file = open(data_file_name, "w")

		command = "cp LOGS/history.data " + data_file_name
		os.system(command)
		data_file.close()		





















