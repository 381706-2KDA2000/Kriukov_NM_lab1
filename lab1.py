# -*- coding: utf-8 -*-

import PySimpleGUI as sg

import matplotlib.pyplot as plt

from math import sin


def func(delta, x, y):
    return -delta * y - sin(x)
    

fig, ax = plt.subplots(figsize=(5, 3))
ax.grid()
ax.plot([0], [0])
fig.savefig('plot.png')

layout = [ [sg.Text('Уравнение маятника с диссипацией')],
          [sg.Text("x'' + d*x' + sinx = 0")],
          [sg.Text('Шаг')],
          [sg.Text('h =', size=(5, 1)), sg.Input('0.1')],
          [sg.Text('Задача Коши')],
          [sg.Text('x0 =', size=(5, 1)), sg.Input('0')],
          [sg.Text("x'0 =", size=(5, 1)), sg.Input('0')],
          [sg.Text('Параметр')],
          [sg.Text("d =", size=(5, 1)), sg.Input('0')],
          [sg.Text('Количество точек')],
          [sg.Text("n =", size=(5, 1)), sg.Input('100')],
          [sg.Button('Plot'), sg.Button('Clear'), sg.Button('Cancel')],
          [sg.Image(r'plot.png', key='plot')]]

window = sg.Window('NM lab1', layout)


while True:
    event, values = window.Read(timeout = 100)
    
    if event in (None, 'Cancel'):
        break
    if event in ('Clear'):
        fig, ax = plt.subplots(figsize=(5, 3))
        ax.grid()
        ax.plot([0], [0], 'b')
        fig.savefig('plot.png')
        window['plot'].update(r'plot.png')
    
    if event in ('Plot'):
        try:
            h = float(values[0])
            if h == 0 :
                continue
            x0 = float(values[1])
            deriv_x = float(values[2])
            delta = float(values[3])
            n = int(values[4])
        except:
            continue
    
        values_y = [0 for x in range(n)]
        values_x = [0 for x in range(n)]
    
        values_x[0] = x0
        values_y[0] = deriv_x
    
        for i in range(1, n):
            k1 = h * values_y[i-1]
            l1 = h * func(delta, values_x[i - 1], values_y[i - 1])
            k2 = h * (values_y[i - 1] + l1/2)
            l2 = h * func(delta, values_x[i - 1] + k1/2, values_y[i - 1] + l1/2)
            k3 = h * (values_y[i - 1] + l2/2)
            l3 = h * func(delta, values_x[i - 1] + k2/2, values_y[i - 1] + l2/2)
            k4 = h * (values_y[i - 1] + l3)
            l4 = h * func(delta, values_x[i - 1] + k3, values_y[i - 1] + l3)
            values_x[i] = values_x[i - 1] + (k1 + 2*k2 + 2*k3 + k4)/6
            values_y[i] = values_y[i - 1] + (l1 + 2*l2 + 2*l3 + l4)/6
            
        ax.plot(values_x, values_y, 'b')
        fig.savefig('plot.png')
        window['plot'].update(r'plot.png')

window.close()