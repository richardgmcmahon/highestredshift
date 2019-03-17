
reproducing previous versions of redshift history plots:

Your can select the historical year and the year range to plot
on the x-axis separately.


optional arguments:
  -h, --help            show this help message and exit
  --any                 Plot independent of classification (default: False)
  --quasar              Plot quasar history (default: False)
  --radio               Identify radio selected objects (default: False)
  --galaxy              Plot galaxy history (default: False)
  --classify            Identify class/type of source e.g. galaxy, quasar
                        (default: False)
  --year_min YEAR_MIN   Manimum year to plot (default: None)
  --year_max YEAR_MAX   Maximum year to plot (default: None)
  --year_xmin YEAR_XMIN
                        Minimum year for plot x-axis (default: 1955)
  --year_xmax YEAR_XMAX
                        Maximum year for plot x-axis (default: 2020)
  --redshift_ymax REDSHIFT_YMAX
                        Maximum redshuft for plot y-axis (default: 10.0)
  --markersize MARKERSIZE
                        Marker size (size as diameter as in plot) (default:
                        7.0)
  --plotdir PLOTDIR     Output/Result directory (default: None)
  --infile INFILE       Input file name (default: None)
  --configfile CONFIGFILE
                        configuration file (default: None)
  --debug               debug option (default: False)
  --verbose             verbose option (default: False)
  --version             verbose option (default: False)

WARNING: Not all options may be supported

examples

Epoch 1999 corresponding to launch of Chandra, XMM-Newton

python plot_history.py --any --markersize 10.0 --radio --class --year_max 1999 --year_xmax 2020 --redshift_ymax 10.0

python plot_history.py --any --markersize 10.0 --radio --class --year_max 2020 --year_xmax 2020 --redshift_ymax 10.0





Epoch 2005 which is when I first made a compilation and my plots used IDL

python plot_history.py --any --markersize 10.0 --radio --class --year_max 2005 --year_xmax 2010 --redshift_ymax 8.0
