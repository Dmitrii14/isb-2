#include <iostream>
#include <ctime>
#define MAX_BIT 128


int main() 
{
    srand(time(0));
    for (int i = 0; i < MAX_BIT; i++) 
    {
        unsigned long long rand_num = std::rand() % 32767;
        bool binary_num = rand_num % 2;
        std::cout << binary_num;
    }
    return 0;
}

// 00001011101011001010101100111000111111100011001110100110101011110111001101110010010111001111111101100100000010100001011010011001