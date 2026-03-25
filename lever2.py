import streamlit as st

st.set_page_config(page_title="Физика 6. клас: Прости механизми", layout="centered")

st.title("🧪 Виртуална лаборатория по Физика")
st.write("Изследвайте законите на лоста и макарите интерактивно!")

tab1, tab2 = st.tabs(["🏗️ Интерактивен Лост", "⚙️ Макари (Подвижна и Неподвижна)"])

# --- ТАБ 1: ЛОСТ ---
with tab1:
    st.header("Закон на лоста")
    st.info("Правило: Лостът е в равновесие, когато $F_1 \cdot d_1 = F_2 \cdot d_2$")
    
    c1, c2 = st.columns(2)
    with c1:
        f1 = st.number_input("Тежест $F_1$ (Н)", 10, 200, 100, step=10, key="f1")
        d1 = st.slider("Разстояние $d_1$ (м)", 0.5, 4.5, 2.0, step=0.5, key="d1")
    with c2:
        f2 = st.number_input("Тежест $F_2$ (Н)", 10, 200, 100, step=10, key="f2")
        d2 = st.slider("Разстояние $d_2$ (м)", 0.5, 4.5, 2.0, step=0.5, key="d2")

    moment1, moment2 = f1 * d1, f2 * d2
    balanced = abs(moment1 - moment2) < 0.1
    tilt = 0 if balanced else (-10 if moment1 > moment2 else 10)

    # Визуализация на лоста с линийка
    lever_html = f"""
    <div style="text-align: center; margin-top: 30px; font-family: sans-serif;">
        <div style="position: relative; height: 160px; display: flex; align-items: flex-end; justify-content: center;">
            <div style="transform: rotate({tilt}deg); transition: all 0.6s; width: 90%; height: 10px; background: #444; position: relative; border-radius: 5px; border-bottom: 2px dashed #ccc;">
                <div style="position: absolute; width: 100%; top: 12px; display: flex; justify-content: space-between; font-size: 10px; color: #888;">
                    <span>4.5m</span><span>3m</span><span>1.5m</span><span>0</span><span>1.5m</span><span>3m</span><span>4.5m</span>
                </div>
                <div style="position: absolute; left: {50 - d1*10}%; bottom: 10px; transform: translateX(-50%); width: {30+f1/10}px; height: {30+f1/10}px; background: #007bff; color: white; border-radius: 4px; display: flex; align-items: center; justify-content: center; font-size: 12px;">{f1}N</div>
                <div style="position: absolute; left: {50 + d2*10}%; bottom: 10px; transform: translateX(-50%); width: {30+f2/10}px; height: {30+f2/10}px; background: #ff4b4b; color: white; border-radius: 4px; display: flex; align-items: center; justify-content: center; font-size: 12px;">{f2}N</div>
            </div>
        </div>
        <div style="width: 0; height: 0; border-left: 20px solid transparent; border-right: 20px solid transparent; border-bottom: 40px solid #333; margin: 0 auto; margin-top: -2px;"></div>
    </div>
    """
    st.components.v1.html(lever_html, height=220)
    
    if st.button("⚖️ Провери равновесието"):
        if balanced: st.success(f"✅ Равновесие! {moment1} Nm = {moment2} Nm"); st.balloons()
        else: st.error(f"❌ Няма равновесие! {moment1} Nm ≠ {moment2} Nm")

# --- ТАБ 2: МАКАРИ ---
with tab2:
    st.header("Видове макари")
    type_m = st.radio("Избери механизъм:", ["Неподвижна макара", "Подвижна макара"])
    p_load = st.number_input("Товар P (Нютони):", 20, 500, 100, step=20)

    if type_m == "Неподвижна макара":
        f_needed = p_load
        desc = "Печелим само **удобство** (посока). Силата е равна на товара: $F = P$"
        color = "#555"
        y_pos = "20px" # Въжето е фиксирано горе
    else:
        f_needed = p_load / 2
        desc = "Печелим **сила 2 пъти**! Но губим 2 пъти от пътя: $F = P/2$"
        color = "#28a745"
        y_pos = "60px" # Макарата "слиза" надолу

    st.write(desc)
    st.metric("Необходима сила (F)", f"{f_needed} N", delta=f"{f_needed - p_load} N спестени" if type_m == "Подвижна макара" else None)

    # Визуализация на макара (SVG)
    pulley_svg = f"""
    <div style="text-align: center; background: #f9f9f9; padding: 20px; border-radius: 10px;">
        <svg width="200" height="250" viewBox="0 0 200 250">
            <line x1="20" y1="10" x2="180" y2="10" stroke="black" stroke-width="4" />
            
            {"<circle cx='100' cy='60' r='30' stroke='black' stroke-width='3' fill='none' /> <line x1='70' y1='60' x2='70' y2='180' stroke='blue' stroke-width='2' /> <rect x='50' y='180' width='40' height='40' fill='gray' /> <text x='60' y='205' fill='white' font-size='12'>{p_load}N</text> <line x1='130' y1='60' x2='130' y2='150' stroke='red' stroke-width='2' /> <text x='140' y='140' fill='red'>F={f_needed}N</text>" 
            if type_m == "Неподвижна макара" else 
            "<line x1='70' y1='10' x2='70' y2='120' stroke='blue' stroke-width='2' /> <circle cx='100' cy='120' r='30' stroke='black' stroke-width='3' fill='none' /> <rect x='80' y='150' width='40' height='40' fill='gray' /> <text x='90' y='175' fill='white' font-size='12'>{p_load}N</text> <line x1='130' y1='120' x2='130' y2='10' stroke='red' stroke-width='2' /> <text x='140' y='40' fill='red'>F={f_needed}N</text>"}
        </svg>
    </div>
    """
    st.components.v1.html(pulley_svg, height=300)
