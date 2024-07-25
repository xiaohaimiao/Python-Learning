#include <iostream>
#include <cstdlib>
using namespace std;
int main()
{
  // 设置控制台输出为UTF-8编码，以支持中文输出
  system("chcp 65001>nul");

  int n = 0;
  while (true)
  {
    cout << "请输入密码\n";
    cin >> n;
    if (n == 123456)
    {
      cout << "主人，欢迎回来\n";
      break;
    }
    else
      cout << "密码错误，请重新输入\n";
  }

  return 0;
}