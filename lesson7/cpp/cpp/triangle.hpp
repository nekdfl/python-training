#ifndef TRIANGLE_HPP
#define TRIANGLE_HPP

#include <cmath>
#include <iostream>

#include "figure.hpp" // Base class: figure.hpp

class Triangle : public Figure
 {
public:
    Triangle(double side_a, double side_b, double side_c);
    ~Triangle();
    
    void print_square() override;

protected:
    double m_side_a;
    double m_side_b;
    double m_side_c;

private:

};

#endif // TRIANGLE_HPP
