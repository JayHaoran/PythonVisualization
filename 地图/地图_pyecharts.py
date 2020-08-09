def draw_map(city: str,
             sub_cities: (list, tuple, set),
             value_lst: (list, tuple, set), 
             map_title: str,
             pic_path: str)
  """
  绘制指定地区的地图热力图
  :param city: 指定地区，用于地图api选择使用指定地区地图作为底图
  :param sub_cities: 指定地区的下属地区序列
  :param value_lst: 下属地区值序列，与sub_cities长度相同且一一对应
  :param map_title: 标题
  :param pic_path: 图片保存路径
  """
  
  # 用于对数据分段，不同段使用不同颜色，可根据需要进行调整
  # 若使用连续方式，则不需要pieces和pieces_color的指定
  pieces = [{'max': 30, 'min': 6, 'label': '6-'}, {'max': 5, 'min': 4, 'label': '4~5'},
            {'max': 3, 'min': 3, 'label': '3'}, {'max': 2, 'min': 2, 'label': '2'},
            {'max': 1, 'min': 1, 'label': '1'}]
  pieces_color = ["#e0f2c7", "#8cbf64", "#ffe8c7", "#ff9d43", "#b01818"]
  map_type = city
  
  if len(cities) != len(value_lst):
    raise ValueError(f"cities, value_lst 长度不同cities: {len(cities)}, rank：{len(value_lst)}")
  else:
    maps = Map(map_title, width=500, height=500)
    maps.add("", sub_cities, value_lst, maptype=map_type, is_visualmap=True, visual_range=[0, 30],
             is_label_show=Ture, # 是否显示地区标签（默认显示） 
             visual_text_color='#000', 
             is_piecewise=True,  # 使用分段展示
             label_text_size=13,
             title_text_size=13, is_map_symbol_show=False, is_geo_effect_show=False, is_xaxis_inverse=True,
             is_yaxis_inverse=False, name_map=new_name_dict, visual_range_color=pieces_color, pieces=pieces)
    maps.render(pic_path)
