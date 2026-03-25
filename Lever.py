import streamlit as st

st.set_page_config(page_title="Физика за 6. клас", layout="wide")

st.title("🧪 Виртуална лаборатория: Лост и Макара")
st.write("Добре дошли! Тук ще научите как работят простите механизми.")

tab1, tab2 = st.tabs(["🏗️ Двустранен Лост", "⚙️ Макари"])

# --- ТАБ 1: ЛОСТ ---
with tab1:
    st.header("Правило за равновесие на лоста")
    st.info("Формула: $F_1 \cdot d_1 = F_2 \cdot d_2$")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Лява страна")
        f1 = st.slider("Сила $F_1$ (Нютони)", 1, 100, 50)
        d1 = st.slider("Рамо $d_1$ (метра)", 0.1, 5.0, 2.0)
        moment1 = f1 * d1

    with col2:
        st.subheader("Дясна страна")
        f2 = st.slider("Сила $F_2$ (Нютони)", 1, 100, 50)
        d2 = st.slider("Рамо $d_2$ (метра)", 0.1, 5.0, 2.0)
        moment2 = f2 * d2

    st.divider()

    # Проверка за равновесие
    diff = abs(moment1 - moment2)
    if diff < 0.5:
        st.success(f"✅ Лостът е в равновесие! ({moment1:.1f} Nm = {moment2:.1f} Nm)")
    else:
        st.error(f"❌ Лостът не е в равновесие! Разлика: {diff:.1f} Nm")
        if moment1 > moment2:
            st.warning("⬅️ Лявата страна натежава.")
        else:
            st.warning("➡️ Дясната страна натежава.")

# --- ТАБ 2: МАКАРИ ---
with tab2:
    st.header("Видове макари")

    mode = st.radio("Избери вид макара:", ["Неподвижна макара", "Подвижна макара"])

    weight = st.number_input("Тежест на товара (Нютони):", min_value=1, value=10)

    if mode == "Неподвижна макара":
        st.subheader("📍 Неподвижна макара")
        st.write("**Резултат:** Печелим само **удобство** (променяме посоката на силата).")
        st.metric(label="Необходима сила (F)", value=f"{weight} N")
        st.write("⚠️ Тук не печелим сила: $F = P$")

    else:
        st.subheader("🏗️ Подвижна макара")
        st.write("**Резултат:** Печелим **сила** два пъти!")
        st.metric(label="Необходима сила (F)", value=f"{weight / 2} N")
        st.write("✅ Формула: $F = \\frac{P}{2}$")
        st.info("Забележка: Тук губим от пътя (трябва да изтеглим двойно повече въже).")
