import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt, QTimer, QPointF
from PyQt5.QtGui import QPainter, QColor, QBrush, QPen

class Bubble:
    def __init__(self, width, height):
        self.pos = QPointF(random.uniform(0, width), random.uniform(0, height))
        self.vel = QPointF(random.uniform(-2, 2), random.uniform(-2, 2))
        self.radius = random.randint(20, 40)
        self.color = QColor(random.randint(50, 255), random.randint(50, 255), 255, 180)

    def move(self, width, height):
        self.pos += self.vel
        # Bounce off edges
        if self.pos.x() < 0 or self.pos.x() > width:
            self.vel.setX(-self.vel.x())
        if self.pos.y() < 0 or self.pos.y() > height:
            self.vel.setY(-self.vel.y())

class BubbleScreensaver(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🪐 Space Bubble Loading")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("background-color: #000000;")
        self.bubbles = [Bubble(self.width(), self.height()) for _ in range(15)]

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_animation)
        self.timer.start(16)  # ~60 FPS

    def update_animation(self):
        for bubble in self.bubbles:
            bubble.move(self.width(), self.height())
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        for bubble in self.bubbles:
            painter.setBrush(QBrush(bubble.color, Qt.SolidPattern))
            pen = QPen(Qt.white)
            pen.setWidth(1)
            painter.setPen(pen)
            painter.drawEllipse(bubble.pos, bubble.radius, bubble.radius)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    screen = BubbleScreensaver()
    screen.show()
    sys.exit(app.exec_())
