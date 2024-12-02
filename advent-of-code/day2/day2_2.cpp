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
    std::vector<std::vector<int>> data;

    std::ifstream file("input.txt");
    std::vector<int> lineData;
    std::string line;

    int cnt = 0;
    if (file.is_open())
    {

        while (std::getline(file, line))
        {
            lineData = {};
            std::stringstream lineStream(line);

            int value;
            // Read an integer at a time from the line
            while (lineStream >> value)
            {
                // Add the integers from a line to a 1D array (vector)
                lineData.push_back(value);
            }
            // When all the integers have been read, add the 1D array
            // into a 2D array (as one line in the 2D array)
            data.push_back(lineData);
            for (auto token : lineData)
            {
                std::cout << token << " ";
            }
            if(checkReportSafety(lineData)){
                cnt+=1;
            }
            std::cout << "   " << checkReportSafety(lineData) << "<-";

            std::cout << "\n";
        }
        std::cout << cnt << "\n";
        file.close();
    }
    return 0;
}
