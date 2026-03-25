{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "name": "Lever.ipynb",
      "authorship_tag": "ABX9TyMigeZiqG9CHyeU4A4d16el",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/dmechkova-dev/blank-app/blob/main/Lever.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "v43AiuFG8D0x"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "iuK0HTup7_TM"
      },
      "outputs": [],
      "source": [
        "import streamlit as st\n",
        "\n",
        "st.set_page_config(page_title=\"Физика за 6. клас\", layout=\"wide\")\n",
        "\n",
        "st.title(\"🧪 Виртуална лаборатория: Лост и Макара\")\n",
        "st.write(\"Добре дошли! Тук ще научите как работят простите механизми.\")\n",
        "\n",
        "tab1, tab2 = st.tabs([\"🏗️ Двустранен Лост\", \"⚙️ Макари\"])\n",
        "\n",
        "# --- ТАБ 1: ЛОСТ ---\n",
        "with tab1:\n",
        "    st.header(\"Правило за равновесие на лоста\")\n",
        "    st.info(\"Формула: $F_1 \\cdot d_1 = F_2 \\cdot d_2$\")\n",
        "\n",
        "    col1, col2 = st.columns(2)\n",
        "\n",
        "    with col1:\n",
        "        st.subheader(\"Лява страна\")\n",
        "        f1 = st.slider(\"Сила $F_1$ (Нютони)\", 1, 100, 50)\n",
        "        d1 = st.slider(\"Рамо $d_1$ (метра)\", 0.1, 5.0, 2.0)\n",
        "        moment1 = f1 * d1\n",
        "\n",
        "    with col2:\n",
        "        st.subheader(\"Дясна страна\")\n",
        "        f2 = st.slider(\"Сила $F_2$ (Нютони)\", 1, 100, 50)\n",
        "        d2 = st.slider(\"Рамо $d_2$ (метра)\", 0.1, 5.0, 2.0)\n",
        "        moment2 = f2 * d2\n",
        "\n",
        "    st.divider()\n",
        "\n",
        "    # Проверка за равновесие\n",
        "    diff = abs(moment1 - moment2)\n",
        "    if diff < 0.5:\n",
        "        st.success(f\"✅ Лостът е в равновесие! ({moment1:.1f} Nm = {moment2:.1f} Nm)\")\n",
        "    else:\n",
        "        st.error(f\"❌ Лостът не е в равновесие! Разлика: {diff:.1f} Nm\")\n",
        "        if moment1 > moment2:\n",
        "            st.warning(\"⬅️ Лявата страна натежава.\")\n",
        "        else:\n",
        "            st.warning(\"➡️ Дясната страна натежава.\")\n",
        "\n",
        "# --- ТАБ 2: МАКАРИ ---\n",
        "with tab2:\n",
        "    st.header(\"Видове макари\")\n",
        "\n",
        "    mode = st.radio(\"Избери вид макара:\", [\"Неподвижна макара\", \"Подвижна макара\"])\n",
        "\n",
        "    weight = st.number_input(\"Тежест на товара (Нютони):\", min_value=1, value=10)\n",
        "\n",
        "    if mode == \"Неподвижна макара\":\n",
        "        st.subheader(\"📍 Неподвижна макара\")\n",
        "        st.write(\"**Резултат:** Печелим само **удобство** (променяме посоката на силата).\")\n",
        "        st.metric(label=\"Необходима сила (F)\", value=f\"{weight} N\")\n",
        "        st.write(\"⚠️ Тук не печелим сила: $F = P$\")\n",
        "\n",
        "    else:\n",
        "        st.subheader(\"🏗️ Подвижна макара\")\n",
        "        st.write(\"**Резултат:** Печелим **сила** два пъти!\")\n",
        "        st.metric(label=\"Необходима сила (F)\", value=f\"{weight / 2} N\")\n",
        "        st.write(\"✅ Формула: $F = \\\\frac{P}{2}$\")\n",
        "        st.info(\"Забележка: Тук губим от пътя (трябва да изтеглим двойно повече въже).\")"
      ]
    }
  ]
}
