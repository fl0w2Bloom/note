//#include <iostream>
//#include <type_traits>
//using namespace std;
//#define LEN 10
//
//void foo(char*)
//{
//	cout << "foo(char*)" << endl;
//}
//
//void foo(int)
//{
//	cout << "foo(int)" << endl;
//}
//
//void test1()
//{
//	if (is_same<decltype(NULL), decltype(nullptr)>::value)
//		cout << "NULL == 0" << endl;
//	if (is_same<decltype(NULL), decltype((void*)0)>::value)
//		cout << "NULL == (void*)0" << endl;
//	if (is_same<decltype(NULL), nullptr_t>::value)
//		cout << "NULL == nullptr" << endl;
//	if (is_same<decltype(nullptr), nullptr_t>::value)
//		cout << "nullptr == nullptr_t" << endl;
//}
//
//int len_foo()
//{
//	int i = 2;
//	return i;
//}
//
//constexpr int len_foo_constexpr()
//{
//	return 5;
//}
//
//constexpr int fibonacci(const int n)
//{
//	return n == 1 || n == 2 ? 1 : fibonacci(n - 1) + fibonacci(n - 2);
//}
//
//int main(int argc, char* argv[])
//{
//	foo(nullptr);
//	test1();
//	int arr_1[10];
//	int arr_2[LEN];
//	int len = 10;
//	/*int arr_3[len];*/
//	/*const int len_2 = len + 1;*/
//	/*int arr_len_2[len_2];*/
//	constexpr int len_2_constexpr = 3 + 5 + 5;
//	int len_constexpr[len_2_constexpr];
//	/*int foo1[len_foo()];*/
//	int foo2[len_foo_constexpr()];
//	cout << fibonacci(10) << endl;
//	return 0;
//}
