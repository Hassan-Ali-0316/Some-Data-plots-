from matplotlib import pyplot as plt

# Data as provided in the question
data = """
1950    543,979,233    357,021,100    -186,958,133    1.76    2.19
1955    603,320,147    398,577,992    -204,742,155    2.24    2.25
1960    654,170,692    445,954,579    -208,216,113    -0.04    2.30
1965    723,846,349    500,114,346    -223,732,003    2.68    2.17
1970    822,534,450    557,501,301    -265,033,149    2.61    2.22
1975    915,124,661    623,524,219    -291,600,442    1.60    2.22
1980    982,372,466    696,828,385    -285,544,081    1.47    2.28
1985    1,060,239,979    780,242,084    -279,997,895    1.57    2.24
1990    1,153,704,252    870,452,165    -283,252,087    1.72    2.12
1995    1,218,144,426    964,279,129    -253,865,297    0.86    1.97
2000    1,264,099,069    1,059,633,675    -204,465,394    0.71    1.82
2005    1,304,887,562    1,154,638,713    -150,248,849    0.62    1.56
2010    1,348,191,368    1,240,613,620    -107,577,748    0.67    1.38
2015    1,393,715,448    1,322,866,505    -70,848,943    0.56    1.17
2020    1,424,929,781    1,396,387,127    -28,542,654    0.13    0.92
2021    1,425,893,465    1,407,563,842    -18,329,623    0.00    0.68
"""

# Initialize empty lists for each column
years = []
china_population = []
india_population = []
india_china_difference = []
china_growth_rate = []
india_growth_rate = []

# Process the data
for line in data.strip().split('\n'):
    parts = line.split()
    years.append(int(parts[0]))
    china_population.append(int(parts[1].replace(',', '')))
    india_population.append(int(parts[2].replace(',', '')))
    india_china_difference.append(int(parts[3].replace(',', '')))
    china_growth_rate.append(float(parts[4]))
    india_growth_rate.append(float(parts[5]))


plt.xkcd()
plt.style.use('ggplot')
plt.plot(years,china_population,'--r',marker = 'o',linewidth = '3')
plt.plot(years,india_population,'-.g',linewidth = '4')


plt.xlabel('year')
plt.ylabel('population in billions')
plt.title("Population of china vs india")
plt.legend(['CHINA','INDIA'])
plt.tight_layout()

plt.grid(True)
plt.show()