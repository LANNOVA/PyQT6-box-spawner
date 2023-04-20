from PyQt6.QtWidgets import QMainWindow, QGraphicsView, QGraphicsScene, QApplication, QGraphicsItem
from PyQt6.QtGui import QPainter, QPen, QBrush, QColor
from PyQt6.QtCore import Qt, QRectF, QPointF, QTimer
import random

class Shape(QGraphicsItem):
    def __init__(self, x, y, size):
        super().__init__()
        self.x = x
        self.y = y
        self.size = size
        self.color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.setPos(x, y)

    def boundingRect(self):
        return QRectF(-self.size / 2, -self.size / 2, self.size, self.size)

    def paint(self, painter, option, widget):
        painter.setPen(QPen(Qt.GlobalColor.black, 2))
        painter.setBrush(QBrush(self.color))
        painter.drawRect(self.boundingRect())

class Game(QMainWindow):
    def __init__(self):
        super().__init__()
        self.view = QGraphicsView(self)
        self.view.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.view.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.view.setScene(QGraphicsScene(self))
        self.view.setSceneRect(0, 0, 500, 500)
        self.timer = QTimer(self)
        self.setCentralWidget(self.view)
        self.timer.timeout.connect(self.spawn_shape)
        self.timer.start(1000)

    def spawn_shape(self):
        size = random.randint(10, 50)
        x = random.randint(0, 500)
        y = random.randint(0, 500)
        shape = Shape(x, y, size)
        self.view.scene().addItem(shape)

if __name__ == "__main__":
    app = QApplication([])
    game = Game()
    game.show()
    app.exec()
"""
DONATE SRAVstudios
BTC - bc1q5kmqqynratseyh7v0n8q58rn7p5xejuemmc4px

USDT(ETH) - 0x8558288490E11E7F900471E7D52F0b0A0B6b8572

USDT(SOLANA) - 4MjmiAwiQT1cqb5fSpvdsKCabZAKxopcMsTqem9gWBqB

USDT(POLYGON) - 0x8558288490E11E7F900471E7D52F0b0A0B6b8572

ETH - 0x8558288490E11E7F900471E7D52F0b0A0B6b8572
"""
