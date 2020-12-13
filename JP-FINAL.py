#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 12:12:28 2020

@author: jeanpierresalendres
"""

import pandas as pd
import numpy as np

#%% info covid

csv = '/Users/jeanpierresalendres/Downloads/covid_mexico.csv'


df = pd.read_csv(csv, encoding ='latin-1')


df['Date'] = df['Date'].str.replace('/', '.')

def covid_casos(ciudad):
    ciudades = ['MÉRIDA', 'PUERTO VALLARTA', 'CANCÚN', 'GUANAJUATO', 'LOS CABOS', 'ACAPULCO', 'SAN MIGUEL DE ALLENDE', 'CIUDAD DE MÉXICO', 'CHAPALA', 'PUERTO ESCONDIDO', 'TIJUANA', 'MAZATLÁN', 'PUERTO PEÑASCO', 'PUEBLA', 'OAXACA']                
    
    while ciudad not in ciudades:
            print("Please enter the city in capital letters and/or with accents") 
            ciudad = input("Please choose your destination: ")
            if ciudad in ciudades and not ciudad== 'CIUDAD DE MÉXICO':
                    casos = df.loc[(df['Municipality'])==ciudad, 'Active'].sum()
                    print("The number of active cases in", ciudad, "is:", casos)
                    break
            elif ciudad == 'CIUDAD DE MÉXICO':
                    casos1 = df.loc[(df['State'])==ciudad, 'Active'].sum()
                    print("The number of active cases in", ciudad, "is:", casos1)
                    break
            
    else: 
                if ciudad in ciudades and not ciudad== 'CIUDAD DE MÉXICO':
                    casos = df.loc[(df['Municipality'])==ciudad, 'Active'].sum()
                    print("The number of active cases in", ciudad, "is:", casos)
                elif ciudad == 'CIUDAD DE MÉXICO':
                    casos1 = df.loc[(df['State'])==ciudad, 'Active'].sum()
                    print("The number of active cases in", ciudad, "is:", casos1)

  
 
              
        
#%% info inseguridad


csv_seg = '/Users/jeanpierresalendres/Downloads/IDM_NM_oct2020.csv'

df_seg = pd.read_csv(csv_seg, encoding='latin-1')
  
def inseg_casos(ciudad,delito):
        ciudades_seg = ['Mérida', 'Puerto Vallarta', 'Cancún', 'Guanajuato', "Ciudad de México", 'Los Cabos', 'Acapulco de Juárez', 'San Miguel De Allende', 'Chapala', 'Puerto Escondido', 'Tijuana', 'Mazatlán', 'Puerto Peñasco', 'Puebla', 'Oaxaca de Juárez']
        delitos = ['Homicidio doloso', 'Secuestro', 'Robo a casa habitación', 'Robo a transeúnte en vía pública', 'Feminicidio', 'Violación simple', 'Acoso sexual']   

        while ciudad not in ciudades_seg or delito not in delitos:
            print("Please enter the correct city spelling and the correct crime") 
            ciudad = input("Please choose your destination: ")
            delito = input("Plese enter specific crime: ")
            if ciudad in ciudades_seg and delito in delitos and not ciudad == "Ciudad de México":
                municipios = pd.DataFrame(df_seg.loc[(df_seg['Entidad']== ciudad) & (df_seg['Subtipo de delito']== delito) & (df_seg['Año']>=2019)]).fillna(0)
                suma = municipios.iloc[:,9:21].sum().sum().astype(int)
                print("The number of cases of",delito,"in",ciudad,"is",suma)
                break
            elif ciudad == "Ciudad de México":
                cdmx = pd.DataFrame(df_seg.loc[(df_seg['Entidad']== 'Ciudad de México') & (df_seg['Subtipo de delito']== delito) & (df_seg['Año']>=2019)]).fillna(0)
                suma1 = cdmx.iloc[:,9:21].sum().sum().astype(int)
                print("The number of cases of",delito,"in",ciudad,"is",suma1)
        else:
            if ciudad in ciudades_seg and delito in delitos and not ciudad == "Ciudad de México":
                municipios = pd.DataFrame(df_seg.loc[(df_seg['Entidad']== ciudad) & (df_seg['Subtipo de delito']== delito) & (df_seg['Año']>=2019)]).fillna(0)
                suma = municipios.iloc[:,9:21].sum().sum().astype(int)
                print("The number of cases of",delito,"in",ciudad,"is",suma)
            elif ciudad == "Ciudad de México":
                cdmx = pd.DataFrame(df_seg.loc[(df_seg['Entidad']== 'Ciudad de México') & (df_seg['Subtipo de delito']== delito) & (df_seg['Año']>=2019)]).fillna(0)
                suma1 = cdmx.iloc[:,9:21].sum().sum().astype(int)
                print("The number of cases of",delito,"in",ciudad,"is",suma1)
                



        
       
        
        
        
#%% Code lines to check for spreadsheet summary statistics

df_seg.columns

df.isna().sum()

df_seg['Tipo de delito'].value_counts()

df_seg['Entidad'].value_counts()

df_seg['Año'].value_counts()

#%% RUN TO GET MEXICOME INFORMATION


input("Welcome to Mexicome! Press enter to continue: ")

ciudades = ['MÉRIDA', 'PUERTO VALLARTA', 'CANCÚN', 'GUANAJUATO', 'LOS CABOS', 'ACAPULCO', 'SAN MIGUEL DE ALLENDE', 'CHAPALA', 'PUERTO ESCONDIDO', 'TIJUANA', 'MAZATLÁN', 'PUERTO PEÑASCO', 'PUEBLA', 'OAXACA']

print("Top 15 destinations in Mexico:")

print(ciudades)
    
do_run = ''

while do_run != 'n':
    ciudad = input("Please choose your destination: ")
    print(ciudad)
    covid_casos(ciudad)
    do_run = input('Would you like to try another city for covid statistics? If no, then we will move on to crime statitics. PLEASE ENTER (y/n)')
    if do_run == 'n':
        print("Ok let's move on to crime statistics in your preferred city") 
        break

input("Press enter to continue for criminality information: ")

print("Top 15 destinations in Mexico:")

ciudades_seg = ['Mérida', 'Puerto Vallarta', 'Cancún', 'Guanajuato', 'Los Cabos', 'Acapulco de Juárez', 'San Miguel De Allende', 'Chapala', 'Puerto Escondido', 'Tijuana', 'Mazatlán', 'Puerto Peñasco', 'Puebla', 'Oaxaca de Juárez']

print(ciudades_seg)

do_run1 = ''
while do_run1 != 'n':
    ciudad = input("Please enter destination: ")
    print("List of crimes:")
    delito = ['Homicidio doloso', 'Secuestro', 'Robo a casa habitación', 'Robo a transeúnte en vía pública', 'Feminicidio', 'Violación simple', 'Acoso sexual']
    print(delito)
    delito = input("Plese enter specific crime: ")
    inseg_casos(ciudad, delito)
    do_run1 = input('Would you like to try another city for covid statistics? If no, then we will move on to crime statitics. PLEASE ENTER (y/n)')
    if do_run1 == 'n':
        print("Thank you for suing the Mexicome app. Wishing you healthy and safe holidays in Mexico!") 
        break
        



#%%
