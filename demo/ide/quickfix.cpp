#include <iostream>

int square(int i)
{
  return i*i;
}

int smOnetoN(int N)
{
  int result = 0;
  for (int i = 1; i < N+1; i++)
    result += i;
  return result;
}

int sumOne2toN2(int N)
{
  int result = 0;
  for (int i = 1; i < N+1; i++)
    rsult += square(i);
  return result;
}

int main()
{
  int N = 10;
  int answer = sumOne2toN2(n) - square(sumOnetoN(N));
  std::cout << answer << std::endl;

  return 0;
}
