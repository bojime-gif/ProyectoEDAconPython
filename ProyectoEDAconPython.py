# Importamos pandas y numpy

import pandas as pd
import numpy as np

pd.set_option("display.max_columns", None)

# ======================================

# Cargamos el primer csv

url = "https://raw.githubusercontent.com/bojime-gif/ProyectoEDAconPython/refs/heads/main/bank-additional.csv"
bank_additional = pd.read_csv(url, index_col=0)

# Aseguramos que se ha cargado correctamente
bank_additional.head()



# ======================================

# Vamos a ver la información general sobre el DataFrame. (Nulos o datos faltantes y tipo de los datos)

bank_additional.info()


# ======================================

# Me llama la atención la cantidad de valores Nulos que tenemos especialmente en las columnas de age y default. Vamos a revisar la suma total de cada uno y sacamos el porcentaje para ver qué hacemos con esos datos

bank_additional.isnull().sum()
nulos_porcentaje = (bank_additional.isnull().mean() * 100).round(2)
print(nulos_porcentaje)

# ======================================

# Procedo a eliminar todos los datos nulos en una nueva variable para no perder los datos originales en caso de que necesitemos recuperarlos en algun momento

bank_additional_limpio = bank_additional.dropna()

# Comparamos el tamaño original con el nuevo
print("Tamaño original:", bank_additional.shape)
print("Tamaño tras eliminar TODOS los nulos:", bank_additional_limpio.shape)

# Comprobamos que ya no disponemos de datos nulos en nuestro nuevo df

bank_additional_limpio.info()


# ======================================

# Procedemos a repetir el mismo proceso para el segundo archivo, cargamos el archivo y procedemos a combinar las tres hojas

url_2 = "https://raw.githubusercontent.com/bojime-gif/ProyectoEDAconPython/refs/heads/main/customer-details.xlsx"
xls = pd.ExcelFile(url_2)

# Mostramos los nombres de las hojas disponibles (deberían ser '2012', '2013', '2014')
print("Hojas encontradas en el Excel:", xls.sheet_names)

# Leemos cada hoja en una lista de DataFrames y las unimos todas en una sola
lista_dfs = [pd.read_excel(url_2, sheet_name=sheet) for sheet in xls.sheet_names]
df_customers = pd.concat(lista_dfs, ignore_index=True)

# Comprobamos el resultado
df_customers.head()

# ======================================

# Vamos a ver la información general sobre el DataFrame. (Nulos o datos faltantes y tipo de los datos)

df_customers.info()

# No hay datos nulos, pero identifico que la columna "Unnamed: 0" no nos aporta ningun datos relevante, asi que vamos a eliminarla

df_customers.drop("Unnamed: 0", axis=1, inplace=True)
df_customers.head()

# ======================================

# Una vez hemos realizado la limpieza de datos, vamos a proceder a cruzar los DFs puesto que comparten un identificador comun (id)

df_master = pd.merge(bank_additional_limpio, df_customers, left_on="id_", right_on="ID", how="inner")
df_master.head()

# ======================================

# Ahora que tenemos el DF ya combinado, me he dado cuenta que disponemos de dos columnas (latitude y longitude), que no nos aportan nada. De hecho, no están ni recogidas en el enunciado de la práctica, por lo que vamos a eliminarlas y trabajar sobre un DF mas limpio

df_master.drop("latitude", axis=1, inplace=True)
df_master.drop("longitude", axis=1, inplace=True)
df_master.head()

# ======================================

# Comenzamos con el analisis descriptivo de los datos, vamos a empezar viendo las métricas numéricas estándar

df_master.describe().T

# ======================================

# Vamos a ver ahora el resumen estadístico de las variables tipo texto

descripcion_categorias = df_master.describe(include=["object"]).T
print(descripcion_categorias)

# ======================================

# Además me gustaría ver los porcentajes de distribución de las categorías principales:

print('\n--- Distribución porcentual de las variables clave ---')
for col in ['job', 'marital', 'education', 'contact', 'poutcome', 'y']:
  if col in df_master.columns:
    print(f'\nVariable: {col}')
    print(df_master[col].value_counts(normalize=True) * 100)

# ======================================

# Una vez realizado el análisis descriptivo de los datos, vamos a la parte de visualización. Para ello, vamos a importar matplotlib y seaborn 

import os
import matplotlib.pyplot as plt
import seaborn as sns

# ======================================

# Configuramos el estilo visual de los gráficos
sns.set_theme(style='whitegrid')
plt.rcParams['figure.figsize'] = (10, 6)

# ======================================

# Creamos la carpeta 'graficos' automáticamente si no existe
os.makedirs('graficos', exist_ok=True)

# ======================================

# --- GRÁFICO 1: Histograma de la Edad de los Clientes ---
plt.figure(figsize=(9, 5))
sns.histplot(df_master['age'], bins=25, kde=True, color='teal')
plt.title('Distribución de la Edad de los Clientes', fontsize=14, weight='bold')
plt.xlabel('Edad', fontsize=12)
plt.ylabel('Frecuencia', fontsize=12)
plt.savefig('graficos/distribucion_edad.png', bbox_inches='tight')
plt.close()

# ======================================

# --- GRÁFICO 2: Duración de la llamada vs Suscripción (y) ---
plt.figure(figsize=(9, 5))
sns.boxplot(x='y', y='duration', data=df_master, palette='Set2')
plt.title(
    'Duración de la Interacción según Éxito de la Campaña (Suscripción y)',
    fontsize=14,
    weight='bold',
)
plt.xlabel('¿Suscrito al Depósito? (y)', fontsize=12)
plt.ylabel('Duración de la llamada (segundos)', fontsize=12)
plt.savefig('graficos/duracion_vs_suscripcion.png', bbox_inches='tight')
plt.close()

# ======================================

# --- GRÁFICO 3: Matriz de Correlación de Variables Numéricas ---
plt.figure(figsize=(10, 8))
num_cols = df_master.select_dtypes(include=[np.number])
corr_matrix = num_cols.corr()

sns.heatmap(
    corr_matrix, annot=False, cmap='coolwarm', linewidths=0.5, cbar=True
)
plt.title('Matriz de Correlación Numérica', fontsize=14, weight='bold')
plt.savefig('graficos/matriz_correlacion.png', bbox_inches='tight')
plt.close()

# ======================================

# --- GRÁFICO 4: Éxito de la campaña vs tipo de trabajo ---

plt.figure(figsize=(12, 6))
sns.countplot(y='job', hue='y', data=df_master, palette='viridis')
plt.title('Tasa de Aceptación por Ocupación (Job)', fontsize=14, weight='bold')
plt.xlabel('Cantidad de Clientes', fontsize=12)
plt.ylabel('Ocupación', fontsize=12)
plt.savefig('graficos/job_vs_suscripcion.png', bbox_inches='tight')
plt.close()

# ======================================

# --- GRÁFICO 5: Tasa de conversión según el canal de contacto ---

plt.figure(figsize=(8, 5))
sns.countplot(x='contact', hue='y', data=df_master, palette='Set1')
plt.title('Efectividad según el Canal de Contacto', fontsize=14, weight='bold')
plt.xlabel('Canal de Contacto', fontsize=12)
plt.ylabel('Cantidad de Clientes', fontsize=12)
plt.savefig('graficos/contacto_vs_suscripcion.png', bbox_inches='tight')
plt.close()

# ======================================

# --- GRÁFICO 6: Relación entre Income y Suscripcion (y) ---

plt.figure(figsize=(8, 5))
sns.boxplot(x='y', y='Income', data=df_master, palette='Set2')
plt.title('Distribución de Ingresos según la Suscripción (y)', fontsize=14, weight='bold')
plt.xlabel('¿Suscrito al Depósito? (y)', fontsize=12)
plt.ylabel('Nivel de Ingresos (Income)', fontsize=12)
plt.savefig('graficos/income_vs_y.png', bbox_inches='tight')
plt.close()

# ======================================

# --- GRÁFICO 7: Relación entre Visitas Web y Suscripcion (y) ---

plt.figure(figsize=(8, 5))
sns.boxplot(x='y', y='NumWebVisitsMonth', data=df_master, palette='Pastel1')
plt.title('Visitas Web Mensuales según la Suscripción (y)', fontsize=14, weight='bold')
plt.xlabel('¿Suscrito al Depósito? (y)', fontsize=12)
plt.ylabel('Visitas Web al Mes', fontsize=12)
plt.savefig('graficos/webvisits_vs_y.png', bbox_inches='tight')
plt.close()

# ======================================

