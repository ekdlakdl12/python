using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

//과거 이집트인들은 각 변들의 길이가 3, 4, 5인 삼각형이 직각 삼각형인것을 알아냈다.
//주어진 세변의 길이로 삼각형이 직각인지 아닌지 구분하시오.
// 예제 입력 6,8,10 / 25,52,60/ 5,12,13/ 0,0,0 <-- 종료
// 피타고라스의 정리에 의하면 a^ + b^ = c^ 이면 직각삼각형이다

namespace _4153
{
    internal class Program
    {
        static void Main(string[] args)
        {

            while (true)
            {
                string[] input = Console.ReadLine().Split(); // 다중값을 입력받아야하기때문에 스플릿을위해 문자열로 먼저 받아둠

                int a = int.Parse(input[0]); //여기서 형변환
                int b = int.Parse(input[1]);
                int c = int.Parse(input[2]);

                if (a == 0 && b == 0 && c == 0) //종료
                    break;

                if (a * a + b * b == c * c)
                {
                    Console.WriteLine("right");
                    continue;
                }
                if (c * c + b * b == a * a)
                {
                    Console.WriteLine("right");
                    continue;
                }
                if (c * c + a * a == b * b)
                {
                    Console.WriteLine("right");
                    continue;
                }
                Console.WriteLine("wrong");

            }
        }
    }
}