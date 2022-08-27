import tkinter as tk
import math
import pymysql #打开数据库连接

try:
    conn = pymysql.connect(host="localhost", user="root", password="4231254abc",charset="utf8")
    print("数据库连接成功")
except pymysql.Error as e:
    print("数据库连接失败："+str(e))
conn.select_db('user')
cursor=conn.cursor()
print(cursor)           #连接到数据库


cur = conn.cursor()

cur.execute("select * from data;")
resTuple = cur.fetchall()
time = len(resTuple)
print ('共%d条数据'%len(resTuple))  #取所有数据并计算数据数量
lenth = time


root = tk.Tk()

root.title("痛苦计算器")
root.geometry('445x280+100+100')

root.attributes("-alpha", 1)
root["background"] = "#ffffff"
font = ('宋体', 20)
font_16 = ('宋体', 16)

Is_cal = False  # 记录是否按下了运算符
storage = []  # 存储数字

result_num = tk.StringVar()
result_num.set('')

'''第一行'''
tk.Label(root,
         textvariable=result_num, font=font, height=2,
         width=30, justify=tk.LEFT, anchor=tk.SE  # SE表示右下角
         ).grid(row=1, column=1, columnspan=6)

'''第二行'''
btn_clear = tk.Button(root, text='C', width=5, font=font_16, relief=tk.FLAT, bg='#b1b2b2')
btn_back = tk.Button(root, text='←', width=5, font=font_16, relief=tk.FLAT, bg='#b1b2b2')
btn_division = tk.Button(root, text='÷', width=5, font=font_16, relief=tk.FLAT, bg='#b1b2b2')
btn_multiplication = tk.Button(root, text='x', width=5, font=font_16, relief=tk.FLAT, bg='#b1b2b2')
btn_memoryclear = tk.Button(root, text='MC', width=5, font=font_16, relief=tk.FLAT, bg='#b1b2b2')  #记忆清除功能
btn_memoryrecall = tk.Button(root, text='MR',width=5, font=font_16,relief=tk.FLAT, bg='#b1b2b2')  # 记忆再现功能

btn_clear.grid(row=2, column=1, padx=4, pady=2)
btn_back.grid(row=2, column=2, padx=4, pady=2)
btn_division.grid(row=2, column=3, padx=4, pady=2)
btn_multiplication.grid(row=2, column=4, padx=4, pady=2)
btn_memoryclear.grid(row=2, column=5, padx=4, pady=2)
btn_memoryrecall.grid(row=2, column=6, padx=4, pady=2)

'''第三行'''
btn_7 = tk.Button(root, text='7', width=5, font=font_16, relief=tk.FLAT, bg='#eacda1')
btn_8 = tk.Button(root, text='8', width=5, font=font_16, relief=tk.FLAT, bg='#eacda1')
btn_9 = tk.Button(root, text='9', width=5, font=font_16, relief=tk.FLAT, bg='#eacda1')
btn_subtraction = tk.Button(root, text='-', width=5, font=font_16, relief=tk.FLAT, bg='#b1b2b2')
btn_memoryup = tk.Button(root, text='M↑', width=5, font=font_16, relief=tk.FLAT, bg='#b1b2b2')  # 查找上一条记忆功能
btn_memoryadd = tk.Button(root, text='M+', width=5, font=font_16, relief=tk.FLAT, bg='#b1b2b2')  # M+功能

btn_7.grid(row=3, column=1, padx=4, pady=2)
btn_8.grid(row=3, column=2, padx=4, pady=2)
btn_9.grid(row=3, column=3, padx=4, pady=2)
btn_subtraction.grid(row=3, column=4, padx=4, pady=2)
btn_memoryup.grid(row=3, column=5, padx=4, pady=2)
btn_memoryadd.grid(row=3, column=6, padx=4, pady=2)

'''第四行'''
btn_4 = tk.Button(root, text='4', width=5, font=font_16, relief=tk.FLAT, bg='#eacda1')
btn_5 = tk.Button(root, text='5', width=5, font=font_16, relief=tk.FLAT, bg='#eacda1')
btn_6 = tk.Button(root, text='6', width=5, font=font_16, relief=tk.FLAT, bg='#eacda1')
btn_addition = tk.Button(root, text='+', width=5, font=font_16, relief=tk.FLAT, bg='#b1b2b2')
btn_memorydown = tk.Button(root, text='M↓', width=5, font=font_16, relief=tk.FLAT, bg='#b1b2b2')  # 查找下一条记忆功能
btn_memorysub = tk.Button(root, text='M-', width=5, font=font_16, relief=tk.FLAT, bg='#b1b2b2')  # M-功能

btn_4.grid(row=4, column=1, padx=4, pady=2)
btn_5.grid(row=4, column=2, padx=4, pady=2)
btn_6.grid(row=4, column=3, padx=4, pady=2)
btn_addition.grid(row=4, column=4, padx=4, pady=2)
btn_memorydown.grid(row=4, column=5, padx=4, pady=2)
btn_memorysub.grid(row=4, column=6, padx=4, pady=2)

'''第五行'''
btn_1 = tk.Button(root, text='1', width=5, font=font_16, relief=tk.FLAT, bg='#eacda1')
btn_2 = tk.Button(root, text='2', width=5, font=font_16, relief=tk.FLAT, bg='#eacda1')
btn_3 = tk.Button(root, text='3', width=5, font=font_16, relief=tk.FLAT, bg='#eacda1')
btn_leftbrackets = tk.Button(root, text='(', width=5, font=font_16, relief=tk.FLAT, bg='#b1b2b2')
btn_MS = tk.Button(root, text='MS', width=5, font=font_16, relief=tk.FLAT, bg='#b1b2b2')
btn_equal = tk.Button(root, text='=', width=5, height=3, font=font_16, relief=tk.FLAT, bg='#b1b2b2')

btn_1.grid(row=5, column=1, padx=4, pady=2)
btn_2.grid(row=5, column=2, padx=4, pady=2)
btn_3.grid(row=5, column=3, padx=4, pady=2)
btn_leftbrackets.grid(row=5, column=4, padx=4, pady=2)
btn_MS.grid(row=5, column=5, padx=4, pady=2)
btn_equal.grid(row=5, column=6, padx=4, pady=2, rowspan=2)


'''第六行'''
btn_0 = tk.Button(root, text='0', width=12, font=font_16, relief=tk.FLAT, bg='#eacda1')
btn_dot = tk.Button(root, text='.', width=5, font=font_16, relief=tk.FLAT, bg='#eacda1')
btn_rightbrackets = tk.Button(root, text=')', width=5, font=font_16, relief=tk.FLAT, bg='#b1b2b2')
btn_sqrt = tk.Button(root, text='sqrt', width=5, font=font_16, relief=tk.FLAT, bg='#b1b2b2')

btn_0.grid(row=6, column=1, columnspan=2, padx=4, pady=2)
btn_dot.grid(row=6, column=3, padx=4, pady=2)
btn_rightbrackets.grid(row=6, column=4, padx=4, pady=2)
btn_sqrt.grid(row=6, column=5, padx=4, pady=2)


'''点击事件'''


def click_button(x):
    """
    点击按钮触发的效果。

    :param x: input x
    """
    print('x:\t', x)
    result_num.set(result_num.get() + x)


def CAL(operator):
    """
    实现计算的主要函数

    :param operator: 计算器上显示的运算符

    """
    global Is_cal
    global storage
    global time,lenth
    cal_str = result_num.get()
    conn.select_db('user')  # 对接数据库
    if operator == 'sqrt':
        try:
            result = math.sqrt(float(result_num.get()))
        except:
            result = 'illegal operation'
        result_num.set(result)
        Is_cal = True
    elif operator == 'MC':
        storage.clear()
    elif operator == 'MR':
        if Is_cal:
            result_num.set('')
        storage.append(result_num.get())
        expression = ''.join(storage)
        try:
            result = eval(expression)
        except:
            result = 'illegal operation'
        result_num.set(result)
        Is_cal = True
    elif operator == 'MS':
        storage.clear()
        storage.append(result_num.get())
    elif operator == 'M+':
        storage.append(result_num.get())
    elif operator == 'M-':
        if result_num.get().startswith('-'):
            storage.append(result_num.get())
        else:
            storage.append('-' + result_num.get())
    elif operator == '=':
        if Is_cal:
            result_num.set('0')
        storage.append(result_num.get())
        expression = ''.join(storage)
        try:
            result = eval(expression)
        # 除以0的情况
        except:
            result = 'illegal operation'
        result_num.set(result)
        storage.clear()
        Is_cal = True
    insert = cursor.execute("insert into data(equation)  values ('" + cal_str + "=" + str(result) + "');")
    conn.commit()
    cur.execute("select * from data;")
    resTuple = cur.fetchall()
    time = len(resTuple)
    lenth =time
    print('后台计算记录已更新为%d条数据' % len(resTuple))  # 取所有数据并计算数据数量


def btnclear():
    """
    清除键，清空计算器显示的结果

    """
    result_num.set('')


def btnback():
    """
    删除上一个输入的数字或者运算符；若已经进行过运算则清空屏幕。

    """
    global Is_cal
    if Is_cal:
        result_num.set('')
        Is_cal = False
    if result_num.get() != '':
        if len(result_num.get()) > 1:
            result_num.set(result_num.get()[:-1])
        else:
            result_num.set('')

def btnshowup():
    '''
    对计算记录进行向上调取
    '''
    global time
    if time > 0:
        time = time -1
        cur.execute("select * from data;")
        cur.scroll(time, mode='relative')
        resTuple = cur.fetchone()
        resTuple = str(resTuple)
        resTuple = resTuple.replace(",", "").replace("'","").lstrip('(').rstrip(')')
        print (resTuple)
        result_num.set(resTuple)
    else:
        result_num.set('no more record!!')
        time = -1




def btnshowdown():
    '''
    对计算记录进行向上调取
    '''
    global time,lenth
    if time < lenth-1:
        time = time+1
        cur.execute("select * from data;")
        cur.scroll(time, mode='relative')
        resTuple = cur.fetchone()
        resTuple = str(resTuple)
        resTuple = resTuple.replace(",", "").replace("'","").lstrip('(').rstrip(')')
        print (resTuple)
        result_num.set(resTuple)
    else:
        time = lenth-1
        cur.execute("select * from data;")
        cur.scroll(time, mode='relative')
        resTuple = cur.fetchone()
        resTuple = str(resTuple)
        resTuple = resTuple.replace(",", "").replace("'","").lstrip('(').rstrip(')')
        print (resTuple)
        result_num.set(resTuple)

def login():        #加密系统
    t = 0
    while True:
        conn.select_db('user')
        cur = conn.cursor()
        c = input('Enter your name')
        sql_update = 'SELECT password FROM login WHERE stuname = "' + c + '";'
        cur.execute(sql_update)
        res = str(cur.fetchone())
        if res=="None":
            print('User Unknown!')
            continue
        else:
            while True:
                p = input('Enter your password')
                p_trans = "('" + p + "',)"
                if p_trans == res:
                    print('Welcome '+c+'~')
                    break
                else:
                    t = t+1
                    if t<5:
                        print('The Password Was Entered Incorrectly!!')
                        continue
                    else:
                        print("The Number of Times You Entered Your Password Exceeded the Limit")
                        exit()

login()
btn_1.config(command=lambda: click_button('1'))
btn_2.config(command=lambda: click_button('2'))
btn_3.config(command=lambda: click_button('3'))
btn_4.config(command=lambda: click_button('4'))
btn_5.config(command=lambda: click_button('5'))
btn_6.config(command=lambda: click_button('6'))
btn_7.config(command=lambda: click_button('7'))
btn_8.config(command=lambda: click_button('8'))
btn_9.config(command=lambda: click_button('9'))
btn_0.config(command=lambda: click_button('0'))
btn_addition.config(command=lambda: click_button('+'))
btn_subtraction.config(command=lambda: click_button('-'))
btn_multiplication.config(command=lambda: click_button('*'))
btn_division.config(command=lambda: click_button('/'))
btn_leftbrackets.config(command=lambda: click_button('('))
btn_rightbrackets.config(command=lambda: click_button(')'))

btn_sqrt.config(command=lambda: CAL('sqrt'))
btn_MS.config(command=lambda: CAL('MS'))
btn_memoryadd.config(command=lambda: CAL('M+'))
btn_memorysub.config(command=lambda: CAL('M-'))
btn_memoryclear.config(command=lambda: CAL('MC'))
btn_memoryrecall.config(command=lambda: CAL('MR'))

btn_memoryup.config(command=btnshowup)
btn_memorydown.config(command=btnshowdown)


btn_clear.config(command=btnclear)
btn_equal.config(command=lambda: CAL('='))
btn_back.config(command=btnback)

root.mainloop()
