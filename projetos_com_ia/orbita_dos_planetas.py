import sys
import numpy as np
from skyfield.api import load
import pyqtgraph as pg
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget

# Carregar dados dos planetas
ephemeris = load('de421.bsp')  # Base de dados de efemérides da NASA
ts = load.timescale()

planets = {
    'Mercúrio': ephemeris['mercury'],
    'Vênus': ephemeris['venus'],
    'Terra': ephemeris['earth'],
    'Marte': ephemeris['mars'],
    'Júpiter': ephemeris['jupiter_barycenter'],
    'Saturno': ephemeris['saturn_barycenter'],
}

# Criar a aplicação PyQt6
app = QApplication(sys.argv)

# Criar a janela principal
window = QMainWindow()
window.setWindowTitle("Órbita dos Planetas")
window.setGeometry(100, 100, 800, 600)

# Criar o layout e widget central
central_widget = QWidget()
layout = QVBoxLayout()
central_widget.setLayout(layout)
window.setCentralWidget(central_widget)

# Criar a janela do gráfico PyQtGraph
win = pg.GraphicsLayoutWidget()
layout.addWidget(win)

# Criar o gráfico principal
plot = win.addPlot(title="Órbita dos Planetas (Sistema Solar)")
plot.setAspectLocked(True)
plot.showGrid(x=True, y=True)
plot.addLegend()

# Adicionar o Sol ao centro
plot.plot([0], [0], pen=None, symbol='o', symbolBrush=(255, 204, 0), symbolSize=10, name="Sol")

# Gerar órbitas dos planetas
for name, planet in planets.items():
    x_vals, y_vals = [], []
    
    for days in np.linspace(0, 365, 100):  # Simulando um ano em 100 pontos
        t = ts.utc(2025, 1, days)  # Data simulada
        position = planet.at(t).position.au  # Posição em Unidades Astronômicas (AU)
        x_vals.append(position[0])
        y_vals.append(position[1])
    
    # Adicionar a órbita ao gráfico
    plot.plot(x_vals, y_vals, pen=pg.mkPen(width=2), name=name)

# Mostrar a janela
window.show()

# Rodar a aplicação PyQt6
sys.exit(app.exec())
