import tkinter as tk

root = tk.Tk()
root.title("成功计算器")
root.geometry('295x280+100+100')

root.attributes("-alpha", 1)
root["background"] = "#ffffff"
font = ('宋体', 20)
font_16 = ('宋体', 16)

result_num = tk.StringVar()
result_num.set('')

'''第一行'''
tk.Label(root,
         textvariable=result_num, font=font, height=2,
         width=20, justify=tk.LEFT, anchor=tk.SE  # SE表示右下角
         ).grid(row=1, column=1, columnspan=4)

'''第二行'''
btn_clear = tk.Button(root, text='C', width=5, font=font_16, relief=tk.FLAT, bg='#b1b2b2')
btn_back = tk.Button(root, text='←', width=5, font=font_16, relief=tk.FLAT, bg='#b1b2b2')
btn_division = tk.Button(root, text='÷', width=5, font=font_16, relief=tk.FLAT, bg='#b1b2b2')
btn_multiplication = tk.Button(root, text='x', width=5, font=font_16, relief=tk.FLAT, bg='#b1b2b2')

btn_clear.grid(row=2, column=1, padx=4, pady=2)
btn_back.grid(row=2, column=2, padx=4, pady=2)
btn_division.grid(row=2, column=3, padx=4, pady=2)
btn_multiplication.grid(row=2, column=4, padx=4, pady=2)

'''第三行'''
btn_7 = tk.Button(root, text='7', width=5, font=font_16, relief=tk.FLAT, bg='#eacda1')
btn_8 = tk.Button(root, text='8', width=5, font=font_16, relief=tk.FLAT, bg='#eacda1')
btn_9 = tk.Button(root, text='9', width=5, font=font_16, relief=tk.FLAT, bg='#eacda1')
btn_subtraction = tk.Button(root, text='-', width=5, font=font_16, relief=tk.FLAT, bg='#b1b2b2')

btn_7.grid(row=3, column=1, padx=4, pady=2)
btn_8.grid(row=3, column=2, padx=4, pady=2)
btn_9.grid(row=3, column=3, padx=4, pady=2)
btn_subtraction.grid(row=3, column=4, padx=4, pady=2)

'''第四行'''
btn_4 = tk.Button(root, text='4', width=5, font=font_16, relief=tk.FLAT, bg='#eacda1')
btn_5 = tk.Button(root, text='5', width=5, font=font_16, relief=tk.FLAT, bg='#eacda1')
btn_6 = tk.Button(root, text='6', width=5, font=font_16, relief=tk.FLAT, bg='#eacda1')
btn_addition = tk.Button(root, text='+', width=5, font=font_16, relief=tk.FLAT, bg='#b1b2b2')

btn_4.grid(row=4, column=1, padx=4, pady=2)
btn_5.grid(row=4, column=2, padx=4, pady=2)
btn_6.grid(row=4, column=3, padx=4, pady=2)
btn_addition.grid(row=4, column=4, padx=4, pady=2)

'''第五行'''
btn_1 = tk.Button(root, text='1', width=5, font=font_16, relief=tk.FLAT, bg='#eacda1')
btn_2 = tk.Button(root, text='2', width=5, font=font_16, relief=tk.FLAT, bg='#eacda1')
btn_3 = tk.Button(root, text='3', width=5, font=font_16, relief=tk.FLAT, bg='#eacda1')
btn_equal = tk.Button(root, text='=', width=5, height=3, font=font_16, relief=tk.FLAT, bg='#b1b2b2')

btn_1.grid(row=5, column=1, padx=4, pady=2)
btn_2.grid(row=5, column=2, padx=4, pady=2)
btn_3.grid(row=5, column=3, padx=4, pady=2)
btn_equal.grid(row=5, column=4, padx=4, pady=2, rowspan=2)

'''第六行'''
btn_0 = tk.Button(root, text='0', width=12, font=font_16, relief=tk.FLAT, bg='#eacda1')
btn_dot = tk.Button(root, text='.', width=5, font=font_16, relief=tk.FLAT, bg='#eacda1')

btn_0.grid(row=6, column=1, columnspan=2, padx=4, pady=2)
btn_dot.grid(row=6, column=3, padx=4, pady=2)


'''点击事件'''


def click_button(x):
    """
    This is a function, click_button!

    :param x: input x
    :return:
    """
    print('x:\t', x)
    result_num.set(result_num.get() + x)


def calculation():
    cal_str = result_num.get()
    print(cal_str)
    result = eval(cal_str)  # 计算字符串的结果
    result_num.set(str(result))  # 最终在label上显示的结果


def btclear():
    result_num.set('')


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
btn_dot.config(command=lambda: click_button('.'))
btn_addition.config(command=lambda: click_button('+'))
btn_subtraction.config(command=lambda: click_button('-'))
btn_multiplication.config(command=lambda: click_button('*'))
btn_division.config(command=lambda: click_button('/'))

btn_clear.config(command=btclear)
btn_equal.config(command=calculation)

root.mainloop()
