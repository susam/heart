#!/usr/bin/python3

# The MIT License (MIT)
#
# Copyright (c) 2014-2019 Susam Pal
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
# If you redistribute this code with modification, you must remove the
# strings 'Cutie Pai' and 'Susam' from the last statement in this code.


"""My heart for Cutie Pai."""

__version__ = '0.1'
__date__ = '14 February 2014'
__author__ = 'Susam Pal <susam@susam.in>'
__credits__ = 'Sunaina Pai, the inspiration behind my creativity.'


import numpy
from matplotlib import pyplot
from matplotlib import ticker


def plot_heart(message, signature, filename):
    """Plot heart shaped curves.

    The following two functions are used to plot the curves:

      1. y = sqrt(1 - |x|) * sqrt(|x|)
      2. y = -(3/2) * sqrt(1 - sqrt(|x|))

    Arguments:

    message -- Message to be displayed within the heart
    signature -- Name of the person writing the message
    filename -- Name of the file where the graph is to be saved
    """
    # Legend label
    function1 = r'$y = \sqrt{1 - |x|} \sqrt{|x|}$'
    function2 = r'$y = -\frac{3}{2} \sqrt{1 - \sqrt{|x|}}$'

    # Plot points
    x = numpy.linspace(-1, 1, 10001)
    y1 = numpy.sqrt(1 - numpy.abs(x)) * numpy.sqrt(numpy.abs(x))
    y2 = (-3/2) * numpy.sqrt(1 - numpy.sqrt((numpy.abs(x))))
    pyplot.plot(x, y1, color='red', label=function1 + ', ' + function2)
    pyplot.plot(x, y2, color='red')

    # Write messages
    text_args = {
        'size': 'x-large',
        'color': '#ff1493',
        'family': 'fantasy',
    }
    pyplot.text(0, -0.4, message,
                horizontalalignment='center', **text_args)
    pyplot.text(0.98, -1.3, signature,
                horizontalalignment='right', **text_args)

    # Set graph properties
    pyplot.legend(fancybox=True, shadow=True)
    pyplot.xlim([-1.5, 1.5])
    pyplot.ylim([-1.6, 1.0])
    pyplot.tick_params(which='major', colors='green', width='0.2')
    pyplot.tick_params(which='minor', colors='green', width='0.1')
    pyplot.grid(True, which='major', color='green',
                linestyle='-', linewidth='0.2')
    pyplot.grid(True, which='minor', color='green',
                linestyle='-', linewidth='0.1')
    axes = pyplot.axes()
    axes.set_aspect('equal')
    axes.spines['bottom'].set_color('green')
    axes.spines['top'].set_color('green')
    axes.spines['right'].set_color('green')
    axes.spines['left'].set_color('green')
    axes.xaxis.set_major_locator(ticker.MultipleLocator(0.5))
    axes.xaxis.set_minor_locator(ticker.MultipleLocator(0.1))
    axes.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
    axes.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))

    # Save the graph to a file
    figure = pyplot.gcf()
    figure.set_size_inches(9.6, 7.2)
    pyplot.savefig(filename)

if __name__ == '__main__':
    plot_heart('I love you, my Cutie Pai!', '\u2014 Susam',
               'heart-2014-02-14.png')
