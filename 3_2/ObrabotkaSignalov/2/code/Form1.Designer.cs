namespace Fourier
{
    partial class Form1
    {
        /// <summary>
        /// Обязательная переменная конструктора.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Освободить все используемые ресурсы.
        /// </summary>
        /// <param name="disposing">истинно, если управляемый ресурс должен быть удален; иначе ложно.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Код, автоматически созданный конструктором форм Windows

        /// <summary>
        /// Требуемый метод для поддержки конструктора — не изменяйте 
        /// содержимое этого метода с помощью редактора кода.
        /// </summary>
        private void InitializeComponent()
        {
            System.Windows.Forms.DataVisualization.Charting.ChartArea chartArea1 = new System.Windows.Forms.DataVisualization.Charting.ChartArea();
            System.Windows.Forms.DataVisualization.Charting.Series series1 = new System.Windows.Forms.DataVisualization.Charting.Series();
            System.Windows.Forms.DataVisualization.Charting.ChartArea chartArea2 = new System.Windows.Forms.DataVisualization.Charting.ChartArea();
            System.Windows.Forms.DataVisualization.Charting.Series series2 = new System.Windows.Forms.DataVisualization.Charting.Series();
            System.Windows.Forms.DataVisualization.Charting.ChartArea chartArea3 = new System.Windows.Forms.DataVisualization.Charting.ChartArea();
            System.Windows.Forms.DataVisualization.Charting.Series series3 = new System.Windows.Forms.DataVisualization.Charting.Series();
            System.Windows.Forms.DataVisualization.Charting.ChartArea chartArea4 = new System.Windows.Forms.DataVisualization.Charting.ChartArea();
            System.Windows.Forms.DataVisualization.Charting.Series series4 = new System.Windows.Forms.DataVisualization.Charting.Series();
            this.chart = new System.Windows.Forms.DataVisualization.Charting.Chart();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.labelloses = new System.Windows.Forms.Label();
            this.labelPk = new System.Windows.Forms.Label();
            this.labelPc = new System.Windows.Forms.Label();
            this.label9 = new System.Windows.Forms.Label();
            this.textBox_Loses = new System.Windows.Forms.TextBox();
            this.label8 = new System.Windows.Forms.Label();
            this.textBox_timpuls = new System.Windows.Forms.TextBox();
            this.label7 = new System.Windows.Forms.Label();
            this.textBox_Emax = new System.Windows.Forms.TextBox();
            this.button_Start = new System.Windows.Forms.Button();
            this.label3 = new System.Windows.Forms.Label();
            this.textBox_tochek = new System.Windows.Forms.TextBox();
            this.chart_finale = new System.Windows.Forms.DataVisualization.Charting.Chart();
            this.chart_A = new System.Windows.Forms.DataVisualization.Charting.Chart();
            this.chart_F = new System.Windows.Forms.DataVisualization.Charting.Chart();
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.label4 = new System.Windows.Forms.Label();
            this.label5 = new System.Windows.Forms.Label();
            ((System.ComponentModel.ISupportInitialize)(this.chart)).BeginInit();
            this.groupBox1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.chart_finale)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.chart_A)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.chart_F)).BeginInit();
            this.SuspendLayout();
            // 
            // chart
            // 
            this.chart.Anchor = System.Windows.Forms.AnchorStyles.None;
            chartArea1.Name = "ChartArea1";
            this.chart.ChartAreas.Add(chartArea1);
            this.chart.Location = new System.Drawing.Point(177, 28);
            this.chart.Name = "chart";
            series1.ChartArea = "ChartArea1";
            series1.ChartType = System.Windows.Forms.DataVisualization.Charting.SeriesChartType.Line;
            series1.Name = "Series1";
            this.chart.Series.Add(series1);
            this.chart.Size = new System.Drawing.Size(316, 198);
            this.chart.TabIndex = 0;
            this.chart.Text = "chart1";
            // 
            // groupBox1
            // 
            this.groupBox1.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left)));
            this.groupBox1.Controls.Add(this.labelloses);
            this.groupBox1.Controls.Add(this.labelPk);
            this.groupBox1.Controls.Add(this.labelPc);
            this.groupBox1.Controls.Add(this.label9);
            this.groupBox1.Controls.Add(this.textBox_Loses);
            this.groupBox1.Controls.Add(this.label8);
            this.groupBox1.Controls.Add(this.textBox_timpuls);
            this.groupBox1.Controls.Add(this.label7);
            this.groupBox1.Controls.Add(this.textBox_Emax);
            this.groupBox1.Controls.Add(this.button_Start);
            this.groupBox1.Controls.Add(this.label3);
            this.groupBox1.Controls.Add(this.textBox_tochek);
            this.groupBox1.Location = new System.Drawing.Point(13, 12);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(148, 454);
            this.groupBox1.TabIndex = 1;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "Ввод";
            // 
            // labelloses
            // 
            this.labelloses.AutoSize = true;
            this.labelloses.Location = new System.Drawing.Point(16, 333);
            this.labelloses.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.labelloses.Name = "labelloses";
            this.labelloses.Size = new System.Drawing.Size(66, 13);
            this.labelloses.TabIndex = 23;
            this.labelloses.Text = "(Pc-Pk)/Pc=";
            // 
            // labelPk
            // 
            this.labelPk.AutoSize = true;
            this.labelPk.Location = new System.Drawing.Point(16, 313);
            this.labelPk.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.labelPk.Name = "labelPk";
            this.labelPk.Size = new System.Drawing.Size(26, 13);
            this.labelPk.TabIndex = 22;
            this.labelPk.Text = "Pk=";
            // 
            // labelPc
            // 
            this.labelPc.AutoSize = true;
            this.labelPc.Location = new System.Drawing.Point(16, 292);
            this.labelPc.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.labelPc.Name = "labelPc";
            this.labelPc.Size = new System.Drawing.Size(26, 13);
            this.labelPc.TabIndex = 21;
            this.labelPc.Text = "Pc=";
            // 
            // label9
            // 
            this.label9.AutoSize = true;
            this.label9.Location = new System.Drawing.Point(14, 262);
            this.label9.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.label9.Name = "label9";
            this.label9.Size = new System.Drawing.Size(44, 13);
            this.label9.TabIndex = 20;
            this.label9.Text = "Потери";
            // 
            // textBox_Loses
            // 
            this.textBox_Loses.Location = new System.Drawing.Point(66, 260);
            this.textBox_Loses.Margin = new System.Windows.Forms.Padding(2);
            this.textBox_Loses.Name = "textBox_Loses";
            this.textBox_Loses.Size = new System.Drawing.Size(76, 20);
            this.textBox_Loses.TabIndex = 19;
            this.textBox_Loses.Text = "0,1";
            // 
            // label8
            // 
            this.label8.AutoSize = true;
            this.label8.Location = new System.Drawing.Point(22, 240);
            this.label8.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.label8.Name = "label8";
            this.label8.Size = new System.Drawing.Size(16, 13);
            this.label8.TabIndex = 18;
            this.label8.Text = "tи";
            // 
            // textBox_timpuls
            // 
            this.textBox_timpuls.Location = new System.Drawing.Point(66, 237);
            this.textBox_timpuls.Margin = new System.Windows.Forms.Padding(2);
            this.textBox_timpuls.Name = "textBox_timpuls";
            this.textBox_timpuls.Size = new System.Drawing.Size(76, 20);
            this.textBox_timpuls.TabIndex = 17;
            this.textBox_timpuls.Text = "12";
            // 
            // label7
            // 
            this.label7.AutoSize = true;
            this.label7.Location = new System.Drawing.Point(14, 214);
            this.label7.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.label7.Name = "label7";
            this.label7.Size = new System.Drawing.Size(33, 13);
            this.label7.TabIndex = 16;
            this.label7.Text = "Emax";
            // 
            // textBox_Emax
            // 
            this.textBox_Emax.Location = new System.Drawing.Point(66, 214);
            this.textBox_Emax.Margin = new System.Windows.Forms.Padding(2);
            this.textBox_Emax.Name = "textBox_Emax";
            this.textBox_Emax.Size = new System.Drawing.Size(76, 20);
            this.textBox_Emax.TabIndex = 15;
            this.textBox_Emax.Text = "240";
            // 
            // button_Start
            // 
            this.button_Start.Location = new System.Drawing.Point(6, 39);
            this.button_Start.Name = "button_Start";
            this.button_Start.Size = new System.Drawing.Size(136, 36);
            this.button_Start.TabIndex = 11;
            this.button_Start.Text = "Выполнить";
            this.button_Start.UseVisualStyleBackColor = true;
            this.button_Start.Click += new System.EventHandler(this.button_Start_Click);
            // 
            // label3
            // 
            this.label3.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(6, 123);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(98, 13);
            this.label3.TabIndex = 5;
            this.label3.Text = "Точек на графике";
            // 
            // textBox_tochek
            // 
            this.textBox_tochek.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.textBox_tochek.Location = new System.Drawing.Point(110, 120);
            this.textBox_tochek.Name = "textBox_tochek";
            this.textBox_tochek.Size = new System.Drawing.Size(32, 20);
            this.textBox_tochek.TabIndex = 4;
            this.textBox_tochek.Text = "1000";
            // 
            // chart_finale
            // 
            this.chart_finale.Anchor = System.Windows.Forms.AnchorStyles.None;
            chartArea2.Name = "ChartArea1";
            this.chart_finale.ChartAreas.Add(chartArea2);
            this.chart_finale.Location = new System.Drawing.Point(177, 268);
            this.chart_finale.Name = "chart_finale";
            series2.ChartArea = "ChartArea1";
            series2.ChartType = System.Windows.Forms.DataVisualization.Charting.SeriesChartType.Line;
            series2.Name = "Series1";
            this.chart_finale.Series.Add(series2);
            this.chart_finale.Size = new System.Drawing.Size(316, 198);
            this.chart_finale.TabIndex = 2;
            this.chart_finale.Text = "chart_final";
            // 
            // chart_A
            // 
            this.chart_A.Anchor = System.Windows.Forms.AnchorStyles.None;
            chartArea3.Name = "ChartArea1";
            this.chart_A.ChartAreas.Add(chartArea3);
            this.chart_A.Location = new System.Drawing.Point(571, 28);
            this.chart_A.Name = "chart_A";
            series3.ChartArea = "ChartArea1";
            series3.Name = "Series1";
            this.chart_A.Series.Add(series3);
            this.chart_A.Size = new System.Drawing.Size(316, 198);
            this.chart_A.TabIndex = 3;
            this.chart_A.Text = "chart_A";
            // 
            // chart_F
            // 
            this.chart_F.Anchor = System.Windows.Forms.AnchorStyles.None;
            chartArea4.Name = "ChartArea1";
            this.chart_F.ChartAreas.Add(chartArea4);
            this.chart_F.Location = new System.Drawing.Point(571, 268);
            this.chart_F.Name = "chart_F";
            series4.ChartArea = "ChartArea1";
            series4.Name = "Series1";
            this.chart_F.Series.Add(series4);
            this.chart_F.Size = new System.Drawing.Size(316, 198);
            this.chart_F.TabIndex = 4;
            this.chart_F.Text = "chart_F";
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(174, 12);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(96, 13);
            this.label1.TabIndex = 5;
            this.label1.Text = "Исходный сигнал";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(174, 252);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(137, 13);
            this.label2.TabIndex = 6;
            this.label2.Text = "Восстановленный сигнал";
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(571, 12);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(134, 13);
            this.label4.TabIndex = 7;
            this.label4.Text = "Амплитудная диаграмма";
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Location = new System.Drawing.Point(571, 252);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(114, 13);
            this.label5.TabIndex = 8;
            this.label5.Text = "Фазовая диаграмма";
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(960, 483);
            this.Controls.Add(this.label5);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.chart_F);
            this.Controls.Add(this.chart_A);
            this.Controls.Add(this.chart_finale);
            this.Controls.Add(this.groupBox1);
            this.Controls.Add(this.chart);
            this.Name = "Form1";
            ((System.ComponentModel.ISupportInitialize)(this.chart)).EndInit();
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.chart_finale)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.chart_A)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.chart_F)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.DataVisualization.Charting.Chart chart;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.TextBox textBox_tochek;
        private System.Windows.Forms.Button button_Start;
        private System.Windows.Forms.Label label8;
        private System.Windows.Forms.TextBox textBox_timpuls;
        private System.Windows.Forms.Label label7;
        private System.Windows.Forms.TextBox textBox_Emax;
        private System.Windows.Forms.Label label9;
        private System.Windows.Forms.TextBox textBox_Loses;
        private System.Windows.Forms.DataVisualization.Charting.Chart chart_finale;
        private System.Windows.Forms.DataVisualization.Charting.Chart chart_A;
        private System.Windows.Forms.DataVisualization.Charting.Chart chart_F;
        private System.Windows.Forms.Label labelPc;
        private System.Windows.Forms.Label labelloses;
        private System.Windows.Forms.Label labelPk;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Label label5;
    }
}

