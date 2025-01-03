#include "FillVectors.hpp"
#include <time.h>
int main()
{
    clock_t tStart = clock();
    std::vector<int> leftCol = {};
    std::vector<int> rightCol = {};

    fillVectors(leftCol, rightCol);

    int similarityScores = 0;
    int left = 0;
    int right = 0;
    int j = 0;
    int res = 0;
    for (size_t i = 0; i < leftCol.size(); i++)
    {
        left = leftCol.at(i);

        while (left >= right)
        {
            if (left == right)
            {
                similarityScores += right;
            }
            if (j < rightCol.size())
            {
                right = rightCol.at(j);
            }
            else
            {
                break;
            }
            j++;
        }
        res += abs(left - rightCol.at(i));
    }

   
    std::cout << similarityScores << std::endl;
    std::cout << res << std::endl;
    printf("Time taken: %.8fs\n", (double)(clock() - tStart) / CLOCKS_PER_SEC);
    return 0;
}