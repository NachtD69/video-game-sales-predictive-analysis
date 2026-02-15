# Video Game Sales Predictive Analysis

> Análisis predictivo de ventas de videojuegos para identificar proyectos prometedores y planificar campañas publicitarias

![Python](https://img.shields.io/badge/Python-3.9-blue)
![Pandas](https://img.shields.io/badge/Pandas-1.x-green)
![NumPy](https://img.shields.io/badge/NumPy-1.x-013243)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.x-orange)
![SciPy](https://img.shields.io/badge/SciPy-1.x-8CAAE6)
![Status](https://img.shields.io/badge/Status-Independent%20Project-brightgreen)

##  Descripción

Análisis de datos históricos de ventas globales de videojuegos para **Ice**, tienda online internacional. El objetivo es **identificar patrones de éxito** que permitan detectar proyectos prometedores y optimizar inversión publicitaria para 2017.

###  Logro destacado
**Proyecto completamente autónomo** - Desarrollado sin guías ni plantillas, aplicando lógica analítica profesional desde cero.

### Contexto de negocio
Ice necesita responder:
- ¿Qué hace que un juego tenga éxito?
- ¿Qué plataformas están en declive vs en ascenso?
- ¿Qué géneros generan más ventas?
- ¿Cómo varían las preferencias por región?
- ¿Las reseñas de expertos predicen ventas?
- ¿En qué proyectos invertir presupuesto publicitario 2017?

##  Objetivos del proyecto

1. **Exploración histórica** - Analizar tendencias de ventas desde orígenes hasta 2016
2. **Identificación de patrones** - Descubrir qué factores correlacionan con éxito
3. **Análisis por plataforma** - Detectar plataformas en crecimiento vs obsoletas
4. **Segmentación regional** - Comparar preferencias NA/EU/JP
5. **Pruebas de hipótesis** - Validar relaciones estadísticamente
6. **Recomendaciones** - Definir estrategia publicitaria data-driven para 2017

##  Estructura de datos

### Dataset: Ventas históricas de videojuegos

| Columna | Descripción |
|---------|-------------|
| `Name` | Nombre del videojuego |
| `Platform` | Plataforma (PS4, Xbox One, PC, etc.) |
| `Year_of_Release` | Año de lanzamiento |
| `Genre` | Género (Action, Sports, RPG, etc.) |
| `NA_sales` | Ventas en Norteamérica (millones USD) |
| `EU_sales` | Ventas en Europa (millones USD) |
| `JP_sales` | Ventas en Japón (millones USD) |
| `Other_sales` | Ventas en resto del mundo (millones USD) |
| `Critic_Score` | Puntuación de críticos (0-100) |
| `User_Score` | Puntuación de usuarios (0-10) |
| `Rating` | Clasificación ESRB (E, T, M, AO, etc.) |

### Clasificación ESRB
- **E** (Everyone) - Todo público
- **E10+** - Mayores de 10 años
- **T** (Teen) - Adolescentes (13+)
- **M** (Mature) - Adultos (17+)
- **AO** (Adults Only) - Solo adultos (18+)

##  Tecnologías utilizadas

- **Python 3.x** - Lenguaje de programación
- **Pandas** - Manipulación y análisis de datos
- **NumPy** - Cálculos estadísticos y agregaciones
- **Matplotlib** - Visualización de tendencias temporales
- **SciPy** - Pruebas de hipótesis y correlaciones
- **Jupyter Notebook** - Desarrollo y documentación

##  Metodología de análisis

### Fase 1: Preprocesamiento autónomo
```python
# Sin plantilla - diseño propio de limpieza
- Manejo de años faltantes
- Conversión de User_Score (string → float)
- Tratamiento de valores TBD (To Be Determined)
- Cálculo de ventas totales globales
- Filtrado de datos relevantes (últimos años)
```

### Fase 2: Análisis exploratorio
**Preguntas investigadas:**

1. **Evolución temporal**
   - ¿Cómo han evolucionado las ventas por año?
   - ¿Cuándo alcanzaron el pico?

2. **Análisis de plataformas**
   - ¿Qué plataformas dominaron cada era?
   - ¿Cuál es el ciclo de vida típico de una plataforma?
   - ¿Qué plataformas están en ascenso para 2017?

3. **Impacto de reseñas**
   - Correlación entre Critic_Score y ventas
   - Correlación entre User_Score y ventas
   - ¿Las reseñas predicen el éxito comercial?

4. **Análisis de género**
   - ¿Qué géneros generan más ingresos?
   - ¿Varía por plataforma?

5. **Segmentación regional**
   - Top 5 plataformas por región (NA/EU/JP)
   - Top 5 géneros por región
   - ¿Impacta la clasificación ESRB en ventas por región?

### Fase 3: Pruebas de hipótesis

**Hipótesis 1: Comparación de plataformas**
```python
# H₀: Calificaciones promedio Xbox One = PC
# H₁: Calificaciones promedio son diferentes

from scipy import stats
t_stat, p_value = stats.ttest_ind(xbox_scores, pc_scores)
```

**Hipótesis 2: Comparación de géneros**
```python
# H₀: Calificaciones promedio Action = Sports
# H₁: Calificaciones promedio son diferentes

t_stat, p_value = stats.ttest_ind(action_scores, sports_scores)
```

### Fase 4: Recomendaciones de negocio
- Plataformas en las que invertir publicidad
- Géneros más prometedores
- Estrategias diferenciadas por región

##  Análisis realizados

###  Por plataforma
- Ciclo de vida de consolas (lanzamiento → pico → declive)
- Identificación de plataformas "moribundas" vs "emergentes"
- Ventas acumuladas por generación

### Por género
- Ranking de géneros por ventas globales
- Preferencias regionales (JP ama RPG, NA prefiere Action/Sports)
- Evolución de popularidad de géneros

###  Por región
- Patrones culturales de consumo
- Impacto de clasificación ESRB por región
- Diferencias en valoración crítica vs comercial

###  Correlaciones
- Critic_Score vs ventas (correlación moderada-alta)
- User_Score vs ventas (correlación débil-moderada)
- Años de plataforma vs ventas

##  Aprendizajes clave

- **Autonomía analítica** - Diseñar proceso de análisis desde cero sin guías
- **Pensamiento de producto** - Entender ciclo de vida de plataformas
- **Análisis multicultural** - Adaptar estrategias por región
- **Estadística aplicada** - Pruebas de hipótesis para validar insights
- **Business intelligence** - Traducir datos históricos en predicciones accionables
- **Storytelling avanzado** - Construir narrativa completa sin estructura predefinida


##  Habilidades demostradas

- **Análisis autónomo** - Sin plantillas ni guías
- **Pensamiento crítico** - Formular preguntas de negocio relevantes
- **Estadística inferencial** - Múltiples pruebas de hipótesis
- **Análisis temporal** - Tendencias y predicciones
- **Segmentación geográfica** - Estrategias diferenciadas por región
- **Visualización** - Comunicar tendencias complejas
- **Análisis de correlación** - Identificar drivers de éxito

##  Logros del proyecto

-  **100% autónomo** - Sin instrucciones paso a paso
-  **Dataset histórico amplio** - Décadas de datos de videojuegos
-  **Análisis multidimensional** - Plataforma × Género × Región × Tiempo
-  **Validación estadística** - Hipótesis probadas rigurosamente
-  **Recomendaciones accionables** - Estrategia publicitaria 2017
-  **Industria relevante** - Gaming = mercado de $180B+ anuales

##  Contexto de industria

El mercado global de videojuegos es altamente competitivo:
- Inversiones millonarias en desarrollo
- Ciclos de vida de plataformas de ~5-7 años
- Preferencias culturales marcadas (JP vs Occidente)
- Impacto crítico de reseñas en semana de lanzamiento

**Este análisis simula decisiones reales** de publishers como EA, Ubisoft, o Nintendo.



---

**Proyecto:** Bootcamp Data Analysis - Proyecto Final Autónomo  
**Autor:** Marcos - [@NachtD69](https://github.com/NachtD69)  
**Fecha:** 2026  
**Cliente:** Ice (Tienda Online de Videojuegos)  
**Metodología:** Análisis exploratorio + Pruebas de hipótesis + Predicción de tendencias  
**Status:** Proyecto independiente completado
