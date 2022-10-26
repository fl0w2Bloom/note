//#include <iostream>
//#include <type_traits>
//using namespace std;
//#include <vector>
//#include <string>
//
//std::vector<int> foo()
//{
//	std::vector<int> temp = {1, 2, 3, 4};
//	cout << (void*)&temp << endl;
//	return temp;
//}
//
//void reference(std::string& str)
//{
//	cout << "left value" << endl;
//}
//
//void reference(std::string&& str)
//{
//	cout << "right value" << endl;
//}
//
//int main(int argc, char* argv[])
//{
//	/*const char (&left)[6] = "01234";
//	static_assert(is_same<decltype("01234"), const char(&)[6]>::value, "qqqqqq");
//	auto v = foo();
//	cout << (void*)&v << endl;
//	for (auto i : v) cout << i;*/
//	string lv1 = "string";
//	/*string&& r1 = lv1;*/
//	string&& rv1 = move(lv1);
//	cout << rv1 << endl;
//
//	const string& lv2 = lv1 + lv1; //lv2已经是右值
//	cout << lv2 << endl;
//	
//	/*lv2 += "q";*/
//
//	string&& rv2 = lv1 + lv2;
//	cout << rv2 << endl;
//
//	return 0;
//}
