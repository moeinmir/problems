#include "helpers.h"
#include <stdio.h>
#include <math.h>
// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{

    for (int i = 0; i < height;i++)
    {
        for (int j = 0; j < width; j++)
        {
RGBTRIPLE pixel = image[i][j];
int average = round((pixel.rgbtBlue + pixel.rgbtGreen + pixel.rgbtRed)/3.0);
            image[i][j].rgbtBlue=image[i][j].rgbtRed=image[i][j].rgbtGreen=average;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{

    for (int i = 0; i < height;i++)
    {
        for (int j = 0; j < width; j++)
        {
RGBTRIPLE pixel = image[i][j];


int sepiaRed = round(.393 * pixel.rgbtRed + .769 * pixel.rgbtGreen + .189 * pixel.rgbtBlue);
int sepiaGreen = round(.349 * pixel.rgbtRed + .686 * pixel.rgbtGreen + .168 *pixel.rgbtBlue);
int sepiaBlue = round(.272 * pixel.rgbtRed + .534 * pixel.rgbtGreen + .131 * pixel.rgbtBlue);

image[i][j].rgbtRed=sepiaRed>255 ? 255:sepiaRed;
image[i][j].rgbtGreen=sepiaGreen>255 ? 255:sepiaGreen;
image[i][j].rgbtBlue=sepiaBlue>255 ? 255:sepiaBlue;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
RGBTRIPLE temp[height][width];


for (int i=0;i<height;i++)
{
    int curPos=0;
    for (int j= width -1; j>=0;j--,curPos++)
    {
        temp[i][curPos]=image[i][j];
    }
}


    for (int i = 0; i < height;i++)
    {
        for (int j = 0; j < width; j++)
        {
 image[i][j] = temp[i][j];

        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
{
    RGBTRIPLE temp[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            temp[i][j] = image[i][j];
        }
    }

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int redblur = 0;
            int blueblure = 0;
            int greenblure = 0;
            int counter = 0;
            for (int k = 0; k <= 2; k++)
            {
                for (int m = 0; m <= 2; m++)
                {

                    if ((i - 1 + k >= 0 && i + k - 1 < height)  && (j - 1 + m >= 0 && j - 1 + m < width))
                    {
                        redblur = redblur + temp[i - 1 + k][j - 1 + m].rgbtRed;
                        blueblure = blueblure + temp[i - 1 + k][j - 1 + m].rgbtBlue;
                        greenblure = greenblure + temp[i - 1 + k][j - 1 + m].rgbtGreen;
                        counter += 1;
                    }
                }
            }
            // printf("%d",counter);
            redblur = round((float)(float)redblur / (float)counter);
            blueblure = round((float)((float)blueblure / (float)counter));
            greenblure = round((float)((float)greenblure / (float)counter));
            image[i][j].rgbtBlue = blueblure;
            image[i][j].rgbtGreen = greenblure;
            image[i][j].rgbtRed = redblur;
        }
    }
    return;
}