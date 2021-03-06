
Examples publications using this data are:

https://www.nature.com/articles/443128a

https://swift.gsfc.nasa.gov/results/releases/images/recordzs/

https://www.nature.com/articles/4611221a


Current spectroscopically confirmed 'record' holders:
```
Galaxy: z=9.110, MACS1149-JD1, Hashimoto et al, 2018Natur.557..392H
Quasar: z=7.51, ULASJ1342+0928, Banados et al, 2018Natur.553..473B
Gamma Ray Burst (GRB): z=8.23, GRB 090423, Salvaterra et al, 2009Natur.461.1258S; Tanvir et al., 2009Natur.461.1254T"
```

The highest redshifts at the end of 1999 were:
```
Galaxy: z=5.74; Hu, McMahon, Cowie, 1999ApJ...522L…9H 
Quasar: z=5.00; Fan et al, 1999AJ....118….1F
GRB: z=3.40; Kulkarni et al, 1998Natur.393…35K
```

Example plot: https://github.com/richardgmcmahon/highestredshift/blob/master/results/highestz_history_2020_20190317.png


![alt text](https://github.com/richardgmcmahon/highestredshift/blob/master/results/highestz_history_2020_20190317.png)

Producing redshift history plots for different epochs

Your can select the historical year and the year range to plot
on the x-axis separately.

```
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
```


examples

python plot_history.py 

python plot_history.py --any --markersize 10.0 --radio --class --year_max 1999 --year_xmax 2020 --redshift_ymax 10.0

Epoch 1999 corresponding to launch of Chandra, XMM-Newton

python plot_history.py --any --markersize 10.0 --radio --class --year_max 1999 --year_xmax 2020 --redshift_ymax 10.0

python plot_history.py --any --markersize 10.0 --radio --class --year_max 2020 --year_xmax 2020 --redshift_ymax 10.0





Epoch 2005 which is when I first made a compilation and my plots used IDL

python plot_history.py --any --markersize 10.0 --radio --class --year_max 2005 --year_xmax 2010 --redshift_ymax 8.0

