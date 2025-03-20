st = 'I am learnig Python. hello, WORLD!'

one = st[:st.find('h')]
ind = st[st.find('h'): st.rfind('h') + 1]
two = st[st.rfind("h") + 1:]

print(one + ind[::-1] + two)

# I am learnig Python. hello, WORLD!
