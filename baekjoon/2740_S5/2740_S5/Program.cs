using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

//행렬의 곱셈

namespace _2740_S5
{
    public class Program
    { 
        static void Main(string[] args)
        {
            //출력용 배열
            int[,] insert = new int[3, 3]; 

            //입력
            int n, m = 0;
            int z, k = 0;
            int sum = 0;

            //행렬 2차원 배열 선언
            //A행렬
            string[] index = Console.ReadLine().Split();
            n = int.Parse(index[0]);
            m = int.Parse(index[1]);

            int[,] matrixA = new int[n, m]; // 2,3

            //A 행렬 입력
            for (int i = 0; i < n; i++) // 2
            {
                for (int j = 0; j < m; j++) // 3
                {
                    matrixA[i, j] = Int32.Parse(Console.ReadLine());
                }
            }
            Console.WriteLine();
            
            //B행렬
            string[] index2 = Console.ReadLine().Split();
            z = int.Parse(index2[0]);
            k = int.Parse(index2[1]);

            int[,] matrixB = new int[z, k]; // 3,3

            //B 행렬 입력
            for (int o = 0; o < z; o++)
            {
                for (int p = 0; p < k; p++)
                {
                    matrixB[o, p] = Int32.Parse(Console.ReadLine());
                }
            }

            //곱셈 넣을 배열
            int[,] answer = new int[matrixA.GetLength(0), matrixB.GetLength(1)];
            
            //곱셈
            for(int e = 0; e<matrixA.GetLength(0); e++) 
            {
                for(int f =0; f<matrixB.GetLength(1); f++) 
                {
                    for (int g = 0; g<matrixA.GetLength(1); g++)
                        answer[e, f] += matrixA[e, g]* matrixB[g, f];
                 }
            }
            //출력

            for (int x = 0; x < matrixA.GetLength(0); x++)
            {
                for (int y = 0; y < matrixB.GetLength(1); y++)
                    Console.WriteLine(answer[x,y]);
            }
        }
    }
}