#include "helpers.h"
#include <math.h>
// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            RGBTRIPLE pixel = image[i][j];
            int average = round((pixel.rgbtBlue + pixel.rgbtGreen + pixel.rgbtRed) / 3.0);
            image[i][j].rgbtBlue = image[i][j].rgbtRed = image[i][j].rgbtGreen = average;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE temp[height][width];

    for (int i = 0; i < height; i++)
    {
        int curPos = 0;
        for (int j = width - 1; j >= 0; j--, curPos++)
        {
            temp[i][curPos] = image[i][j];
        }
    }

    for (int i = 0; i < height; i++)
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

                    if ((i - 1 + k >= 0 && i + k - 1 < height) && (j - 1 + m >= 0 && j - 1 + m < width))
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

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
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
            int redblurx = 0;
            int redblury = 0;
            int blueblurex = 0;
            int blueblurey = 0;
            int greenblurex = 0;
            int greenblurey = 0;
            int redblur = 0;
            int blueblure = 0;
            int greenblure = 0;
            int counter = 0;
            for (int k = 0; k <= 2; k++)
            {
                for (int m = 0; m <= 2; m++)
                {

                    if ((i - 1 + k >= 0 && i + k - 1 <= height) && (j - 1 + m >= 0 && j - 1 + m <= width))
                    {
                        // redblur = redblur + temp[i-1+k][j-1+m].rgbtRed;
                        // blueblure = blueblure + temp[i-1+k][j-1+m].rgbtBlue;
                        // greenblure = greenblure + temp[i-1+k][j-1+m].rgbtGreen;
                        if (k == 0)
                        {
                            if (m == 0 || m == 2)
                            {
                                redblurx = redblurx - temp[i - 1 + k][j - 1 + m].rgbtRed;
                                blueblurex = blueblurex - temp[i - 1 + k][j - 1 + m].rgbtBlue;
                                greenblurex = greenblurex - temp[i - 1 + k][j - 1 + m].rgbtGreen;
                            }
                            if (m == 1)
                            {
                                redblurx = redblurx - 2 * temp[i - 1 + k][j - 1 + m].rgbtRed;
                                blueblurex = blueblurex - 2 * temp[i - 1 + k][j - 1 + m].rgbtBlue;
                                greenblurex = greenblurex - 2 * temp[i - 1 + k][j - 1 + m].rgbtGreen;
                            }
                        }
                        if (k == 2)
                        {
                            if (m == 0 || m == 2)
                            {
                                redblurx = redblurx + temp[i - 1 + k][j - 1 + m].rgbtRed;
                                blueblurex = blueblurex + temp[i - 1 + k][j - 1 + m].rgbtBlue;
                                greenblurex = greenblurex + temp[i - 1 + k][j - 1 + m].rgbtGreen;
                            }
                            if (m == 1)
                            {
                                redblurx = redblurx + 2 * temp[i - 1 + k][j - 1 + m].rgbtRed;
                                blueblurex = blueblurex + 2 * temp[i - 1 + k][j - 1 + m].rgbtBlue;
                                greenblurex = greenblurex + 2 * temp[i - 1 + k][j - 1 + m].rgbtGreen;
                            }
                        }
                        if (m == 0)
                        {
                            if (k == 0 || k == 2)
                            {
                                redblury = redblury - temp[i - 1 + k][j - 1 + m].rgbtRed;
                                blueblurey = blueblurey - temp[i - 1 + k][j - 1 + m].rgbtBlue;
                                greenblurey = greenblurey - temp[i - 1 + k][j - 1 + m].rgbtGreen;
                            }
                            if (k == 1)
                            {
                                redblury = redblury - 2 * temp[i - 1 + k][j - 1 + m].rgbtRed;
                                blueblurey = blueblurey - 2 * temp[i - 1 + k][j - 1 + m].rgbtBlue;
                                greenblurey = greenblurey - 2 * temp[i - 1 + k][j - 1 + m].rgbtGreen;
                            }
                        }
                        if (m == 2)
                        {
                            if (k == 0 || k == 2)
                            {
                                redblury = redblury + temp[i - 1 + k][j - 1 + m].rgbtRed;
                                blueblurey = blueblurey + temp[i - 1 + k][j - 1 + m].rgbtBlue;
                                greenblurey = greenblurey + temp[i - 1 + k][j - 1 + m].rgbtGreen;
                            }
                            if (k == 1)
                            {
                                redblury = redblury + 2 * temp[i - 1 + k][j - 1 + m].rgbtRed;
                                blueblurey = blueblurey + 2 * temp[i - 1 + k][j - 1 + m].rgbtBlue;
                                greenblurey = greenblurey + 2 * temp[i - 1 + k][j - 1 + m].rgbtGreen;
                            }
                        }
                    }
                }
            }
            // printf("%d",counter);

            redblur = round(sqrt((redblurx * redblurx) + (redblury * redblury)));
            blueblure = round(sqrt((blueblurex * blueblurex) + (blueblurey * blueblurey)));
            greenblure = round(sqrt((greenblurex * greenblurex) + (greenblurey * greenblurey)));
            image[i][j].rgbtRed = redblur > 255 ? 255 : redblur;
            image[i][j].rgbtGreen = greenblure > 255 ? 255 : greenblure;
            image[i][j].rgbtBlue = blueblure > 255 ? 255 : blueblure;
        }
    }
    return;
}
