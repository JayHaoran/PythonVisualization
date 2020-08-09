import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

def _plot_single_line_bar_chart(bar_data: pd.DataFrame,
                                line_data: pd.DataFrame,
                                x_index: str,
                                bar_value_col: str,
                                line_value_col: str,
                                bar_label: str,
                                line_label: str,
                                title: str,
                                bar_color: str,
                                line_color: str,
                                major_y_label: str,
                                miner_y_label: str,
                                pic_file: str):
    """
    绘制单系列柱+线组合图
    :param bar_data: 用于绘制柱状图的数据
    :param line_data: 用于绘制折线图的数据
    :param x_index: 指定x轴的字段名
    :param bar_value_col: 柱状图值字段
    :param line_value_col: 折线图值字段
    :param bar_label: 柱状图标签，用于绘制图例
    :param line_label: 折线图标签，用于绘制图例
    :param title: 标题
    :param bar_color: 柱状图颜色，可以是颜色缩写或颜色代码
    :param line_color: 折线图颜色，可以是颜色缩写或颜色代码
    :param major_y_label: 双y轴中主y轴的标签
    :param miner_y_label: 双y轴中副y轴的标签
    :param pic_file: 图片保存路径
    :return: None
    """
    fig, ax = plt.subplots(figsize=(12, 6))
    
    ax.bar(x=bar_data[x_index], height=bar_data[bar_value_col], label=bar_label, color=bar_color, alpha=0.8)
    ax.set_title(title, fontsize=20)
    ax.set_ylabel(major_y_label, fontsize=14)
    ax.grid(axis='y', linestyle='--')
    
    ax2 = ax.twinx()
    ax2.set_ylabel(miner_y_label, fontsize=14)
    ax2.plot(line_data[x_index], line_data[line_value_col], marker='o', color=line_color, linewidth=3, label=line_label)

    # 给折线图设置数值标签
    for a, b in zip(np.arange(len(line_data[x_index])), line_data[line_value_col]):
      plt.text(a, b + 0.35, round(b, 1), ha='center', va='bottom', fontsize=14)

    for ax_i, loc_i in zip([ax, ax2], ['upper left', 'upper right']):
      ax_i.spines["top"].set_visible(False) 
      ax_i.spines["right"].set_visible(False)
      ax_i.spines["left"].set_visible(False)
      ax_i.tick_params(axis='y', which='both', length=0)
      ax_i.legend(loc=loc_i, fontsize=12)
      ax_i.tick_params(labelsize=12)

    fig.tight_layout()
    plt.savefig(pic_file, dpi=150, edgecolor="#D9D9D9", bbox_inches='tight')
