#include <fstream>
#include <iostream>
#include <list>
#include <string>
#include <vector>
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
    int lineNumber = 0;
    if (file.is_open())
    {
        while (std::getline(file, line))
        {

            for (size_t charPos = 0; charPos < line.length(); charPos++)
            {

                inputMatrix[lineNumber][charPos] = line.at(charPos);  // Create 2D array of characters
            }

            lineNumber += 1;
        }

        file.close();
    }

    bool found = true;
    int result = 0;

    for (size_t row = 1; row < sizeof(inputMatrix) / sizeof(inputMatrix[0]) - 1; row++)
    {
        for (size_t col = 1; col < sizeof(inputMatrix[0]) / sizeof(inputMatrix[0][0]) - 1; col++)
        {
            if (inputMatrix[row][col] == 'A') // If A is found, apply center of matrix to nearby characters to try match
            {

                for (size_t kernelIndex = 0; kernelIndex < sizeof(kernels) / sizeof(kernels[0]); kernelIndex++) // Go through all 4 matrices
                {
                    found = true;

                    for (size_t i = 0; i < sizeof(kernels[0]) / sizeof(kernels[0][0]); i++) // Matrix Y
                    {
                        for (size_t j = 0; j < sizeof(kernels[0][0]) / sizeof(kernels[0][0][0]); j++) // Matrix X
                        {
                            if (kernels[kernelIndex][i][j] != 0) // Look only for diagonals (not zeros)
                            {
                                if (inputMatrix[row - 1 + i][col - 1 + j] - kernels[kernelIndex][i][j] != 0) // If elementwise kernel diff is not zero (char1 - char2 = 0) <=> char1 = char2
                                {
                                    found = false;
                                }
                            }
                        }
                    }
                    if (found)
                    {
                        result += 1;
                        break; // Only one matrix needs to match
                    }
                }
            }
        }
    }
    std::cout << result << "\n";
    return 0;
}