#include "square.hpp"

Square::Square(double side_a, double side_b)
{
    m_side_a = side_a;
    m_side_b = side_b;
}

Square::~Square()
{
}

void Square::print_square()
{
    double square = m_side_a * m_side_b;
    std::cout << "Площадь прямоугольника " << square << std::endl;
}