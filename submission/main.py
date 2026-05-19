import sys, json, os
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide6.QtGui import QPixmap
from PySide6.QtCore import QEvent
from design import Ui_MainWindow


FILE = "data.json"


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.AttributeFrame.setVisible(False)

        self.data = json.load(open(FILE)) if os.path.exists(FILE) else {}
        self.current = None

        self.ui.AddButton.clicked.connect(self.add_item)
        self.ui.RemoveButton.clicked.connect(self.remove_item)
        self.ui.ListItem.itemSelectionChanged.connect(self.update_ui)

        self.ui.AttributeText.installEventFilter(self)
        self.ui.ImagePreview.mousePressEvent = self.set_image

        self.refresh()

    # ---------------- SAVE ON EXIT ----------------
    def closeEvent(self, e):
        json.dump(self.data, open(FILE, "w"), indent=4)
        e.accept()

    # ---------------- ENTER KEY ----------------
    def eventFilter(self, o, e):
        if o == self.ui.AttributeText and e.type() == QEvent.KeyPress:
            if e.key() in (16777220, 16777221):
                self.add_attr()
                return True
        return super().eventFilter(o, e)

    # ---------------- REFRESH LIST ----------------
    def refresh(self):
        self.ui.ListItem.clear()
        for i, n in enumerate(self.data, 1):
            self.ui.ListItem.addItem(f"{i}. {n}")

    def name(self, t):
        return t.split(". ", 1)[1] if ". " in t else t

    # ---------------- ITEM ----------------
    def add_item(self):
        t = self.ui.TextAddBar.toPlainText().strip()
        if t and t not in self.data:
            self.data[t] = {"attrs": [], "image": None}
            self.refresh()
            self.ui.TextAddBar.clear()
            self.ui.ListItem.setCurrentRow(self.ui.ListItem.count()-1)

    def remove_item(self):
        it = self.ui.ListItem.currentItem()
        if not it:
            return

        self.data.pop(self.name(it.text()), None)
        self.refresh()

        if self.ui.ListItem.count():
            self.ui.ListItem.setCurrentRow(0)
        else:
            self.ui.AttributeFrame.setVisible(False)
            self.ui.AttributeList.clear()
            self.ui.ImagePreview.clear()
            self.current = None

    # ---------------- SELECT ITEM ----------------
    def update_ui(self):
        it = self.ui.ListItem.currentItem()
        if not it:
            self.ui.AttributeFrame.setVisible(False)
            return

        n = self.name(it.text())
        self.current = n
        d = self.data[n]

        self.ui.AttributeFrame.setVisible(True)
        self.ui.AttributeList.clear()
        self.ui.AttributeList.addItems(d["attrs"])

        if d["image"]:
            self.ui.ImagePreview.setPixmap(
                QPixmap(d["image"]).scaled(self.ui.ImagePreview.size())
            )
        else:
            self.ui.ImagePreview.setText("Click image")

        self.ui.AttributeText.clear()

    # ---------------- ATTRIBUTE ----------------
    def add_attr(self):
        t = self.ui.AttributeText.toPlainText().strip()
        if t and self.current:
            self.data[self.current]["attrs"].append(t)
            self.ui.AttributeList.addItem(t)
            self.ui.AttributeText.clear()

    # ---------------- IMAGE ----------------
    def set_image(self, _):
        if not self.current:
            return

        f, _ = QFileDialog.getOpenFileName(self, "Image", "", "Images (*.png *.jpg *.jpeg)")
        if f:
            self.data[self.current]["image"] = f
            self.ui.ImagePreview.setPixmap(QPixmap(f).scaled(self.ui.ImagePreview.size()))


# ---------------- APP ENTRY POINT ----------------
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.resize(800, 600)
    window.show()

    sys.exit(app.exec())
