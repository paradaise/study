using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace _5.Сигналы_с_ограниченным_спектром
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private static double Ec()
        {
            return 2.79 * 6 * 6 * 6/3;
        }

        private static double A(double w)
        {
            return -10 * 0.000006 / (6 * w) * Math.Sin(0.000006 * w) + 10 / (6 *w *w) * Math.Cos(0.000006 * w);
        }

        private static double B(double w)
        {
            return 10 * 0.000006 / (6 * w) * Math.Cos(0.000006 * w) - 10 / (6 * w * w) * Math.Sin(0.000006 * w);
        }

        private static double Polinom(double S, double t, int k, int wv)
        {
            return S*Math.Sin(wv * (t - k * Math.PI / wv)) / (wv * (t - k * Math.PI / wv));
        }
               
        private void button1_Click(object sender, EventArgs e)
        {
            chart3.ChartAreas[0].AxisX.Minimum = 0;
            chart3.ChartAreas[0].AxisX.Maximum = 0.00000601;
            chart3.ChartAreas[0].AxisX.Interval = 0.000001;

            int wvn = 3141592;
            double[] SV = new double [100];
            double Ew = 0;
            double wv = 0;
            int line=2;
            for (double x = 0; x <= 0.000006; x += 0.000001)
            {
                chart3.Series[line].Points.AddXY(x,0);
                chart3.Series[line].Points.AddXY(x, x*1000000*-1.6667);
                line++;
            }

            goto A;
            for (double w = 1; Ew / Ec() <= 0.95; w++)
            {
                Func<double, double> Si = x => A(w) + B(w);
                Integral I = new Integral(0.000001, w, Si);
                double Sum = Math.Abs(I.Simpson(0.000001, w, 1000));
                Ew += 1 / Math.PI * Sum;
                wv = w;
            }

           A: 
            int T = 7;
            double[] S = new double[T];
            double[] Sk = new double[T];
            for (int i = 0; i < T; i++)
            {
                Func<double, double> Si = x => Math.Sqrt(Math.Pow(1.67 / x * Math.Sin(x * 0.000006), 2) + Math.Pow(1.67 / x * Math.Cos(x * 0.000006), 2)) * Math.Cos(i * Math.PI * x / wvn);
                Integral I = new Integral(-wv, wv, Si);
                double Sum = Math.Abs(I.Simpson(-wv, wv, 10000));
                Sk[i] = Sum / (2 * Math.PI);
            }

            #region
            S[0] = 0;
            S[1] = -1.667 * 1;
            S[2] = -1.667 * 2;
            S[3] = -1.667 * 3;
            S[4] = -1.667 * 4;
            S[5] = -1.667 * 5;
            S[6] = -1.667 * 6;
            #endregion
                   
            
            int count = 0;
            for (int k = 0; k < 7; k++)
            {
                for (double t = 0; t <= 0.000006; t += 0.000006 / 100)
                {
                    SV[count] += Polinom(S[k], t, k, wvn);
                    count++;
                }
                count = 0;
            }

            count = 0;
            for (double i = 0; i <= 0.000006; i += 0.000006 / 100)
            {
                chart3.Series[0].Points.AddXY(i, SV[count]);
                count++;
            }

            count = 0;
            for (double i = 0; i <= 0.000006; i += 0.000001)
            {
                chart3.Series[1].Points.AddXY(i, S[count]);
                count++;
            }

        }
    }
}
