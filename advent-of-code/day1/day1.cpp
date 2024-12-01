#include "./FillVectors.hpp"


int main()
{

    std::vector<int> leftCol = {};
    std::vector<int> rightCol = {};

    fillVectors(leftCol, rightCol);

    int res = 0;
    for (size_t i = 0; i < leftCol.size(); i++)
    {
        res += abs(leftCol.at(i) - rightCol.at(i));
    }

    std::cout << res << std::endl;

    return 0;
}