#include <iostream>
using namespace std;

void ref(int& v)
{
	cout << "left" << endl;
}

void ref(int&& v)
{
	cout << "right" << endl;
}

int main(int argc, char* argv[])
{
	int a = 0;
	a = 3;
	ref(forward<int>(a));
	return 0;
}
