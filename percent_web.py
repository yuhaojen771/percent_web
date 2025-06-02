import streamlit as st

st.title("📊 百分比計算工具")

# 初始化 session_state
if "a" not in st.session_state:
    st.session_state.a = ""
if "b" not in st.session_state:
    st.session_state.b = ""
if "result" not in st.session_state:
    st.session_state.result = ""

# 輸入欄位（綁定 session_state）
st.session_state.a = st.text_input("數字 A", value=st.session_state.a, key="input_a")
st.session_state.b = st.text_input("數字 B", value=st.session_state.b, key="input_b")

# 計算
if st.button("計算百分比"):
    try:
        a_val = float(st.session_state.a)
        b_val = float(st.session_state.b)
        if b_val == 0:
            st.error("❌ 除數不能為 0")
        else:
            percentage = (a_val / b_val) * 100
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
            st.session_state.result = display
    except ValueError:
        st.error("❌ 請輸入正確數字")

# 顯示結果
if st.session_state.result:
    st.success("✅ 計算結果如下（可複製）：")
    st.code(f"{st.session_state.result} %", language='text')

# 清除按鈕
if st.button("🧹 清除所有欄位"):
    st.session_state.a = ""
    st.session_state.b = ""
    st.session_state.result = ""
    st.rerun()
