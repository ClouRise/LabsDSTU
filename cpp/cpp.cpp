#include <iostream>
#include <cmath>
#include <string>
using namespace std;
int w(string t)
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

int main()
{
    setlocale(LC_ALL, "");
    string z, y;
    cout << "введите z: ";
    cin >> z;
    if (w(z) == 0) { return 0; }
    cout << "введите y: ";
    cin >> y;
    if (w(y) == 0) { return 0; }

    int zz{ stoi(z) };
    int yy{ stoi(y) };
    cout << -pow(zz,yy)+pow(yy,zz) << endl;
}
