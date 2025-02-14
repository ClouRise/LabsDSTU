#include <iostream>
#include <cmath>
#include <string>
using namespace std;
int man()
{
    setlocale(LC_ALL, "");
    int zz;
    cout << "введите z: ";
    cin >> zz;
    if (cin.fail())
    {
        cout << "введите число" << endl;
        return 0;
    }
    double f;

    if (zz>0)
    {
        f = 3 * pow(zz, 3) * pow(zz, 0.5) - 5 * pow(zz, 5);
        cout << f;
        return 0;
    }
    if(zz==0)
    {
        f = cos(2 * pow(zz, 3) - 1) + 5 * pow(zz, 5);
        cout << f;
        return 0;
    }
    if(zz<0)
    {
        f = (3 * pow(zz, 2) + sin(pow(zz, 3) - 3)) / 5;
        cout << f;
        return 0;
    }
    return 0;
}
