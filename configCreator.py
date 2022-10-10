import configparser

def createConfig():
    config = configparser.ConfigParser()
    config['DEFAULT'] = {'howManyLevels': '10',
                         'indentationWidth': '5',
                         'showHiddenFilesAndFolders': 'no'}

    with open('config.ini', 'w') as configfile:
        config.write(configfile)

def createCustomConfig(howManyLevels, indentationWidth, showHiddenFilesAndFolders='no'):


    config = configparser.ConfigParser()
    config['DEFAULT'] = {'howManyLevels': '10',
                         'indentationWidth': '5',
                         'showHiddenFilesAndFolders': 'no'}

    config['USER'] = {'howManyLevels': str(howManyLevels),
                         'indentationWidth': str(indentationWidth),
                         'showHiddenFilesAndFolders': showHiddenFilesAndFolders}

    with open('config.ini', 'w') as configfile:
        config.write(configfile)

if __name__ == '__main__':
    createConfig()