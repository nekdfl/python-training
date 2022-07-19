#ifndef FIGURE_HPP
#define FIGURE_HPP

#include <iostream>

class Figure
{
public:
    Figure(){ std::cout<<"i am figure" << std::endl;};
    virtual ~Figure(){};
    
    virtual void print_square() =0;
//    {
//        std::cout << "what is it?" << std::endl;
//    };
    
   

};

#endif // FIGURE_HPP
