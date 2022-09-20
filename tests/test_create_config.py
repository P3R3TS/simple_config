from simple_config import config
import os.path

def test_create_without_args():
    config_01 = config()
    assert os.path.isfile("./config.ini") == True
    
def test_create_with_custom_path_01():
    path = "configs"
    config_02 = config(path = path)
    assert os.path.isfile("./configs/config.ini") == True

def test_create_with_custom_path_and_filename():
    path = "configs"
    filename = "conf.ini"
    config_03 = config(path = path, filename = filename)
    assert os.path.isfile("./configs/conf.ini") == True

def test_create_with_custom_path_02():
    path = "configs/conf"
    filename = "confi.ini"
    config_04 = config(path = path, filename = filename)
    assert os.path.isfile("./configs/conf/confi.ini") == True
