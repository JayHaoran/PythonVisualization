def _plot_bubble_chart(bubble_x: (pd.Series, list, tuple),
bubble_y: (pd.Series, list, tuple),
                         bubble_size: (pd.Series, list, tuple),
                         bubble_text: (pd.Series, list, tuple),
                         x_label: str,
                         y_label: str,
                         title: str,
                         pic_file: str,
                         size_mag=1,
                         y_lim=None):
      """
      绘制气泡图
      :param bubble_x: 气泡的x轴位置
      :param bubble_y: 气泡的y轴位置
      :param bubble_size: 气泡大小
      :param bubble_text: 气泡文本
      :param x_label:
      :param y_label:
      :param title:
      :param pic_file:
      :param size_mag:
      :param y_lim:
      :return:
      """
