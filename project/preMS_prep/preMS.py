#in order to make system calls, use os
import os 
#to ensure mutual exclusion and to ensure that there are no concurrency issues, use subprocess
import subprocess

if __name__=="__main__":
    
	#to open the inlist project file for configurations that we will consistently update with our script
	inlist_project_file = open("inlist_project", "r")
	#read all the lines in the file; we will write the lines with the updated configurations back
	inlist_project_lines = inlist_project_file.readlines()
	inlist_project_file.close()

        #iterating through a set of configurations for initial mass of a star
	for m in [1.75, 2, 2.25, 2.5, 2.75, 3, 3.25, 3.5, 3.75, 4, 4.25, 4.5, 4.75, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10]:
		#iterating through a set of metallicities
		for z in [0.1, 0.2, 0.5, 1, 2]:

			#removing floating point uncertainty, e.g. 3.000000000003 instead  of 3
			m = round(m, 3)
			z = round(z*0.014, 4)
			   
			#iterating through every line of the project configuration files
			for i in range(len(inlist_project_lines)):
	    
				#scanning for the line that specifies the filename of the saved model and updating it accordingly
				if inlist_project_lines[i][4:23]=="save_model_filename":
					inlist_project_lines[i] = "    save_model_filename = " + str(m) + "M" + str(z) + "ZpreMS.mod" + "\n"

				#performing similar operations for initial mass, y, z. you can see this can be generalized easily
				if inlist_project_lines[i][4:16]=="initial_mass":
					inlist_project_lines[i] = "    initial_mass = " + str(m) + "\n"
				if inlist_project_lines[i][4:13]=="initial_z":
					inlist_project_lines[i] = "    initial_z = " + str(z) + "\n"
				if inlist_project_lines[i][4:13]=="initial_y":
					inlist_project_lines[i] = "    initial_y = " + str(round(1.0-z, 4)) + "\n"
			
			#write the updated configuration project file 
			inlist_project_file = open("inlist_project", "w")
			inlist_project_file.writelines(inlist_project_lines)
			inlist_project_file.close()

			#make a system call to run MESA with this updated project file
			command = "./rn"
			#wait on MESA to finish executing
			process = subprocess.Popen(command)
			process.wait()
			#print(process.returncode) - you can use this for debugging purposes

			#writing the data after the run completes to a file of your choice filename 
			data_file_name = str(m) + "M" + str(z) + "ZpreMS.data"
			data_file = open(data_file_name, "w")
	    		
			#another system call to copy the history.data file to your file, since it is where the data is stored
			command = "cp LOGS/history.data " + data_file_name
			os.system(command)
			data_file.close()


