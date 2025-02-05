#include<iostream>
#include<iomanip>
#include<cmath>
using namespace std;

//ЛР05 ІПЗ-32 Шевченко Ростислав

int main(){

cout << "Цю програму створив студент Шевченко Ростислав Андрійович групи ІПЗ-32 у 2024 році" << endl;
int X=0;
int x=0;
int c=0;
int b=0;
int a=0;
int j;
float A=4;

cout << "What is your number? (Ex.1)" << std::endl;
cout << "X=";
cin >> X;

cout << A << endl;
cout << X << endl;

sqrt(A-X) < 0 ? (A=(A+(sqrt(A-X)))) : (A=(pow(X+2,2.0)*pow(X-1,3.0)+sin(A*3.14)));

cout << "A=," << A << "," << endl;
cout << "X=," << X << "," << endl;

cout << "What are your numbers? (Ex.2)" << std::endl;

cout << "x=";
cin >> x;
cout << "a=";
cin >> a;
cout << "b=";
cin >> b;
cout << "c=";
cin >> c;


cout << "Results:" << endl;
//cout << "Ex.2.1: 2*" << c << "*" << x << "+" << b << "*" << x << "^3 = ";
cout << setw(7) << 1 << setw(7) << 2 << setw(7) << 3 << endl;
cout << setw(7) << setprecision(-2) << 2*c*x+pow(b*x,3.0);
//cout << "Ex.2.2: (V" << x << "^3)^2 +((2*" << x << "^2)/(" << c << "*" << x << "+" << c << ")) = ";
j=(c*x+a);
(j = 0) ? (cout << -555 << endl) : (j < 0) ? (cout << -777 << endl) : (cout << setw(7) << setprecision(-2) << (pow(sqrt(pow(x,3.0)),2.0)+(2*pow(x,2.0))/(c*x+a)));

//cout << "Ex.2.3: " << a << "*" << x << "^2 *(" << x << "+" << c << ")+(" << x << "-" << b << "*" << b << ")^2 = ";

cout << setw(7) << setprecision(-2) << a*pow(x, 2.0)*(x+c)+pow(x-a*b,2.0);
return 0;
}