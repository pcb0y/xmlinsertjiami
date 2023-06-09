import xml.etree.ElementTree as ET
import tkinter as tk
from tkinter import filedialog
import json
import time

# Create GUI window to select XML file
window = tk.Tk()
# 设置窗口标题
window.title("北方XML基材插入加密")

# 设置窗口大小
window.geometry("400x120+500+150")
color_dict = []
with open("config.ini", 'r', encoding='utf-8') as f:
    color_str = f.read()
    lb_color = tk.Label(window, text='', )
    lb_color.config(text=color_str)
    color_dict = json.loads(color_str)



def update_xml(filename):
    # Parse XML file
    tree = ET.parse(filename)
    root = tree.getroot()
    # Find node with attribute '花色'
    num = 0
    for color in color_dict:
        bar_color = root.findall(f'.//Panel[@Material="{color}"]')

        for Panel in bar_color:

            if Panel.attrib.get('BasicMaterial') == '实芯板' and Panel.attrib.get('Thickness') == "18":
                # 修改基材
                Panel.set('BasicMaterial', '实芯板-加密')
                num += 1

    tree.write(filename)
    lb.config(text=f'修改成功!')

    lb1 = tk.Label(window, text=f'{num}', font=("黑体", 30), foreground='#E33E30').pack()


# 设置回调函数
def openfile():

    # 从本地选择一个文件，并返回文件的目录
    filename = filedialog.askopenfilename()
    if filename != '':
        lb.config(text=filename)
        update_xml(filename)
    else:
        lb.config(text='您没有选择任何文件')


# 使用按钮控件调用函数
b = tk.Button(window, text="打开北方XML文件", command=openfile).pack()
lb = tk.Label(window, text='', )
lb.pack()
lb_color.pack()

window.mainloop()
