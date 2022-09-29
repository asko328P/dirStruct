import os

textFile=open('dirStruct.txt', 'w')
currentFilePath=os.path.dirname(os.path.abspath(__file__))

howManyLevels=10
indentationWidth=3
showHiddenFilesAndFolders=True

indentationBeforeFolder=		"│       "
indentationFolder=				"├──────[ ]"
indentationBeforeLastFolder=	"│       "
indentationLastFolder=			"└──────[ ]"

indentationBeforeFile=			"│       "
indentationFile=				"├──────"
indentationBeforeLastFile=		"│       "
indentationLastFile=			"└──────"


#constructs the strings which are used for visual representation of the tree
if(indentationWidth!=0):
	indentationBeforeFolder = "│ "
	indentationFolder = "├[ ]"
	indentationBeforeLastFolder = "│ "
	indentationLastFolder = "└[ ]"

	indentationBeforeFile = "│ "
	indentationFile = "├"
	indentationBeforeLastFile = "│ "
	indentationLastFile = "└"

	indentationSpaceSymbol = " "
	indentationContinuationSymbol="─"

	for i in range(indentationWidth):
		indentationBeforeFolder = indentationBeforeFolder[:1]+indentationSpaceSymbol+indentationBeforeFolder[1:]
		indentationFolder = indentationFolder[:1]+indentationContinuationSymbol+indentationFolder[1:]
		indentationBeforeLastFolder = indentationBeforeLastFolder[:1]+indentationSpaceSymbol+indentationBeforeLastFolder[1:]
		indentationLastFolder = indentationLastFolder[:1]+indentationContinuationSymbol+indentationLastFolder[1:]

		indentationBeforeFile = indentationBeforeFile[:1]+indentationSpaceSymbol+indentationBeforeFile[1:]
		indentationFile = indentationFile[:1]+indentationContinuationSymbol+indentationFile[1:]
		indentationBeforeLastFile = indentationBeforeLastFile[:1]+indentationSpaceSymbol+indentationBeforeLastFile[1:]
		indentationLastFile = indentationLastFile[:1]+indentationContinuationSymbol+indentationLastFile[1:]



def recursiveFolder(pathname, level):
	if(level>howManyLevels):
		return
	entryList=os.listdir(pathname)

	if(showHiddenFilesAndFolders==True):
		for item in entryList:
			if item.startswith("."):
				entryList.remove(item)

	onlyFolderList=[]
	for item in entryList:
		if(os.path.isdir(pathname+"/"+item)):
			onlyFolderList.append(item)
	entryList.sort()
	onlyFolderList.sort()
	for itemToRemove in onlyFolderList:
		entryList.pop(entryList.index(itemToRemove))

	for folder in onlyFolderList:
		stringToWrite = " "
		print(stringToWrite, end="")
		textFile.write(stringToWrite)
		if(len(entryList)==0 and onlyFolderList.index(folder)==len(onlyFolderList)-1):
			stringToWrite = indentationBeforeLastFolder*(level-1)+indentationLastFolder+folder+"/"+ "\n"
			print(stringToWrite, end="")
			textFile.write(stringToWrite)
		else:
			stringToWrite = indentationBeforeFolder*(level-1)+indentationFolder+folder+"/"+"\n"
			print(stringToWrite, end="")
			textFile.write(stringToWrite)
		level+=1
		recursiveFolder(pathname+"/"+folder,level)
		level-=1
	level-=1
	for file in entryList:
		stringToWrite = " "
		print(stringToWrite, end="")
		textFile.write(stringToWrite)
		if(entryList.index(file)==len(entryList)-1):
			stringToWrite = indentationBeforeLastFile*(level)+indentationLastFile+file+"\n"
			print(stringToWrite, end="")
			textFile.write(stringToWrite)
			continue
		stringToWrite=indentationBeforeFile*(level)+indentationFile+file+"\n"
		print(stringToWrite, end="")
		textFile.write(stringToWrite)
	return

stringToWrite="[ ]"+currentFilePath+"/"+"\n"
print(stringToWrite,end="")
textFile.write(stringToWrite)

recursiveFolder(currentFilePath,1)
