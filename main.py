import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

#タイトルを追加
st.title('Streamlit 超入門')

#テキストの追加
st.write('DataFrame')

# #データフレームを追加
# ##write(df)でもできるけど、dataframeの方が拡張性が良い
# df = pd.DataFrame({
#     '1列目':[1,2,3,4],
#     '2列目':[10,20,30,40]
#     })
# st.dataframe(df,width=100,height=100)
# #動的なテーブル
# st.dataframe(df.style.highlight_max(axis=0))
# #静的なテーブル
# st.table(df.style.highlight_max(axis=0))

#マークダウンを書く
"""
# 章
## 節
### 項
```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""

# #折れ線グラフを書く
# df = pd.DataFrame(
#     np.random.rand(20,3),
#     columns=['a','b','c']
#     )
# st.line_chart(df)
# #エリアチャート
# st.area_chart(df)
# #棒グラフ
# st.bar_chart(df)

# #マップを作成
# df = pd.DataFrame(
#     np.random.rand(100,2)/[50,50] + [35.69,139.70],
#     columns=['lat','lon']
#     )
# st.map(df)

# #画像を表示
# img = Image.open('plus.png')
# st.image(img,caption = 'Sample_img',use_column_width = True)

#チェックボックス
if st.checkbox('Show Image'):
    img = Image.open('plus.png')
    st.image(img,caption = 'Sample_img',use_column_width = True)

# #セレクトボックス
# option = st.selectbox(
#     'あなたが好きな数字を教えてください',
#     list(range(1,10))
# )
# 'あなたの好きな数字は、',option,'です'

# #テキストインプット
# text = st.text_input('あなたの趣味を教えてください')
# 'あなたの趣味：',text

# #スライダー
# condition = st.slider('あなたの今の調子は',0,100,50)
# 'コンディション：',condition

# #テキストインプット
# text = st.sidebar.text_input('あなたの趣味を教えてください')
# 'あなたの趣味：',text

# #スライダー
# condition = st.sidebar.slider('あなたの今の調子は',0,100,50)
# 'コンディション：',condition

#カラムの設定
left_column,right_column = st.columns(2)
button = left_column.button("右カラムに文字を表示")
if button:
    right_column.write("ここは右カラム")

#エクスパンダー
expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')

latest_iteration = st.empty()
bar = st.progress(0)

#プログレスバー
for i in range(100):
    latest_iteration.text(f'Iteration: {i+1} ')
    bar.progress(i + 1)
    time.sleep(0.1)
