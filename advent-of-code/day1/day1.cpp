#include "./FillVectors.hpp"


int main()
{
    clock_t tStart = clock();
    std::vector<int> leftCol = {};
    std::vector<int> rightCol = {};

    fillVectors(leftCol, rightCol);

    int res = 0;
    for (size_t i = 0; i < leftCol.size(); i++)
    {
        res += abs(leftCol.at(i) - rightCol.at(i));
    }

    std::cout << res << std::endl;
    printf("Time taken: %.4fs\n", (double)(clock() - tStart) / CLOCKS_PER_SEC);
    return 0;
}