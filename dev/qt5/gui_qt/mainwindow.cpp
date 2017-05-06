#include "mainwindow.h"
#include "ui_mainwindow.h"

void salt(cv::Mat &image, int n);
void colorReduce(cv::Mat &image, int div);

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
    //salt(image,30000);
    colorReduce(image, 64);
    cv::resize(image, image, cv::Size(), 0.5, 0.5);//resize image
    cv::namedWindow("Original Image");
    cv::imshow("Original Image", image);
}

void MainWindow::on_pushButton_2_clicked()
{
    /*cv::flip(image,image,1);
    cv::namedWindow("Output Image");
    cv::imshow("Output Image", image);*/
    cv::flip(image,image,1); // process the image
    // change color channel ordering
    cv::cvtColor(image,image,CV_BGR2RGB);
    // Qt image
    QImage img= QImage((const unsigned char*)(image.data),
             image.cols,image.rows,QImage::Format_RGB888);
    // display on label
    ui->label->setPixmap(QPixmap::fromImage(img));
    // resize the label to fit the image
    ui->label->resize(ui->label->pixmap()->size());
}

void salt(cv::Mat &image, int n)
{
      for (int k=0; k<n; k++) {
         // rand() is the MFC random number generator
         // try qrand() with Qt
         int i= rand()%image.cols;
         int j= rand()%image.rows;
         if (image.channels() == 1) { // gray-level image
            image.at<uchar>(j,i)= 255;
         } else if (image.channels() == 3) { // color image
            image.at<cv::Vec3b>(j,i)[0]= 255;
            image.at<cv::Vec3b>(j,i)[1]= 255;
            image.at<cv::Vec3b>(j,i)[2]= 255;
         }
      }
}


void colorReduce(cv::Mat &image, int div=64)
{
        int nl= image.rows; // number of lines
        // total number of elements per line
        int nc= image.cols * image.channels();
        for (int j=0; j<nl; j++) {
            // get the address of row j
            uchar* data= image.ptr<uchar>(j);
            for (int i=0; i<nc; i++) {
                // process each pixel ---------------------
                data[i]=    data[i]/div*div + div/2;
                // end of pixel processing ----------------
            } // end of line
        }
}
