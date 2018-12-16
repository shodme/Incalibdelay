# -*- coding: UTF-8 -*-
import xml.etree.cElementTree as ET
import os

# 读入xml文件，获取xml的根节点
tree = ET.parse('test2.xml')
root = tree.getroot()
dict = {}
# -------------------读取HH模式下的时延-------------------
# 发射时延
for elem in root.iterfind('./HH_Pol/tiemDelay/headincalib/headincalibceof'):
    ceof = elem.getchildren()
    # 如果条目'quality'为'VALID'，证明该数据有效，保存
    if ceof[0].text == 'VALID':
        key = ceof[2].text + ' & ' + ceof[3].text
        # 如果该key存在，timedelay累加（列表第一位），数目加1（列表第二位）
        if key in dict:
            dict[key][0] += float(ceof[4].text)
            dict[key][1] += 1
        # 如果该key不存在，创建新的key，出现数量设置为1（列表第二位）
        else:
            dict[key] = [float(ceof[4].text), 1]

# 接收时延
for elem in root.iterfind('./HH_Pol/tiemDelay/tailincalib/tailincalibceof'):
    ceof = elem.getchildren()
    # 如果条目'quality'为'VALID'，证明该数据有效，保存
    if ceof[0].text == 'VALID':
        key = ceof[2].text + ' & ' + ceof[3].text
        # 如果该key存在，timedelay累加（列表第一位），数目加1（列表第二位）
        if key in dict:
            dict[key][0] += float(ceof[4].text)
            dict[key][1] += 1
        # 如果该key不存在，创建新的key，出现数量设置为1（列表第二位）
        else:
            dict[key] = [float(ceof[4].text), 1]

# -------------------读取HV模式下的时延-------------------
# 发射时延
for elem in root.iterfind('./HV_Pol/tiemDelay/headincalib/headincalibceof'):
    ceof = elem.getchildren()
    # 如果条目'quality'为'VALID'，证明该数据有效，保存
    if ceof[0].text == 'VALID':
        key = ceof[2].text + ' & ' + ceof[3].text
        # 如果该key存在，timedelay累加（列表第一位），数目加1（列表第二位）
        if key in dict:
            dict[key][0] += float(ceof[4].text)
            dict[key][1] += 1
        # 如果该key不存在，创建新的key，出现数量设置为1（列表第二位）
        else:
            dict[key] = [float(ceof[4].text), 1]

# 接收时延
for elem in root.iterfind('./HV_Pol/tiemDelay/tailincalib/tailincalibceof'):
    ceof = elem.getchildren()
    # 如果条目'quality'为'VALID'，证明该数据有效，保存
    if ceof[0].text == 'VALID':
        key = ceof[2].text + ' & ' + ceof[3].text
        # 如果该key存在，timedelay累加（列表第一位），数目加1（列表第二位）
        if key in dict:
            dict[key][0] += float(ceof[4].text)
            dict[key][1] += 1
        # 如果该key不存在，创建新的key，出现数量设置为1（列表第二位）
        else:
            dict[key] = [float(ceof[4].text), 1]

# -------------------读取VH模式下的时延-------------------
# 发射时延
for elem in root.iterfind('./VH_Pol/tiemDelay/headincalib/headincalibceof'):
    ceof = elem.getchildren()
    # 如果条目'quality'为'VALID'，证明该数据有效，保存
    if ceof[0].text == 'VALID':
        key = ceof[2].text + ' & ' + ceof[3].text
        # 如果该key存在，timedelay累加（列表第一位），数目加1（列表第二位）
        if key in dict:
            dict[key][0] += float(ceof[4].text)
            dict[key][1] += 1
        # 如果该key不存在，创建新的key，出现数量设置为1（列表第二位）
        else:
            dict[key] = [float(ceof[4].text), 1]

# 接收时延
for elem in root.iterfind('./VH_Pol/tiemDelay/tailincalib/tailincalibceof'):
    ceof = elem.getchildren()
    # 如果条目'quality'为'VALID'，证明该数据有效，保存
    if ceof[0].text == 'VALID':
        key = ceof[2].text + ' & ' + ceof[3].text
        # 如果该key存在，timedelay累加（列表第一位），数目加1（列表第二位）
        if key in dict:
            dict[key][0] += float(ceof[4].text)
            dict[key][1] += 1
        # 如果该key不存在，创建新的key，出现数量设置为1（列表第二位）
        else:
            dict[key] = [float(ceof[4].text), 1]

# -------------------读取VV模式下的时延-------------------
# 发射时延
for elem in root.iterfind('./VV_Pol/tiemDelay/headincalib/headincalibceof'):
    ceof = elem.getchildren()
    # 如果条目'quality'为'VALID'，证明该数据有效，保存
    if ceof[0].text == 'VALID':
        key = ceof[2].text + ' & ' + ceof[3].text
        # 如果该key存在，timedelay累加（列表第一位），数目加1（列表第二位）
        if key in dict:
            dict[key][0] += float(ceof[4].text)
            dict[key][1] += 1
        # 如果该key不存在，创建新的key，出现数量设置为1（列表第二位）
        else:
            dict[key] = [float(ceof[4].text), 1]

# 接收时延
for elem in root.iterfind('./VV_Pol/tiemDelay/tailincalib/tailincalibceof'):
    ceof = elem.getchildren()
    # 如果条目'quality'为'VALID'，证明该数据有效，保存
    if ceof[0].text == 'VALID':
        key = ceof[2].text + ' & ' + ceof[3].text
        # 如果该key存在，timedelay累加（列表第一位），数目加1（列表第二位）
        if key in dict:
            dict[key][0] += float(ceof[4].text)
            dict[key][1] += 1
        # 如果该key不存在，创建新的key，出现数量设置为1（列表第二位）
        else:
            dict[key] = [float(ceof[4].text), 1]


print(dict)