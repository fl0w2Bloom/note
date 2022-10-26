//#include <iostream>
//using foo = void(int);
//#include <functional>
//#include <initializer_list>
//#include <vector>
//
//std::vector<int> vec;
//
//void function(foo f)
//{
//	f(1);
//}
//
//
//int fooc(std::initializer_list<int> list)
//{
//	for (auto element : list)
//	{
//		vec.push_back(element);
//	}
//	return vec[0];
//}
//
//int fooi(int para)
//{
//	return para;
//}
//
//int fooBind(int a, int b, int c)
//{
//	return a + b + c;
//}
//
//int main(int argc, char* argv[])
//{
//	auto bindFoo = std::bind(fooBind, std::placeholders::_1, 1, 2);
//	std::cout << bindFoo(3);
//	std::function<int(int)> foo1 = fooi;
//	std::cout << foo1(5) << std::endl;
//
//	int important = 10;
//	std::function<int(void)> lambda1 = [&important]() { return important + 1; };
//	std::cout << lambda1() << std::endl;
//	std::function<void(std::vector<int>)> lambdavec = [](std::vector<int> vec)
//	{
//		for (auto i : vec) std::cout << i << std::endl;
//	};
//	std::vector<int> vec = {1, 2, 3, 4};
//	lambdavec(vec);
//	function([](int value)-> void { std::cout << value << std::endl; });
//	return 0;
//}
