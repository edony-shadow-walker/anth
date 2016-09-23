#ifndef FILELIST_H
#define FILELIST_H

#include <QWidget>

namespace Ui {
class FileList;
}

class FileList : public QWidget
{
    Q_OBJECT

public:
    explicit FileList(QWidget *parent = 0);
    ~FileList();

private slots:
    void on_listButton_clicked();

private:
    Ui::FileList *ui;
};

#endif // FILELIST_H
