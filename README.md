# ProyectoEDAconPython
Este proyecto consiste en un Análisis Exploratorio de Datos (EDA) completo implementado en Python sobre un dataset de marketing bancario integrado a partir de dos fuentes independientes. El objetivo principal es identificar el perfil demográfico de los clientes, analizar su comportamiento comercial y determinar los factores clave que impactan en la tasa de conversión para la contratación de un depósito bancario a plazo fijo.

🛠️ Tecnologías y Librerías Utilizadas
Python 3.x
Pandas
NumPy
Matplotlib & Seaborn
Visual Studio Code (Entorno de desarrollo)

📂 Estructura del Proyecto
├── bank-additional.csv        # Dataset 1
├── customer-details.xlsx      # Dataset 2
├── ProyectoEDAconPython.py    # Script ejecutable de Python (EDA + Limpieza + Gráficos)
├── graficos/                  # Carpeta generada automáticamente con las imágenes
│   ├── distribucion_edad.png
│   ├── duracion_vs_suscripcion.png
│   ├── matriz_correlacion.png
│   ├── job_vs_suscripcion.png
│   ├── contacto_vs_suscripcion.png
│   ├── income_vs_y.png
│   └── webvisits_vs_y.png
├── InformeEDA.docx/  
└── README.md                  # Documentación del proyecto e informe final


🚀 Pasos Seguidos en el Desarrollo
1. Integración y Limpieza de Datos: Fusión (merge) de dos datasets mediante el identificador único en común (id). Eliminación de columnas no relevantes o irrelevantes para el análisis (Unnamed: 0, latitude, longitude). Tratamiento de valores perdidos/incompletos mediante dropna().

2. Análisis Estadístico Exploratorio: Evaluación de variables cuantitativas filtrando redundancias numéricas. Análisis de frecuencia en variables categóricas (job, marital, education, contact). Cálculo de la tasa de conversión global (12.74%) sobre la variable objetivo (y).

3. Generación Automatizada de Visualizaciones: Desarrollo de código modular en Python para guardar automáticamente los gráficos en la carpeta /graficos.

📄 INFORME EXPLICATIVO DEL ANÁLISIS DE DATOS

1. Introducción y Objetivo del Proyecto

El presente proyecto realiza un Análisis Exploratorio de Datos (EDA) sobre una campaña de marketing telefónico de un grupo bancario. La finalidad es comprender en profundidad la base de clientes, evaluar la efectividad de las interacciones directas y extraer insights estratégicos para optimizar el retorno de inversión en futuras campañas.

2. Limpieza y Preparación de los Datos

Antes de iniciar el análisis estadístico y visual, se llevó a cabo un riguroso proceso de preprocesamiento, integración y limpieza del dataset:

Integración de fuentes de datos: Se combinaron ambos archivos de origen en un único conjunto de datos unificado (df_master), aprovechando que compartían un identificador común (id), lo que permitió consolidar toda la información demográfica, de comportamiento y de campaña de cada cliente en una sola estructura analítica.

Depuración de columnas: Se eliminaron variables redundantes o no correspondientes (tales como Unnamed: 0, latitude y longitude) para evitar sesgos y ruidos analíticos.

Gestión de valores nulos: Se trataron y limpiaron los registros incompletos (dropna()) para garantizar que todas las métricas estadísticas se calcularan sobre datos consistentes y fiables.

3. Análisis Descriptivo (Numérico y Categórico)

El análisis cuantitativo y cualitativo inicial permitió caracterizar la base de clientes:

Estadística Numérica: Mediante el estudio de las métricas clave (como la edad, la duración de las interacciones y métricas financieras/digitales), se identificaron los rangos operativos habituales de la base de datos.

Estadística Categórica y Tasa de Conversión Global:

Se analizaron distribuciones de variables cualitativas como la ocupación (job), estado civil (marital), nivel educativo (education) y canal de contacto (contact).

Métrica Clave de Conversión: El análisis de la variable objetivo (y) reveló una tasa de conversión global del 12.74%, lo que indica que un 12.74% de los clientes contactados aceptaron finalmente el depósito bancario frente a un 87.25% que lo rechazó. Esto subraya la necesidad de enfocar los esfuerzos comerciales en perfiles altamente cualificados.

4. Análisis Visual y Hallazgos Clave

Distribución de la Edad (distribucion_edad.png):

Se observa que la mayor concentración de clientes se sitúa en la franja de población adulta en edad laboral activa (30 a 50 años), decreciendo drásticamente en los extremos (jóvenes y personas de edad avanzada), lo que delimita el núcleo demográfico principal de la entidad.

Duración de la Interacción vs. Suscripción (duracion_vs_suscripcion.png):

Este es uno de los indicadores más determinantes. El diagrama de caja demuestra que los clientes que aceptan el depósito (yes) registran duraciones de llamada significativamente superiores a los que lo rechazan (no). Las llamadas cortas rara vez fructifican, evidenciando que una explicación comercial detallada y de calidad incrementa exponencialmente las probabilidades de éxito.

Éxito por Tipo de Ocupación y Canal de Contacto (job_vs_suscripcion.png & contacto_vs_suscripcion.png):

Aunque colectivos masivos (como administrativos o trabajadores de cuello azul) concentran el mayor volumen de llamadas, ciertos segmentos específicos muestran tasas de conversión relativas muy interesantes. Asimismo, el canal de contacto digital/móvil demuestra diferencias notables en la accesibilidad y predisposición del cliente frente al teléfono fijo tradicional.

Matriz de Correlación Numérica (matriz_correlacion.png):

Permitió analizar de forma global las relaciones lineales entre las distintas variables cuantitativas del conjunto de datos. El mapa de calor ayudó a descartar multicolinealidades indeseadas entre los factores numéricos y a identificar qué métricas guardan mayor vinculación matemática dentro del perfil del cliente y de la interacción.

Relación entre el Nivel de Ingresos y la Suscripción (income_vs_y.png):

Permitió evaluar si el poder adquisitivo del cliente influye de forma directa en su propensión a contratar el depósito a plazo fijo. Este análisis facilita la identificación de los tramos de ingresos con mayor capacidad de ahorro, ayudando a perfilar futuras estrategias comerciales hacia segmentos con mayor potencial de inversión.

Relación entre las Visitas Web y la Suscripción (webvisits_vs_y.png):

Analizó el impacto de la actividad digital previa del usuario (a través de sus visitas mensuales a la web corporativa) sobre el éxito de la campaña telefónica. Permite observar si los clientes con mayor familiaridad digital muestran un comportamiento o tasa de conversión diferenciada frente a aquellos usuarios con menor interacción online.

5. Conclusiones y Recomendaciones de Negocio

Optimización del tiempo comercial: Dado que la duración de la llamada es directamente proporcional al éxito de la venta, se recomienda dotar a los agentes de mejores argumentos de valor y guiones que prolonguen de forma constructiva las interacciones con potencial de conversión.

Segmentación estratégica: En lugar de realizar campañas masivas e indiscriminadas, los resultados sugieren enfocar los recursos hacia los rangos de edad, actividad digital y perfiles profesionales que estadísticamente arrojan una mayor propensión a la contratación.

Eficiencia operativa: La baja tasa de conversión global (12.74%) refuerza la urgencia de priorizar los leads más cualificados detectados en este EDA, reduciendo costes operativos en llamadas improductivas.
