"""
Based on pro plot_history,png=png

TODO:

merge all the files together with a class column

e.g. Q, G, GRB so that a single file can be maintained.

Plot the history of the progression of higher redshifts
for galaxies, quasars and GRBs

will have command line options and config file

First version created for Crafoord Symposium, Stockholm, Sep 2005


2006 version of the plot here based on my compilation for my News and Views
article.
https://www.nature.com/articles/443128a


Also, see 2009 version credited to Nial Tanvir based on Nial's
addition of GRBs to my compilation

https://www.nature.com/articles/4611221a

https://swift.gsfc.nasa.gov/results/releases/images/recordzs/

"""
from __future__ import print_function

# make code future proof for python 3 since raw_input() replaced by input()
from builtins import input
from six.moves import input
try:
   input = raw_input
except NameError:
   pass

import os
import sys
import time

import numpy as np
import matplotlib.pyplot as plt
from astropy.table import Table

from plotid import plotid
#from getargs import getargs
#from getconfig import getconfig


def read_table(filename=None):
    """

    """
    print('Reading:', filename)
    table = Table.read(filename,
                       guess=False,
                       format='ascii.csv',
                       comment='#',
                       header_start=0)
    #                  data_start=5, data_end=6)
    table.meta['filename'] = filename
    table.info()
    table.info('stats')
    print('Number of rows:', len(table))

    return table


def plot_quasar(table=None,
                plot_technique=True,
                markersize=None,
                year_min=1955.0, year_max=2020.0,
                year_xmin=None, year_xmax=None,
                redshift_ymax=10.0,
                title='Redshift Record History',
                xlabel='Year of spectroscopic confirmation',
                ylabel='Redshift'):

    """


    """

    print(table['Year'])
    print(table['Redshift'])

    xdata = table['Year']
    ydata = table['Redshift']

    print(xdata)
    print('year_max:', year_max, np.min(xdata), np.max(xdata), len(xdata))
    print(type(xdata))
    year_max = int(year_max)
    print(type(year_max))
    xdata = np.asarray(xdata)
    print(type(xdata))
    # xdata = np.ndarray.tolist(xdata)
    itest = (xdata <= year_max)
    print(itest)
    #itest = np.where(xdata <= year_max)
    #print(itest)
    xdata = xdata[itest]
    ydata = ydata[itest]

    print('Number of sources:', len(xdata))

    if plot_technique:
        print(table.meta['filename'])
        TechniqueList = ['R', 'O']
        Technique = table['Technique'][itest]
        print('Technique:', Technique[0:1])

        # strip off leading and trailing blanks
        Technique = np.core.defchararray.strip(Technique)
        print('Technique:', Technique[0:1])
        index = np.where(Technique == 'R')
        print(index)
        index2 = np.core.defchararray.find(Technique, 'R')
        print(index2)
        # avoid confusion between R and IR
        index = np.where(index2 == 0 )
        print(index)

        key = input("Enter any key to continue: ")

        plt.plot(xdata[index], ydata[index],
                 marker='o',
                 markersize=markersize,
                 color='black', linestyle='None',
                 label='Radio selected Quasar')

        index = np.where(Technique != 'R')
        print(index)

        plt.plot(xdata[index], ydata[index],
                 marker='o',
                 markersize=markersize,
                 color='blue', linestyle='None',
                 label='Optically selected Quasar')

        plt.plot(xdata, ydata,
                 marker='None',
                 markersize=markersize,
                 color='blue',
                 linewidth=1.0,
                 label='_nolegend_')


        #for technique in TechniqueList:
        #    itest =

        key = input("Enter any key to continue: ")

    if not plot_technique:
        plt.plot(xdata, ydata,
                 marker='o',
                 markersize=markersize,
                 color='blue',
                 label='Quasar')

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    if year_xmin is None:
        year_xmin = year_min
    if year_xmax is None:
        year_xmax = year_max

    print(year_xmin, year_xmax, type(year_xmin), type(year_xmax))
    plt.xlim(year_xmin, year_xmax)
    plt.ylim(0.0, redshift_ymax)

    print('year_min:', year_min)
    print('year_xmin:', year_xmin)
    print('year_max:', year_max)
    print('year_xmax:', year_xmax)
    key = input("Enter any key to continue: ")

    plt.grid()
    plt.legend(loc='upper left')
    plotid()

    plotfile = 'highestz_history_quasar_' + datestamp + '.png'
    if year_max is not None:
        plotfile = 'highestz_history_quasar_' + str(int(year_max)) + \
                   '_' + datestamp + '.png'
    if plotdir is not None:
        plotfile = plotdir + plotfile
    print('Saving:', plotfile)
    plt.savefig(plotfile)

    # plt is a global I think

    return


def plot_galaxy(table=None,
                plot_technique=True,
                markersize=None,
                year_min=1955.0, year_max=2020.0,
                year_xmin=None, year_xmax=None,
                redshift_ymax=10.0,
                title='Redshift Record History',
                xlabel='Year of spectroscopic confirmation',
                ylabel='Redshift'):
    """



    """

    xdata = table['Year']
    ydata = table['Redshift']
    print('Year range:', np.min(xdata), np.max(xdata), len(xdata))

    print('year_max:', year_max)
    itest = xdata <= year_max
    print(len(itest), len(xdata[itest]))
    xdata = xdata[itest]
    ydata = ydata[itest]

    print('Year range:', np.min(xdata), np.max(xdata), len(xdata))
    key = input("Enter any key to continue: ")

    print('plot_technique:', plot_technique)
    if plot_technique:
        TechniqueList = ['R', 'O']
        Technique = table['Technique'][itest]
        print('Technique:', Technique[0:1])
        index = np.where(Technique == 'R')
        print(index)

        plt.plot(xdata[index], ydata[index],
                 marker='*',
                 color='black',
                 markersize=markersize,
                 linestyle='None',
                 label='Radio selected Galaxy')

        index = np.where(Technique != 'R')
        print(index)

        plt.plot(xdata[index], ydata[index],
                 marker='*',
                 color='red',
                 markersize=markersize,
                 linestyle='None',
                 label='Optically selected Galaxy')

        plt.plot(xdata, ydata,
                 marker='None',
                 color='red', linewidth=1.0, label='_nolegend_')

        #for technique in TechniqueList:
        #    itest =

        key = input("Enter any key to continue: ")

    if not plot_technique:
        plt.plot(xdata, ydata, marker='*',
                 color='red',
                 markersize=markersize,
                 label='Galaxy')

    plt.legend(loc='upper left')

    print(year_xmin, year_xmax, type(year_xmin), type(year_xmax))
    plt.xlim(year_xmin, year_xmax)
    plt.ylim(0.0, redshift_ymax)

    plotfile = 'highestz_history_galaxy_' + datestamp + '.png'

    if year_max is not None:
        plotfile = 'highestz_history_galaxy_' + str(int(year_max)) + \
                   '_' + datestamp + '.png'
    if plotdir is not None:
        plotfile = plotdir + plotfile
    print('Saving:', plotfile)
    plt.savefig(plotfile)

    return


def plot_grb(table=None,
             markersize=None,
             year_min=1955.0, year_max=2020.0,
             year_xmin=None, year_xmax=None,
             redshift_ymax=10.0,
             title='Redshift Record History',
             xlabel='Year of spectroscopic confirmation',
             ylabel='Redshift'):


    xdata = table['Year']
    ydata = table['Redshift']

    itest = xdata <= year_max
    xdata = xdata[itest]
    ydata = ydata[itest]

    plt.plot(xdata, ydata,
             marker='*',
             markersize=markersize,
             color='purple',
             label='GRB')


    print(year_xmin, year_xmax, type(year_xmin), type(year_xmax))
    plt.xlim(year_xmin, year_xmax)
    plt.ylim(0.0, redshift_ymax)

    plt.legend(loc='upper left')

    plotfile = 'highestz_history_all_' + datestamp + '.png'
    if year_max is not None:
        plotfile = 'highestz_history_all_' + str(int(year_max)) + \
                   '_' + datestamp + '.png'
    if plotdir is not None:
        plotfile = plotdir + plotfile
    print('Saving:', plotfile)
    plt.savefig(plotfile)

    return


def plot_any(table=None,
             plot_technique=True,
             markersize=None,
             radio=False,
             classify=False,
             year_min=1955.0, year_max=2020.0,
             year_xmin=None, year_xmax=None,
             redshift_ymax=10.0,
             title='Redshift Record History',
             xlabel='Year of spectroscopic confirmation',
             ylabel='Redshift'):

    xdata = table['Year']
    ydata = table['Redshift']
    print(type(year_min), type(year_max))
    print(year_min, year_max)
    itest = xdata <= year_max
    xdata = xdata[itest]
    ydata = ydata[itest]

    print('markersize:', markersize)
    print('Number of data points:', len(xdata), len(ydata))
    plt.plot(xdata, ydata,
             marker='*',
             markersize=markersize,
             color='red',
             label='Any source [Galaxy, Quasar, GRB]')


    print(year_xmin, year_xmax, type(year_xmin), type(year_xmax))
    plt.xlim(year_xmin, year_xmax)
    plt.ylim(0.0, redshift_ymax)

    if radio:
        Technique = table['Technique'][itest]
        index = np.core.defchararray.find(Technique, 'R')
        # needed to distinguish, R, IR, GRB
        index = np.where(index == 0 )
        plt.plot(xdata[index], ydata[index],
                 marker='*',
                 markersize=markersize/2.0,
                 color='black',
                 linestyle='none',
                 label='Radio selected')


    if classify:
        Type = table['Type'][itest]
        index = np.core.defchararray.find(Type, 'Q')
        # needed to distinguish, R, IR, GRB
        index = np.where(index == 0 )
        plt.plot(xdata[index], ydata[index],
                 marker='o',
                 markersize=markersize*1.2,
                 color='none',
                 markeredgecolor='blue',
                 linestyle='none',
                 label='Quasar')

        index = np.core.defchararray.find(Type, 'GRB')
        # needed to distinguish, R, IR, GRB
        index = np.where(index == 0 )
        plt.plot(xdata[index], ydata[index],
                 marker='s',
                 markersize=markersize*1.2,
                 color='none',
                 markeredgecolor='black',
                 linestyle='none',
                 label='Gamma ray burst')

    print(year_xmin, year_xmax, type(year_xmin), type(year_xmax))
    plt.xlim(year_xmin, year_xmax)
    plt.ylim(0.0, redshift_ymax)

    plt.grid()
    plt.legend(loc='upper left')
    plotid()


    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    plotfile = 'highestz_history_any_' + datestamp + '.png'
    if year_max is not None:
        plotfile = 'highestz_history_any_' + str(int(year_max)) + \
                   '_' + datestamp + '.png'
    if plotdir is not None:
        plotfile = plotdir + plotfile
    print('Saving:', plotfile)
    plt.savefig(plotfile)


    return



def plot_quasar_optical_radio(
        table_optical=None,
        table_radio=None,
        plot_technique=True,
        radio=False,
        classify=False,
        year_min=1955.0, year_max=2020.0,
        year_xmin=None, year_xmax=None,
        redshift_ymax=10.0,
        title='Redshift Record History',
        xlabel='Year of spectroscopic confirmation',
        ylabel='Redshift',
        markersize=None):
    """

    plot quasars split by radio and optical

    """
    print()
    print('year_min:', year_min)
    print('year_max:', year_max)
    print('year_xmin:', year_xmin)
    print('year_xmax:', year_xmax)

    # plot the optical data
    xdata = table_optical['Year']
    ydata = table_optical['Redshift']
    print(type(year_min), type(year_max))
    print(year_min, year_max)
    itest = xdata <= year_max
    xdata = xdata[itest]
    ydata = ydata[itest]

    print('markersize:', markersize)
    print('Number of data points:', len(xdata), len(ydata))
    plt.plot(xdata, ydata,
             marker='o',
             markersize=markersize,
             linestyle = 'dashed',
             color='blue',
             label='Quasar (Optically selected)')

    print(year_xmin, year_xmax, type(year_xmin), type(year_xmax))
    plt.xlim(year_xmin, year_xmax)
    plt.ylim(0.0, redshift_ymax)


    # plot the optical data
    xdata = table_radio['Year']
    ydata = table_radio['Redshift']
    print(type(year_min), type(year_max))
    print(year_min, year_max)
    itest = xdata <= year_max
    xdata = xdata[itest]
    ydata = ydata[itest]

    print('markersize:', markersize)
    print('Number of data points:', len(xdata), len(ydata))
    plt.plot(xdata, ydata,
             marker='o',
             markersize=markersize,
             linestyle = 'dashed',
             color='black',
             label='Quasar (Radio selected)')

    print(year_xmin, year_xmax, type(year_xmin), type(year_xmax))
    plt.xlim(year_xmin, year_xmax)
    plt.ylim(0.0, redshift_ymax)

    plt.grid()
    plt.legend(loc='upper left')
    plotid()

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    plotfile = 'highestz_history_quasar_radio_optical_' + datestamp + '.png'
    if year_max is not None:
        plotfile = 'highestz_history_quasar_radio_optical_' + \
                   str(int(year_max)) + '_' + datestamp + '.png'
    if plotdir is not None:
        plotfile = plotdir + plotfile
    print('Saving:', plotfile)
    plt.savefig(plotfile)

    plt.show()


    return


def plot_history(filename_quasar=None,
                 filename_quasar_optical=None,
                 filename_quasar_radio=None,
                 filename_galaxy=None,
                 filename_grb=None,
                 filename_any=None,
                 quasar=True,
                 galaxy=True,
                 grb=True,
                 any=False,
                 radio=False,
                 optical=False,
                 classify=False,
                 markerlist=None,
                 markersize=None,
                 colorlist=None,
                 year_min=1955.0, year_max=2020.0,
                 year_xmin=None, year_xmax=None,
                 redshift_ymax=10.0,
                 title = 'Redshift Record History',
                 xlabel='Year of spectroscopic confirmation',
                 ylabel='Redshift',
                 plotdir=None):
    """
    year_min, year_max limits the range of data plotted
    year_xmin, year_xmax limits the plot limits and can
    be different.

    e.g. if you want to produce a set of plots that show the change over
    time on the same x-axis scale; fix the values of _xmin, _xmax

    markers:
    https://matplotlib.org/api/markers_api.html
    https://matplotlib.org/api/_as_gen/matplotlib.markers.MarkerStyle.html


    https://matplotlib.org/api/_as_gen/matplotlib.pyplot.scatter.html



    """

    import os
    import time
    datestamp = time.strftime("%Y%m%d")

    if plotdir is not None:
        if not os.path.exists(plotdir):
            os.makedirs(plotdir)

    if quasar and radio:
        filename = filename_quasar_optical
        table_quasar_optical = read_table(filename=filename)
        key = input("Enter any key to continue: ")

        filename = filename_quasar_radio
        table_quasar_radio = read_table(filename=filename)
        key = input("Enter any key to continue: ")

        print()
        print('year_min:', year_min)
        print('year_max:', year_max)
        print('year_xmin:', year_xmin)
        print('year_xmax:', year_xmax)

        plot_quasar_optical_radio(
            table_optical=table_quasar_optical,
            table_radio=table_quasar_radio,
            plot_technique=False,
            radio=radio,
            classify=False,
            year_min=year_min, year_max=year_max,
            year_xmin=year_xmin, year_xmax=year_xmax,
            redshift_ymax=redshift_ymax,
            title='Redshift Record History',
            xlabel='Year of spectroscopic confirmation',
            ylabel='Redshift',
            markersize=markersize)


    print('any:', any)
    if any:
        filename = filename_any
        table_any = read_table(filename=filename)
        key = input("Enter any key to continue: ")

        plot_technique = False
        if radio:
            plot_technique = True
        plot_any(table=table_any,
                 radio=radio,
                 classify=classify,
                 plot_technique=plot_technique,
                 year_min=year_min, year_max=year_max,
                 year_xmin=year_xmin, year_xmax=year_xmax,
                 redshift_ymax=redshift_ymax,
                 title=title,
                 xlabel=xlabel,
                 ylabel=ylabel,
                 markersize=markersize)

    if not any and quasar:
        filename = filename_quasar
        table_quasar = read_table(filename=filename)
        key = input("Enter any key to continue: ")

        plot_technique = True
        plot_quasar(table=table_quasar,
                    plot_technique=plot_technique,
                    year_min=year_min, year_max=year_max,
                    year_xmin=year_xmin, year_xmax=year_xmax,
                    title=title,
                    xlabel=xlabel,
                    ylabel=ylabel)

    if not any and galaxy:
        filename = filename_galaxy
        table_galaxy = read_table(filename=filename)
        key = input("Enter any key to continue: ")

        plot_technique = True
        plot_galaxy(table=table_galaxy,
                    plot_technique=plot_technique,
                    year_min=year_min, year_max=year_max,
                    year_xmin=year_xmin, year_xmax=year_xmax,
                    redshift_ymax=redshift_ymax,
                    title=title,
                    xlabel=xlabel,
                    ylabel=ylabel)

    if not any and grb:
        filename = filename_grb
        table_grb = read_table(filename=filename)
        key = input("Enter any key to continue: ")

        plot_grb(table=table_grb,
                    year_min=year_min, year_max=year_max,
                    year_xmin=year_xmin, year_xmax=year_xmax,
                    redshift_ymax=redshift_ymax,
                    title=title,
                    xlabel=xlabel,
                    ylabel=ylabel)


    return

"""

TODO: catch exceptions

Support for lists:

see:

https://stackoverflow.com/questions/335695/lists-in-configparser

https://github.com/cacois/python-configparser-examples

useage:

config = getconfig()
inpath = config.get('INPUTS', 'inpath')





"""
def getconfig(configfile=None, debug=False, silent=False):
    """


    read config file

    Note the ConfigParser module has been renamed to configparser in Python 3

    look in cwd, home and home/.config

    home/.config not implemented yet




    """
    import os
    import configparser

    from configparser import SafeConfigParser
    # parser = SafeConfigParser()

    print('__file__', __file__)
    if configfile is None:
        if debug:
            print('__file__', __file__)
        configfile_default = os.path.splitext(__file__)[0] + '.cfg'
        if debug:
            print('configfile_default:', configfile_default)
            configfile = configfile_default

    print('Open configfile:', configfile)
    if debug:
        print('Open configfile:', configfile)

    # read the configuration file
    config = configparser.RawConfigParser()

    try:
        if not silent:
           print('Reading config file', configfile)

        try:
            config.read(configfile)
        except IOError:
            print('config file', configfile, "does not exist")
            configfile = os.path.join(os.environ["HOME"], configfile)
            print('trying ', configfile)
            config.read(configfile)

    except Exception as e:
        print('Problem reading config file: ', configfile)
        print(e)


    if debug:
        print('configfile:', configfile)
        print('sections:', config.sections())
        for section_name in config.sections():
            print('Section:', section_name)
            print('Options:', config.options(section_name))
            for name, value in config.items(section_name):
                print('  %s = %s' % (name, value))
        print()


    return config


def getargs(verbose=False):
    """


    Template getargs function

    Usage

    python getargs.py --help


    def getargs():

    ....

    if __name__=='__main__':

        args = getargs()
        debug = args.debug()

    parse command line arguements

    not all args are active

    """
    import sys
    import pprint
    import argparse

    # there is probably a version function out there
    __version__ = '0.1'

    description = 'This is a template using getargs'
    epilog = """WARNING: Not all options may be supported
             """
    parser =  argparse.ArgumentParser(
        description=description, epilog=epilog,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)


    # the destination defaults to the option parameter
    # defaul=False might not be needed


    parser.add_argument("--any",
                        action='store_true',
                        help="Plot independent of classification")

    parser.add_argument("--quasar",
                        action='store_true',
                        help="Plot quasar history")

    parser.add_argument("--radio",
                        action='store_true',
                        help="Identify radio selected objects")

    parser.add_argument("--galaxy",
                        action='store_true',
                        help="Plot galaxy history")

    # note type is a python function so class needs to be used
    parser.add_argument(
        "--classify",
        action='store_true',
        help="Identify class/type of source e.g. galaxy, quasar")

    parser.add_argument("--year_min",
                        default=None,
                        help="Manimum year to plot")

    parser.add_argument("--year_max",
                        default=None,
                        help="Maximum year to plot")

    parser.add_argument("--year_xmin", type=float,
                        default=1955,
                        help="Minimum year for plot x-axis")

    parser.add_argument("--year_xmax", type=float,
                        default=2020,
                        help="Maximum year for plot x-axis")

    parser.add_argument("--redshift_ymax", type=float,
                        default=10.0,
                        help="Maximum redshuft for plot y-axis")


    # Default is rcParams['lines.markersize'] ** 2.
    # scatter:
    # s : scalar or array_like, shape (n, ), optional
    # The marker size in points**2.
    #
    # plot:
    # markersize, ms
    # Set the marker size in points
    parser.add_argument("--markersize", type=float,
                        default=7.0,
                        help="Marker size (size as diameter as in plot)")

    parser.add_argument("--plotdir",
                        help="Output/Result directory")

    parser.add_argument("--infile",
                        help="Input file name")

    parser.add_argument("--configfile",
                        default=None,
                        help="configuration file")

    parser.add_argument("--debug",
                        action='store_true',
                        help="debug option")

    parser.add_argument("--verbose", default=verbose,
                        action='store_true',
                        help="verbose option")

    parser.add_argument("--version", action='store_true',
                        help="verbose option")


    args = parser.parse_args()


    if args.debug or args.verbose:
        print()
        print('Number of arguments:', len(sys.argv),
              'arguments: ', sys.argv[0])

    if args.debug or args.verbose:
       print()
       for arg in vars(args):
          print(arg, getattr(args, arg))


    if args.debug or args.verbose:
        print()
        pprint.pprint(args)

    if args.version:
        print('version:', __version__)
        sys.exit(0)


    return args



if __name__ == "__main__":
    """
    key = input("Enter any key to continue: ")

    args = getargs()

    debug = True
    conf = getconfig(debug=debug)

    """
    t0 = time.time()
    print('Elapsed time(secs):', time.time() - t0)

    import matplotlib
    print('Elapsed time(secs):', time.time() - t0, 'after import matplotlib')

    rcParams = matplotlib.rcParams
    print(rcParams)
    rcParamlist = [
                   'backend',
                   'figure.figsize',
                   'figure.dpi',
                   'savefig.dpi',
                   'savefig.directory',
                   'font.size',
                   'image.cmap',
                   'lines.markersize',
                   'lines.linewidth',
                   'lines.marker',
                   'lines.markeredgewidth',
                   'scatter.marker']
    print()
    print('Matplotlib Defaults:')
    for rcParam in rcParamlist:
        print(rcParam, matplotlib.rcParams[rcParam])

    # keep 4:3 ratio like (6.4, 4.8)
    matplotlib.rcParams['figure.figsize'] = (8.0, 6.0)
    key = input("Enter any key to continue: ")

    import time
    datestamp = time.strftime("%Y%m%d")

    args = getargs()
    debug = args.debug
    any = args.any
    markersize = args.markersize
    radio = args.radio
    classify = args.classify

    if args.configfile is None:
        configfile = 'plot_history.cfg'
    config = getconfig(configfile=configfile, debug=True)

    filename_quasar = config.get('INPUTS', 'filename_quasar')
    filename_quasar_optical = config.get('INPUTS', 'filename_quasar_optical')
    filename_quasar_radio = config.get('INPUTS', 'filename_quasar_radio')
    filename_galaxy = config.get('INPUTS', 'filename_galaxy')
    filename_grb = config.get('INPUTS', 'filename_grb')
    filename_any = config.get('INPUTS', 'filename_any')

    plotdir = config.get('OUTPUTS', 'plotdir')
    if plotdir is not None:
        if not os.path.exists(plotdir):
            os.makedirs(plotdir)

    # Next implement
    # filename_any = config.get('INPUTS', 'filename_any')

    year_min = args.year_min
    year_max = args.year_max

    title = 'Redshift Record History'
    if year_max is not None:
       title = 'Redshift History: ' + str(year_max)

    # could be float
    if year_max is None:
        year_max = 2020
    year_max = int(year_max)

    # could be set in config
    year_xmin = args.year_xmin
    year_xmax = args.year_xmax

    redshift_ymax = args.redshift_ymax

    print(year_xmin)
    print(year_xmax)

    plot_history(filename_quasar=filename_quasar,
                 filename_quasar_optical=filename_quasar_optical,
                 filename_quasar_radio=filename_quasar_radio,
                 filename_galaxy=filename_galaxy,
                 filename_grb=filename_grb,
                 filename_any=filename_any,
                 any=any,
                 galaxy=True,
                 grb=True,
                 radio=radio,
                 classify=classify,
                 title=title,
                 year_max=year_max,
                 year_xmax=year_xmax,
                 redshift_ymax=redshift_ymax,
                 plotdir=plotdir,
                 markersize=markersize)

    plotfile_prefix = 'highestz_history_'
    if any:
        plotfile_prefix = 'highestz_history_any_'
    plotfile = plotfile_prefix + datestamp + '.png'
    if year_max is not None:
            plotfile = plotfile_prefix + str(int(year_max)) + \
                       '_' + datestamp + '.png'
    if plotdir is not None:
        plotfile = plotdir + plotfile
    print('Saving:', plotfile)
    plt.savefig(plotfile)

    print('Matplotlib Defaults:')
    for rcParam in rcParamlist:
        print(rcParam, matplotlib.rcParams[rcParam])

    plt.show()
