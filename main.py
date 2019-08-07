import taylorseriesplot


def main():

    print("--------------------------")
    print("| codedrome.com          |")
    print("| Plotting Taylor Series |")
    print("--------------------------\n")

    taylorseriesplot.taylor_sin_plot(2, 360, 8, 1440, 800, "tsp1.svg")
    taylorseriesplot.taylor_sin_plot(2, 360, 4, 720, 400, "tsp2.svg")
    taylorseriesplot.taylor_sin_plot(4, 720, 8, 720, 400, "tsp3.svg")


main()
