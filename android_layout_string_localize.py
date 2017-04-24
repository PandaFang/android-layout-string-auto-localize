#!/usr/bin/python
# -*- coding:utf-8 -*-

' a module to auto put string in layout,xml into values/string.xml for adobe air native extension for android'
import sys
import os
import re
import types
import xml.dom.minidom

# 测试用例
# <TextView android:textSize="20.0dip" android:textColor="#ff04bebd" android:layout_gravity="center_horizontal" android:id="@id/tutu_action_sucess_tips" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginTop="20.0dip" android:text="修改支付密码成功" />

#<TextView android:textSize="20.0dip" android:textColor="#ff04bebd" android:layout_gravity="center_horizontal" android:id="@id/tutu_action_sucess_tips" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginTop="20.0dip" android:text=" 修改支付 密码成功 " />

#<TextView android:id="@id/tutu_contact_us_email" android:text="E-mail" android:layout_height="wrap_content"  />

#<TextView android:textSize="20.0dip" android:textColor="#ff04bebd" android:layout_gravity="center_horizontal" android:id="@id/tutu_action_sucess_tips" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginTop="20.0dip" android:text="@string/haha" />

# <TextView android:id="@id/tutu_contact_us_email" android:text="@android:string/cancel" android:layout_height="wrap_content"  />

pattern = re.compile(r'android:text="(?!@\w*:?string)([^"]+)"')



stringset = set()
fileStringDict = {}
files = os.listdir("res/layout")
count = 0

for file in files:
    path = os.path.join(".", "res/layout/" + file)
    with open(path, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            mat = pattern.search(line)
            if mat:
           
                foundStr = mat.group(1)
                print("found'", foundStr, "'in ", file)
                stringset.add(foundStr)

                if fileStringDict.get(file) == None:
                    fileStringDict[file] = set();
                fileStringDict[file].add(foundStr)

stringNameDict = dict()             
for stri in stringset:
    count = count + 1
    stringNameDict[stri] = "auto_localized_string_" + str(count)



# insert into strings.xml

path = "res/values/strings.xml"
def addToStringsXml(path):
    dom = xml.dom.minidom.parse(path)
    root = dom.documentElement
    stringss = root.getElementsByTagName("string")
    print(type(stringss))
    #for s in strings:
     #   print(s.nodeName, s.getAttribute('name'))



    for (k , v) in stringNameDict.items():
        print("stringNameDict key:", k, "value:",v)

        stringElem = dom.createElement('string')
        stringElem.setAttribute('name', v)
        stringTxtElem = dom.createTextNode(k)
        stringElem.appendChild(stringTxtElem)
        root.appendChild(dom.createTextNode('    '))
        root.appendChild(stringElem)
        root.appendChild(dom.createTextNode('\n'))
    with open(path, "w", encoding='utf-8') as f:
        dom.writexml(f, '', '')

    print(dom.toxml())

addToStringsXml(path)
addToStringsXml('res/values-zh-rCN/strings.xml')


def replaceStringsInLayout():
    for (layoutfile , stringSet) in fileStringDict.items():
        with open('res/layout/' + layoutfile, 'r+', encoding='utf-8') as f:
            content = f.read()
            f.seek(0)

            for st in stringSet:
                print(st)

                stringname = stringNameDict.get(st)
                replacesrc = 'android:text="' + st + '"'
                replacedest = 'android:text="@string/' + stringname + '"'

                print('................................')
                print(replacesrc, replacedest)
                print(',,,,,,,,,,,,,,,,,,,,,,,,,,,,')
                content = content.replace(replacesrc, replacedest)
                
               
            f.write(content)
            print("replaceStringsInLayout done ......")

                



replaceStringsInLayout()

    
                
