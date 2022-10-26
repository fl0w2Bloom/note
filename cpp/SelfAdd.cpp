////#include <iostream>
////
////class People
////{
////public:
////	People(int value, int id): id_(id), money_value_(value)
////	{
////		std::cout << "call People function\n";
////	}
////
////	void show();
////
////	static bool initpool();
////	static void freepool();
////
////	void* operator new(size_t size)
////	{
////		std::cout << "rewrite new in class :\n";
////		if (m_pool[0] == 0)
////		{
////			m_pool[0] = 1;
////			std::cout << "block 1 success \n";
////			return m_pool + 1;
////		}
////		if (m_pool[9] == 0)
////		{
////			m_pool[9] = 1;
////			std::cout << "block 2 success \n";
////			return m_pool + 10;
////		}
////		void* m_ptr = malloc(size);
////
////		std::cout << "system allocate memory\n";
////		return m_ptr;
////	}
////
////	void operator delete(void* ptr)
////	{
////		if (ptr == nullptr) return;
////		if (m_pool[0])
////		{
////			m_pool[0] = 0;
////			std::cout << "释放第一块分配的内存\n";
////			memset(m_pool + 1, 0, 8);
////		}
////		else if (m_pool[9])
////		{
////			std::cout << "释放第二块分配的内存\n";
////			m_pool[9] = 0;
////			memset(m_pool + 10, 0, 8);
////		}
////		else
////		{
////			std::cout << "释放由系统分配的内存\n";
////			free(ptr);
////			ptr = nullptr;
////		}
////	}
////
////	People& operator+(int num)
////	{
////		money_value_ += num;
////		std::cout << "-------------------- " << money_value_ << "\n";
////		return *this;
////	}
////
////
////private:
////	int id_;
////	int money_value_;
////	static char* m_pool;
////};
////
////char* People::m_pool = nullptr;
////
////bool People::initpool()
////{
////	std::cout << " init memory pool" << std::endl;
////	m_pool = (char*)malloc(18);
////	memset(m_pool, 0, 18);
////	std::cout << "分配地址为:" << (void*)m_pool << "\n";
////	if (m_pool) return true;
////	return false;
////}
////
////void People::freepool()
////{
////	if (!m_pool) return;
////	free(m_pool);
////	std::cout << "free m_pool address" << (void*)m_pool << "\n";
////	m_pool = nullptr;
////	std::cout << " mpool free \n";
////}
////
////void People::show()
////{
////	std::cout << "money: " << this->money_value_ << "\t id = " << this->id_ << std::endl;
////}
////
////
////int main()
////{
////	People::initpool();
////	People people(0, 1);
////	people + 9999;
////	people.show();
////	People* p1 = new People(3, 4);
////	p1->show();
////	*p1 + 5555;
////	p1->show();
////
////
////	delete p1;
////	People* p2 = new People(5, 6);
////	p2->show();
////	People* p3 = new People(7, 8);
////	p3->show();
////	delete p1;
////	People* p4 = new People(9, 10);
////	p1->show();
////	delete p2;
////	delete p3;
////
////	People::freepool();
////	return 0;
////}
//
//
//#include <iostream>
//#include <vector>
//#include <functional>
//
//class Key
//{
//public:
//	Key(int id, int name);
//	static void initpool();
//	static void freepool();
//	void* operator new(size_t size);
//	void operator delete(void* ptr);
//	void show();
//
//	void operator()()
//	{
//		std::cout << "id + name " << this->m_key_id + this->m_key_name << std::endl;
//	}
//
//private:
//	static char* p_pool;
//	int m_key_id;
//	int m_key_name;
//};
//
//char* Key::p_pool = nullptr;
//
//void Key::operator delete(void* ptr)
//{
//	if (ptr == nullptr) return;
//	if (p_pool[0])
//	{
//		p_pool[0] = 0;
//		memset(p_pool + 1, 0, 8);
//	}
//	else if (p_pool[9])
//	{
//		p_pool[9] = 0;
//		memset(p_pool + 10, 0, 8);
//	}
//	else
//	{
//		free(ptr);
//		ptr = nullptr;
//		std::cout << "system allocate memory free" << std::endl;
//	}
//}
//
//void Key::show()
//{
//	std::cout << "key id " << this->m_key_id << " key name : " << this->m_key_name << std::endl;;
//}
//
//Key::Key(int id, int name): m_key_id(id), m_key_name(name)
//{
//	std::cout << "Key run finished.\n";
//}
//
//void* Key::operator new(size_t size)
//{
//	if (!p_pool[0])
//	{
//		p_pool[0] = 1;
//		std::cout << "block 1 finish.\n";
//		std::cout << "address is " << (void*)(p_pool + 1) << std::endl;
//		return p_pool + 1;
//	}
//	else if (!p_pool[9])
//	{
//		p_pool[9] = 1;
//		std::cout << "block 2 finish \n";
//		std::cout << "block 2 address is " << (void*)(p_pool + 10) << std::endl;;
//		return p_pool + 10;
//	}
//	else
//	{
//		void* ptr = malloc(size);
//		std::cout << "system finish" << (void*)ptr << std::endl;
//		return ptr;
//	}
//}
//
//void Key::initpool()
//{
//	p_pool = (char*)malloc(18);
//	memset(p_pool, 0, 18);
//	std::cout << "init finish \n";
//	std::cout << "p_pool address: " << (void*)p_pool << std::endl;;
//}
//
//void Key::freepool()
//{
//	free(p_pool);
//	p_pool = nullptr;
//	std::cout << "free finish \n";
//}
//
//void show()
//{
//	std::cout << "this is show function   \t" << std::endl;
//}
//
//int main(int argc, char* argv[])
//{
//	Key::initpool();
//
//	Key* key1 = new Key(1, 2);
//	key1->show();
//
//	Key* key2 = new Key(3, 4);
//	key2->show();
//
//	Key* key3 = new Key(5, 6);
//	key3->show();
//
//
//	(*key2)();
//
//
//	std::function<void()> f1 = std::bind(show);
//	f1();
//
//	std::cout << "-----------------------------" << std::endl;
//	std::function<void(Key&)> f2 = &Key::show;
//	f2(*key1);
//	std::cout << "-----------------------------" << std::endl;
//
//	std::cout << "-----------------------------" << std::endl;
//	std::function<void(Key&)> f3 = std::bind(&Key::show, std::placeholders::_1);
//	f3(*key1);
//	std::cout << "-----------------------------" << std::endl;
//
//
//	Key key(99, 99);
//	std::function<void()> fkey = std::bind(&Key::show, key);
//	fkey();
//	std::cout << "-----------------------------" << std::endl;
//	std::function<void()> fn3 = std::bind(&Key::show, *key1);
//	fn3();
//	std::cout << "-----------------------------" << std::endl;
//
//
//	std::function<void()> fn4 = std::bind(&Key::show, *key3);
//	fn4();
//
//	std::function<void(Key&)> fn5 = std::bind(&Key::show, std::placeholders::_1);
//	fn5(*key3);
//	delete key1;
//	delete key2;
//	delete key3;
//	Key::freepool();
//
//
//	return 0;
//}
