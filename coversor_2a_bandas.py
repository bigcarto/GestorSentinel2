import arcpy
import os
import shutil

base_folder = "C:/SENTINEL/20180224/L2A_T29TPH_A005068_20180224T112228/"
destiny_base_folder = base_folder[:21]
UTM = base_folder[:31][-6:]
UTM_folder = destiny_folder + UTM
m10_folder =  base_folder + "IMG_DATA/R10m"
m20_folder =  base_folder + "IMG_DATA/R20m"
m60_folder =  base_folder + "IMG_DATA/R60m"

m_folders = (m10_folder, m20_folder, m60_folder)
for m_folder in m_folders:
    print m_folder
    try:
        os.stat(UTM_folder)
    except:
        print "Create UTM destiny folder " + UTM_folder
        os.mkdir(UTM_folder)
    arcpy.env.workspace = m_folder
    bandas = arcpy.ListRasters("*B*", "jp2")
    for banda in bandas:
        print banda
        print banda[27:][:3]
        in_file = m_folder + "/" + banda
        print in_file
        output_file = UTM_folder +"/" + banda[27:][:3] + ".jp2"
        print output_file
        if os.path.exists(output_file):
            print "el fichero ya exisxte"
        else:
            shutil.copy(in_file,output_file)
