import os
from os import path

output_dir = "/Users/glennsalaman/temp/iweb/lego/stats/"
output_html = output_dir+"page.html"
input_dir = "/Users/glennsalaman/Desktop/Domain.sites2/"
input_xml = output_dir+"stats.xml" 

# Write the headers
f = open(output_html, "w")
f.write("<!DOCTYPE html>")
f.write("<html>")
f.write("  <head>")
f.write("    <title>IWEB Extract tests</title>")
f.write("  </head>")
f.write("  <body>")

with open(input_xml) as infile:
  # first line is the xml verision.  read and go on.
  infile.readline()

  # second line is the *ENTIRE* XML file.  I'm gonna split it based on "<"
  file_lines = infile.readline().split("<")

  # now, cycle through all the lines.  We're looking for one with "sf:path="
  for line in file_lines:
    if (line.find('sf:path=') != -1):
      print("Potential file!")

      # Now we need to get the string after that sf:path= tag.
      # start by splitting it on the spaces
      line_pieces = line.split(" ")
     
      # then check each piece for the sf:path tag..
      for piece in line_pieces:
        if (piece[:8] == "sf:path="):
          #now we need to grab the string that follows
            temp_line = piece[9:]
            path_list = temp_line.split('"') 
   
            candidate_path = path_list[0]
           
            #now check to see if it's in our import dir
            if (path.exists(input_dir+candidate_path)):
              print(candidate_path+" exists")
              # copy the file into our output location
              os.system("cp "+input_dir+candidate_path+" "+output_dir+candidate_path)
              # ...and drop a link in our HTML file
              f.write("  <hr>")
              f.write("  <p><img src=\""+candidate_path+"\"></p>")
            else:
              print(candidate_path+" doesn't exist")
    
    # guess on text:  it's after a closing ">".
    else:
      line_pieces = line.split(">")
      if (len(line_pieces) == 2):      
        f.write("<p>"+line_pieces[1]+"</p>")
      elif (len(line_pieces) > 2):
        print("Line len > 2?!?!")
      
f.write("  </body>")
f.write("</html>")
f.close()




  
