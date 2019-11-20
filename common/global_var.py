# coding:utf-8


def init():
    global global_dict
    global_dict = {}


def set_value(name, value):
    global_dict[name] = value


def get_value(name, def_val=None):
    try:
        return global_dict[name]
    except KeyError:
        return def_val

