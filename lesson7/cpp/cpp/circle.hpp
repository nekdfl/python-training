#ifndef CIRCLE_HPP
#define CIRCLE_HPP

#include <iostream>

class Circle
{
public:
    Circle(double radius);
    ~Circle();
    
    void print_circle_square();

protected:
    double m_radius;

};

#endif // CIRCLE_HPP
