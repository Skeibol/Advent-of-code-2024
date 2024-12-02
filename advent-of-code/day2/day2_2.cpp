#include <chrono>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

bool checkReportSafetyWithDampener(std::vector<int> &inputLine)
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

bool checkReportSafety(std::vector<int> &inputLine)
{
    int currentChar = 0;
    int prevChar = 0;
    int difference = 0;
    int prevDifference = 0;
    bool isValid = true;
    for (int num : inputLine)
    {

        prevChar = currentChar;
        currentChar = num;
        if (prevChar == 0)
        {
            continue;
        }

        prevDifference = difference;
        difference = currentChar - prevChar;

        if (prevDifference >= 0 && difference > 0 && difference <= 3)
        {
            continue;
        }
        else if (prevDifference <= 0 && difference < 0 && difference >= -3)
        {
            continue;
        }
        else
        {
            return false;
        }
    }
    return true;
}
int main()
{
    auto begin = std::chrono::high_resolution_clock::now();

    std::ifstream file("input.txt");
    std::vector<int> lineData;
    std::string line;
    std::stringstream lineStream;

    int cnt = 0;
    int part1cnt = 0;
    int parsedNumber;

    if (file.is_open())
    {

        while (std::getline(file, line))
        {
            lineData = {};

            parsedNumber = 0;
            lineStream.clear();
            lineStream.str(std::move(line));

            while (lineStream >> parsedNumber)
            {
                lineData.push_back(parsedNumber);
            }
            if (checkReportSafety(lineData))
            {
                part1cnt += 1;
                cnt += 1;
                continue;
            }
            if (checkReportSafetyWithDampener(lineData))
            {
                cnt += 1;
            }
        }
        file.close();
    }
    std::cout << "Part 1:" << part1cnt << "\n";
    std::cout << "Part 2:" << cnt << "\n";
    auto end = std::chrono::high_resolution_clock::now();
    std::cout << std::chrono::duration_cast<std::chrono::nanoseconds>(end - begin).count() / 1000000000.0f << "sec" << std::endl;
    return 0;
}
