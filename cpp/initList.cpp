//#include <iostream>
//#include <vector>
//#include <initializer_list>
//using namespace std;
//
//class Foo
//{
//public:
//	int mValueA;
//	int mValueB;
//
//	Foo(int i, int b): mValueA(i), mValueB(b)
//	{
//	}
//};
//
//constexpr auto foo() -> int
//{
//	return 3;
//}
//
//class InitListFoo
//{
//public:
//	vector<int> vec;
//
//	InitListFoo(initializer_list<int> list)
//	{
//		for (initializer_list<int>::iterator iter = list.begin(); iter != list.end(); iter++)
//		{
//			vec.push_back(*iter);
//		}
//	}
//};
//
//template <typename T>
//constexpr auto add1(initializer_list<T> list) -> int
//{
//	int sum = 0;
//	for (initializer_list<int>::iterator iter = list.begin(); iter != list.end(); iter++)
//		sum += *iter;
//	return sum;
//}
//
//int main(int argc, char* argv[])
//{
//	InitListFoo foo = {1, 2, 3, 4, 5};
//	for (auto i : foo.vec)
//	{
//		cout << i << endl;
//	}
//	cout << add1<int>({'a', 'b', 'c'}) << endl;
//	/*
//	int arr[foo()] = {1, 2, 3};
//	Foo foo1(5, 6);
//	cout << "arr[0]" << arr[0] << endl;
//	cout << "foo" << foo1.mValueA << foo1.mValueB << endl;
//	vector<int> vec = {1, 2, 3, 4, 5};
//	for (auto i : vec)
//	{
//		cout << i << endl;
//	}
//	for (vector<int>::iterator iter1 = vec.begin(); iter1 != vec.end(); iter1++)
//	{
//		cout << *iter1 << endl;
//	}*/
//	return 0;
//}
