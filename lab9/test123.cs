using System;

class Program
{
    static void Main(string[] args)
    {
        // Координаты центра окружности
        double x_c = 0;
        double y_c = 0;
        // Радиус окружности
        double r = 5;

        // Координаты точки
        double x = 3;
        double y = 4;

        string result = CheckPointOnCircle(x, y, x_c, y_c, r);
        Console.WriteLine(result);
    }

    static string CheckPointOnCircle(double x, double y, double x_c, double y_c, double r)
    {
        double distance = Math.Sqrt(Math.Pow(x - x_c, 2) + Math.Pow(y - y_c, 2));
        if (distance == r)
        {
            return "Точка лежит на окружности";
        }
        else if (distance < r)
        {
            return "Точка внутри окружности";
        }
        else
        {
            return "Точка вне окружности";
        }
    }
}