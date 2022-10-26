//#include <iostream>
//#include <utility>
//#include <vector>
//#include <string>
//
//using namespace std;
//
//class A
//{
//public:
//	int* pointer;
//
//	A(): pointer(new int(1))
//	{
//		cout << "¹¹Ôì" << endl;
//	}
//
//	A(A& a): pointer(new int(*a.pointer))
//	{
//		cout << "Copy" << endl;
//	}
//
//	A(A&& a) noexcept: pointer(a.pointer)
//	{
//		a.pointer = nullptr;
//		cout << "Move" << endl;
//	}
//
//	~A()
//	{
//		cout << "xigou" << endl;
//		pointer = nullptr;
//		delete pointer;
//	}
//};
//
//A ren_rvalue(bool test)
//{
//	A a, b;
//	if (test) return a;
//	else return b;
//}
//
//int main(int argc, char* argv[])
//{
//	//A obj = ren_rvalue(false);
//	//cout << "obj" << endl;
//	//cout << obj.pointer << endl;
//	//cout << *obj.pointer << endl;
//
//	string str = "Hello Wolrd";
//	vector<string> vec;
//	vec.push_back(str);
//	cout << "Str**" << str << endl;
//
//	vec.push_back(move(str));
//	cout << "--Str--" << str << endl;
//	return 0;
//}
