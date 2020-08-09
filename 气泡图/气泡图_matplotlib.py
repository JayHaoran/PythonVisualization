import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

def _plot_bubble_chart(bubble_x: (pd.Series, list, tuple),
                       bubble_y: (pd.Series, list, tuple),
                       bubble_size: (pd.Series, list, tuple),
                       bubble_text: (pd.Series, list, tuple),
                       x_label: str,
                       y_label: str,
                       title: str,
                       pic_file: str,
                       size_mag: (int, float)=1,
                       y_lim=None):
  """
  绘制气泡图
  :param bubble_x: 气泡的x轴位置
  :param bubble_y: 气泡的y轴位置
  :param bubble_size: 气泡大小
  :param bubble_text: 气泡注释
  :param x_label: x轴标签
  :param y_label: y轴标签
  :param title: 标题
  :param pic_file: 图片保存路径
  :param size_mag: 气泡的放大倍数，默认是1
  :param y_lim: y轴范围，默认使用自动范围，若顶端气泡无法完全展示则需要自定义y轴范围
  :return: None
  """
  fig, ax = plt.subplots(figsize=(12, 6))
  x_min, y_min = bubble_x.min(), bubble_y.min()
  
  ax.scatter(bubble_x, bubble_y, s=bubble_size*size_mag, color="#ED7D31", alpha=0.6)
  
  if y_lim is not None:
    ax.set_ylim(y_lim)
  
  ax.set_title(title, fontsize=20)
  ax.set_xlabel(x_label, fontsize=12, position=(0.98, 0.2), rotation='horizontal')
  ax.set_ylabel(y_label, fontsize=12, position=(0, 0.93), rotation='horizontal')
  ax.spines["top"].set_visible(False)
  ax.spines["right"].set_visible(False)
  
  # x轴与y轴位置的调整
  if x_min < 0:
    ax.spines['bottom'].set_position(('data', 0))
  if y_min < 0:
    ax.spines['left'].set_position(('data', 0))
  
  # 设置气泡注释
  for i, j, z in zip(bubble_x, bubble_y, bubble_text):
    if x_min < 0 or y_min < 0:
      ax.text(x=i-0.75, y=j-0.6, s=z, fontsize=14)
    else:
      ax.text(x=i-0.27, y=j-0.25, s=z, fontsize=14)
  
  fig.tight_layout()
  plt.savefig(pic_file, dpi=150, edgecolor="#D9D9D9", bbox_inches='tight')
