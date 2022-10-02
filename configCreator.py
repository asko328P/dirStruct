import configparser

def createConfig():
    config = configparser.ConfigParser()
    config['DEFAULT'] = {'howManyLevels': '10',
                         'indentationWidth': '5',
                         'showHiddenFilesAndFolders': 'no'}
    print("created config")

    with open('config.ini', 'w') as configfile:
        config.write(configfile)

if __name__ == '__main__':
    createConfig()