import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager



st.title("🎮 CSGO 皮肤加仓盈亏平衡模拟器")

st.sidebar.header("输入参数")
buy_price_initial = st.sidebar.number_input("初始购买价 (元)", value=2000.0, step=10.0)
qty_initial = st.sidebar.number_input("初始数量", value=3, step=1)
buy_price_bottom = st.sidebar.number_input("加仓价格 (元)", value=580.0, step=10.0)
qty_bottom = st.sidebar.number_input("加仓数量", value=3, step=1)

# 计算总成本与盈亏平衡价
total_cost = qty_initial * buy_price_initial + qty_bottom * buy_price_bottom
total_qty = qty_initial + qty_bottom
break_even_price = total_cost / total_qty

st.write(f"### 📊 盈亏平衡价格：**{break_even_price:.2f} 元**")

# 绘制盈亏曲线
P_range = np.linspace(0, buy_price_initial * 2, 200)
profit = (P_range * total_qty) - total_cost

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(P_range, profit, label="总盈亏曲线", linewidth=2)
ax.axhline(0, color="gray", linestyle="--")
ax.axvline(break_even_price, color="red", linestyle="--", label=f"盈亏平衡点 = {break_even_price:.2f}元")
ax.set_xlabel("Market Price")
ax.set_ylabel("Revenue")
ax.set_title("Revenue-Price Plot")
ax.legend()
st.pyplot(fig)

st.markdown(f"""
💡 **解释：**
- 当前加仓后总成本：{total_cost:.0f} 元  
- 总持有数量：{total_qty} 个  
- 当皮肤市场价回升至 **{break_even_price:.2f} 元** 时，你整体盈亏平衡。
""")
