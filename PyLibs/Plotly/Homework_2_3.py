import plotly.graph_objects as go
import numpy as np
import pandas as pd

# Загрузка данных (предполагается, что data_stocks уже загружена)
# data_stocks = pd.read_csv(...)

# Создание интерактивного рисунка
fig = go.FigureWidget()

# График изменения цен акций (точки)
fig.add_scatter(
    x=data_stocks["date"],
    y=data_stocks["NFLX"],
    mode="markers",
    name="NFLX price",
    marker=dict(size=6, color='blue', symbol='circle')
)

# График изменения стоимости (столбцы)
fig.add_bar(
    x=data_stocks["date"],
    y=data_stocks["NFLX"].diff(),
    marker_color=np.where(data_stocks["NFLX"].diff() > 0, 'green', 'red'),
    marker_opacity=0.5,
    name="price difference"
)

# Добавляем названия
fig.update_layout(title="Netflix stock price", xaxis_title="date", yaxis_title="relative price")

# Вспомогательные функции для работы с маркерами
def get_num_of_markers(trace):
    if trace.x is not None:
        return len(trace.x)
    else:
        return len(trace.y)

def get_list_from_attr(trace, attr_name):
    attr = getattr(trace.marker, attr_name)
    if isinstance(attr, tuple):
        return list(attr)
    else:
        return [attr]*get_num_of_markers(trace)

def marker_update(**kwargs):
    def update(trace, points, state):
        for attr_key, attr_new_val in kwargs.items():
            new_attr = get_list_from_attr(trace, attr_key)
            for i in points.point_inds:
                new_attr[i] = attr_new_val
            setattr(trace.marker, attr_key, new_attr)
    return update

def marker_deselect(**kwargs):
    def deselect(trace, points):
        for attr_key, attr_new_val in kwargs.items():
            new_attr = get_list_from_attr(trace, attr_key)
            for i in points.point_inds:
                new_attr[i] = attr_new_val
            setattr(trace.marker, attr_key, new_attr)
    return deselect

# Настройка интерактивности для точек (первый график)
fig.data[0].on_hover(marker_update(size=15))
fig.data[0].on_unhover(marker_update(size=6))
fig.data[0].on_selection(marker_update(symbol='square'))
fig.data[0].on_deselection(marker_deselect(symbol='circle'))
fig.data[0].on_click(marker_update(color='yellow', symbol='star'))

# Настройка интерактивности для столбцов (второй график)
fig.data[1].on_selection(marker_update(opacity=1))
fig.data[1].on_click(marker_update(opacity=1))
fig.data[1].on_deselection(marker_deselect(opacity=0.5))

# Отображение графика
display(fig)