def plot_multi_line_bar_chart(data: pd.DataFrame,
                              x_index: str,
                              bar_col: str,
                              line_col: str
                              bar_value_col: str,
                              line_value_col: str
                              bars_color: (tuple, list, set), 
                              lines_colors: (tuple, list, set), 
                              bar_y_label: str, 
                              line_y_label: str, 
                              title: str, 
                              pic_file: str):
    """
    使用matplotlib绘制多系列柱+线组合图
    :param data: 原数据
    :param x_index: data中用于指定x轴的字段名
    :param bar_col: 多系列柱状图的分类字段
    :param line_col: 多系列折线图的分类字段
    :param bar_value_col: 多系列柱状图的值字段
    :param line_value_col: 多系列折线图的值字段
    :param bars_colors: 
    :param lines_colors:
    :param bar_y_label:
    :param line_y_label:
    :param title:
    :param pic_file:
    :return:
    """
    bar_data = pd.crosstab(data[x_index], data[bar_col], values=ele_df[bar_value_col], aggfunc=np.sum)
    line_data = pd.crosstab(data[x_index], data[line_col], values=ele_df[line_value_col], aggfunc=np.sum)
    labels = list(bars_data.index)
    x = np.arange(len(labels))  # the label locations
    width = 0.2  # the width of the bars
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # 画柱状图
    bars = []
    for i, se_i, c in zip([-1, 0, 1], bars_data.columns, bars_colors):
        cs = [c] * len(x)
        bars.append(ax.bar(x + width / 0.9 * i, bars_data[se_i], width, label=se_i, color=cs))
    ax.set_ylabel(bar_y_label, fontsize=14)
    ax.set_xlabel(self.trans_time_level[self.time_level], fontsize=14)
    ax.set_title(title, fontsize=20)
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=14)
    ax.grid(axis='y', linestyle='--')
    
    # 画折线图图
    ax2 = ax.twinx()
    ax2.set_ylabel(line_y_label, fontsize=14)
    lines = []
    for se_i, c in zip(lines_data.columns, lines_colors):
        lines.append(ax2.plot(x, lines_data[se_i], marker='o', color=c, linewidth=3))
        # 给折线图设置数值标签
        data_se_i = lines_data[se_i].dropna()
        for a, b in zip(np.arange(len(data_se_i)), data_se_i):
            plt.text(a, b + 0.35, round(b, 1), ha='center', va='bottom', fontsize=14)

    
    # 图形设置：坐标轴显示、刻度设置、图例设置等
    for ax_i in [ax, ax2]:
        ax_i.spines["top"].set_visible(False)    # 去除上方框线
        ax_i.spines["right"].set_visible(False)  # 去除右侧框线
        ax_i.spines["left"].set_visible(False)   # 去除左侧框线
        ax_i.tick_params(axis='y', which='both', length=0)  # 保留刻度数值但删除刻度短线
        ax_i.legend(fontsize=12)
        ax_i.tick_params(labelsize=12)
    
    fig.tight_layout()
    plt.savefig(pic_file, dpi=150, edgecolor="#D9D9D9", bbox_inches='tight')
    
    
    
