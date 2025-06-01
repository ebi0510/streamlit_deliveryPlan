import streamlit as st
import pandas as pd

st.title("プレゼント配送計画 🦌")

# ファイル形式を指定（複数種類可）して、ファイルをアップロードする。
uploaded_file = st.file_uploader("CSVファイルをアップロードしてください", type=["csv"])
if uploaded_file is None:
    st.write("ファイルがアップロードされていません")
    # これ以降の動作をストップさせる
    # 止めないと読み込みたいのに読み込めないよって感じになる
    st.stop()

# アップロードされたファイルを読み込む
# read_excelメソッドとかもある
data = pd.read_csv(uploaded_file)

# データの中身を表形式で表示する
st.dataframe(data)

# 国一覧を取得
# nuique()だと国の数が出せる
countries = data['area_jp'].unique()

# 複数選択できる
selected_countries = st.multiselect(
    '国を選んでください',
    options = countries
)

# selected_countriesで選んだ国のデータをfiltered_dataに格納
# isin()は該当のデータがTrueかFalseが返す（selected_countriesで日本を選んでたら、そのデータが日本であればTrueを返す）
# ここではarea_jpの中に日本（仮）含まれる行を探している
filtered_data = data[data['area_jp'].isin(selected_countries)]
# filtered_dataに格納された日本（仮）が含まれる全ての行のdelivered_countの合計値を出す
total_delivered_count = filtered_data["delivered_count"].sum()
# でっかく合計値を表示
st.metric("🎁 予定配達数", total_delivered_count)

