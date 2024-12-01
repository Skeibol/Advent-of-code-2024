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
        file.close();
    }
    else
    {
        std::cerr << "Unable to open file!" << std::endl;
    }
}

int main()
{

    std::vector<int> leftCol = {};
    std::vector<int> rightCol = {};

    fillVectors(leftCol, rightCol);
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

    int res = 0;
    for (size_t i = 0; i < leftCol.size(); i++)
    {
        res += abs(leftCol.at(i) - rightCol.at(i));
    }

    std::cout << res << std::endl;

    return 0;
}