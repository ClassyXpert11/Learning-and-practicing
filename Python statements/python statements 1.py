st = "Print only the words that start with s in this sentence"

print(st.split())

for wordsthatstartwithS in st:
  if st == "s":
    st.pop("start")

