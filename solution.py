import pandas as pd
import numpy as np


chat_id = 423200009 # Ваш chat ID, не меняйте название переменной

def solution(...) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    alpha = 0.03
    stat, p_value = stats.ttest_ind(x, y, alternative='two-sided')
    return ( p_value < alpha)
# Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    #return ... # Ваш ответ, True или False
