#include <stdio.h>
#include <list>
#include "figure.hpp"
#include "triangle.hpp"
#include "circle.hpp"
#include "square.hpp"



int main(int argc, char **argv)
{
    
    Triangle mytriangle = Triangle(3.23, 4.0, 5.0);
    Circle mycircle =  Circle(4.321);
    Square mysquare =  Square(3.12, 4.456);
//    Figure myfigure = Figure();
    
//    mytriangle.print_square();
//    mycircle.print_circle_square();
//    mysquare.print_square();
//    myfigure.print_square();

    std::list<Figure> mytriangle_list;
    mytriangle_list.push_back(mytriangle);
    mytriangle_list.push_back(mycircle);
    mytriangle_list.push_back(mysquare);

    
    for (auto&it : mytriangle_list)
    {
        it->print_square();
    }
    
    mycircle;
    mytriangle;
    mysquare;
    
    
	
	return 0;
}
