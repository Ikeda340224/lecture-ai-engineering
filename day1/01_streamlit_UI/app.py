import streamlit as st
import pandas as pd
import numpy as np
import time
st.title("BMI計算機")

st.sidebar.header("BMIと適正体重")
st.sidebar.info("身長と体重を入力してください。")

name = st.text_input("あなたの名前", "ゲスト")
st.write(f"こんにちは、{name}さん！")
st.write(f"身長と体重から{name}さんのBMIを計算します！")

height = st.number_input("身長 (cm)",value=170.0)
weight = st.number_input("体重 (kg)",value=60.0)

bmi = weight / ((height / 100) ** 2)
st.write(f"{name}さんのBMIは **{bmi:.2f}** です。") 

cor_weight = ((height / 100) ** 2)*22
st.write(f"{name}さんの適正体重は **{cor_weight:.2f}** です。")

# ============================================
# データ表示
# ============================================
st.header("肥満の判定基準について")
st.write(f"BMIの計算式は世界共通ですが、肥満の判定基準は国により異なります。")


# サンプルデータフレームを作成
df_jp = pd.DataFrame({
     'BMI値':['18.5未満', '18.5〜25未満', '25〜30未満', '30〜35未満', '35〜40未満', '40以上'],
     '判定': ['低体重(痩せ型)', '普通体重', '肥満(1度)', '肥満(2度)', '肥満(3度)', '肥満(4度)']
 })

df_who = pd.DataFrame({
     'BMI値':['16未満', '16.00〜16.99以下', '17.00〜18.49以下', '18.50〜24.99以下', '25.00〜29.99以下', '30.00〜34.99以下', '35.00〜39.99以下', '40.00以上'],
     '判定': ['痩せすぎ', '痩せ', '痩せぎみ', '普通体重', '前肥満', '肥満(1度)', '肥満(2度)', '肥満(3度)']
 })

# データフレーム表示
#st.subheader("データフレーム")
st.write(f'日本肥満学会の判定基準(成人)')
st.dataframe(df_jp, use_container_width=True)

st.write(f'世界保健機関(WHO)の判定基準')
st.dataframe(df_who, use_container_width=True)


st.subheader("参考文献")
st.write(f'『BMIと適正体重』:https://keisan.casio.jp/exec/system/1161228732')
