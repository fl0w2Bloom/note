//#include <iostream>
//#include <memory>
//#include <utility>
//
//void lambdaExpression_capture()
//{
//	std::unique_ptr<int> important = std::make_unique<int>(1);
//	std::cout << *important << std::endl;
//	auto add = [v1 = 1, v2 = std::move(important)](int x, int y) -> int
//	{
//		return x + y + v1 + (*v2);
//	};
//	std::cout << add(3, 4) << std::endl;
//}
//
//void lambda_ref_capt()
//{
//	int value = 1;
//	auto copy_value = [&value] { return value; };
//	value = 100;
//	auto storedValue = copy_value();
//	std::cout << "stored value " << storedValue << std::endl;
//}
//
//int main(int argc, char* argv[])
//{
//	lambdaExpression_capture();
//	lambda_ref_capt();
//	return 0;
//}
