import streamlit as st


st.set_page_config(page_title="Физика 6. клас", layout="wide")

# --- СТРАНИЧНА ЛЕНТА (SIDEBAR) ---
st.sidebar.title("📘 Указания")
st.sidebar.markdown("""
### Как да ползвате приложението:
1. **Лост:** Променяй тежестите и виж кога ще светне в зелено.
2. **Макари:** Избери вид макара, за да видиш как се печели сила.
3. **Тест:** Провери какво си научил!
---
**Формула за лост:**
$$F_1 \cdot d_1 = F_2 \cdot d_2$$
""")

st.title("🧪 Виртуална лаборатория по Физика")
# ... следва останалият код ...


st.set_page_config(page_title="Физика 6. клас: Прости механизми", layout="centered")

st.title("🧪 Виртуална лаборатория по Физика")
st.write("Изследвайте законите на лоста и макарите и проверете знанията си!")
# Обнови реда с табовете в началото:
tab1, tab2, tab3, tab4 = st.tabs(["🏗️ Интерактивен Лост", "⚙️ Макари", "📝 Тест за знания", "💡 Любопитно"])


# --- ТАБ 1: ЛОСТ ---
with tab1:
    st.header("Закон на лоста")
    st.info("Формула: $F_1 \cdot d_1 = F_2 \cdot d_2$")
    
    c1, c2 = st.columns(2)
    with c1:
        f1 = st.number_input("Тежест $F_1$ (Н)", 10, 200, 100, step=10, key="l_f1")
        d1 = st.slider("Разстояние $d_1$ (м)", 0.5, 4.5, 2.0, step=0.5, key="l_d1")
    with c2:
        f2 = st.number_input("Тежест $F_2$ (Н)", 10, 200, 100, step=10, key="l_f2")
        d2 = st.slider("Разстояние $d_2$ (м)", 0.5, 4.5, 2.0, step=0.5, key="l_d2")

    moment1, moment2 = f1 * d1, f2 * d2
    balanced = abs(moment1 - moment2) < 0.1
    tilt = 0 if balanced else (-10 if moment1 > moment2 else 10)

    lever_html = f"""
    <div style="text-align: center; margin-top: 30px; font-family: sans-serif;">
        <div style="position: relative; height: 160px; display: flex; align-items: flex-end; justify-content: center;">
            <div style="transform: rotate({tilt}deg); transition: all 0.6s; width: 90%; height: 10px; background: #444; position: relative; border-radius: 5px;">
                <div style="position: absolute; left: {50 - d1*10}%; bottom: 10px; transform: translateX(-50%); width: {30+f1/10}px; height: {30+f1/10}px; background: #007bff; color: white; border-radius: 4px; display: flex; align-items: center; justify-content: center; font-size: 12px;">{f1}N</div>
                <div style="position: absolute; left: {50 + d2*10}%; bottom: 10px; transform: translateX(-50%); width: {30+f2/10}px; height: {30+f2/10}px; background: #ff4b4b; color: white; border-radius: 4px; display: flex; align-items: center; justify-content: center; font-size: 12px;">{f2}N</div>
            </div>
        </div>
        <div style="width: 0; height: 0; border-left: 20px solid transparent; border-right: 20px solid transparent; border-bottom: 40px solid #333; margin: 0 auto; margin-top: -2px;"></div>
    </div>
    """
    st.components.v1.html(lever_html, height=200)
    
    if st.button("⚖️ Провери равновесието"):
        if balanced: st.success("✅ Равновесие!"); st.balloons()
        else: st.error("❌ Няма равновесие!")

# --- ТАБ 2: МАКАРИ ---
with tab2:
    st.header("Видове макари")
    type_m = st.radio("Избери механизъм:", ["Неподвижна макара", "Подвижна макара"])
    p_load = st.number_input("Товар P (Нютони):", 20, 500, 100, step=20)
    
    f_needed = p_load if type_m == "Неподвижна макара" else p_load / 2
    st.metric("Необходима сила (F)", f"{f_needed} N")
    
    st.write("*(Виж графичната симулация по-долу)*")
    # Тук може да се добави SVG кода от предишния ми отговор за визуализация

# --- ТАБ 3: ТЕСТ ---
# --- ТАБ 3: ТЕСТ ---
with tab3:
    st.header("📝 Тест по физика")
    st.write("Избери отговорите и натисни бутона най-отдолу, за да видиш резултата си.")
    
    # Речник с верните отговори
    correct_answers = {
        "q1": "Променяме посоката на силата за удобство",
        "q2": "2 пъти по-малка от F2",
        "q3": "2 пъти",
        "q4": 50,
        "q5": "Губим път (дърпаме двойно повече въже)",
        "q6": "Прости механизми"
    }

    # Въпросите
    q1 = st.radio("1. Кое е основното предимство на неподвижната макара?", 
                 ["Печелим сила 2 пъти", "Променяме посоката на силата за удобство", "Намаляваме триенето до нула"])
    
    q2 = st.radio("2. Ако лост е в равновесие и рамото d1 е 2 пъти по-голямо от d2, то силата F1 е:", 
                 ["2 пъти по-малка от F2", "2 пъти по-голяма от F2", "Равна на F2"])
    
    q3 = st.radio("3. Колко пъти печелим сила при използване на една подвижна макара?", 
                 ["Не печелим сила", "2 пъти", "4 пъти"])
    
    q4 = st.number_input("4. Изчисли: На лявото рамо на лост (2м) има товар 100N. Каква сила (N) е нужна на дясното рамо (4м) за равновесие?", min_value=0)
    
    q5 = st.radio("5. Какво се случва с 'пътя' при подвижната макара?", 
                 ["Печелим път", "Пътят остава същият", "Губим път (дърпаме двойно повече въже)"])
    
    q6 = st.selectbox("6. Лостът и макарата са видове:", 
                     ["Електрически уреди", "Прости механизми", "Топлинни двигатели"])

    if st.button("🏁 Предай теста"):
        score = 0
        st.divider()
        st.subheader("Резултати и обяснения:")

        # Функция за проверка и оцветяване
        def check_q(user_ans, correct_ans, explanation):
            if user_ans == correct_ans:
                st.success(f"✅ Правилно! {explanation}")
                return 1
            else:
                st.error(f"❌ Грешно! Верният отговор е: **{correct_ans}**")
                return 0

        # Изпълнение на проверката
        score += check_q(q1, correct_answers["q1"], "(Неподвижната макара само пренасочва силата).")
        score += check_q(q2, correct_answers["q2"], "(Колкото по-голямо е рамото, толкова по-малка сила е нужна).")
        score += check_q(q3, correct_answers["q3"], "(Подвижната макара разпределя товара на две въжета).")
        score += check_q(q4, correct_answers["q4"], f"(100 * 2 = {q4} * 4. Уравнението е вярно при 50N).")
        score += check_q(q5, correct_answers["q5"], "(Златно правило: Печелим сила, но губим път).")
        score += check_q(q6, correct_answers["q6"], "(Това са най-древните инструменти за улесняване на работата).")

        # Краен резултат
        st.divider()
        if score == 6:
            st.balloons()
            st.metric("Твоят резултат", f"{score}/6", "Отличен 6! 🎉")
        else:
            st.metric("Твоят резултат", f"{score}/6")

# --- ТАБ 4: ЛЮБОПИТНО ---
with tab4:
    st.header("Знаете ли, че...?")
    
    col_a, col_b = st.columns([1, 2])
    
    with col_a:
        st.image("https://upload.wikimedia.org/wikipedia/commons/2/20/Archimedes_lever.png", caption="Архимед повдига Земята")
    
    with col_b:
        st.subheader("🌍 Силата на Архимед")
        st.write("""
        Древногръцкият учен **Архимед** е бил толкова впечатлен от силата на лоста, че е казал:
        > *"Дайте ми опорна точка и достатъчно дълъг лост и ще повдигна Земята!"*
        
        Разбира се, за да повдигне Земята само с 1 сантиметър, на Архимед би му бил нужен лост с дължина квадрилиони километри!
        """)

    st.divider()

    st.subheader("🦴 Лостове в човешкото тяло")
    st.write("Нашите тела са пълни с лостове! Костите ни са лостовете, а ставите са опорните точки.")
    
    col_c, col_d = st.columns(2)
    
    with col_c:
        st.info("**🦵 Стъпалото:**")
        st.write("Когато се повдигате на пръсти, стъпалото ви действа като лост от втори род. Опорната точка са пръстите, а тежестта е цялото ви тяло!")
        
    with col_d:
        st.info("**💪 Ръката:**")
        st.write("Когато вдигате гиричка, лакътят е опорната точка, а мускулът (бицепсът) прилага силата. Това е лост от трети род.")

    st.success("🎯 **Физиката е навсякъде!** Следващият път, когато използвате ножица, клещи или дори когато дъвчете, се сетете, че използвате прост механизъм.")
