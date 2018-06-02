# tìm thứ trong tuần của một ngày bất kì
# https://en.wikipedia.org/wiki/Zeller%27s_congruence

day_in_week = ['Sat', 'Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri']
month = [0,13,14,3,4,5,6,7,8,9,10,11,12]

def zeller(d, m, y):
	K = y % 100
	J = int(y/100)
	t = d + int(13*(month[m] + 1) / 5) + K + int(K/4) + int(J/4) -2*J
	return day_in_week[t % 7]

print(zeller(1,3,2016))