#include <iostream>


using namespace std;


int function(int a)
{
    a = 10;
    return 0;
}

int main(int argc, char** argv)
{
    int a = 0;
    function(a);
    printf("a = %d\n", a);
    return 0;
}
