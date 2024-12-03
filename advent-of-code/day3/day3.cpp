#include <fstream>
#include <iostream>
#include <string>

class DeterministicStateAutomata
{
  public:
    int result = 0;

    DeterministicStateAutomata(std::string fileName)
    {
        std::ifstream file(fileName);
        char state = startState;
        char c;
        if (file.is_open())
        {
            while (file.get(c))
            {
                state = getNextState(c, state);
                for (char finalState : finalStates)
                {
                    if (state == finalState)
                    {
                        handleFinalState(state);
                        state = startState;
                        _buffer.clear();
                    }
                }
            }
            file.close();
            std::cout << result;
        }
    }

  private:
    std::string ALPHABET = "0123456789mul(,)don't";
    std::string _buffer;
    bool canDo = true;
    char states[18] = {'1', '2', '3', '4', '5', '6', '7', // states for "mul(...)"
                       '8', '9', 'A', 'B',                // states for "do()"
                       'C', 'D', 'E', 'F', 'G'};          // states for "don't()"

    char startState = states[0];
    char finalStates[3] = {states[6],   // End state for "mul(...)"
                           states[10],  // End state for "do()"
                           states[15]}; // End state for "don't()"
    char transitionTable[40][3] = {
        // Transitions for "mul()"

        {'m', states[0], states[1]},
        {'u', states[1], states[2]},
        {'l', states[2], states[3]},
        {'(', states[3], states[4]},

        {'0', states[4], states[4]},
        {'1', states[4], states[4]},
        {'2', states[4], states[4]},
        {'3', states[4], states[4]},
        {'4', states[4], states[4]},
        {'5', states[4], states[4]},
        {'6', states[4], states[4]},
        {'7', states[4], states[4]},
        {'8', states[4], states[4]},
        {'9', states[4], states[4]},

        {',', states[4], states[5]},

        {'0', states[5], states[5]},
        {'1', states[5], states[5]},
        {'2', states[5], states[5]},
        {'3', states[5], states[5]},
        {'4', states[5], states[5]},
        {'5', states[5], states[5]},
        {'6', states[5], states[5]},
        {'7', states[5], states[5]},
        {'8', states[5], states[5]},
        {'9', states[5], states[5]},

        {')', states[5], states[6]},

        // Transitions for "do()"
        {'d', states[0], states[7]},
        {'o', states[7], states[8]},
        {'(', states[8], states[9]},
        {')', states[9], states[10]},

        // Transitions for "don't()"
        {'n', states[8], states[11]},
        {'\'', states[11], states[12]},
        {'t', states[12], states[13]},
        {'(', states[13], states[14]},
        {')', states[14], states[15]}};

    char getNextState(char input, char currentState)
    {
        if (ALPHABET.find(input) == std::string::npos)
        {
            _buffer.clear();
            return startState;
        }

        for (size_t i = 0; i < sizeof(transitionTable) / sizeof(transitionTable[0]); i++)
        {
            if (transitionTable[i][0] == input)
            {
                if (transitionTable[i][1] == currentState)
                {

                    _buffer.push_back(input);

                    return transitionTable[i][2];
                }
            }
        }

        return startState;
    }
    void handleFinalState(char state)
    {
        if (state == '7' && canDo) // If its in mul final state, and it can do, do the multiplying
        {
            int res = 0;
            std::string num;
            for (char token : _buffer)
            {
                if (isdigit(token))
                {
                    num.push_back(token);
                }
                else if (token == ',')
                {
                    res = std::stoi(num);
                    num.clear();
                }
            }
            result += res * std::stoi(num);
        }
        if (state == 'B')
        {
            canDo = true;
        }
        if (state == 'G')
        {
            canDo = false;
        }
    }
};

int main()
{
    DeterministicStateAutomata DSA("input.txt");
    return 0;
}