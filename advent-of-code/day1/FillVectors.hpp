#pragma once
#include <algorithm>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

void fillVectors(std::vector<int> &leftCol, std::vector<int> &rightCol)
{
    std::ifstream file("input.txt");
    std::string line;
    std::stringstream contents;

    if (file.is_open())
    {
        char c;
        bool leftSide = true;
        std::string buff;
        while (file.get(c))
        {
            if (isdigit(c))
            {
                buff.push_back(c);
            }
            else if (buff.size() > 0)
            {
                if (leftSide)
                {
                    leftCol.push_back(std::stoi(buff));
                }
                else
                {
                    rightCol.push_back(std::stoi(buff));
                }
                buff.clear();

                leftSide = !leftSide;
            }
        }
        rightCol.push_back(std::stoi(buff));
        std::sort(leftCol.begin(), leftCol.end(), // Sort strings
                  [](float a, float b)
                  {
                      return a <= b;
                  });

        std::sort(rightCol.begin(), rightCol.end(), // Sort strings
                  [](float a, float b)
                  {
                      return a <= b;
                  });
        file.close();
    }
    else
    {
        std::cerr << "Unable to open file!" << std::endl;
    }
}