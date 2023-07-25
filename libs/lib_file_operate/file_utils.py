#!/usr/bin/env python
# encoding: utf-8

import os


def file_is_exist(file_path):
    # 判断文件是否存在
    return os.path.exists(file_path)


def file_is_empty(file_path):
    # 判断一个文件是否为空
    return not os.path.exists(file_path) or not os.path.getsize(file_path)


def file_name_remove_ext(file_name, ext_list):
    """
    切割去除文件名的后缀,支持后缀列表
    :param file_name: 文件名
    :param ext_list: 后缀名列表
    :return: 无后缀的文件名
    """
    # 去除文件名中的路径
    file_name = os.path.basename(file_name)
    # 去重并按长度排序后缀列表
    ext_list = [ext_list] if isinstance(ext_list, str) else sorted(list(set(ext_list)), key=len, reverse=True)
    # 使用列表推导式简化代码 next 函数在找到第一个满足条件的元素后，会立即停止并返回该元素，
    file_name = next((file_name.rsplit(ext, 1)[0] for ext in ext_list if ext in file_name), file_name)
    return file_name


def file_name_add_new_ext(file_name, new_ext):
    # 基于当前文件名去除后缀添加新的文件名
    # 使用os.path模块来简化文件名和扩展名的处理
    file_name_base, file_ext = os.path.splitext(file_name)
    return f"{file_name_base}.{new_ext}"


def auto_create_file(file_path):
    # 自动创建空文件
    if not os.path.exists(file_path):
        open(file_path, 'w').close()
        return True
    return False


def auto_make_dir(path):
    # 自动创建目录
    if not os.path.exists(path):
        os.makedirs(path)
        return True
    return False
