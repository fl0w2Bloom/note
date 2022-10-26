//#include <iostream>
//#include <initializer_list>
//#include <vector>
//
//template <typename T>
//void printf1(T value)
//{
//	std::cout << "<typename T>" << value << std::endl;
//}
//
//template <typename T, typename ... Ts>
//void printf1(T value, Ts ... args)
//{
//	std::cout << "<typename T,typename ... Ts>" << value << std::endl;
//	printf1(args...);
//}
//
//template <typename T, typename ...Ts>
//void print2(T value, Ts ... args)
//{
//	std::cout << value << std::endl;
//	if constexpr (sizeof...(args) > 0) print2(args...);
//}
//
//template <typename ...T>
//auto sum(T ...t) -> decltype((t + ...))
//{
//	return (t + ...);
//}
//
//using namespace std;
//
//template <typename T, typename ...Ts>
//void print3(T value, Ts ...args)
//{
//	// for (auto i : initializer_list<T>{args..., value})
//	// 	cout << i << endl;
//	auto _ = {(cout << args << endl, 0)...};
//}
//
//
//int main(int argc, char* argv[])
//{
//	print3(99, 2, 3, 4, 5);
//
//	//for (auto iter = value.begin(); iter != value.end(); iter++) std::cout << *iter << std::endl;
//	return 0;
//}
