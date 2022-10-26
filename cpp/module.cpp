//#include <iostream>
//#include <vector>
//
//template <class T, class U>
//class MagicType
//{
//public:
//	T mDark;
//	U mMagic;
//	void operator()();
//};
//
//template <class T, class U>
//void MagicType<T, U>::operator()()
//{
//	std::cout << mMagic << std::endl;
//	for (auto i : mDark) std::cout << i;
//}
//
//typedef int (*process)(void*);
//using NewProcess = int(*)(void*);
//template <typename T>
//using TrueDarkMagic = MagicType<std::vector<T>, std::string>;
//
//int main(int argc, char* argv[])
//{
//	TrueDarkMagic<bool> you;
//	you.mDark.push_back(true);
//	you.mMagic = "hello";
//	you();
//	return 0;
//}
