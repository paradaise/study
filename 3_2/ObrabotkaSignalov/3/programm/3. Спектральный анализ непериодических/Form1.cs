using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace _3.Спектральный_анализ_непериодических
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            chart2.ChartAreas[0].AxisX.Maximum = 50;
            chart1.ChartAreas[0].AxisX.Maximum = 50;
            chart1.ChartAreas[0].AxisX.Minimum = 0;
            chart2.ChartAreas[0].AxisX.Minimum = 0;
            chart1.Series[0].ChartType = System.Windows.Forms.DataVisualization.Charting.SeriesChartType.Spline;
            chart2.Series[0].ChartType = System.Windows.Forms.DataVisualization.Charting.SeriesChartType.Line;
            chart1.Series[0].BorderWidth = 3;
            chart2.Series[0].BorderWidth = 3;
        }

        private static double A(double x)
        {
            return -60 * Math.Sin(x * 48) / x; /*-(60 * Math.Sin(48 * x)) / x;*/
        }

        private static double Ecm()
        {
            return 30*30*96;
        }

         private void button1_Click(object sender, EventArgs e)
        {
            double Ew = 0;
            int Wv=0;
            double Ec=Ecm();
            for (int w = 1; Ew < Ec * 0.95; w++)
            {
                chart1.Series[0].Points.AddXY(w, Math.Sqrt(Math.Pow(A(w),2)));
                Func<double, double> Si = x => Math.Sin(x * 96 / 2) / x;
                Integral B = new Integral(0.000001, w, Si);
                double S = Math.Abs(A(w)) / Math.PI;

                Ew += S;
                Wv = w;
            }
            double[] fh = new double[Wv + 1];
            for (int i = 0; i < Wv; i++)
            {
                if (A(i + 1) < 0)
                {
                    fh[i] = Math.PI;
                }
                else
                {
                    fh[i] = 0;
                }
            }
            for (int i = 0; i < Wv; i++)
            {
                chart2.Series[0].Points.AddXY(i + 1, fh[i]);
                if (fh[i] > 0)
                {
                    if (fh[i + 1] > 0)
                    {
                    }
                    else
                    {
                        chart2.Series[0].Points.AddXY(i + 1, 0);
                    }
                }
                else
                {
                    if (fh[i + 1] > 0)
                    {
                        chart2.Series[0].Points.AddXY(i + 1, Math.PI);
                    }
                    else
                    {
                    }
                }
            }
            label1.Text += Wv + " МГц";

        }
    }
}
