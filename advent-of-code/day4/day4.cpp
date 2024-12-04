#include <fstream>
#include <iostream>
#include <list>
#include <string>
#include <vector>
void checkInputMatrix(int (&arr)[140][140])
{
}
int main()
{
    int kernels[4][3][3] = {
        {

            {77, 0, 77},
            {0, 65, 0},
            {83, 0, 83}

        },
        {

            {83, 0, 77},
            {0, 65, 0},
            {83, 0, 77}

        },
        {

            {83, 0, 83},
            {0, 65, 0},
            {77, 0, 77}

        },
        {

            {77, 0, 83},
            {0, 65, 0},
            {77, 0, 83}

        }};

    std::string line;
    std::ifstream file("input.txt");

    int inputMatrix[140][140] = {};
    int character;
    int j = 0;
    if (file.is_open())
    {
        while (std::getline(file, line))
        {

            for (size_t charPos = 0; charPos < line.length(); charPos++)
            {
                character = line.at(charPos);
                if (character == 65 || character == 83 || character == 77) // 77 - M , 65 - A, 83 - S
                {
                    inputMatrix[charPos][j] = line.at(charPos);
                }
            }

            j += 1;
        }

        file.close();
    }
    bool found = true;
    int result = 0;
    for (size_t row = 1; row < sizeof(inputMatrix) / sizeof(inputMatrix[0]) - 1; row++)
    {
        for (size_t col = 1; col < sizeof(inputMatrix[0]) / sizeof(inputMatrix[0][0]) - 1; col++)
        {
            if (inputMatrix[col][row] == 'A')
            {

                for (size_t kernelIndex = 0; kernelIndex < sizeof(kernels) / sizeof(kernels[0]); kernelIndex++)
                {
                    found = true;

                    for (size_t j = 0; j < sizeof(kernels[0]) / sizeof(kernels[0][0]); j++)
                    {
                        for (size_t k = 0; k < sizeof(kernels[0][0]) / sizeof(kernels[0][0][0]); k++)
                        {
                            if (kernels[kernelIndex][j][k] != 0)
                            {

                                if (inputMatrix[col - 1 + k][row - 1 + j] - kernels[kernelIndex][j][k] != 0)
                                {
                                    found = false;
                                }
                            }
                        }
                    }
                    if (found)
                    {
                        result += 1;
                        break;
                    }
                }
            }
        }
    }
    std::cout << result << "\n";

    return 0;
}