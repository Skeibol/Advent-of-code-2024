#include <algorithm>
#include <chrono>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

struct Guard
{
    std::vector<int> direction = {0, 0};
    std::vector<int> position = {0, 0};
    std::vector<int> initialPosition;
};

struct Directions
{
    std::vector<std::vector<int>> dir = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
    int currentDirection = 3;
} directions;

std::vector<int> getNextPosition(std::vector<int> pos, std::vector<int> dir)
{
    std::transform(pos.begin(), pos.end(), dir.begin(), pos.begin(), std::plus<int>());
    return pos;
}
std::vector<int> getNextDirection(Directions &direction)
{

    if (direction.currentDirection == 3)
    {
        direction.currentDirection = 0;
    }
    else
    {
        direction.currentDirection++;
    }
    return direction.dir.at(direction.currentDirection);
}

void resetGuard(Guard &guard)
{
    guard.direction = directions.dir[3];
    directions.currentDirection = 3;
    guard.position = guard.initialPosition;
}

void printField(std::vector<std::vector<int>> &field)
{
    std::cout << "===============================" << '\n';
    for (std::vector<int> row : field)
    {
        for (int element : row)
        {
            switch (element)
            {
            case 0:
                std::cout << '.';
                break;
            case 1:
                std::cout << '#';
                break;
            case 3:
                std::cout << 'x';
                break;
            case 5:
                std::cout << 'o';
                break;

            default:
                break;
            }
        }
        std::cout << '\n';
    }
    std::cout << "===============================" << '\n';
}
bool checkBounds(std::vector<int> pos, std::vector<std::vector<int>> &field)
{
    if (pos[0] > field.at(0).size() - 1 || pos[0] < -1 || pos[1] > field.size() - 1 || pos[1] < -1)
    {
        return false;
    }
    return true;
}

int runSimulation(Guard guard, std::vector<std::vector<int>> &field)
{
    std::vector<int> nextPosition;
    std::vector<std::pair<std::vector<int>, std::vector<int>>> illegalPositions;
    bool changedDirection;

    while (true)
    {

        nextPosition = getNextPosition(guard.position, guard.direction);
        if (!checkBounds(nextPosition, field))
        {

            return 0;
        }
        while (field[nextPosition[1]][nextPosition[0]] == 1)
        {
            guard.direction = getNextDirection(directions);
            nextPosition = getNextPosition(guard.position, guard.direction);
            changedDirection = true;
        }
        if (changedDirection)
        {
            auto it = std::find(illegalPositions.begin(), illegalPositions.end(), std::make_pair(guard.direction, guard.position));

            if (it != illegalPositions.end())
            {
                return 1;
                // std::cout << "Pair found in illegalPositions!" << std::endl;
            }
            illegalPositions.emplace_back(guard.direction, guard.position);
        }
        guard.position = nextPosition;
    }
}

std::vector<std::vector<int>> generateMovesToCheck(Guard guard, std::vector<std::vector<int>> &field)
{

    std::vector<int> nextPosition;
    std::vector<std::vector<int>> previousMoves;

    while (true)
    {

        nextPosition = getNextPosition(guard.position, guard.direction);
        if (!checkBounds(nextPosition, field))
        {

            return previousMoves;
        }
        while (field[nextPosition[1]][nextPosition[0]] == 1)
        {

            guard.direction = getNextDirection(directions);
            nextPosition = getNextPosition(guard.position, guard.direction);
        }
        guard.position = nextPosition;
        int cnt;
        if (std::find(previousMoves.begin(), previousMoves.end(), guard.position) != previousMoves.end())
        {
        }
        else
        {
            cnt = 0;
            if (guard.position != guard.initialPosition)
            {

                previousMoves.push_back(guard.position);
            }
        }
    }
}

std::vector<std::vector<int>> generateField(Guard &guard)
{
    std::vector<std::vector<int>> field = {};
    std::vector<int> row;
    std::ifstream file("input.txt");
    int fieldWidth;
    char ch;
    if (file.is_open())
    {
        while (file.get(ch))
        {
            if (ch == '\n')
            {
                if (fieldWidth == 0)
                {

                    fieldWidth = field.size();
                }
                field.push_back(row);
                row.clear();
            }
            else
            {
                switch (ch)
                {
                case '#':
                    row.push_back(1);
                    break;
                case '.':
                    row.push_back(0);

                    break;

                default:

                    if (row.empty()) // Cover edge case for some reason
                    {
                        guard.position[0] = 0;
                    }
                    else
                    {
                        guard.position[0] = row.size();
                    }
                    if (field.empty())
                    {
                        guard.position[1] = 0;
                    }
                    else
                    {
                        guard.position[1] = field.size();
                    }

                    row.push_back(3);
                    break;
                }
            }
        }
        field.push_back(row);
    }

    return field;
}

bool setObstacle(std::vector<int> &currPos, std::vector<int> &prevPos, std::vector<std::vector<int>> &field)
{
    if (field[currPos[1]][currPos[0]] == 1)
    {
        return false;
    }
    if (!prevPos.empty())
    {
        field[currPos[1]][currPos[0]] = 1;
        field[prevPos[1]][prevPos[0]] = 0;
    }
    else
    {
        field[currPos[1]][currPos[0]] = 1;
    }

    return true;
}

int main()
{
    int loopCount = 0;
    Guard guard;

    std::vector<std::vector<int>> field;

    std::vector<int> prevObstaclePosition = {2, 2}; // random empty space
    std::vector<int> currentObstaclePosition;

    field = generateField(guard);

    guard.initialPosition = guard.position;
    resetGuard(guard);
    std::vector<std::vector<int>> positionsToCheck = generateMovesToCheck(guard, field);

    for (int i = 1; i < positionsToCheck.size(); i++)
    {
        guard.direction = directions.dir[3];
        directions.currentDirection = 3;
        guard.position = guard.initialPosition;
        //resetGuard(guard);
        currentObstaclePosition = {positionsToCheck[i][0], positionsToCheck[i][1]};
        setObstacle(currentObstaclePosition, prevObstaclePosition, field);
        prevObstaclePosition = currentObstaclePosition;

        loopCount += runSimulation(guard, field);
        if (i % 200 == 0)
        {

            std::cout << i << " out of " << positionsToCheck.size() << " complete. Loops = " << loopCount << '\n';
        }
    }

    std::cout << "count " << loopCount << '\n';
    return 0;
}