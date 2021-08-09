# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NLP.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import json
from reg_ex import regular_exp_matcher
from check_search import searcher
from tokenizec import NlpTokenizer
import numpy as np
import pandas as pd
from zone_match import zone_matching
import re
from matcher import matcher
from exact_match import exact_match_fun
from collections import Counter
from boolean_query import boolean
from nltk.corpus import stopwords
from semantic import semantic
from cosine import cosine_sim
from proximity import prox
import time
data = json.loads(open("dataset.json").read())

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(945, 917)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 30, 51, 31))
        self.label.setObjectName("label")
        self.reg_ex_flag = QtWidgets.QCheckBox(self.centralwidget)
        self.reg_ex_flag.setGeometry(QtCore.QRect(430, 100, 141, 20))
        self.reg_ex_flag.setObjectName("reg_ex_flag")
        self.bool_flag = QtWidgets.QCheckBox(self.centralwidget)
        self.bool_flag.setGeometry(QtCore.QRect(80, 80, 141, 20))
        self.bool_flag.setObjectName("bool_flag")
        self.exct_match_flag = QtWidgets.QCheckBox(self.centralwidget)
        self.exct_match_flag.setGeometry(QtCore.QRect(580, 80, 141, 20))
        self.exct_match_flag.setObjectName("exct_match_flag")
        self.cos_sim_flag = QtWidgets.QCheckBox(self.centralwidget)
        self.cos_sim_flag.setGeometry(QtCore.QRect(240, 80, 141, 20))
        self.cos_sim_flag.setObjectName("cos_sim_flag")
        self.stemmers_list = QtWidgets.QComboBox(self.centralwidget)
        self.stemmers_list.setGeometry(QtCore.QRect(80, 127, 141, 22))
        self.stemmers_list.setObjectName("stemmers_list")
        self.stemmers_list.addItem("")
        self.stemmers_list.addItem("")
        self.stemmers_list.addItem("")
        self.stemmers_list.addItem("")
        self.stemmers_list.addItem("")
        self.prox_mtch_flag = QtWidgets.QCheckBox(self.centralwidget)
        self.prox_mtch_flag.setGeometry(QtCore.QRect(430, 80, 141, 20))
        self.prox_mtch_flag.setObjectName("prox_mtch_flag")
        self.wild_card_flag = QtWidgets.QCheckBox(self.centralwidget)
        self.wild_card_flag.setGeometry(QtCore.QRect(580, 100, 141, 20))
        self.wild_card_flag.setObjectName("wild_card_flag")
        self.zone_flag = QtWidgets.QCheckBox(self.centralwidget)
        self.zone_flag.setGeometry(QtCore.QRect(80, 100, 151, 20))
        self.zone_flag.setObjectName("zone_flag")
        self.sem_flag = QtWidgets.QCheckBox(self.centralwidget)
        self.sem_flag.setGeometry(QtCore.QRect(240, 100, 181, 20))
        self.sem_flag.setObjectName("sem_flag")
        self.sem_ont = QtWidgets.QComboBox(self.centralwidget)
        self.sem_ont.setGeometry(QtCore.QRect(240, 127, 141, 22))
        self.sem_ont.setObjectName("sem_ont")
        self.sem_ont.addItem("")
        self.sem_ont.addItem("")
        self.sem_ont.addItem("")
        self.stp_wrd_flag = QtWidgets.QCheckBox(self.centralwidget)
        self.stp_wrd_flag.setGeometry(QtCore.QRect(740, 80, 181, 20))
        self.stp_wrd_flag.setObjectName("stp_wrd_flag")
        self.reg_ex_list = QtWidgets.QComboBox(self.centralwidget)
        self.reg_ex_list.setGeometry(QtCore.QRect(430, 127, 101, 22))
        self.reg_ex_list.setObjectName("reg_ex_list")
        self.reg_ex_list.addItem("")
        self.reg_ex_list.addItem("")
        self.reg_ex_list.addItem("")
        self.search = QtWidgets.QPushButton(self.centralwidget)
        self.search.setGeometry(QtCore.QRect(830, 30, 93, 31))
        self.search.setObjectName("search")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(30, 150, 901, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.query = QtWidgets.QLineEdit(self.centralwidget)
        self.query.setGeometry(QtCore.QRect(80, 30, 741, 31))
        self.query.setObjectName("query")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(30, 460, 411, 191))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_3.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_3.setMidLineWidth(0)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.title = QtWidgets.QLabel(self.gridLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy)
        self.title.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.title.setFont(font)
        self.title.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.title.setFrameShape(QtWidgets.QFrame.Panel)
        self.title.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.title.setMidLineWidth(0)
        self.title.setText("")
        self.title.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.title.setWordWrap(True)
        self.title.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.title.setObjectName("title")
        self.verticalLayout_3.addWidget(self.title)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_10.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_10.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_10.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_10.setMidLineWidth(0)
        self.label_10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_3.addWidget(self.label_10)
        self.location = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.location.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.location.setFont(font)
        self.location.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.location.setFrameShape(QtWidgets.QFrame.Panel)
        self.location.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.location.setMidLineWidth(0)
        self.location.setText("")
        self.location.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.location.setWordWrap(True)
        self.location.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.location.setObjectName("location")
        self.verticalLayout_3.addWidget(self.location)
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_12.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_12.setFont(font)
        self.label_12.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_12.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_12.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_12.setMidLineWidth(0)
        self.label_12.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_3.addWidget(self.label_12)
        self.date = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.date.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.date.setFont(font)
        self.date.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.date.setFrameShape(QtWidgets.QFrame.Panel)
        self.date.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.date.setMidLineWidth(0)
        self.date.setText("")
        self.date.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.date.setWordWrap(True)
        self.date.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.date.setObjectName("date")
        self.verticalLayout_3.addWidget(self.date)
        self.gridLayout_6.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 170, 411, 281))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.listWidget = QtWidgets.QListWidget(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setEditTriggers(QtWidgets.QAbstractItemView.EditKeyPressed)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout_5.addWidget(self.listWidget, 0, 0, 1, 1)
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 660, 901, 191))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_6.setMidLineWidth(0)
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_4.addWidget(self.label_6)
        self.description = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.description.sizePolicy().hasHeightForWidth())
        self.description.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.description.setFont(font)
        self.description.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.description.setFrameShape(QtWidgets.QFrame.Panel)
        self.description.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.description.setMidLineWidth(0)
        self.description.setText("")
        self.description.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.description.setWordWrap(True)
        self.description.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.description.setObjectName("description")
        self.verticalLayout_4.addWidget(self.description)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_7.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_7.setMidLineWidth(0)
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_4.addWidget(self.label_7)
        self.notes = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.notes.sizePolicy().hasHeightForWidth())
        self.notes.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.notes.setFont(font)
        self.notes.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.notes.setFrameShape(QtWidgets.QFrame.Panel)
        self.notes.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.notes.setMidLineWidth(0)
        self.notes.setText("")
        self.notes.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.notes.setWordWrap(True)
        self.notes.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.notes.setObjectName("notes")
        self.verticalLayout_4.addWidget(self.notes)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(449, 170, 480, 480))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(210, 210))
        self.label_2.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_2.setText("")
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.results_lable = QtWidgets.QLabel(self.centralwidget)
        self.results_lable.setGeometry(QtCore.QRect(740, 126, 181, 25))
        self.results_lable.setFrameShape(QtWidgets.QFrame.Panel)
        self.results_lable.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.results_lable.setAlignment(QtCore.Qt.AlignCenter)
        self.results_lable.setObjectName("results_lable")
        self.url_flag = QtWidgets.QCheckBox(self.centralwidget)
        self.url_flag.setGeometry(QtCore.QRect(740, 100, 83, 22))
        self.url_flag.setObjectName("url_flag")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 945, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.reg_ex_list.setEnabled(False)    
        self.reg_ex_flag.clicked.connect(self.flag_check)
        self.sem_flag.clicked.connect(self.flag_check)
        self.exct_match_flag.clicked.connect(self.flag_check)
        self.bool_flag.clicked.connect(self.flag_check)
        self.prox_mtch_flag.clicked.connect(self.flag_check)
        self.zone_flag.clicked.connect(self.flag_check)
        self.sem_ont.setEnabled(False)
        self.stp_wrd_flag.clicked.connect(self.flag_check)
        self.search.clicked.connect(self.action)
        self.sem_ont.currentIndexChanged.connect(self.flag_check)
        self.listWidget.itemClicked.connect(self.get_info)
        self.wild_card_flag.clicked.connect(self.flag_check)
        self.cos_sim_flag.clicked.connect(self.flag_check)
        self.url_flag.clicked.connect(self.flag_check)
        self.data=data #assign default dataset is the dataset without any stemming 
        self.stemmed_data={}  # assign empty dictionary to stemmed data
        self.stemmed_query=[] # assign empty list to stemmed query
        self.flags=pd.DataFrame(data=np.zeros([1,12]),columns=['boolean','zone_based','cosine','wildcard','stemming','stemmer','proximity','semantic','ontology','exact_match','regex','stop_words'])
    def get_info(self,item):
        index=self.listWidget.currentRow()
        if len(self.freq):
            target_doc = self.freq['docs'][index]
        else:
            target_doc = list(self.files.keys())[index]
        self.title.setText(self.files[target_doc]['TITLE'])
        self.location.setText(self.files[target_doc]['LOCATION'])
        self.date.setText(self.files[target_doc]['DATE'])
        self.description.setText(self.files[target_doc]['DESCRIPTION'])
        self.notes.setText(str(self.files[target_doc]['NOTES']))
        self.label_2.setPixmap(QtGui.QPixmap(self.files[target_doc]['IMAGE']))
        
            
                    
    def stemmer(self,query_tokens):
        self.flags['stemmer']=self.stemmers_list.currentText()
        if self.stemmers_list.currentText()=='Porter Stemmer':
            if self.flags['stop_words'][0] == 0:
                self.stemmed_data=json.loads(open("stemmers/ps_stemmed.json").read())
                self.pos_index=json.loads(open("pos_index/pos_ps_stemmed.json").read())
            else:
                self.stemmed_data=json.loads(open("stemmers/without_stopword_ps_stemmed.json").read())
                self.pos_index=json.loads(open("pos_index/pos_without_stopword_ps_stemmed.json").read())
            sr=searcher()
            self.stemmed_query=sr.Porter_Stemmer(query_tokens)
    
        elif self.stemmers_list.currentText()=='Snowball Stemmer':
            if self.flags['stop_words'][0] == 0:
                self.stemmed_data=json.loads(open("stemmers/sb_stemmed.json").read())
                self.pos_index=json.loads(open("pos_index/pos_sb_stemmed.json").read())
            else:
                self.stemmed_data=json.loads(open("stemmers/without_stopword_sb_stemmed.json").read())
                self.pos_index=json.loads(open("pos_index/pos_without_stopword_sb_stemmed.json").read())
            sr=searcher()
            self.stemmed_query=sr.Snowball_Stemmer(query_tokens)
            
        elif self.stemmers_list.currentText()=='Lancaster Stemmer':
            if self.flags['stop_words'][0] == 0:
                self.stemmed_data=json.loads(open("stemmers/lc_stemmed.json").read())
                self.pos_index=json.loads(open("pos_index/pos_lc_stemmed.json").read())
            else:
                self.stemmed_data=json.loads(open("stemmers/without_stopword_lc_stemmed.json").read())
                self.pos_index=json.loads(open("pos_index/pos_without_stopword_lc_stemmed.json").read())
            sr=searcher()
            self.stemmed_query=sr.Lancaster_Stemmer(query_tokens)
            
        elif self.stemmers_list.currentText()=='Customized Stemmer':
            if self.flags['stop_words'][0] == 0:
                self.stemmed_data=json.loads(open("stemmers/custom_stemmed.json").read())
                self.pos_index=json.loads(open("pos_index/pos_custom_stemmed.json").read())
            else:
                self.stemmed_data=json.loads(open("stemmers/without_stopword_custom_stemmed.json").read())
                self.pos_index=json.loads(open("pos_index/pos_without_stopword_custom_stemmed.json").read())
            sr=searcher()
            self.stemmed_query=sr.Customized_Stemmer(query_tokens)
        else:
            if self.flags['stop_words'][0] == 0:
                self.stemmed_data=json.loads(open("stemmers/tokenized.json").read())
                self.pos_index=json.loads(open("pos_index/pos_tokenized.json").read())
            else:
                self.stemmed_data=json.loads(open("stemmers/without_stopword_tokenized.json").read())
                self.pos_index=json.loads(open("pos_index/pos_without_stopword_tokenized.json").read())
            self.stemmed_query=query_tokens
        
        return self.stemmed_query

    def flag_update(self):
        'boolean','zone_based','cosine','wildcard','stemming','stemmer','proximity','semantic','ontology','exact_match','regex','stop_words'
        update=[self.bool_flag.isEnabled() and self.bool_flag.isChecked(),
                self.zone_flag.isEnabled() and self.zone_flag.isChecked(),
                self.cos_sim_flag.isEnabled() and self.cos_sim_flag.isChecked(),
                self.wild_card_flag.isEnabled() and self.wild_card_flag.isChecked(),
                self.stemmers_list.isEnabled(),
                self.stemmers_list.currentText(),
                self.prox_mtch_flag.isEnabled() and self.prox_mtch_flag.isChecked(),
                self.sem_flag.isEnabled() and self.sem_flag.isChecked(),
                self.sem_ont.currentText(),
                self.exct_match_flag.isEnabled() and self.exct_match_flag.isChecked(),
                self.reg_ex_flag.isEnabled() and self.reg_ex_flag.isChecked(),
                self.stp_wrd_flag.isEnabled() and self.stp_wrd_flag.isChecked(),
                ]
        self.flags.loc[0]=update
    def flag_check(self):
        self.bool_flag.setEnabled(True)
        self.zone_flag.setEnabled(True)
        self.wild_card_flag.setEnabled(True)
        self.cos_sim_flag.setEnabled(True)
        self.exct_match_flag.setEnabled(True)
        self.reg_ex_flag.setEnabled(True)
        self.prox_mtch_flag.setEnabled(True)
        self.stp_wrd_flag.setEnabled(True)
        self.sem_flag.setEnabled(True)
        self.stemmers_list.setEnabled(True)
        self.reg_ex_list.setEnabled(False)
        self.sem_ont.setEnabled(False)
        self.url_flag.setEnabled(True)
        
        if self.bool_flag.isChecked():
            self.wild_card_flag.setEnabled(False)
            self.reg_ex_flag.setEnabled(False)
            self.prox_mtch_flag.setEnabled(False)
            self.stp_wrd_flag.setEnabled(False)
            self.cos_sim_flag.setEnabled(False)
            self.reg_ex_list.setEnabled(False)
            self.sem_flag.setEnabled(False)
            self.exct_match_flag.setEnabled(False)
            self.url_flag.setEnabled(False)
            self.flag_update()
            self.flags['boolean'][0]=True
        
        if self.reg_ex_flag.isChecked():
            self.bool_flag.setEnabled(False)
            self.wild_card_flag.setEnabled(False)
            self.exct_match_flag.setEnabled(False)
            self.prox_mtch_flag.setEnabled(False)
            self.stp_wrd_flag.setEnabled(False)
            self.zone_flag.setEnabled(False)
            self.cos_sim_flag.setEnabled(False)
            self.sem_flag.setEnabled(False)
            self.reg_ex_list.setEnabled(True)
            self.stemmers_list.setEnabled(False)
            self.url_flag.setEnabled(False)
            self.flag_update()
            self.flags['regex'][0]=True

            
        if self.exct_match_flag.isChecked():
            self.bool_flag.setEnabled(False)
            self.zone_flag.setEnabled(False)
            self.wild_card_flag.setEnabled(False)
            self.cos_sim_flag.setEnabled(False)
            self.reg_ex_flag.setEnabled(False)
            self.prox_mtch_flag.setEnabled(False)
            self.stp_wrd_flag.setEnabled(False)
            self.sem_flag.setEnabled(False)
            self.stemmers_list.setEnabled(False)
            self.reg_ex_list.setEnabled(False)
            self.sem_ont.setEnabled(False)
            self.url_flag.setEnabled(False)
            self.flag_update()
            self.flags['exact_match'][0]=True
            
       
        if self.sem_flag.isChecked():
            self.sem_ont.setEnabled(True)
            self.bool_flag.setEnabled(False)
            self.exct_match_flag.setEnabled(False)
            self.cos_sim_flag.setEnabled(False)
            self.reg_ex_flag.setEnabled(False)
            self.prox_mtch_flag.setEnabled(False)
            self.stp_wrd_flag.setEnabled(True)
            self.sem_flag.setEnabled(True)
            self.stemmers_list.setEnabled(True)
            self.reg_ex_list.setEnabled(False)
            self.flag_update()
            self.flags['semantic'][0]=True
            
            
            
        if self.prox_mtch_flag.isChecked():
            self.bool_flag.setEnabled(False)
            self.cos_sim_flag.setEnabled(False)
            self.exct_match_flag.setEnabled(False)
            self.stp_wrd_flag.setEnabled(False)
            self.reg_ex_flag.setEnabled(False)
            self.sem_flag.setEnabled(False)
            self.reg_ex_list.setEnabled(False)
            self.wild_card_flag.setEnabled(False)
            self.url_flag.setEnabled(False)
            self.flag_update()
            self.flags['proximity'][0]=True
            
        if self.wild_card_flag.isChecked():
            self.bool_flag.setEnabled(False)
            self.cos_sim_flag.setEnabled(False)
            self.exct_match_flag.setEnabled(False)
            self.reg_ex_flag.setEnabled(False)
            self.sem_flag.setEnabled(False)
            self.prox_mtch_flag.setEnabled(False)
            self.reg_ex_list.setEnabled(False)
            self.stp_wrd_flag.setEnabled(False)
            self.stemmers_list.setEnabled(False)
            self.url_flag.setEnabled(False)
            self.flag_update()
            self.flags['wildcard'][0]=True
            
        
        if self.stp_wrd_flag.isChecked():
            self.reg_ex_flag.setEnabled(False)
            self.exct_match_flag.setEnabled(False)
            self.prox_mtch_flag.setEnabled(False)
            self.wild_card_flag.setEnabled(False)
            self.bool_flag.setEnabled(False)
            self.flag_update()
            self.flags['stop_words'][0]=True
            
        if self.zone_flag.isChecked():
            self.reg_ex_flag.setEnabled(False)
            self.url_flag.setEnabled(False)
            self.flag_update()
            self.flags['zone_based'][0]=True  
            
        if self.cos_sim_flag.isChecked():
            self.bool_flag.setEnabled(False)
            self.wild_card_flag.setEnabled(False)
            self.exct_match_flag.setEnabled(False)
            self.reg_ex_flag.setEnabled(False)
            self.prox_mtch_flag.setEnabled(False)
            self.sem_flag.setEnabled(False)
            self.stp_wrd_flag.setEnabled(True)
            self.stemmers_list.setEnabled(True)
            self.reg_ex_list.setEnabled(False)
            self.flag_update()
            self.flags['cosine'][0]=True
            
        if self.url_flag.isChecked():
            self.bool_flag.setEnabled(False)
            self.zone_flag.setEnabled(False)
            self.wild_card_flag.setEnabled(False)
            self.exct_match_flag.setEnabled(False)
            self.reg_ex_flag.setEnabled(False)
            self.prox_mtch_flag.setEnabled(False)
            self.reg_ex_list.setEnabled(False)
            self.flag_update()
            
            
         
    def result_lister(self,files,freq=''):
        self.freq=freq
        self.results_lable.setText(str(len(files))+' Results Found')
        self.listWidget.clear()
        titles=[]
        if len(freq) > 0 :
            for file in freq['docs']:
                titles.append(files[file]['TITLE'])
            
        else:
            for file in files:
                titles.append(files[file]['TITLE'])
        if len(titles)==0: 
            self.listWidget.addItem('No Results')
            self.title.clear()
            self.location.clear()
            self.date.clear()
            self.description.clear()
            self.notes.clear()
            self.label_2.clear()
        else:
            self.listWidget.addItems(titles)
        QApplication.restoreOverrideCursor()
        self.statusbar.showMessage('Finished.',10000)
    def action(self):
        tk=NlpTokenizer()
        QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)        
        if self.url_flag.isChecked():
            sr=searcher()
            self.query_tokens = sr.if_url(self.query.text())
            print(NlpTokenizer().tokenizec(self.query_tokens))
            
        else: 
            self.query_tokens = self.query.text()
        
        if self.zone_flag.isChecked() and self.zone_flag.isEnabled():
            self.flags['zone_based']=True
            self.files,query_tokens,freq=zone_matching(self.query_tokens,self.flags)
            if len(query_tokens.keys()):
                stemmed_queries={}
                files2={}
                freq_2=pd.DataFrame(data=None, columns=['docs','freq'])
                for key in query_tokens.keys():
                    stemmed_queries[key]=self.stemmer(query_tokens[key])        
                    fr_2,f2= matcher(stemmed_queries[key],self.flags,tags=[key])
                    files2.update(f2)
                    freq_2=freq_2.append(fr_2,ignore_index=True)
                
                self.files.update(files2)
                freq=freq.append(freq_2)
                freq=freq.groupby(by='docs')['freq'].sum().reset_index().sort_values(by='freq',ascending=False,ignore_index=True)    
            self.result_lister(self.files,freq)
            
        elif self.exct_match_flag.isChecked() and  self.zone_flag.isEnabled()==False:
            freq, self.files=exact_match_fun(self.query_tokens,self.flags)
            self.result_lister(self.files,freq)
        
        elif self.reg_ex_flag.isChecked() and self.zone_flag.isEnabled()==False:
            exp=self.query_tokens
            func=self.reg_ex_list.currentText()
            self.files =regular_exp_matcher().reg_ex(func,exp)
            self.result_lister(self.files)        

        elif self.wild_card_flag.isChecked() and self.zone_flag.isChecked()==False:
            qr=self.query_tokens
            wilds=re.findall("\w*\*\w*",qr)                    
            text=re.findall("\*?\w\w*[.|:|?|'||...|!|-|()]?\w\w*\*?",qr)
            tokens=[item for item in text if item not in wilds]
            file_names=[]
            docs={}
            freq=pd.DataFrame(data=None,columns=['docs,freq'])
            for tk in wilds:
                exp=tk.replace('*','\w*')
                files =regular_exp_matcher().reg_ex('Find All',exp)
                file_names.extend(list(files.keys()))
                docs.update(files)
            freq_files=Counter(file_names)
            freq=freq.append(pd.DataFrame(zip(freq_files.keys(),freq_files.values()),columns=['docs','freq'],ignore_index=True).sort_values(by='freq',ascending=False,ignore_index=True))
            
            self.stemmer(tokens)            
            f2,freq_2=matcher(self.stemmed_query,self.flags)
            freq=freq.append(freq_2,ignore_index=True)
            freq=freq.groupby(by='docs')['freq'].sum().reset_index().sort_values(by='freq',ascending=False,ignore_index=True)
            docs.update(f2) 
            self.files=docs
            self.result_lister(self.files,freq)
       
        elif self.bool_flag.isChecked() and self.zone_flag.isChecked()==False:
            self.files=boolean().bool_match(tk.tokenizec(self.query_tokens), self.flags)
            self.result_lister(self.files)
            
        elif self.sem_ont.isEnabled() and self.zone_flag.isChecked()==False: 
            qr=self.query_tokens
            self.files,freq= semantic().semantic_search(qr,self.flags)
            self.result_lister(self.files,freq)
        elif self.cos_sim_flag.isChecked() and self.zone_flag.isChecked()==False:
            qr=self.query_tokens         
            self.files= cosine_sim().cosine(self.flags,qr) 
            self.result_lister(self.files)   
        elif self.prox_mtch_flag.isChecked() and self.zone_flag.isChecked()==False:
            qr=self.query_tokens       
            self.files,freq=prox().proximity(qr,self.flags)
            self.result_lister(self.files,freq)
        else:  # other checks for flags can be done here
            query_tokens=tk.tokenizec(self.query_tokens)   
            self.stemmer(query_tokens)
            if self.flags['stop_words'][0]==1:
                Stopwords=stopwords.words('english')
                self.stemmed_query=[tk for tk in self.stemmed_query if tk not in Stopwords]
            freq, self.files= matcher(self.stemmed_query,self.flags)
            self.result_lister(self.files,freq)
                    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Search"))
        self.reg_ex_flag.setText(_translate("MainWindow", "Regular Expression"))
        self.bool_flag.setText(_translate("MainWindow", "Boolean Query"))
        self.exct_match_flag.setText(_translate("MainWindow", "Exact Match"))
        self.cos_sim_flag.setText(_translate("MainWindow", "Cosine Similarity"))
        self.stemmers_list.setItemText(0, _translate("MainWindow", "No Stemming"))
        self.stemmers_list.setItemText(1, _translate("MainWindow", "Porter Stemmer"))
        self.stemmers_list.setItemText(2, _translate("MainWindow", "Snowball Stemmer"))
        self.stemmers_list.setItemText(3, _translate("MainWindow", "Lancaster Stemmer"))
        self.stemmers_list.setItemText(4, _translate("MainWindow", "Customized Stemmer"))
        self.prox_mtch_flag.setText(_translate("MainWindow", "Proximity Matching"))
        self.wild_card_flag.setText(_translate("MainWindow", "Wild Card Matching"))
        self.zone_flag.setText(_translate("MainWindow", "Zone Based Matching"))
        self.sem_flag.setText(_translate("MainWindow", "Semantic-Based Matching"))
        self.sem_ont.setItemText(0, _translate("MainWindow", "Word Net"))
        self.sem_ont.setItemText(1, _translate("MainWindow", "Yago5"))
        self.stp_wrd_flag.setText(_translate("MainWindow", "Stop Words Removal"))
        self.reg_ex_list.setItemText(0, _translate("MainWindow", "Match"))
        self.reg_ex_list.setItemText(1, _translate("MainWindow", "Search"))
        self.reg_ex_list.setItemText(2, _translate("MainWindow", "Find All"))
        self.search.setText(_translate("MainWindow", "Search"))
        self.label_3.setText(_translate("MainWindow", "Title:"))
        self.label_6.setText(_translate("MainWindow", "Description:"))
        self.label_7.setText(_translate("MainWindow", "Notes:"))
        self.label_10.setText(_translate("MainWindow", "Location:"))
        self.label_12.setText(_translate("MainWindow", "Date:"))
        self.results_lable.setText(_translate("MainWindow", "0 Results Found"))
        self.url_flag.setText(_translate("MainWindow", "URL"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    


    
        
        
        
