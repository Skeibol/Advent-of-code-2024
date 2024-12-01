#include "FillVectors.hpp"

int main()
{
    std::vector<int> leftCol = {};
    std::vector<int> rightCol = {};

    fillVectors(leftCol, rightCol);
    int similarityScores = 0;
    int foundNumbers = 0;
    for (size_t i = 0; i < leftCol.size(); i++)
    {

        for (size_t j = 0; j < rightCol.size(); j++)
        {
            if (leftCol.at(i) == rightCol.at(j))
            {
                foundNumbers++;
            }
            
            if (rightCol.at(j) > leftCol.at(i))
            {
                break;
            }
        }
        similarityScores += + leftCol.at(i) * foundNumbers;
        foundNumbers = 0;
    }
    std::cout << similarityScores << std::endl;
    return 0;
}