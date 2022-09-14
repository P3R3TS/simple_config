import configparser as cfg
import os

def writeChangies(path, config):
    with open(path, "w") as config_file:
        config.write(config_file)
    print ("create configuration file")

def createConfig(path):
    config = cfg.ConfigParser()

    try:
        os.mkdir("configs")
    except OSError:
        print("The directory already exists")
        
    print ("create configuration file")
    writeChangies(path, config)

def readConfig (path):
    if not os.path.exists(path):
        createConfig(path)

    config = cfg.ConfigParser()
    config.read(path)
    print("read configuration file")
    return config

def addNewSection (config, section, settings, path):
    config.add_section(section)
    ReurnSetting = addNewSettings (config, section, settings, path)
    return ReurnSetting

def addNewSettings (config, section, settings, path):
    value = input("input your " + settings + " ")
    config.set(section, settings, value)
    
    writeChangies(path, config)

    ReurnSetting = config.get(section, settings)
    
    return ReurnSetting

def getSettings (path, section, settings):
    config = readConfig (path)

    try:
        ReurnSetting = config.get(section, settings)
    except cfg.NoSectionError:
        ReurnSetting = addNewSection(config, section, settings, path)
    except cfg.NoOptionError:
        ReurnSetting = addNewSettings(config, section, settings, path)

    print("get " + settings + " setting")
    return ReurnSetting

def addSectionForList (config, section, settings, path):
    config.add_section(section)
    ReurnSetting = addNewSettingsForList (config, section, settings, path)
    return ReurnSetting

def addNewSettingsForList (config, section, settings, path):
    value = input("input your " + settings + " ").split()

    config.set(section, settings, " ".join(value))
    
    writeChangies(path, config)

    ReurnSetting = config.get(section, settings)
    
    return ReurnSetting

def addToList (path, section, settings, value):
    config = readConfig (path)

    setting = getList(path, section, settings)

    setting = setting.split()
    setting.append(value)
    setting = " ".join(setting)

    config.set(section, settings, setting)

    writeChangies(path, config)

    ReurnSetting = config.get(section, settings)
    
    return ReurnSetting

def deleteFromList(path, section, settings, value):
    config = readConfig (path)

    setting = getList(path, section, settings)

    setting = setting.split()
    try:
        setting.remove(value)
    except ValueError:
        return False
    setting = " ".join(setting)

    config.set(section, settings, setting)

    writeChangies(path, config)
    return True

def getList (path, section, settings):
    config = readConfig (path)

    try:
        ReurnSetting = config.get(section, settings)
    except cfg.NoSectionError:
        ReurnSetting = addSectionForList(config, section, settings, path)
    except cfg.NoOptionError:
        ReurnSetting = addNewSettingsForList(config, section, settings, path)

    print("get " + settings + " setting")
    return ReurnSetting