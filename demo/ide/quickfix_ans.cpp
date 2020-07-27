#include <iostream>
// (\sum_{i=1}^{n} i)^2 - \sum_{i=1}^{n} i^2

int square(int i)
{
  return i*i;
}

int sumOnetoN(int N)
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
    result += square(i);
  return result;
}

int main()
{
  int N = 10;
  int answer = sumOne2toN2(N) - square(sumOnetoN(N));
  std::cout << answer << std::endl;

  return 0;
}
