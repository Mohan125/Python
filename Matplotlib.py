import csv
import numpy as np
from collections import Counter
from matplotlib import pyplot as plt
with open('data.csv') as csv_file:
    csv_reader=csv.DictReader(csv_file)
    counter=Counter()
    line=next(csv_reader)
    for line in csv_reader:
        counter.update(line['LanguagesWorkedWith'].split(';'))
language = []
users = []
counter=counter.most_common(10)
for dash in counter:
    language.append(dash[0])
    users.append(dash[1])
language.reverse()
users.reverse()
plt.style.use('bmh')
plt.title('Most Popular Languages')
plt.ylabel('Language')
plt.grid('true')
plt.xlabel('No.of.Users')
plt.barh(language,users,color='r')
plt.show()
plt.savefig('Most_Popular_Languages')








