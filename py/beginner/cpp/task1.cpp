// Создать переменную text типа string. 
// Вывести каждый символ с новой строки.
#include <iostream>

int main()
{
    std::string text = "some text";
    for (int i = 0; i < text.length(); ++i)
    {
        std::cout << text[i] << std::endl;
    }

    return 0;
}
