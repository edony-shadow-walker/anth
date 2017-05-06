/********************************************************************************
** Form generated from reading UI file 'filelist.ui'
**
** Created by: Qt User Interface Compiler version 5.6.1
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_FILELIST_H
#define UI_FILELIST_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QTextEdit>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_FileList
{
public:
    QLabel *label;
    QLineEdit *lineEdit;
    QPushButton *listButton;
    QTextEdit *textEdit;

    void setupUi(QWidget *FileList)
    {
        if (FileList->objectName().isEmpty())
            FileList->setObjectName(QStringLiteral("FileList"));
        FileList->resize(400, 300);
        label = new QLabel(FileList);
        label->setObjectName(QStringLiteral("label"));
        label->setGeometry(QRect(20, 20, 59, 16));
        lineEdit = new QLineEdit(FileList);
        lineEdit->setObjectName(QStringLiteral("lineEdit"));
        lineEdit->setGeometry(QRect(80, 20, 171, 21));
        listButton = new QPushButton(FileList);
        listButton->setObjectName(QStringLiteral("listButton"));
        listButton->setGeometry(QRect(270, 20, 113, 32));
        textEdit = new QTextEdit(FileList);
        textEdit->setObjectName(QStringLiteral("textEdit"));
        textEdit->setGeometry(QRect(20, 60, 361, 221));

        retranslateUi(FileList);

        QMetaObject::connectSlotsByName(FileList);
    } // setupUi

    void retranslateUi(QWidget *FileList)
    {
        FileList->setWindowTitle(QApplication::translate("FileList", "FileList", 0));
        label->setText(QApplication::translate("FileList", "File List", 0));
        listButton->setText(QApplication::translate("FileList", "List", 0));
    } // retranslateUi

};

namespace Ui {
    class FileList: public Ui_FileList {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_FILELIST_H
