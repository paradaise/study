using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _5.Сигналы_с_ограниченным_спектром
{
    class Integral
    {
        private double A, B, Sum = 0;

        // конструктор класса
        public Integral(double a, double b, Func<double, double> f)
        {
            this.A = a;
            this.B = b;
            this.f = f;
        }

        // Функция для интегрирования
        Func<double, double> f;

        /// <summary>
        /// Численное вычисление интеграла методом Симпсона
        /// без контроля погрешности
        /// </summary>
        /// <param name="a">Нижний предел интегрирования</param>
        /// <param name="b">Верхний предел интегрирования</param>
        /// <param name="N">Количество разбиений</param>
        /// <returns></returns>
        public double Simpson(double a, double b, int N)
        {
            // a, b - пределы интегрирования, N - число разбиений
            //int i;
            double xi, h, h2, s, p, v;

            N = (int)(N / 2) * 2; // N - должно быть четным, чисто точек N+1
            h = (b - a) / N; // длина отрезка
            h2 = h * 2; // длина двойного интервала
            v = p = 0; // обнуляем сумматоры (суммируют интегралы на малых участках)
            s = f(a) + f(b); // сумма значений функции в крайних точках

            // начало прохода узлов с нечетным индексом
            xi = a + h;

            // р - сумматор для узлов с нечетным индексом
            while (xi < b)
            {
                p = p + f(xi);
                xi = xi + h2;
            }

            // начало прохода узлов с четным индексом
            xi = a + h2;

            // v - сумматор для узлов с четным индексом
            while (xi < (b - h))
            {
                v = v + f(xi);
                xi = xi + h2;
            }

            // формула Симпсона 
            /* выводится путём замены значения функции на сдвоенном отрезке
             * интерполяционным полиномом Лагранжа третьей степени (парабола, 
             * проходящая через три точки на графике)
             */

            return h / 3 * (s + 4 * p + 2 * v);
        }
    }
}
