import streamlit as st
from sudachipy import tokenizer, dictionary

st.text_input("なんか文章を入力してくれぃ", key="value")

dic = dictionary.Dictionary(dict_type="full").create()
words = [m.surface() for m in dic.tokenize(st.session_state.value, tokenizer.Tokenizer.SplitMode.C)]

st.caption("検索システム内部ではこういう風に分割されるよ！")
for word in words:
    st.write(word)
