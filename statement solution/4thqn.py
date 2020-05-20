st = 'Print every word in this sentence that has an even number of letters'

st = st.split(" ")

for word in st:
    if len(word) % 2 == 0:
        print(f'{word} : even!')
        # print("even!")