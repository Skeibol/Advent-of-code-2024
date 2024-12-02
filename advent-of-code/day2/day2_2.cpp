#include <chrono>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

bool checkReportSafety(std::vector<int> &inputLine)
{
    int currentChar = 0;
    int prevChar = 0;
    int difference = 0;
    int prevDifference = 0;
    bool isValid = true;
    for (size_t indexToIgnore = 0; indexToIgnore < inputLine.size(); indexToIgnore++)
    {
        difference = 0;
        prevDifference = 0;
        prevChar = 0;
        isValid = true;
        currentChar = 0;
        for (size_t i = 0; i < inputLine.size(); i++)
        {

            if (i == indexToIgnore)
            {
                continue;
            }
            prevChar = currentChar;
            currentChar = inputLine.at(i);
            prevDifference = difference;
            if (prevChar == 0)
            {
                continue;
            }
            else
            {

                difference = currentChar - prevChar;
                if (difference > 0 && difference <= 3 && !(prevDifference < 0))
                {

                    continue;
                }
                else if (difference < 0 && difference >= -3 && !(prevDifference > 0))
                {

                    continue;
                }
                else
                {
                    isValid = false;
                    break;
                }
            }
        }
        if (isValid)
        {
            return true;
        }
    }
    return false;
}
int main()
{
    auto begin = std::chrono::high_resolution_clock::now();
    std::vector<std::vector<int>> data;

    std::ifstream file("input.txt");
    std::vector<int> lineData;
    std::string line;
    std::stringstream lineStream;
    int cnt = 0;
    int value;
    if (file.is_open())
    {

        while (std::getline(file, line))
        {
            lineData = {};

            value = 0;
            lineStream.clear();
            lineStream.str(std::move(line));

            while (lineStream >> value)
            {
                lineData.push_back(value);
            }

            if (checkReportSafety(lineData))
            {
                cnt += 1;
            }
        }
        file.close();
    }
    std::cout << cnt << "\n";
    auto end = std::chrono::high_resolution_clock::now();
    std::cout << std::chrono::duration_cast<std::chrono::nanoseconds>(end - begin).count() / 1000000000.0f << "sec" << std::endl;
    return 0;
}
