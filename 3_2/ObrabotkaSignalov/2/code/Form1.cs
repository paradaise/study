using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Fourier
{
    public partial class Form1 : Form
    {
        public delegate double fooHandler(double x);
        MathFunctions math = new MathFunctions();
        int tochek=1000;
        public Form1()
        {
            InitializeComponent();
            math.current_foo = (x) => { return MathFunctions.tri(x,12,240); };
            createChart(-12, 12, (x)=> { return math.current_foo(x); });
        }

        public void createChartAmplitude(List<double> array_a, List<double> array_b)
        {
            chart_A.Series[0].Points.Clear();
            for (int i = 0; i < array_a.Count; i++)
            {
                chart_A.Series[0].Points.AddXY(i+1, Math.Sqrt(Math.Pow(array_a[i], 2) + Math.Pow(array_b[i], 2)));
            }
        }
        public void createChartPhase(List<double> array_a, List<double> array_b)
        {
            chart_F.Series[0].Points.Clear();
            for (int i = 0; i < array_a.Count; i++)
            {
                chart_F.Series[0].Points.AddXY(i+1, Math.Abs(Math.Atan(array_b[i] / array_a[i])));
            }
        }
        public void createChartFinale(double a, double b, fooHandler foo)
        {
            chart_finale.Series[0].Points.Clear();
            double h = (b - a) / tochek;
            for (int i = 0; i < tochek; i++)
            {
                chart_finale.Series[0].Points.AddXY(a + i * h, foo(a + i * h));
            }
        }
        public void createChart(double a, double b,fooHandler foo)
        {
            chart.Series[0].Points.Clear();
            double h = (b - a) / tochek;
            for (int i = 0; i < tochek; i++)
            {
                chart.Series[0].Points.AddXY(a + i * h, foo(a + i * h));
            }
        }
        public double fourierSeries(double x,double t_imp, List<double> array_a, List<double> array_b)
        {
            double sum = 0;
            for (int k = 1; k <= array_a.Count; k++)
            { sum += array_a[k-1] * Math.Cos(k * x * 2d*Math.PI / t_imp) + array_b[k-1] * Math.Sin(k * 2d  * x * Math.PI / t_imp); }
            return sum;
        }
        private void button_Start_Click(object sender, EventArgs e)
        {
            int N=1;
            double a, b,t_imp,loses,e_max;
            if (!double.TryParse(textBox_timpuls.Text, out t_imp))
            {
                MessageBox.Show("Не правильно введено мя импульса");
                return;
            }
            if (!double.TryParse(textBox_Loses.Text, out loses))
            {
                MessageBox.Show("Не правильно введено потери");
                return;
            }
            if (!double.TryParse(textBox_Emax.Text, out e_max))
            {
                MessageBox.Show("Не правильно введено Emax");
                return;
            }
            if (!int.TryParse(textBox_tochek.Text, out tochek))
            {
                MessageBox.Show("Не правильно введено кол-во точек на графике");
                return;
            }
            double Pc, Pk;
            List<double> array_a = new List<double>();
            List< double > array_b = new List<double>();
            double a0 = 0;
            math.current_foo = (x) => { return MathFunctions.tri(x,t_imp,e_max); };
            a0 = (2d / t_imp) * math.integration(0, t_imp,10000);
            math.current_foo = (x) => { return Math.Pow(MathFunctions.tri(x, t_imp, e_max), 2); };
            Pc = math.integration(0,t_imp,10000)/t_imp;
            Pk = Math.Pow(a0 / 2, 2);
            while ((Pc-Pk)/Pc >loses)
            {
                //if (N % 2 == 1)
                //    array_a.Add(4 * e_max / Math.Pow(Math.PI * N, 2));
                //else
                //    array_a.Add(0);
                //array_b.Add(0);
                math.current_foo = (double x) =>
                { 
                    return MathFunctions.tri(x,t_imp,e_max)*Math.Cos(x*(double)N*2d*Math.PI/12d);
                };
                array_a.Add((2d / t_imp) * math.integration(-t_imp, t_imp, 10000));

                math.current_foo = (double x) =>
                {
                    return (MathFunctions.tri(x, t_imp, e_max) * Math.Sin(2d*(double)N * x * ((2d * Math.PI) / t_imp)));
                };
                array_b.Add((2d / t_imp) * math.integration(-t_imp, t_imp, 10000));
                Pk += 0.5 * (Math.Pow(array_a[array_a.Count-1], 2)+ Math.Pow(array_b[array_b.Count-1],2));
                N++;
            }
            labelPc.Text = "Pc=" + Math.Round(Pc,5).ToString();
            labelPk.Text = "Pk=" + Math.Round(Pk,5).ToString();
            labelloses.Text = "(Pc-Pk)/Pc=\n" + ((Pc - Pk) / Pc).ToString();

            createChart(-t_imp, t_imp, (x) => { return MathFunctions.tri(x,t_imp,e_max); });
            createChartAmplitude(array_a, array_b);
            createChartPhase(array_a, array_b);
            createChartFinale(-t_imp, t_imp, (x) => { return (a0/2d)+fourierSeries(x,t_imp, array_a, array_b); });
        }
    }
    public class MathFunctions
    {
        public delegate double fooHandler(double x);
        public fooHandler current_foo ;
        
        public static double tri(double x, double t_imp, double e_max)//напильник
        {
            return (2 * e_max / Math.PI) * Math.Atan(1/Math.Tan(x*Math.PI/t_imp));
        }
        public double integration(double a,double b ,int n)
        {
            double h = (b - a) / n;
            double sum1 = 0d;
            double sum2 = 0d;
            for (int k = 1; k <= n; k++)
            {
                double xk = a + k * h;
                if (k <= n - 1)
                {
                    sum1 += current_foo(xk);
                }

                double xk_1 = a + (k - 1) * h;
                sum2 += current_foo((xk + xk_1) / 2);
            }

            double result = h / 3d * (1d / 2d * current_foo(a) + sum1 + 2 * sum2 + 1d / 2d * current_foo(b));
            return result;
        }
    }
}
