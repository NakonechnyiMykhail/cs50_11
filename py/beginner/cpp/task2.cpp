// Создать функцию print_text которая принимает на вход строку и 
// выводит каждый символ с новой строки. 
// В функции main применить эту функцию с любым примером текстовой переменной.

#include <iostream>

void print_text(std::string txt)
{
    for (int i = 0; i < txt.length(); ++i)
    {
        std::cout << txt[i] << std::endl;
    }
}

int main()
{
    std::string text = "some text";

    print_text(text);

    return 0;
}