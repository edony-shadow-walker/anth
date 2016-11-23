#include "filelist.h"
#include "ui_filelist.h"
#include <iostream>

FileList::FileList(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::FileList)
{
    ui->setupUi(this);
}

FileList::~FileList()
{
    delete ui;
}

void FileList::on_listButton_clicked()
{
    std::cout << "this is button\n" << std::endl;
}
