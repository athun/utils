#!/usr/bin/env python3

def display(field):

	"""
	tableStyle = [
		[unicode("┌─┬─┐",'utf8')],
		[unicode("│ │ │",'utf8')],
		[unicode("├─┼─┤",'utf8')],
		[unicode("│ │ │",'utf8')],
		[unicode("└─┴─┘",'utf8')],
	]
	"""
	
	tableStyle=[
		["╔","═","╦","═","╗"],
		["║"," ","║"," ","║"],
		["╠","═","╬","═","╣"],
		["║"," ","║"," ","║"],
		["╚","═","╩","═","╝"],
	]

	tableStyleExample=[
		["┌","─","┬","─","┐"],
		["│"," ","║"," ","│"],
		["├","─","┼","─","┤"],
		["║"," ","║"," ","║"],
		["└","─","┴","─","┘"],
	]

	rows=[]
	chrs = []


	for row in field:
		rows.append(len(row))
		for c in row:
			chrs.append(len(c))
	fdomain=len(field)
	frange=max(rows)

	for row in field:
		while len(row)<frange:
			row.append(" ")


	xpadding = 1
	a=""
	a=a+tableStyle[0][0] + (frange-1)*((2*xpadding+max(chrs))*tableStyle[0][1]+tableStyle[0][2]) + (2*xpadding+max(chrs))*tableStyle[0][1] + tableStyle[0][-1] + "\n"
	#   corner             except the last, print "═╦" as much as appropriate                      finally ═══ ...                         corner
	for x in range(fdomain):
		for y in range(frange):
			#print("(%s,%s)"%(x,y))
			n = field[x][y]
			if y< frange - 1:
				a=a+tableStyle[1][0]+xpadding*" "+n+((max(chrs)-len(n)) + xpadding)*" "
			else:
				a=a+tableStyle[1][0]+xpadding*" "+n+((max(chrs)-len(n)) + xpadding)*" " + tableStyle[1][-1] +"\n"
		
		if x<fdomain - 1:
			#a=a+"╠" + (frange-1)*((2*xpadding+max(chrs))*"═"+"╬") + (2*xpadding+max(chrs))*"═" + "╣\n"
			a=a+tableStyle[2][0]+(frange-1)*((2*xpadding+max(chrs))*tableStyle[2][1]+tableStyle[2][2])+(2*xpadding+max(chrs))*tableStyle[2][1]+tableStyle[2][-1]+"\n"





	#a=a+"╚" + (frange-1)*((2*xpadding+max(chrs))*"═"+"╩") + (2*xpadding+max(chrs))*"═" + "╝"
	a=a+tableStyle[-1][0] + (frange-1)*((2*xpadding+max(chrs))*tableStyle[-1][1]+tableStyle[-1][2]) + (2*xpadding+max(chrs))*tableStyle[-1][1] + tableStyle[-1][-1] + "\n"
	print(a)


if __name__=='__main__':
	f = [
		['o','o','x'],
		[' ','x',' '],
		['0','x',' ','alexander'],
	]
	print(f[1][1])
	display(f)