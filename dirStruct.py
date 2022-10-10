import os
import configparser

from StringOutput import StringOutputClass
from configCreator import createConfig





config = configparser.ConfigParser()
config.read('config.ini')

while(('DEFAULT' in config)==False):
	createConfig()
	config = configparser.ConfigParser()
	config.read('config.ini')

if(('USER' in config) == True):
	howManyLevels=int(config['USER']['howManyLevels'])
	indentationWidth = int(config['USER']['indentationWidth'])
	showHiddenFilesAndFolders = config['USER']['showHiddenFilesAndFolders']
else:
	howManyLevels =int(config['DEFAULT']['howManyLevels'])
	indentationWidth =int(config['DEFAULT']['indentationWidth'])
	showHiddenFilesAndFolders = config['DEFAULT']['showHiddenFilesAndFolders']



indentationBeforeFolder =		"│       "
indentationFolder =				"├──────[ ]"
indentationBeforeLastFolder =	"│       "
indentationLastFolder =			"└──────[ ]"

indentationBeforeFile =			"│       "
indentationFile =				"├──────"
indentationBeforeLastFile =		"│       "
indentationLastFile =			"└──────"

# constructs the strings which are used for visual representation of the tree
if (indentationWidth != 0):
	indentationBeforeFolder = "│ "
	indentationFolder = "├[ ]"
	indentationBeforeLastFolder = "│ "
	indentationLastFolder = "└[ ]"

	indentationBeforeFile = "│ "
	indentationFile = "├"
	indentationBeforeLastFile = "│ "
	indentationLastFile = "└"

	indentationSpaceSymbol = " "
	indentationContinuationSymbol = "─"

	for i in range(indentationWidth):
		indentationBeforeFolder = indentationBeforeFolder[:1] + indentationSpaceSymbol + indentationBeforeFolder[1:]
		indentationFolder = indentationFolder[:1] + indentationContinuationSymbol + indentationFolder[1:]
		indentationBeforeLastFolder = indentationBeforeLastFolder[:1] + indentationSpaceSymbol + indentationBeforeLastFolder[1:]
		indentationLastFolder = indentationLastFolder[:1] + indentationContinuationSymbol + indentationLastFolder[1:]

		indentationBeforeFile = indentationBeforeFile[:1] + indentationSpaceSymbol + indentationBeforeFile[1:]
		indentationFile = indentationFile[:1] + indentationContinuationSymbol + indentationFile[1:]
		indentationBeforeLastFile = indentationBeforeLastFile[:1] + indentationSpaceSymbol + indentationBeforeLastFile[1:]
		indentationLastFile = indentationLastFile[:1] + indentationContinuationSymbol + indentationLastFile[1:]


def recursiveFolder(pathname, level):
	# Do not go deeper than a certain level
	if (level > howManyLevels):
		return

	# Get all items in directory
	entryList = os.listdir(pathname)

	# Remove entries starting with '.', as those should be hidden
	if (showHiddenFilesAndFolders == 'no'):
		for item in entryList:
			if item.startswith("."):
				entryList.remove(item)
			if item.startswith("__"):
				entryList.remove(item)

	onlyFolderList = []
	# Extracting only folders from all entries, since those should be displayed first
	for item in entryList:
		if (os.path.isdir(pathname + "/" + item)):
			onlyFolderList.append(item)

	# Alphabetically sorting files and folders
	entryList.sort()
	onlyFolderList.sort()

	# Removing items from all entries which are determined to be folders
	for itemToRemove in onlyFolderList:
		entryList.pop(entryList.index(itemToRemove))

	# Going through all folders first
	for folder in onlyFolderList:
		# Inserting a leading character, to offset the the '[' sign from '[ ]' of the previous folder, so it is nicely spaced
		stringToWrite = " "
		output.output_a_string(stringToWrite)

		# If it is the last folder and there are no files after it, write out the according prefacing strings
		if (len(entryList) == 0 and folder == onlyFolderList[-1]):
			# Construct a string prefacing folder according to the current level, by default using "│     " and "└──────[ ]"
			stringToWrite = indentationBeforeLastFolder * (level - 1) + indentationLastFolder + folder + "/" + "\n"
			output.output_a_string(stringToWrite)
		else:
			# Same thing, with the difference of using "│       " and "├──────[ ]", indicating there are more files or folders below it
			stringToWrite = indentationBeforeFolder * (level - 1) + indentationFolder + folder + "/" + "\n"
			output.output_a_string(stringToWrite)
		# Raise level, indicating going one level deeper
		level += 1
		# Recursively call the same function
		recursiveFolder(pathname + "/" + folder, level)
		# Lower level again, because all folder
		level -= 1

	# Lower level, because these files are inside the previous folder
	level -= 1
	# Go through all files, same as with folders except recursively calling the function again
	for file in entryList:
		stringToWrite = " "
		output.output_a_string(stringToWrite)
		if (file == entryList[-1]):
			stringToWrite = indentationBeforeLastFile * (level) + indentationLastFile + file + "\n"
			output.output_a_string(stringToWrite)
			continue
		stringToWrite = indentationBeforeFile * (level) + indentationFile + file + "\n"
		output.output_a_string(stringToWrite)
	return


output = StringOutputClass()

currentFilePath = os.path.dirname(os.path.abspath(__file__))
stringToWrite = "[ ]" + currentFilePath + "/" + "\n"
output.output_a_string(stringToWrite)

recursiveFolder(currentFilePath, 1)

output.close_file()
