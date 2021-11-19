import streamlit as st
from sudachipy import tokenizer, dictionary

st.text_input("なんか文章を入力してくれぃ", key="value")

dic = dictionary.Dictionary(dict_type="full").create()

st.caption("検索システム内部ではこういう風に名刺だけ分割・抽出されるよ！")
is_noun = lambda x: x.part_of_speech()[0] == "名詞"
for morph in dic.tokenize(st.session_state.value, tokenizer.Tokenizer.SplitMode.C):
    if not is_noun(morph):
        continue
    st.write(morph.surface())
