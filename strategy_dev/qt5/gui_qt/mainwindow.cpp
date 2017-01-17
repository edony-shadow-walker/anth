#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_pushButton_clicked()
{
    QString fileName = QFileDialog::getOpenFileName(this,
                                                    tr("Open Image"),
                                                    ".",
                                                    tr("Image Files (*.png *.jpg *.jpeg *.bmp)"));
    image= cv::imread(fileName.toUtf8().data());
    cv::namedWindow("Original Image");
    cv::imshow("Original Image", image);
}

void MainWindow::on_pushButton_2_clicked()
{
    cv::flip(image,image,1);
    cv::namedWindow("Output Image");
    cv::imshow("Output Image", image);
}
