# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd

def load_and_select_data():
    data_df = pd.read_csv('./Empleados.csv')
    data_df = data_df[['DNI','Sexo','FechaNacimiento','Estudios','Oficina','Responsable','NivelIngles','CosteMesAnterior',
                       'tipo_incorporacion','parent_company','seniority','HorasSemanales','Situacion']]
    return(data_df)

Empleados = load_and_select_data()