from simple_config import config

config_01 = config()

def test_add_get_str_01():
    config_01.add(section = "settings", option = "test_option", value = "string")
    _str = config_01.get(section = "settings", option = "test_option", gettingtype = "str")
    assert _str == "string"
    assert type(_str) == str

def test_add_get_str_02():
    config_01.add(section = "settings", option = "test_option", value = "String")
    _str = config_01.get(section = "settings", option = "test_option", gettingtype = "str")
    assert _str == "String"
    assert type(_str) == str

def test_add_get_str_03():
    config_01.add(section = "settings", option = "test_option", value = 42)
    _str = config_01.get(section = "settings", option = "test_option", gettingtype = "str")
    assert _str == "42"
    assert type(_str) == str

def test_add_get_int_01():
    config_01.add(section = "settings", option = "test_option", value = 42)
    _str = config_01.get(section = "settings", option = "test_option", gettingtype = "int")
    assert _str == 42
    assert type(_str) == int

def test_add_get_int_02():
    config_01.add(section = "settings", option = "test_option", value = "42")
    _str = config_01.get(section = "settings", option = "test_option", gettingtype = "int")
    assert _str == 42
    assert type(_str) == int

def test_add_get_float_01():
    config_01.add(section = "settings", option = "test_option", value = 42)
    _str = config_01.get(section = "settings", option = "test_option", gettingtype = "float")
    assert _str == 42.0
    assert type(_str) == float

def test_add_get_float_02():
    config_01.add(section = "settings", option = "test_option", value = "42")
    _str = config_01.get(section = "settings", option = "test_option", gettingtype = "float")
    assert _str == 42.0
    assert type(_str) == float