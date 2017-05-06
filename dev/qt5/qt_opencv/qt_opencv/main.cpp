#include <opencv2/opencv.hpp>
#include <opencv2/highgui/highgui.hpp>

int main(int argc, char *argv[])
{
    cv::Mat image = cv::imread("/Users/edony/Pictures/cube_fire_dark_light_alloy_36536_1920x1080.jpg");
    cv::namedWindow("my image");
    cv::imshow("my image", image);
    cv::waitKey(5000);

    return 1;
}
