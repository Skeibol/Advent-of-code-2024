#include <algorithm>
#include <chrono>
#include <fstream>
#include <iostream>
#include <string>
int main()
{
    auto begin = std::chrono::high_resolution_clock::now();
    std::ifstream file("input.txt");
    std::string line;
    std::string buffer;
    int currentChar = 0;
    int prevChar = 0;
    int difference = 0;
    int prevDifference = 0;
    bool isValid = true;
    int cnt = 0;

    if (file.is_open())
    {
        while (getline(file, line))
        {
            isValid = true;

            line.push_back(' ');
            for (char token : line)
            {

                if (isdigit(token))
                {
                    buffer.push_back(token);
                }
                else
                {
                    prevChar = currentChar;
                    currentChar = std::stoi(buffer);
                    buffer.clear();
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
                    if (prevDifference <= 0 && difference < 0 && difference >= -3)
                    {
                        continue;
                    }

                    isValid = false;
                    break;
                }
            }

            if (isValid)
            {
                cnt += 1;
            }
            difference = 0;
            currentChar = 0;
        }
        std::cout << cnt << "\n";
        file.close();
    }
    auto end = std::chrono::high_resolution_clock::now();
    std::cout << std::chrono::duration_cast<std::chrono::nanoseconds>(end - begin).count() / 1000000000.0f << "sec" << std::endl;

    return 0;
}