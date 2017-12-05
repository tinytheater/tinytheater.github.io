import pandas as pd

data = pd.read_excel('input.xlsx')
headers = data.columns
committees = ['Board', 'Production', 'Marketing', 'Logistics', 'Outreach']

with open('a.txt', 'w') as f:

	for c in committees:
		f.write('<div class="header">\n')
		f.write('<h2 class="header__headline-typed">\n')
		f.write(c + "\n")
		f.write('</h2>')
		f.write('</div>')
		f.write('<div class="section">\n')
		f.write('<div class="container about-management">\n')
		last = 'xxx'
		j = 0
		for i in data.index:
			committee = data['committee'][i]
			if committee != c:
				continue
			name = data['name'][i]
			grade = data['grade'][i]
			major = data['major'][i]
			intro = data['intro'][i]

			if committee != last:
				j = 0
				if last != 'xxx':
					f.write('</div>')
				last = committee
			else:
				j += 1

			if j % 4 == 0:
				f.write('<div class="row">\n')
			f.write('<div class="col-sm-9 col-lg-6 col-xl-3 about-management__item">\n')
			f.write('<div data-parallax-type="card">\n')
			f.write('<img src="../img/about/%s.jpg">\n' % name)
			f.write('<div class="card about-management__card">\n')
			f.write('<h3 class="h2">\n')
			f.write(name + '\n')
			f.write('</h3>\n')
			f.write('<div>\n')
			f.write('年级：%s<br>\n' % grade)
			f.write('专业：%s<br>\n' % major)
			f.write(intro + '\n')
			f.write('</div>\n')
			f.write('</div>\n')
			f.write('</div>\n')
			f.write('</div>\n')
			if j % 4 == 3:
				f.write('</div>')
		f.write('</div>')
		f.write('</div>')

