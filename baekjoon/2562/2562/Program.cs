using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Xml.Schema;

//9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.
//예를 들어, 서로 다른 9개의 자연수
//3, 29, 38, 12, 57, 74, 40, 85, 61
//이 주어지면, 이들 중 최댓값은 85이고, 이 값은 8번째 수이다.

namespace _2562
{
    internal class Program
    {
        static void Main(string[] args)
        {
            // 9개의 숫자가 주어지므로 길이 9의 배열 생성
            int[] arr = new int[9];
            // 최대값을 저장할 변수
            int max = 0;
            // 배열번호를 저장할 변수
            int num = 0;

            // 숫자를 배열에 입력
            for (int i = 0; i < 9; i++)
            {
                arr[i] = int.Parse(Console.ReadLine());
            }
            // 최대값 찾기
            for (int i = 0; i < arr.Length; i++)
            {
                if (arr[i] > max)
                {
                    // 현재값이 max보다 크면, max에 저정하고 인덱스번호도 저장.
                    max = arr[i];
                    num = i + 1; // 배열번호에 +1을 해줘야 입력된 순서의 번호가 된다.
                }
            }
            Console.WriteLine(max);
            Console.WriteLine(num);
        }
    }
}