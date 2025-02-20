#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;
int main()  
{   
   setlocale(LC_ALL, "");


   //int A[10] = {};

   //int* b;
   //b = A;
   //int minEl = *b;
   //int *a = b;
   //srand(time(NULL));
   //for (int p = 0; p < 10; p++)
   //{
	  // *(b + p) = rand() % 20 - 10;
	  // cout << *(b + p) << endl;
   //}
   //for (int j = 0; j < 10;j++)
   //{
	  // if(minEl > *(b+j))
	  // {
		 //  minEl = *(b + j);
		 //  a = (b + j);
	  // }
	  // 
   //}
   //cout << "наименьший " << minEl << endl;
   //int t = *(b + 9);
   //*(b + 9) = *a;
   //*a = t;
   //cout << "новый массив:" << " ";
   //for (int k = 0; k < 10; k++)
   //{
	  // cout << *(b+k) << " ";
   //}
   //cout << endl;



	float A[10] = {};

	float* b;
	b = A;
	float minEl = *b;
	float *a = b;
	float sum = 0;
	srand(time(NULL));
	int count = 0;
	for (int p = 0; p < 10; p++)
	{
		*(b+p) = -1.0 + 4.0 * rand() / (float)RAND_MAX-1;
		cout << *(b + p) << endl;
		if (*(b+p)>=0)
		{
			sum += *(b + p);
			count += 1;
		}
	}
	cout << "сумма:" << sum << " " << count << endl;
	}
//ctrl+k + ctrl+c - закомментировать
//ctrl+k + ctrl+u - раскоммент.


