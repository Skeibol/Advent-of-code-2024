#include <algorithm>
#include <fstream>
#include <iostream>
#include <string>
int main()
{
    std::ifstream file("input.txt");
    std::string line;
    std::string buffer;
    int currentChar = 0;
    int prevChar = 0;
    int difference = 0;
    int prevDifference = 0;
    char token;
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
                if (!isValid)
                {
                    break;
                }

                if (isdigit(token))
                {
                    buffer.push_back(token);
                }
                else
                {
                    prevChar = currentChar;
                    currentChar = std::stoi(buffer);
                    prevDifference = difference;
                    buffer.clear();
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
            }

            if (isValid)
            {

                cnt += 1;
            }
            difference = 0;
            currentChar = 0;
        }
        //std::cout << cnt;
        file.close();
    }
    return 0;
}