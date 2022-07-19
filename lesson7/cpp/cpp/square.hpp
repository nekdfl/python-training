#ifndef SQUARE_HPP
#define SQUARE_HPP

#include <iostream>
#include "figure.hpp"

class Square : public Figure
{
public:
    Square(double side_a, double side_b);
    ~Square();
    
    void print_square();
    

protected:
    double m_side_a;
    double m_side_b;

};

#endif // SQUARE_HPP
