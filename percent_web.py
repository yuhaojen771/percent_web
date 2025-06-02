import streamlit as st

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
            st.success("✅ 計算結果如下（可複製）：")
            st.code(f"{result} %", language='text')
    except ValueError:
        st.error("❌ 請輸入正確數字")

# 清除（用重新載入實作）
if st.button("🧹 清除所有欄位"):
    st.experimental_rerun()
