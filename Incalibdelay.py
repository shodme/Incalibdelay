# -*- coding: UTF-8 -*-
"""
时间：2018-12-16
作者：wwt117@163.com
说明：统计GF3中所有内定标XML中时延情况
补充：字典格式：{带宽&脉宽:[时延均值，数量，时延标准差, 最大时延，最小时延]}
"""
import xml.etree.cElementTree as ET
import os
import numpy as np
from math import isnan


def ReadFileList(file_dir):
    """
    读入文件夹下所有文件名
    :param file_dir: 文件存放目录
    :return: 路径下所有文件名列表
    """
    file_name = os.listdir(file_dir)
    file_name.sort()
    return file_name


# -------------------读取HH模式下的时延-------------------
def IncalibDelay_HH(file_name, dict):
    """
    统计所有内定标文件中HH模式下带脉组合的时延信息
    :param file_name: 内定标文件名
    :param dict: 用于保存带脉组合信息的字典
    :return: 保存带脉组合信息的字典
    """
    # 读入xml文件，获取xml的根节点
    tree = ET.parse(file_name)
    root = tree.getroot()

    # 发射时延
    for elem in root.iterfind('./HH_Pol/tiemDelay/headincalib/headincalibceof'):
        ceof = elem.getchildren()
        # 如果条目'quality'为'VALID'，证明该数据有效，保存
        if ceof[0].text == 'VALID':
            key = ceof[2].text + ' & ' + ceof[3].text
            if isnan(float(ceof[4].text)):
                break
            # 如果该key存在，timedelay累加（列表第一位），数目加1（列表第二位）
            if key in dict:
                dict[key][0].append(float(ceof[4].text))
                dict[key][1] += 1
            # 如果该key不存在，创建新的key，出现数量设置为1（列表第二位）
            else:
                dict[key] = [[float(ceof[4].text)], 1]

    # 接收时延
    for elem in root.iterfind('./HH_Pol/tiemDelay/tailincalib/tailincalibceof'):
        ceof = elem.getchildren()
        # 如果条目'quality'为'VALID'，证明该数据有效，保存
        if ceof[0].text == 'VALID':
            key = ceof[2].text + ' & ' + ceof[3].text
            if isnan(float(ceof[4].text)):
                break
            # 如果该key存在，timedelay累加（列表第一位），数目加1（列表第二位）
            if key in dict:
                dict[key][0].append(float(ceof[4].text))
                dict[key][1] += 1
            # 如果该key不存在，创建新的key，出现数量设置为1（列表第二位）
            else:
                dict[key] = [[float(ceof[4].text)], 1]
    return dict


# -------------------读取HV模式下的时延-------------------
def IncalibDelay_HV(file_name, dict):
    """
    统计所有内定标文件中HV模式下带脉组合的时延信息
    :param file_name: 内定标文件名
    :param dict: 用于保存带脉组合信息的字典
    :return: 保存带脉组合信息的字典
    """
    # 读入xml文件，获取xml的根节点
    tree = ET.parse(file_name)
    root = tree.getroot()

    # 发射时延
    for elem in root.iterfind('./HV_Pol/tiemDelay/headincalib/headincalibceof'):
        ceof = elem.getchildren()
        # 如果条目'quality'为'VALID'，证明该数据有效，保存
        if ceof[0].text == 'VALID':
            key = ceof[2].text + ' & ' + ceof[3].text
            if isnan(float(ceof[4].text)):
                break
            # 如果该key存在，timedelay累加（列表第一位），数目加1（列表第二位）
            if key in dict:
                dict[key][0].append(float(ceof[4].text))
                dict[key][1] += 1
            # 如果该key不存在，创建新的key，出现数量设置为1（列表第二位）
            else:
                dict[key] = [[float(ceof[4].text)], 1]

    # 接收时延
    for elem in root.iterfind('./HV_Pol/tiemDelay/tailincalib/tailincalibceof'):
        ceof = elem.getchildren()
        # 如果条目'quality'为'VALID'，证明该数据有效，保存
        if ceof[0].text == 'VALID':
            key = ceof[2].text + ' & ' + ceof[3].text
            if isnan(float(ceof[4].text)):
                break
            # 如果该key存在，timedelay累加（列表第一位），数目加1（列表第二位）
            if key in dict:
                dict[key][0].append(float(ceof[4].text))
                dict[key][1] += 1
            # 如果该key不存在，创建新的key，出现数量设置为1（列表第二位）
            else:
                dict[key] = [[float(ceof[4].text)], 1]
    return dict


# -------------------读取VH模式下的时延-------------------
def IncalibDelay_VH(file_name, dict):
    """
    统计所有内定标文件中VH模式下带脉组合的时延信息
    :param file_name: 内定标文件名
    :param dict: 用于保存带脉组合信息的字典
    :return: 保存带脉组合信息的字典
    """
    # 读入xml文件，获取xml的根节点
    tree = ET.parse(file_name)
    root = tree.getroot()

    # 发射时延
    for elem in root.iterfind('./VH_Pol/tiemDelay/headincalib/headincalibceof'):
        ceof = elem.getchildren()
        # 如果条目'quality'为'VALID'，证明该数据有效，保存
        if ceof[0].text == 'VALID':
            key = ceof[2].text + ' & ' + ceof[3].text
            if isnan(float(ceof[4].text)):
                break
            # 如果该key存在，timedelay累加（列表第一位），数目加1（列表第二位）
            if key in dict:
                dict[key][0].append(float(ceof[4].text))
                dict[key][1] += 1
            # 如果该key不存在，创建新的key，出现数量设置为1（列表第二位）
            else:
                dict[key] = [[float(ceof[4].text)], 1]

    # 接收时延
    for elem in root.iterfind('./VH_Pol/tiemDelay/tailincalib/tailincalibceof'):
        ceof = elem.getchildren()
        # 如果条目'quality'为'VALID'，证明该数据有效，保存
        if ceof[0].text == 'VALID':
            key = ceof[2].text + ' & ' + ceof[3].text
            if isnan(float(ceof[4].text)):
                break
            # 如果该key存在，timedelay累加（列表第一位），数目加1（列表第二位）
            if key in dict:
                dict[key][0].append(float(ceof[4].text))
                dict[key][1] += 1
            # 如果该key不存在，创建新的key，出现数量设置为1（列表第二位）
            else:
                dict[key] = [[float(ceof[4].text)], 1]
    return dict


# -------------------读取VV模式下的时延-------------------
def IncalibDelay_VV(file_name, dict):
    """
    统计所有内定标文件中VV模式下带脉组合的时延信息
    :param file_name: 内定标文件名
    :param dict: 用于保存带脉组合信息的字典
    :return: 保存带脉组合信息的字典
    """
    # 读入xml文件，获取xml的根节点
    tree = ET.parse(file_name)
    root = tree.getroot()

    # 发射时延
    for elem in root.iterfind('./VV_Pol/tiemDelay/headincalib/headincalibceof'):
        ceof = elem.getchildren()
        # 如果条目'quality'为'VALID'，证明该数据有效，保存
        if ceof[0].text == 'VALID':
            key = ceof[2].text + ' & ' + ceof[3].text
            if isnan(float(ceof[4].text)):
                break
            # 如果该key存在，timedelay累加（列表第一位），数目加1（列表第二位）
            if key in dict:
                dict[key][0].append(float(ceof[4].text))
                dict[key][1] += 1
            # 如果该key不存在，创建新的key，出现数量设置为1（列表第二位）
            else:
                dict[key] = [[float(ceof[4].text)], 1]

    # 接收时延
    for elem in root.iterfind('./VV_Pol/tiemDelay/tailincalib/tailincalibceof'):
        ceof = elem.getchildren()
        # 如果条目'quality'为'VALID'，证明该数据有效，保存
        if ceof[0].text == 'VALID':
            key = ceof[2].text + ' & ' + ceof[3].text
            if isnan(float(ceof[4].text)):
                break
            # 如果该key存在，timedelay累加（列表第一位），数目加1（列表第二位）
            if key in dict:
                dict[key][0].append(float(ceof[4].text))
                dict[key][1] += 1
            # 如果该key不存在，创建新的key，出现数量设置为1（列表第二位）
            else:
                dict[key] = [[float(ceof[4].text)], 1]
    return dict


if __name__ == '__main__':

    # 内定标文件路径
    file_dir = "C:\\Users\\wwt117\\Desktop\\incalib_path"

    # 读入所有文件名的列表
    file_list = ReadFileList(file_dir)

    # 设置字典用于存放不同带脉组合的时延和出现次数
    dict = {}

    # 统计每个文件中的内定标时延信息
    for file_name in file_list:
        # 获得文件绝对路径
        file_path = os.path.join(file_dir, file_name)
        dict = IncalibDelay_HH(file_path, dict)
        dict = IncalibDelay_HV(file_path, dict)
        dict = IncalibDelay_VH(file_path, dict)
        dict = IncalibDelay_VV(file_path, dict)

    # 计算时延平均值
    for key in dict:
        dict[key].append(np.std(dict[key][0]))  # 标准差
        dict[key].append(np.max(dict[key][0]))  # 最大值
        dict[key].append(np.min(dict[key][0]))  # 最小值
        dict[key][0] = np.sum(dict[key][0]) / dict[key][1]

    # 打印所有的带脉组合统计信息
    print("%s %14s %8s %10s %8s % 10s" % ("Bandwidth & Pulsewidth", "时延均值", "景数",
                                          "时延标准差", "最大时延", "最小时延"))
    for key, value in dict.items():
        print('{0:25s}:{1:15.5f}{2:10d}{3:15.5f}{4:15.5f}{5:15.5f}'
              .format(key, value[0], value[1], value[2], value[3],value[4]))

    # 输出到文件中
    f = open("Incalibdelay.txt", "w", encoding="utf-8")
    print("%s %14s %8s %10s %8s % 10s" % ("Bandwidth & Pulsewidth", "时延均值", "数量",
                                          "时延标准差", "最大时延", "最小时延"), file=f)
    for key, value in dict.items():
        print('{0:25s}:{1:15.5f}{2:10d}{3:15.5f}{4:15.5f}{5:15.5f}'
              .format(key, value[0], value[1], value[2], value[3],value[4]), file=f)
    f.close()
