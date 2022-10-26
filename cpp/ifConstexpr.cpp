//#include <iostream>
//
//template <typename T>
//auto print_type_info(const T& t)
//{
//	if constexpr (std::is_floating_point<T>::value)
//	{
//		return t + 0.01;
//	}
//	else
//	{
//		return t + 999;
//	}
//}
//
//int main(int argc, char* argv[])
//{
//	std::cout << print_type_info(5) << std::endl;
//	std::cout << print_type_info(3.14) << std::endl;;
//	return 0;
//}
