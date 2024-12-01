#include "FillVectors.hpp"
#include <time.h>
int main()
{
    clock_t tStart = clock();
    std::vector<int> leftCol = {};
    std::vector<int> rightCol = {};

    fillVectors(leftCol, rightCol);
    int similarityScores = 0;
    int foundNumbers = 0;
    int left = 0;
    int right = 0;
    for (size_t i = 0; i < leftCol.size(); i++)
    {
        left = leftCol.at(i);
        for (size_t j = 0; j < rightCol.size(); j++)
        {
            right = rightCol.at(j);
            if (right > left)
            {
                break;
            }
            if (left == right)
            {
                foundNumbers++;
            }

        }
        similarityScores += left * foundNumbers;
        foundNumbers = 0;
    }
    std::cout << similarityScores << std::endl;
    printf("Time taken: %.4fs\n", (double)(clock() - tStart) / CLOCKS_PER_SEC);
    return 0;
}