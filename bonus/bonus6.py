contents =["All carrots are to be slices longitudinally",
            "The carrots were reportedly slices longitudinally.",
            "The carrots are good."]

filenames = ["doc.txt","presentation.txt","report.txt"]


for content,filename in zip(contents,filenames):
    file = open(f"files/{filename}","w")
    file.write(content)



