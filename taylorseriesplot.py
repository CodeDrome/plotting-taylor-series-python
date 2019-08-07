import math

import taylorseries
import svg


def taylor_sin_plot(maxsin, maxdegrees, step, width, height, filename):

    """
    Plots a sine wave using Python's math.sin and then plots sine waves using
    the taylorseries module to various degrees to illustrate increasing accurancy.
    Plots are generated and saved using the svg module.
    """

    topmargin = 64
    bottommargin = 32
    leftmargin = 32
    rightmargin = 128

    graph_height = height - topmargin - bottommargin
    graph_width = width - leftmargin - rightmargin
    pixels_per_unit_x = graph_width / maxdegrees
    pixels_per_unit_y = graph_height / (maxsin * 2.0)
    yzero = topmargin + (graph_height / 2)

    colours = ("blue", "red", "orange", "purple", "green", "cyan")

    # Create svg object
    s = svg.SVG()
    s.create(width, height)
    s.fill("#FFFFFF")

    # header text and border lines
    s.text(leftmargin, 38, "sans-serif", 16, "#000000", "#000000", "start", "Sines calculated with Taylor Polynomials to degree 3, 5, 7, 9 and 11")
    s.line("#808080", 2, leftmargin, topmargin, leftmargin, height - bottommargin)
    s.line("#808080", 2, leftmargin, height - bottommargin, width - rightmargin, height - bottommargin)

    # y axis indexes and values
    y = topmargin
    for i in range(maxsin, (maxsin * -1) - 1, -1):
         s.line("#808080", 1, leftmargin - 8, y, width - rightmargin, y)
         s.text(20, y + 4, "sans-serif", 12, "#000000", "#000000", "end", str(i))
         y += pixels_per_unit_y

    # x axis indexes and values
    x = leftmargin
    for d in range(0, maxdegrees + 1, 90):
         s.line("#808080", 1, x, topmargin, x, height - bottommargin + 8)
         s.text(x, height - bottommargin + 24, "sans-serif", 12, "#000000", "#000000", "middle", str(d))
         x += (pixels_per_unit_x * 90)

    # key
    x = width - rightmargin + 16
    y = topmargin + 16
    currdegree = 3
    for colourindex in range(0, 6):

         s.circle(colours[colourindex], 0, colours[colourindex], 6, x, y)

         if(colourindex == 0):
             s.text( x + 16, y + 4, "sans-serif", 12, "#000000", "#000000", "start", "math.sin")
         else:
             s.text( x + 16, y + 4, "sans-serif", 12, "#000000", "#000000", "start", str(currdegree));
             currdegree += 2

         y+= 24

    # Taylor Series plots
    x = leftmargin

    for degree in range(0, maxdegrees + 1, step):

        radians = math.radians(degree)
        sine = math.sin(radians)
        y = yzero - (sine * pixels_per_unit_y)
        colourindex = 0

        s.circle(colours[colourindex], 0, colours[colourindex], 3, x, y)

        for poly_degree in range(3, 12, 2):

            colourindex += 1

            sine = taylorseries.sine_of_radians(radians, poly_degree)

            if(sine <= maxsin and sine >= (maxsin * -1)):
                y = yzero - (sine * pixels_per_unit_y)
                s.circle(colours[colourindex], 0, colours[colourindex], 3, x, y)

        x += pixels_per_unit_x * step

    s.finalize()

    s.save(filename)

    print("File saved")
