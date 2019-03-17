pro plot_history,png=png
;+
; Plot the history of the progression of higher redshifts
; for galaxies and quasars
;
;-



; file containing the quasar records
filename='highestz_quasars_history.dat'
format='f,f,a'
print,'reading: ',filename
; read in the records independent of technique
readcol,filename,year,redshift,type,format=format,SKIPLINE=5,numline=21
print,'Number of points read in: ',n_elements(year)
print,'year(0): ',year(0)
print,'year(n_elements(year)-1): ',year(n_elements(year)-1)

nrecord=21
nradio_rec=12

pause

; now plot the data
!x.style=1
!y.style=1
!p.thick=2
!x.thick=2
!y.thick=2
!p.charthick=2

xdata=year
ydata=redshift
plot,xdata,ydata,psym=3,xrange=[1960.0,2010.0],yrange=[0.0,8.0], $
  /nodata,color=fsc_color('black'),background=fsc_color('white'), $
  charsize=1.5,title='History',xtitle='Year',ytitle='Redshift(z)'
plotid

oplot,xdata,ydata,psym=3,linestyle=2
oplot,xdata,ydata,linestyle=2,color=fsc_color('black')

xdata=year[0:10]
ydata=redshift[0:10]
plot_psym,xdata,ydata,117,symsize=2.0,color=fsc_color('blue')


xdata=year[11:20]
ydata=redshift[11:20]
plot_psym,xdata,ydata,117,symsize=2.0,color=fsc_color('red')

pause
; Read in the highest radio selected
format='f,f,a'
readcol,filename,year,redshift,type,format=format,SKIPLINE=30,numline=15
print,n_elements(year)
print,year(0)
print,year(n_elements(year)-1)

xdata=year[11:13]
ydata=redshift[11:13]
plot_psym,xdata,ydata,117,symsize=2.0,color=fsc_color('blue')

pause
; Read in the highest optically selected
format='f,f,a'
readcol,filename,year,redshift,type,format=format,SKIPLINE=46,numline=15
print,n_elements(year)
print,year(0)
print,year(n_elements(year)-1)

xdata=year
ydata=redshift
plot_psym,xdata,ydata,117,symsize=2.0,color=fsc_color('red')

; file containing the galaxy records
filename='highestz_galaxies_history.dat'
format='f,f,a'
print,'reading: ',filename
; read in the records independent of technique
readcol,filename,year,redshift,type,format=format,SKIPLINE=5,numline=21
print,'Number of points read in: ',n_elements(year)
print,'year(0): ',year(0)
print,'year(n_elements(year)-1): ',year(n_elements(year)-1)

xdata=year
ydata=redshift
oplot,xdata,ydata,psym=3,linestyle=2,color=fsc_color('green')
oplot,xdata,ydata,linestyle=2,color=fsc_color('green')
plot_psym,xdata,ydata,117,symsize=2.0,color=fsc_color('green')


plot_psym,1965.0,5.0,117,symsize=2.0,color=fsc_color('green')
plot_psym,1965.0,6.0,117,symsize=2.0,color=fsc_color('red')
plot_psym,1965.0,7.0,117,symsize=2.0,color=fsc_color('blue')



snapshot=tvrd(true=1)
write_png,'file.png',snapshot

end
