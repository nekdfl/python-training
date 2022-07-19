#ifndef CIRCLE_HPP
#define CIRCLE_HPP

#include <iostream>
#include "figure.hpp"

class Circle : public Figure
{
public:
    Circle(double radius);
    ~Circle();
    
    void print_square();
    

protected:
    double m_radius;

};

#endif // CIRCLE_HPP
