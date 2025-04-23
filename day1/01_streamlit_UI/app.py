import streamlit as st
import pandas as pd
import numpy as np
import time

# ============================================
# ページ設定
# ============================================
# st.set_page_config(
#     page_title="Streamlit デモ",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# ============================================
# タイトルと説明
# ============================================
st.title("BMI計算機")
#st.markdown("### コメントを解除しながらStreamlitの機能を学びましょう")
#st.markdown("このデモコードでは、コメントアウトされた部分を順番に解除しながらUIの変化を確認できます。")

# ============================================
# サイドバー 
# ============================================
st.sidebar.header("BMIと適正体重")
st.sidebar.info("身長と体重を入力してください。")

# ============================================
# 基本的なUI要素
# ============================================
#st.header("基本的なUI要素")

# テキスト入力
#st.subheader("テキスト入力")
name = st.text_input("あなたの名前", "ゲスト")
st.write(f"こんにちは、{name}さん！")
st.write(f"身長と体重から{name}さんのBMIを計算します！")

height = st.number_input("身長 (cm)",value=170.0)
weight = st.number_input("体重 (kg)",value=60.0)

bmi = weight / ((height / 100) ** 2)
st.write(f"{name}さんのBMIは **{bmi:.2f}** です。")  #ここの小数点の表示で手こずる

cor_weight = ((height / 100) ** 2)*22
st.write(f"{name}さんの適正体重は **{cor_weight:.2f}** です。")

# ============================================
# レイアウト
# ============================================
# st.header("レイアウト")


# タブ
# st.subheader("タブ")
# tab1, tab2 = st.tabs(["第1タブ", "第2タブ"])
# with tab1:
#     st.write("これは第1タブの内容です")
# with tab2:
#     st.write("これは第2タブの内容です")

# エクスパンダー
# st.subheader("エクスパンダー")
# with st.expander("詳細を表示"):
#     st.write("これはエクスパンダー内の隠れたコンテンツです")
#     st.code("print('Hello, Streamlit！')")

# ============================================
# データ表示
# ============================================
st.header("肥満の判定基準について")
st.write(f"BMIの計算式は世界共通ですが、肥満の判定基準は国により異なります。")


# サンプルデータフレームを作成
df_jp = pd.DataFrame({
     'BMI値':['18.5未満', '18.5〜25未満', '25〜30未満', '30〜35未満', '35〜40未満', '40以上'],
     '判定': ['低体重(痩せ型)', '普通体重', '肥満(1度)', '肥満(2度)', '肥満(3度)', '肥満(4度)']
     #左側のインデックスを消したかった
 })

df_who = pd.DataFrame({
     'BMI値':['16未満', '16.00〜16.99以下', '17.00〜18.49以下', '18.50〜24.99以下', '25.00〜29.99以下', '30.00〜34.99以下', '35.00〜39.99以下', '40.00以上'],
     '判定': ['痩せすぎ', '痩せ', '痩せぎみ', '普通体重', '前肥満', '肥満(1度)', '肥満(2度)', '肥満(3度)']
     #左側のインデックスを消したかった
 })

# データフレーム表示
#st.subheader("データフレーム")
st.write(f'日本肥満学会の判定基準(成人)')
st.dataframe(df_jp, use_container_width=True)

st.write(f'世界保健機関(WHO)の判定基準')
st.dataframe(df_who, use_container_width=True)


st.subheader("参考文献")
st.write(f'『BMIと適正体重』:https://keisan.casio.jp/exec/system/1161228732')






# テーブル表示
# st.subheader("テーブル")
# st.table(df)

# メトリクス表示
# st.subheader("メトリクス")
# col1, col2, col3 = st.columns(3)
# col1.metric("温度", "23°C", "1.5°C")
# col2.metric("湿度", "45%", "-5%")
# col3.metric("気圧", "1013hPa", "0.1hPa")

# ============================================
# グラフ表示
# ============================================
# st.header("グラフの表示")

# ラインチャート
# st.subheader("ラインチャート")
# chart_data = pd.DataFrame(
#     np.random.randn(20, 3),
#     columns=['A', 'B', 'C'])
# st.line_chart(chart_data)

# バーチャート
# st.subheader("バーチャート")
# chart_data = pd.DataFrame({
#     'カテゴリ': ['A', 'B', 'C', 'D'],
#     '値': [10, 25, 15, 30]
# }).set_index('カテゴリ')
# st.bar_chart(chart_data)

# ============================================
# インタラクティブ機能
# ============================================
# st.header("インタラクティブ機能")

# プログレスバー
# st.subheader("プログレスバー")
# progress = st.progress(0)
# if st.button("進捗をシミュレート"):
#     for i in range(101):
#         time.sleep(0.01)
#         progress.progress(i / 100)
#     st.balloons()

# ファイルアップロード
# st.subheader("ファイルアップロード")
# uploaded_file = st.file_uploader("ファイルをアップロード", type=["csv", "txt"])
# if uploaded_file is not None:
#     # ファイルのデータを表示
#     bytes_data = uploaded_file.getvalue()
#     st.write(f"ファイルサイズ: {len(bytes_data)} bytes")
#     
#     # CSVの場合はデータフレームとして読み込む
#     if uploaded_file.name.endswith('.csv'):
#         df = pd.read_csv(uploaded_file)
#         st.write("CSVデータのプレビュー:")
#         st.dataframe(df.head())

# ============================================
# カスタマイズ
# ============================================
# st.header("スタイルのカスタマイズ")

# カスタムCSS
# st.markdown("""
# <style>
# .big-font {
#     font-size:20px ！important;
#     font-weight: bold;
#     color: #0066cc;
# }
# </style>
# """, unsafe_allow_html=True)
# 
# st.markdown('<p class="big-font">これはカスタムCSSでスタイリングされたテキストです！</p>', unsafe_allow_html=True)

# ============================================
# デモの使用方法
# ============================================
#st.divider()
#st.subheader("このデモの使い方")
#st.markdown("""
#1. コードエディタでコメントアウトされた部分を見つけます（#で始まる行）
#2. 確認したい機能のコメントを解除します（先頭の#を削除）
#3. 変更を保存して、ブラウザで結果を確認します
#4. 様々な組み合わせを試して、UIがどのように変化するか確認しましょう
#""")

#st.code("""
# コメントアウトされた例:
# if st.button("クリックしてください"):
#     st.success("ボタンがクリックされました！")

# コメントを解除した例:
#if st.button("クリックしてください"):
#    st.success("ボタンがクリックされました！")
#""")