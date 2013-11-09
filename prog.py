
# Use appconsole.myprint instead of print and
# input = yield appconsole.output() instead of raw_input()
from appconsole import myprint, printoutput

def prog_gen(namn=""):

    while True:
        myprint("Enter stock symbol below.")
        name = yield printoutput()
        myprint(display(name))
        myprint()

import urllib2
import math
"""
print '\nStock Checker by Rigel Marcinik \n'
print 'Type in any stock symbol and get some important data'
print 'Additionally an estimated return for next year'
print 'Data is estimated from reuters.com \n'
"""


def run():
	
	sym = raw_input('Stock Symbol: ')
	if 'exit' not in sym:
		display(sym)
		print 'Type "exit" to stop\n'

		run()
	

def display(sym):
	calc = ''
	try:
		calc = calculate(sym)
	except:
		print 'Stock Symbol is invalid, try again'
		prog_gen(namn='')
	
	
	
	a = '\nCompany: '+getname(sym)+'\n'
	b ='Price of share: '+getprice(sym)+'\n'
	c ='Number of Shares (mil): '+getshares(sym)+'\n'
	d ='\nSales in millions'+'\n'
	e ='This year: '+getsales(sym)+'\n'
	f ='Next Year: '+getsalesnext(sym)+'\n'
	g ='\nEarnings per share'+'\n'
	h ='This year mean: '+getepsmean(sym)+'\n'
	i ='Next year high: '+getepsnexthi(sym)+'\n'
	j ='Next year low: '+getepsnextlo(sym)+'\n'
	k ='\nESTIMATED RETURN '+calc+'\n'
	
	return a+b+c+d+e+f+g+h+i+j+k
#each get function reads an html page and returns specific data
#increasingly narrow find functions look for keywords and isolate the wanted data	
def getprice(sym):
	
	response = urllib2.urlopen('http://www.reuters.com/finance/stocks/overview?symbol='+sym)
	html = response.read()
	html = ''.join(html.split())
	startstring = html.find('<spanstyle="font-size:23px;">')
	
	start = html.find('>',startstring+1)+1
	end = html.find('<',start)
	
	return html[start:end]

def getshares(sym):
	
	response = urllib2.urlopen('http://www.reuters.com/finance/stocks/overview?symbol='+sym)
	html = response.read()
	startstring = html.find('Shares Outstanding')
	start = html.find('g>',startstring)
	start = start+2
	end = html.find('<',start)
	
	
	return html[start:end]
	
	
	
def getsales(sym):
	
	response = urllib2.urlopen('http://www.reuters.com/finance/stocks/financialHighlights?symbol='+sym)
	html = response.read()
	
	sales = html.find('SALES')
	currentyear = html.find('Year Ending')
	estimates = html.find('">', currentyear)
	
	start = html.find('">', estimates+1)
	start = start+2
	end = html.find('<',start)
	
	
	return html[start:end]
	
	
def getsalesnext(sym):
	response = urllib2.urlopen('http://www.reuters.com/finance/stocks/financialHighlights?symbol='+sym)
	html = response.read()
	
	sales = html.find('SALES')
	currentyear = html.find('Year Ending')
	nextyear = html.find('Year Ending', currentyear+1)
	estimates = html.find('">', nextyear+1)
	
	start = html.find('">', estimates+1)
	start = start+2
	end = html.find('<',start)
	
	
	return html[start:end]

def getepsmean(sym):
	response = urllib2.urlopen('http://www.reuters.com/finance/stocks/financialHighlights?symbol='+sym)
	html = response.read()
	earnings = html.find('EARNINGS')
	
	year = '<td>Year Ending'
	currentyear = html.find(year,earnings)
	estimates = html.find('">', currentyear)
	means = html.find('">',estimates+1)
	start = means+2
	
	
	end = html.find('<',start)
	
	
	return html[start:end]

def getepsnexthi(sym):
	response = urllib2.urlopen('http://www.reuters.com/finance/stocks/financialHighlights?symbol='+sym)
	html = response.read()
	earnings = html.find('EARNINGS')
	
	year = '<td>Year Ending'
	currentyear = html.find(year,earnings)
	nextyear = html.find(year,currentyear+1)
	estimates = html.find('">', nextyear)
	means = html.find('">',estimates+1)
	hi = html.find('">',means+1)
	
	start = hi+2
	
	
	end = html.find('<',start)
	
	
	return html[start:end]
	
def getepsnextlo(sym):
	response = urllib2.urlopen('http://www.reuters.com/finance/stocks/financialHighlights?symbol='+sym)
	html = response.read()
	earnings = html.find('EARNINGS')
	
	year = '<td>Year Ending'
	currentyear = html.find(year,earnings)
	nextyear = html.find(year,currentyear+1)
	estimates = html.find('">', nextyear)
	means = html.find('">',estimates+1)
	hi = html.find('">',means+1)
	lo = html.find('">',hi+1)
	
	start = lo+2
	
	end = html.find('<',start)
	
	
	return html[start:end]	
	
def getname(sym):

	response = urllib2.urlopen('http://www.reuters.com/finance/stocks/overview?symbol='+sym)
	html = response.read()
	startstring = html.find('<title>')
	start = html.find('>',startstring)
	start = start+1
	end = html.find('Quote',start)
	
	
	return html[start:end]
	
def calculate(sym):
	
	try:	
		M = float(getprice(sym).replace(',',''))
		N = float(getshares(sym).replace(',',''))
		O = float(getsales(sym).replace(',',''))
		P = float(getsalesnext(sym).replace(',',''))
		Q = float(getepsmean(sym).replace(',',''))
		R = float(getepsnexthi(sym).replace(',',''))
		S = float(getepsnextlo(sym).replace(',',''))
		
		
		W = O/N
		rs = [R,S]
		H = (1+((average(rs)-Q)/Q))**(1/1)-1
		U = std(rs)/average(rs)
		I = (1+((P-O)/O))**(1/1)-1
		
		
		Y = O/W
		Z = Q/W
		AK =M/W
		AL =M/Q
		AB =1-U
		
		
		X = P/Y
		AJ =math.sqrt(AB)*(H*100)+5
		AI =math.sqrt(Z)*3.25
		
		AC =AJ*Q
		AD =AI*W
		AF =AJ*S
		
		AA =average(rs)/X
		
		AH =math.sqrt(AA)*3.25
		
		AG =AH*X
		afag = [AF,AG]
		K = average(afag)
		AE =K*(1+H)**-1
		acadae = [AC,AD,AE]
		L = average(acadae)
		J = (M-L)/L
		
		AJ =math.sqrt(AB)*(H*100)+5
		G = (K-M)/M
		
		percent = (G*100)

		if percent > 50:
			return str('%.0f' %(percent))+'%  WOW!!!'
		elif percent > 12:
			return str('%.0f' %(percent))+'% Looks good!'
		elif percent > 1:
			return str('%.0f' %(percent))+'% Not bad'
		elif percent < -20:
			return str('%.0f' %(percent))+'% Eeeek!'
		elif percent < 1:
			return str('%.0f' %(percent))+'% Unadvisable'	
	except:
		print '>ERROR< Stock Symbol is invalid, try again'
		run()
		
def average(s): return sum(s) * 1.0 / len(s)

def std(s):
	
	variance = map(lambda x: (x - average(s))**2, s)
	return math.sqrt(average(variance))
	
	

