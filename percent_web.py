import streamlit as st
import pyperclip

st.title("📊 百分比計算工具")

# 輸入區
a = st.text_input("數字 A")
b = st.text_input("數字 B")

# 計算
result = ""
if st.button("計算百分比"):
    try:
        a_val = float(a)
        b_val = float(b)
        if b_val == 0:
            st.error("❌ 除數不能為 0")
        else:
            percentage = (a_val / b_val) * 100
            # 顯示格式
            if percentage.is_integer():
                display = f"{percentage:.1f}"
            else:
                first_decimal = int(percentage * 10) % 10
                second_decimal = int(percentage * 100) % 10
                if first_decimal == 0:
                    display = f"{percentage:.2f}"
                elif second_decimal == 0:
                    display = f"{percentage:.1f}"
                else:
                    display = f"{percentage:.2f}"
            result = display
            st.success(f"結果：{result} %")
    except ValueError:
        st.error("❌ 請輸入正確數字")

# 複製按鈕
if result and st.button("📋 複製結果"):
    pyperclip.copy(result)
    st.info("已複製到剪貼簿！")

# 清除
if st.button("🧹 清除"):
    st.experimental_rerun()
