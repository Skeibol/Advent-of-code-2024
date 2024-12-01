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
    int j = 0;
    for (size_t i = 0; i < leftCol.size(); i++)
    {
        left = leftCol.at(i);

        right = rightCol.at(j);
        while (left >= right)
        {
            if (left == right)
            {
                foundNumbers += 1;
            }
            j++;
            if (j < leftCol.size())
            {
                right = rightCol.at(j);
            }
            else
            {
                break;
               
            }
        }
      
        similarityScores += left * foundNumbers;
        foundNumbers = 0;
    }
    std::cout << similarityScores << std::endl;
    printf("Time taken: %.4fs\n", (double)(clock() - tStart) / CLOCKS_PER_SEC);
    return 0;
}