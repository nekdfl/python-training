#include "triangle.hpp"

//Формула Герона для вычисления площади треугольника
//Сначала необходимо подсчитать разность полупериметра и каждой его стороны. 
//Потом найти произведение полученных чисел, умножить результат на полупериметр и 
//найти корень из полученного числа.
//
//S = \sqrt{p \cdot (p - a) \cdot (p - b) \cdot (p - c)}S= 
//p⋅(p−a)⋅(p−b)⋅(p−c)
//​
//  , где aa , bb , cc — стороны, pp — полупериметр, который можно найти по формуле: 
//p = (a + b + c) \div 2p=(a+b+c)÷2 
//Источник - Онлайн школа Skysmart: https://skysmart.ru/articles/mathematic/ploshad-treugolnika


Triangle::Triangle(double side_a, double side_b, double side_c)
{
    m_side_a = side_a;
    m_side_b = side_b;
    m_side_c = side_c;
}

Triangle::~Triangle()
{
}

void Triangle::print_square()
{
    double pp = (m_side_a + m_side_b + m_side_c) / 2;
    double square = sqrt(pp * (pp-m_side_a) * (pp-m_side_b)*(pp-m_side_c));
    std::cout << "Площадь треугольника " << square << std::endl;
}