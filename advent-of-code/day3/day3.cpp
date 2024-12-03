#include <chrono>
#include <fstream>
#include <iostream>
#include <sstream>
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
                        state = startState;
                    }
                }
            }
            file.close();
            std::cout << result << '\n';
        }
    }

  private:
    const std::string ALPHABET = "0123456789mul(,)don't";
    std::string _buffer;
    int firstNumber;
    bool canDo = true;
    const char states[16] = {'1', '2', '3', '4', '5', '6', '7', // states for "mul(...)"
                             '8', '9', 'A',                     // states for "do()"
                             'C', 'D', 'E', 'F'};               // states for "don't()" - do is shared

    const char startState = states[0];
    const char finalStates[1] = {
        states[6], // End state for all
    };
    const char transitionTable[35][3] = {
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
        {')', states[9], states[6]},

        // Transitions for "don't()"
        {'n', states[8], states[10]},
        {'\'', states[10], states[11]},
        {'t', states[11], states[12]},
        {'(', states[12], states[13]},
        {')', states[13], states[6]}};

    const char getNextState(char input, char currentState)
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
                    if (transitionTable[i][2] == states[6] && currentState == states[9]) // Transition ifs, implement transition functions
                    {
                        canDo = true;
                    }
                    else if (transitionTable[i][2] == states[6] && currentState == states[13]) // Transition ifs, implement transition functions
                    {
                        canDo = false;
                    }
                    else if (transitionTable[i][2] == states[6] && currentState == states[5]) // Transition ifs, implement transition functions
                    {
                        if (canDo)
                        {

                            result += std::stoi(_buffer) * firstNumber;
                        }
                        _buffer.clear();
                    }
                    else if (transitionTable[i][2] == states[5] && currentState == states[4]) // Transition ifs, implement transition functions
                    {
                        firstNumber = std::stoi(_buffer);
                        _buffer.clear();
                    }

                    if (isdigit(input))
                    {
                        _buffer.push_back(input);
                    }

                    return transitionTable[i][2]; // Return next state after table lookup
                }
            }
        }

        return startState;
    }
};

int main()
{
    auto begin = std::chrono::high_resolution_clock::now();

    DeterministicStateAutomata DSA("input.txt");
    auto end = std::chrono::high_resolution_clock::now();
    std::cout << std::chrono::duration_cast<std::chrono::nanoseconds>(end - begin).count() / 1000000000.0f << "sec" << std::endl;
    return 0;
}