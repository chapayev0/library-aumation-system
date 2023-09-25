from PyQt5.QtWebKit import QWebView
from PyQt5.QtGui import QApplication
from PyQt5.QtCore import QUrl
import sys
import os

app = QApplication(sys.argv)

browser = QWebView()
file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "recip_bill.html"))
local_url = QUrl.fromLocalFile(file_path)
browser.load(local_url)

browser.show()

app.exec_()