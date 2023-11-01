using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

//수를 처리하는 것은 통계학에서 상당히 중요한 일이다. 통계학에서 N개의 수를 대표하는 기본 통계값에는 다음과 같은 것들이 있다. 단, N은 홀수라고 가정하자.
//산술평균: N개의 수들의 합을 N으로 나눈 값
//중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
//최빈값 : N개의 수들 중 가장 많이 나타나는 값
//범위 : N개의 수들 중 최댓값과 최솟값의 차이
//N개의 수가 주어졌을 때, 네 가지 기본 통계값을 구하는 프로그램을 작성하시오.


namespace _2108
{
    class Program
    {
        static void Main()
        {
            int n = int.Parse(Console.ReadLine()); //n값
            int[] counting = new int[7001]; 
            int mean = 0;
            double median = 0;
            int mode = 0;
            List<int> modeList = new List<int>();
            
            int range = 0; 
            double sum = 0; //합계
            int half = n / 2 + 1; //중앙값
            int min = 4000; //절대값
            int max = -4000;

            for (int i = 0; i < n; i++)
            {
                int input = int.Parse(Console.ReadLine());
                counting[input + 4000]++;
                sum += input;

                if (min > input)
                    min = input;

                if (max < input)
                    max = input;
            }

            for (int i = 0; i < 8001; i++)

            {
                if (mode < counting[i])
                    mode = counting[i];

                if (half > 0)

                {
                    half -= counting[i];
                    median = i - 4000;
                }
            }

            for (int i = 0; i < 8001; i++)

                if (mode == counting[i])
                    modeList.Add(i - 4000);

            modeList.Sort();

            mean = (int)Math.Round(sum / n, MidpointRounding.AwayFromZero);
            
            mode = modeList.Count == 1 ? modeList[0] : modeList[1];
            range = max - min;


            Console.Write(mean + "n" + median + "n" + mode + "n" + range);

        }
    }
}