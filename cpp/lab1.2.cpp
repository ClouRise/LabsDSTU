#include <iostream>
#include <cmath>
#include <string>
using namespace std;
int ww(string t)
{
    for (int a = 0; a < t.size();a++)
    {
        if (isdigit(t.at(a)) == 0)
        {
            cout << "нужно ввести число" << endl;
            return 0;
        }
    }
}

int man()
{
    setlocale(LC_ALL, "");
    string z;
    cout << "введите z: ";
    cin >> z;
    if (ww(z) == 0) { return 0; }
    int zz{ stoi(z) };
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
