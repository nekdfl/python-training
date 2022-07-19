#include "circle.hpp"

Circle::Circle(double radius)
{
    m_radius = radius;
}

Circle::~Circle()
{
}

void Circle::print_square()
{
    double square = 2 * 3.14 * m_radius;
    std::cout << "Площадь круга " <<  square << std::endl;
    
}

