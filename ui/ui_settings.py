# Form implementation generated from reading ui file 'settings.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Settings(object):
    def setupUi(self, Settings):
        Settings.setObjectName("Settings")
        Settings.resize(954, 582)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        Settings.setFont(font)
        self.save_button = QtWidgets.QPushButton(parent=Settings)
        self.save_button.setGeometry(QtCore.QRect(330, 510, 80, 31))
        self.save_button.setObjectName("save_button")
        self.close_button = QtWidgets.QPushButton(parent=Settings)
        self.close_button.setGeometry(QtCore.QRect(500, 510, 80, 31))
        self.close_button.setObjectName("close_button")
        self.layoutWidget = QtWidgets.QWidget(parent=Settings)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 180, 451, 51))
        self.layoutWidget.setObjectName("layoutWidget")
        self.vid_quality_hlayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.vid_quality_hlayout.setContentsMargins(0, 0, 0, 0)
        self.vid_quality_hlayout.setObjectName("vid_quality_hlayout")
        self.pref_vid_quality_label = QtWidgets.QLabel(parent=self.layoutWidget)
        self.pref_vid_quality_label.setObjectName("pref_vid_quality_label")
        self.vid_quality_hlayout.addWidget(self.pref_vid_quality_label)
        self.pref_vid_quality_dropdown = QtWidgets.QComboBox(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(12)
        self.pref_vid_quality_dropdown.setFont(font)
        self.pref_vid_quality_dropdown.setObjectName("pref_vid_quality_dropdown")
        self.pref_vid_quality_dropdown.addItem("")
        self.pref_vid_quality_dropdown.addItem("")
        self.pref_vid_quality_dropdown.addItem("")
        self.pref_vid_quality_dropdown.addItem("")
        self.pref_vid_quality_dropdown.addItem("")
        self.pref_vid_quality_dropdown.addItem("")
        self.pref_vid_quality_dropdown.addItem("")
        self.pref_vid_quality_dropdown.addItem("")
        self.pref_vid_quality_dropdown.addItem("")
        self.vid_quality_hlayout.addWidget(self.pref_vid_quality_dropdown)
        self.layoutWidget_2 = QtWidgets.QWidget(parent=Settings)
        self.layoutWidget_2.setGeometry(QtCore.QRect(20, 110, 451, 51))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.pref_video_format_layout = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.pref_video_format_layout.setContentsMargins(0, 0, 0, 0)
        self.pref_video_format_layout.setObjectName("pref_video_format_layout")
        self.pref_vid_format = QtWidgets.QLabel(parent=self.layoutWidget_2)
        self.pref_vid_format.setObjectName("pref_vid_format")
        self.pref_video_format_layout.addWidget(self.pref_vid_format)
        self.pref_vid_format_dropdown = QtWidgets.QComboBox(parent=self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(12)
        self.pref_vid_format_dropdown.setFont(font)
        self.pref_vid_format_dropdown.setObjectName("pref_vid_format_dropdown")
        self.pref_vid_format_dropdown.addItem("")
        self.pref_vid_format_dropdown.addItem("")
        self.pref_vid_format_dropdown.addItem("")
        self.pref_vid_format_dropdown.addItem("")
        self.pref_vid_format_dropdown.addItem("")
        self.pref_vid_format_dropdown.addItem("")
        self.pref_vid_format_dropdown.addItem("")
        self.pref_vid_format_dropdown.addItem("")
        self.pref_video_format_layout.addWidget(self.pref_vid_format_dropdown)
        self.layoutWidget_3 = QtWidgets.QWidget(parent=Settings)
        self.layoutWidget_3.setGeometry(QtCore.QRect(20, 320, 451, 51))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.audio_quality_hlayout = QtWidgets.QHBoxLayout(self.layoutWidget_3)
        self.audio_quality_hlayout.setContentsMargins(0, 0, 0, 0)
        self.audio_quality_hlayout.setObjectName("audio_quality_hlayout")
        self.audio_quality_label = QtWidgets.QLabel(parent=self.layoutWidget_3)
        self.audio_quality_label.setObjectName("audio_quality_label")
        self.audio_quality_hlayout.addWidget(self.audio_quality_label)
        self.pref_aud_quality_dropdown = QtWidgets.QComboBox(parent=self.layoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(12)
        self.pref_aud_quality_dropdown.setFont(font)
        self.pref_aud_quality_dropdown.setObjectName("pref_aud_quality_dropdown")
        self.pref_aud_quality_dropdown.addItem("")
        self.pref_aud_quality_dropdown.addItem("")
        self.pref_aud_quality_dropdown.addItem("")
        self.pref_aud_quality_dropdown.addItem("")
        self.pref_aud_quality_dropdown.addItem("")
        self.pref_aud_quality_dropdown.addItem("")
        self.pref_aud_quality_dropdown.addItem("")
        self.pref_aud_quality_dropdown.addItem("")
        self.audio_quality_hlayout.addWidget(self.pref_aud_quality_dropdown)
        self.layoutWidget_4 = QtWidgets.QWidget(parent=Settings)
        self.layoutWidget_4.setGeometry(QtCore.QRect(20, 250, 458, 51))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.pref_audio_format_layout = QtWidgets.QHBoxLayout(self.layoutWidget_4)
        self.pref_audio_format_layout.setContentsMargins(0, 0, 0, 0)
        self.pref_audio_format_layout.setObjectName("pref_audio_format_layout")
        self.pref_aud_format = QtWidgets.QLabel(parent=self.layoutWidget_4)
        self.pref_aud_format.setObjectName("pref_aud_format")
        self.pref_audio_format_layout.addWidget(self.pref_aud_format)
        self.pref_aud_format_dropdown = QtWidgets.QComboBox(parent=self.layoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(12)
        self.pref_aud_format_dropdown.setFont(font)
        self.pref_aud_format_dropdown.setObjectName("pref_aud_format_dropdown")
        self.pref_aud_format_dropdown.addItem("")
        self.pref_aud_format_dropdown.addItem("")
        self.pref_aud_format_dropdown.addItem("")
        self.pref_aud_format_dropdown.addItem("")
        self.pref_aud_format_dropdown.addItem("")
        self.pref_aud_format_dropdown.addItem("")
        self.pref_aud_format_dropdown.addItem("")
        self.pref_aud_format_dropdown.addItem("")
        self.pref_audio_format_layout.addWidget(self.pref_aud_format_dropdown)
        self.layoutWidget_5 = QtWidgets.QWidget(parent=Settings)
        self.layoutWidget_5.setGeometry(QtCore.QRect(20, 390, 711, 72))
        self.layoutWidget_5.setObjectName("layoutWidget_5")
        self.proxy_server_layout = QtWidgets.QHBoxLayout(self.layoutWidget_5)
        self.proxy_server_layout.setContentsMargins(0, 0, 0, 0)
        self.proxy_server_layout.setObjectName("proxy_server_layout")
        self.proxy_label = QtWidgets.QLabel(parent=self.layoutWidget_5)
        self.proxy_label.setObjectName("proxy_label")
        self.proxy_server_layout.addWidget(self.proxy_label)
        self.proxy_server_type = QtWidgets.QComboBox(parent=self.layoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(12)
        self.proxy_server_type.setFont(font)
        self.proxy_server_type.setObjectName("proxy_server_type")
        self.proxy_server_type.addItem("")
        self.proxy_server_type.addItem("")
        self.proxy_server_type.addItem("")
        self.proxy_server_type.addItem("")
        self.proxy_server_layout.addWidget(self.proxy_server_type)
        self.proxy_server_label = QtWidgets.QLabel(parent=self.layoutWidget_5)
        self.proxy_server_label.setObjectName("proxy_server_label")
        self.proxy_server_layout.addWidget(self.proxy_server_label)
        self.proxy_server_addr = QtWidgets.QLineEdit(parent=self.layoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(12)
        self.proxy_server_addr.setFont(font)
        self.proxy_server_addr.setObjectName("proxy_server_addr")
        self.proxy_server_layout.addWidget(self.proxy_server_addr)
        self.proxy_port_label = QtWidgets.QLabel(parent=self.layoutWidget_5)
        self.proxy_port_label.setObjectName("proxy_port_label")
        self.proxy_server_layout.addWidget(self.proxy_port_label)
        self.proxy_server_port = QtWidgets.QLineEdit(parent=self.layoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.proxy_server_port.sizePolicy().hasHeightForWidth())
        self.proxy_server_port.setSizePolicy(sizePolicy)
        self.proxy_server_port.setMaximumSize(QtCore.QSize(70, 16777215))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(12)
        self.proxy_server_port.setFont(font)
        self.proxy_server_port.setObjectName("proxy_server_port")
        self.proxy_server_layout.addWidget(self.proxy_server_port)
        self.layoutWidget_6 = QtWidgets.QWidget(parent=Settings)
        self.layoutWidget_6.setGeometry(QtCore.QRect(20, 40, 601, 72))
        self.layoutWidget_6.setObjectName("layoutWidget_6")
        self.dl_dir_layout = QtWidgets.QHBoxLayout(self.layoutWidget_6)
        self.dl_dir_layout.setContentsMargins(0, 0, 0, 0)
        self.dl_dir_layout.setObjectName("dl_dir_layout")
        self.save_downloads_label = QtWidgets.QLabel(parent=self.layoutWidget_6)
        self.save_downloads_label.setObjectName("save_downloads_label")
        self.dl_dir_layout.addWidget(self.save_downloads_label)
        self.save_downloads_edit = QtWidgets.QLineEdit(parent=self.layoutWidget_6)
        self.save_downloads_edit.setObjectName("save_downloads_edit")
        self.dl_dir_layout.addWidget(self.save_downloads_edit)
        self.browse_btn = QtWidgets.QPushButton(parent=self.layoutWidget_6)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(12)
        font.setBold(True)
        self.browse_btn.setFont(font)
        self.browse_btn.setObjectName("browse_btn")
        self.dl_dir_layout.addWidget(self.browse_btn)
        self.layoutWidget_7 = QtWidgets.QWidget(parent=Settings)
        self.layoutWidget_7.setGeometry(QtCore.QRect(520, 120, 414, 125))
        self.layoutWidget_7.setObjectName("layoutWidget_7")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget_7)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.check_download_thumbnails = QtWidgets.QCheckBox(parent=self.layoutWidget_7)
        self.check_download_thumbnails.setObjectName("check_download_thumbnails")
        self.verticalLayout.addWidget(self.check_download_thumbnails)
        self.check_audio_only = QtWidgets.QCheckBox(parent=self.layoutWidget_7)
        self.check_audio_only.setObjectName("check_audio_only")
        self.verticalLayout.addWidget(self.check_audio_only)
        self.label = QtWidgets.QLabel(parent=self.layoutWidget_7)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(parent=self.layoutWidget_7)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(parent=self.layoutWidget_7)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)

        self.retranslateUi(Settings)
        QtCore.QMetaObject.connectSlotsByName(Settings)

    def retranslateUi(self, Settings):
        _translate = QtCore.QCoreApplication.translate
        Settings.setWindowTitle(_translate("Settings", "Settings"))
        self.save_button.setText(_translate("Settings", "Save"))
        self.close_button.setText(_translate("Settings", "Close"))
        self.pref_vid_quality_label.setText(_translate("Settings", "Preferred video quality:"))
        self.pref_vid_quality_dropdown.setItemText(0, _translate("Settings", "144p"))
        self.pref_vid_quality_dropdown.setItemText(1, _translate("Settings", "240p"))
        self.pref_vid_quality_dropdown.setItemText(2, _translate("Settings", "360p"))
        self.pref_vid_quality_dropdown.setItemText(3, _translate("Settings", "480p"))
        self.pref_vid_quality_dropdown.setItemText(4, _translate("Settings", "720p (HD)"))
        self.pref_vid_quality_dropdown.setItemText(5, _translate("Settings", "1080p (Full HD)"))
        self.pref_vid_quality_dropdown.setItemText(6, _translate("Settings", "1440p (2K)"))
        self.pref_vid_quality_dropdown.setItemText(7, _translate("Settings", "2160p (4K)"))
        self.pref_vid_quality_dropdown.setItemText(8, _translate("Settings", "Best available"))
        self.pref_vid_format.setText(_translate("Settings", "Preferred video format:"))
        self.pref_vid_format_dropdown.setItemText(0, _translate("Settings", "Any"))
        self.pref_vid_format_dropdown.setItemText(1, _translate("Settings", "mp4"))
        self.pref_vid_format_dropdown.setItemText(2, _translate("Settings", "webm"))
        self.pref_vid_format_dropdown.setItemText(3, _translate("Settings", "avi"))
        self.pref_vid_format_dropdown.setItemText(4, _translate("Settings", "mov"))
        self.pref_vid_format_dropdown.setItemText(5, _translate("Settings", "mkv"))
        self.pref_vid_format_dropdown.setItemText(6, _translate("Settings", "flv"))
        self.pref_vid_format_dropdown.setItemText(7, _translate("Settings", "3gp"))
        self.audio_quality_label.setText(_translate("Settings", "Preferred audio quality:"))
        self.pref_aud_quality_dropdown.setItemText(0, _translate("Settings", "32 kbps"))
        self.pref_aud_quality_dropdown.setItemText(1, _translate("Settings", "64 kbps"))
        self.pref_aud_quality_dropdown.setItemText(2, _translate("Settings", "128 kbps"))
        self.pref_aud_quality_dropdown.setItemText(3, _translate("Settings", "160 kbps"))
        self.pref_aud_quality_dropdown.setItemText(4, _translate("Settings", "192 kbps"))
        self.pref_aud_quality_dropdown.setItemText(5, _translate("Settings", "256 kbps"))
        self.pref_aud_quality_dropdown.setItemText(6, _translate("Settings", "320 kbps"))
        self.pref_aud_quality_dropdown.setItemText(7, _translate("Settings", "Best available"))
        self.pref_aud_format.setText(_translate("Settings", "Preferred audio format:"))
        self.pref_aud_format_dropdown.setItemText(0, _translate("Settings", "Any"))
        self.pref_aud_format_dropdown.setItemText(1, _translate("Settings", "mp3"))
        self.pref_aud_format_dropdown.setItemText(2, _translate("Settings", "ogg / oga [Vorbis]"))
        self.pref_aud_format_dropdown.setItemText(3, _translate("Settings", "m4a"))
        self.pref_aud_format_dropdown.setItemText(4, _translate("Settings", "aac"))
        self.pref_aud_format_dropdown.setItemText(5, _translate("Settings", "opus"))
        self.pref_aud_format_dropdown.setItemText(6, _translate("Settings", "flac"))
        self.pref_aud_format_dropdown.setItemText(7, _translate("Settings", "wav"))
        self.proxy_label.setText(_translate("Settings", "SOCKS / proxy:"))
        self.proxy_server_type.setItemText(0, _translate("Settings", "None"))
        self.proxy_server_type.setItemText(1, _translate("Settings", "HTTPS"))
        self.proxy_server_type.setItemText(2, _translate("Settings", "SOCKS4"))
        self.proxy_server_type.setItemText(3, _translate("Settings", "SOCKS5"))
        self.proxy_server_label.setText(_translate("Settings", "Server:"))
        self.proxy_port_label.setText(_translate("Settings", "Port:"))
        self.save_downloads_label.setText(_translate("Settings", "Save downloads to:"))
        self.browse_btn.setText(_translate("Settings", "Browse"))
        self.check_download_thumbnails.setText(_translate("Settings", "Download thumbnails"))
        self.check_audio_only.setText(_translate("Settings", "Only the associated audio tracks"))
        self.label.setText(_translate("Settings", "(Entire videos may be downloaded, then"))
        self.label_2.setText(_translate("Settings", "audio would be extracted and the videos"))
        self.label_3.setText(_translate("Settings", "will be deleted.)"))
