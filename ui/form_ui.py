# Form implementation generated from reading ui file '/home/djfm/Applications/yt-channel-downloader/ui/form.ui'
#
# Created by: PyQt6 UI code generator 6.8.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridGroupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gridGroupBox.sizePolicy().hasHeightForWidth())
        self.gridGroupBox.setSizePolicy(sizePolicy)
        self.gridGroupBox.setMinimumSize(QtCore.QSize(0, 0))
        self.gridGroupBox.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.gridGroupBox.setFont(font)
        self.gridGroupBox.setObjectName("gridGroupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.gridGroupBox)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.gridLayout.setObjectName("gridLayout")
        self.downloadSelectedVidsButton = QtWidgets.QPushButton(parent=self.gridGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.downloadSelectedVidsButton.sizePolicy().hasHeightForWidth())
        self.downloadSelectedVidsButton.setSizePolicy(sizePolicy)
        self.downloadSelectedVidsButton.setMinimumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.downloadSelectedVidsButton.setFont(font)
        self.downloadSelectedVidsButton.setObjectName("downloadSelectedVidsButton")
        self.gridLayout.addWidget(self.downloadSelectedVidsButton, 0, 2, 1, 1)
        self.chanUrlEdit = QtWidgets.QLineEdit(parent=self.gridGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chanUrlEdit.sizePolicy().hasHeightForWidth())
        self.chanUrlEdit.setSizePolicy(sizePolicy)
        self.chanUrlEdit.setMinimumSize(QtCore.QSize(500, 40))
        self.chanUrlEdit.setMaximumSize(QtCore.QSize(1200, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.chanUrlEdit.setFont(font)
        self.chanUrlEdit.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.chanUrlEdit.setToolTip("")
        self.chanUrlEdit.setText("")
        self.chanUrlEdit.setCursorPosition(0)
        self.chanUrlEdit.setClearButtonEnabled(True)
        self.chanUrlEdit.setObjectName("chanUrlEdit")
        self.gridLayout.addWidget(self.chanUrlEdit, 0, 0, 1, 1)
        self.getVidListButton = QtWidgets.QPushButton(parent=self.gridGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.getVidListButton.sizePolicy().hasHeightForWidth())
        self.getVidListButton.setSizePolicy(sizePolicy)
        self.getVidListButton.setMinimumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.getVidListButton.setFont(font)
        self.getVidListButton.setObjectName("getVidListButton")
        self.gridLayout.addWidget(self.getVidListButton, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.gridGroupBox)
        self.treeView = QtWidgets.QTreeView(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeView.sizePolicy().hasHeightForWidth())
        self.treeView.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.treeView.setFont(font)
        self.treeView.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.treeView.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhNone)
        self.treeView.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.treeView.setObjectName("treeView")
        self.verticalLayout.addWidget(self.treeView)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 24))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(parent=self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(parent=self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionFile = QtGui.QAction(parent=MainWindow)
        self.actionFile.setMenuRole(QtGui.QAction.MenuRole.NoRole)
        self.actionFile.setObjectName("actionFile")
        self.actionExit = QtGui.QAction(parent=MainWindow)
        icon = QtGui.QIcon.fromTheme("system-log-out")
        self.actionExit.setIcon(icon)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.actionExit.setFont(font)
        self.actionExit.setMenuRole(QtGui.QAction.MenuRole.NoRole)
        self.actionExit.setObjectName("actionExit")
        self.actionSettings = QtGui.QAction(parent=MainWindow)
        icon = QtGui.QIcon.fromTheme("preferences-desktop-personal")
        self.actionSettings.setIcon(icon)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.actionSettings.setFont(font)
        self.actionSettings.setMenuRole(QtGui.QAction.MenuRole.NoRole)
        self.actionSettings.setObjectName("actionSettings")
        self.actionAbout = QtGui.QAction(parent=MainWindow)
        icon = QtGui.QIcon.fromTheme("user-available")
        self.actionAbout.setIcon(icon)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.actionAbout.setFont(font)
        self.actionAbout.setMenuRole(QtGui.QAction.MenuRole.NoRole)
        self.actionAbout.setObjectName("actionAbout")
        self.actionYoutube_login = QtGui.QAction(parent=MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/youtube-icon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionYoutube_login.setIcon(icon)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.actionYoutube_login.setFont(font)
        self.actionYoutube_login.setObjectName("actionYoutube_login")
        self.actionDonate = QtGui.QAction(parent=MainWindow)
        icon = QtGui.QIcon.fromTheme("face-smile")
        self.actionDonate.setIcon(icon)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.actionDonate.setFont(font)
        self.actionDonate.setObjectName("actionDonate")
        self.menuFile.addAction(self.actionSettings)
        self.menuFile.addAction(self.actionYoutube_login)
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionDonate)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "YT Channel Downloader"))
        self.downloadSelectedVidsButton.setText(_translate("MainWindow", "Download"))
        self.chanUrlEdit.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>Youtube video, playlist or channel URL</p></body></html>"))
        self.chanUrlEdit.setPlaceholderText(_translate("MainWindow", "Youtube video, playlist or channel URL"))
        self.getVidListButton.setText(_translate("MainWindow", "Fetch"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionFile.setText(_translate("MainWindow", "&File"))
        self.actionFile.setToolTip(_translate("MainWindow", "File"))
        self.actionExit.setText(_translate("MainWindow", "&Exit"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionSettings.setText(_translate("MainWindow", "&Settings"))
        self.actionSettings.setToolTip(_translate("MainWindow", "Settings"))
        self.actionSettings.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionYoutube_login.setText(_translate("MainWindow", "Youtube &login"))
        self.actionYoutube_login.setShortcut(_translate("MainWindow", "Ctrl+Shift+L"))
        self.actionDonate.setText(_translate("MainWindow", "Donate"))
        self.actionDonate.setToolTip(_translate("MainWindow", "Donate to the author"))
