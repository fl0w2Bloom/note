//#include <iostream>
//#include <tuple>
//#include <initializer_list>
//#include <vector>
//
//std::tuple<int, double, std::string> f()
//{
//	return std::make_tuple(1, 2.3, "456");
//}
//
//class Foo
//{
//public:
//	std::vector<int> vec;
//	void setVec(std::initializer_list<int> list);
//	void showVec();
//	void operator()();
//};
//
//void Foo::operator()()
//{
//	for (auto i : vec)
//	{
//		std::cout << i << std::endl;
//	}
//}
//
//void Foo::setVec(std::initializer_list<int> list)
//{
//	for (std::initializer_list<int>::iterator iter = list.begin(); iter != list.end(); iter++)
//	{
//		vec.push_back(*iter);
//	}
//}
//
//void Foo::showVec()
//{
//	for (auto i : vec)
//	{
//		std::cout << i << std::endl;
//	}
//}
//
//template <typename T, typename U>
//auto adddd(T x, U y) -> decltype(x + y)
//{
//	return x + y;
//}
//
//int main(int argc, char* argv[])
//{
//	auto [x, y, z] = f();
//	std::cout << x << y << z << std::endl;
//	Foo foo;
//	foo.setVec({1, 2, 3, 4, 5, 6});
//	foo.showVec();
//
//	auto i = 5;
//	auto j = 6;
//	decltype(1) arr[3] = {1, 2, 3};
//	std::cout << std::is_same<decltype(1), decltype(2)>::value << std::endl;
//	std::cout << adddd(1, 99);
//	return 0;
//}
