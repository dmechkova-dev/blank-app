import streamlit as st

st.set_page_config(page_title="Лаборатория: Лост", layout="centered")

st.title("🏗️ Интерактивен Лост")
st.write("Постави тежестите на различно разстояние от опорната точка и провери дали ще постигнеш равновесие!")

# --- Входни данни ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("Лява страна (Синя)")
    f1 = st.number_input("Тежест $F_1$ (Нютони)", min_value=10, max_value=200, value=100, step=10)
    d1 = st.number_input("Разстояние $d_1$ (метра)", min_value=0.5, max_value=5.0, value=2.0, step=0.5)

with col2:
    st.subheader("Дясна страна (Червена)")
    f2 = st.number_input("Тежест $F_2$ (Нютони)", min_value=10, max_value=200, value=100, step=10)
    d2 = st.number_input("Разстояние $d_2$ (метра)", min_value=0.5, max_value=5.0, value=1.0, step=0.5)

# Изчисления
moment1 = f1 * d1
moment2 = f2 * d2
balanced = abs(moment1 - moment2) < 0.1

# --- Визуализация на лоста ---
# Мащабираме разстоянието за чертежа (5 метра = 45% от ширината)
pos_left = 50 - (d1 * 9) 
pos_right = 50 + (d2 * 9)

# Логика за наклона
tilt = 0
if not balanced:
    tilt = -10 if moment1 > moment2 else 10

lever_style = f"""
<div style="text-align: center; margin-top: 50px; font-family: sans-serif;">
    <div style="position: relative; height: 150px; display: flex; align-items: flex-end; justify-content: center;">
        
        <div style="transform: rotate({tilt}deg); transition: all 0.6s ease-in-out; 
                    width: 90%; height: 12px; background: #444; position: relative; border-radius: 5px;">
            
            <div style="position: absolute; left: {pos_left}%; bottom: 12px; transform: translateX(-50%);
                        width: {30 + f1/10}px; height: {30 + f1/10}px; background: #007bff; 
                        color: white; display: flex; align-items: center; justify-content: center; 
                        border-radius: 5px; font-size: 12px; border: 2px solid #0056b3;">
                {f1}N
            </div>
            
            <div style="position: absolute; left: {pos_right}%; bottom: 12px; transform: translateX(-50%);
                        width: {30 + f2/10}px; height: {30 + f2/10}px; background: #ff4b4b; 
                        color: white; display: flex; align-items: center; justify-content: center; 
                        border-radius: 5px; font-size: 12px; border: 2px solid #b32d2d;">
                {f2}N
            </div>
            
            <div style="position: absolute; left: 50%; top: 0; width: 2px; height: 12px; background: white;"></div>
        </div>
    </div>
    
    <div style="width: 0; height: 0; border-left: 25px solid transparent; 
                border-right: 25px solid transparent; border-bottom: 50px solid #333; 
                margin: 0 auto; position: relative; z-index: -1; margin-top: -5px;">
    </div>
</div>
"""

st.components.v1.html(lever_style, height=250)

# --- Проверка ---
if st.button("⚖️ Провери равновесието"):
    if balanced:
        st.balloons()
        st.success(f"БРАВО! Лостът е в равновесие. ({moment1} Nm = {moment2} Nm)")
    else:
        st.error(f"Лостът ще се наклони! Ляв момент: {moment1} Nm | Десен момент: {moment2} Nm")
        st.info("Съвет: За равновесие трябва $F_1 \cdot d_1 = F_2 \cdot d_2$")

st.markdown("---")
st.caption("Използвайте контролите по-горе, за да променяте силата и позицията на тежестите.")
