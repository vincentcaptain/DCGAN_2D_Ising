from pylab import *
from scipy.optimize import curve_fit

rij=[0.000000,1.000000,2.000000,3.000000,4.000000,5.000000,6.000000,1.414214,3.605551,5.385165,4.472136,2.828427,5.656854,4.123106,6.708204,4.242641,5.830952,7.071068,3.162278,6.082763,7.810250,6.403124,7.211103,8.485281,6.324555,2.236068,5.099020]
cij19=[0.170584,0.065938,0.040010,0.026947,0.019816,0.020737,0.015827,0.051204,0.030052,0.024706,0.028456,0.034771,0.025683,0.025869,0.023487,0.026153,0.029298,0.024597,0.029712,0.021087,0.018121,0.028178,0.023020,0.007740,0.021997,0.039305,0.021840]
cij20=[0.187159,0.059650,0.030747,0.019544,0.018265,0.017036,0.010096,0.040295,0.023059,0.018741,0.022388,0.026402,0.022109,0.019127,0.016317,0.028518,0.017589,0.006544,0.019220,0.012455,0.014141,0.017013,0.015018,0.018702,0.015776,0.026893,0.013047]
cij21=[0.245399,0.077552,0.028969,0.011280,0.002121,0.008559,0.007409,0.047654,0.009626,0.010640,0.010943,0.018523,0.008824,0.005675,0.009236,0.008375,0.006925,0.007304,0.009508,0.017203,0.004172,0.005825,0.004221,0.003087,0.016577,0.022909,0.007626]
cij22=[0.404182,0.161538,0.083360,0.041387,0.028371,0.013199,0.017632,0.112569,0.033772,0.013816,0.021106,0.048855,0.006652,0.023235,0.006695,0.024277,0.006910,0.012452,0.039533,0.011603,0.012550,-0.002475,0.013916,-0.013467,0.013262,0.067180,0.021361]
cij23=[0.960847,0.642701,0.516975,0.460269,0.428453,0.414455,0.401569,0.565521,0.444647,0.408484,0.426945,0.464023,0.409465,0.430363,0.401550,0.433087,0.408870,0.403262,0.451688,0.399075,0.393715,0.411636,0.410256,0.370466,0.409061,0.493734,0.410530]
cij24=[0.995144,0.607593,0.446882,0.377535,0.339658,0.307047,0.280945,0.498894,0.336102,0.287309,0.315479,0.367337,0.287969,0.335275,0.252829,0.315869,0.277434,0.279197,0.362403,0.278794,0.240366,0.281430,0.245635,0.234807,0.259013,0.413574,0.314402]
cij25=[0.998449,0.568760,0.407966,0.316889,0.258237,0.226098,0.206204,0.466328,0.256512,0.194488,0.218388,0.308058,0.183335,0.245948,0.186701,0.233044,0.187582,0.190758,0.293614,0.185718,0.145793,0.167083,0.144391,0.143667,0.199154,0.365978,0.216082]

def func(x, a, b):
	return a*exp(-b*x);


popt19,pcov19= curve_fit(func,array(rij),array(cij19))
popt20,pcov20= curve_fit(func,array(rij),array(cij20))
popt21,pcov21= curve_fit(func,array(rij),array(cij21))
popt22,pcov22= curve_fit(func,array(rij),array(cij22))
popt23,pcov23= curve_fit(func,array(rij),array(cij23))
popt24,pcov24= curve_fit(func,array(rij),array(cij24))
popt25,pcov25= curve_fit(func,array(rij),array(cij25))
plot(linspace(0,9,50), func(linspace(0,9,50),*popt19), '-',linspace(0,9,50), func(linspace(0,9,50),*popt20), '-',linspace(0,9,50), func(linspace(0,9,50),*popt21), '-',linspace(0,9,50), func(linspace(0,9,50),*popt22), '-',linspace(0,9,50), func(linspace(0,9,50),*popt23), '-',linspace(0,9,50), func(linspace(0,9,50),*popt24), '-',linspace(0,9,50), func(linspace(0,9,50),*popt25), '-',)

show()