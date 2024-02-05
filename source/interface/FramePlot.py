# Autor: Gabriel Góes Rocha de Lima
# Data: 20/04/2021
# ---------------------------------------------------------------------------
#
# Canvas Para Visualização de Folhas
# ------------------------------ IMPORTS ------------------------------------
from utils import plotarInicial
from DicionarioFolhas import DicionarioFolhas
from SeletorFolhas import SeletorFolhas
from PlotFolhas import PlotFolhas

from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import ttk
import tkinter as tk
# ---------------------------------------------------------------------------


# ------------------------------- CLASSES ------------------------------------
# Classe para criar o Frame de Plotagem e métodos visuais
class FramePlot:
    '''
    Esta classe é responsável por criar o Frame de Plotagem e métodos visuais.

    Exemplo:
        plotFrame = PlotFrame(mainFrame)
    '''

    def __init__(self, mainFrame, frameSeletor, folhaEstudo, style=None):
        self.mainFrame = mainFrame
        self.folhaEstudo = folhaEstudo
        self.seletorFolhas = SeletorFolhas
        self.frameSeletor = frameSeletor
        self.dicionarioFolhas = DicionarioFolhas()
        self.ax = None
        self.style = style
        self.plotFrame()

    # ------------------------- Frame - Plot Frame
    def plotFrame(self):
        '''
        Cria o Frame para plotar as cartas.
        Implementar reconhecimento de click na tela para pegar coords.
        '''
        plotFrame = ttk.Frame(self.mainFrame, width=1200, height=880,
                              relief=tk.GROOVE, borderwidth=5,
                              style="Custom.TFrame")
        # Plot Frame é fixado na centro esquerda do Main Frame
        plotFrame.grid(row=0, column=0, padx=0, pady=0)
        plotFrame.grid_propagate(False)
        # ------------------- Canvas - Plot Frame
        self.canvas = tk.Canvas(plotFrame,
                                width=1200, height=800, bg='lightgray')
        self.canvas.grid(row=0, column=0, padx=0, pady=0)
        # ------------------- Plot Carta 1:1.000.000
        # Plotar Carta 1:1.000.000
        map, ax = plotarInicial(self.dicionarioFolhas.carta_1kk)
        self.ax = ax
        # plotar mapa no canvas
        canvas = FigureCanvasTkAgg(map, master=self.canvas)
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, column=0, padx=0, pady=0)
        # ------------------- Toolbar - Plot Frame
        toolbar = NavigationToolbar2Tk(canvas, plotFrame)
        toolbar.update()
        toolbar.grid(row=1, column=0, padx=0, pady=0)
        canvas.get_tk_widget().grid(row=0, column=0, padx=0, pady=0)
        # ------------------- Evento de Click no Canvas
        self.plotFolhas = PlotFolhas(self.dicionarioFolhas,
                                     self.seletorFolhas,
                                     self.frameSeletor,
                                     self.ax)
        map.canvas.mpl_connect('button_press_event',
                               self.plotFolhas.on_canvas_click)
