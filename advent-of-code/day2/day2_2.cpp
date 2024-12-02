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
    int checksPassed = 0;
    int numberCount = 1;
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
                    numberCount++;
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
                            checksPassed ++;
                            continue;
                        }
                        else if (difference < 0 && difference >= -3 && !(prevDifference > 0))
                        {
                            checksPassed ++;
                            continue;
                        }
                        else
                        {
                            break;
                        }
                    }
                }
            }
            std::cout << "valid";
            if (checksPassed + 2 >= numberCount)
            {
                
                cnt+=1;
            }
            difference = 0;
            numberCount = 1;
            checksPassed = 0;
            currentChar = 0;
            std::cout << "\n";
        }
        std::cout << cnt;
        file.close();
    }
    return 0;
}