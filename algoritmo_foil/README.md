
# Algoritmo FOIL - Ejercicios de Inducción de Reglas

## 📌 Descripción
Este trabajo corresponde a la práctica del **algoritmo FOIL (First Order Inductive Learner)**.  
El objetivo es aprender cómo inducir reglas lógicas simples a partir de ejemplos positivos y negativos, y calcular el **FOIL Gain** para evaluar condiciones.

---

## 🚀 Ejercicio 1: Identificar empleados en formación

### Dataset
Se tiene un conjunto de empleados con atributos:
- Edad
- Departamento
- Nivel educativo
- En formación (booleano: True o False)

### Resultados del análisis
- **Ejemplos positivos (en formación = True):** edades 21, 22, 23, 24; departamentos IT y RRHH; niveles educativos terciario y universitario.  
- **Ejemplos negativos (en formación = False):** edades 29, 35, 38, 40; departamentos IT, RRHH y Finanzas; niveles educativos universitario y maestría.  

### Diferencias encontradas
- **Departamentos exclusivos en positivos:** ninguno (IT y RRHH aparecen en ambos).  
- **Nivel educativo exclusivo en positivos:** `terciario`.  
- **Edades exclusivas en positivos:** 21, 22, 23, 24.  

### Regla inducida
```
SI nivel_educativo = 'terciario' O edad ≤ 23
ENTONCES en_formacion = True
```

---

## 📊 Ejercicio 2: FOIL Gain

### Fórmula
\[
FOIL\ Gain = p \cdot \left( \log_2\left(\frac{p}{p+n}\right) - \log_2\left(\frac{P}{P+N}\right) \right)
\]

---

### Condición: nivel_educativo == 'terciario'
- P (positivos antes) = 4  
- N (negativos antes) = 4  
- p (positivos después) = 3  
- n (negativos después) = 0  
- Fracción después: \( \frac{p}{p+n} = 1.0 \)  
- Fracción antes: \( \frac{P}{P+N} = 0.5 \)  
- Logaritmos: \( \log_2(1.0) = 0 \), \( \log_2(0.5) = -1 \)  
- **FOIL Gain = 3.0**

👉 Interpretación: esta condición separa muy bien los positivos de los negativos.

---

### Condición: edad ≤ 23
- P (positivos antes) = 4  
- N (negativos antes) = 4  
- p (positivos después) = 3  
- n (negativos después) = 0  
- Fracción después: \( \frac{p}{p+n} = 1.0 \)  
- Fracción antes: \( \frac{P}{P+N} = 0.5 \)  
- Logaritmos: \( \log_2(1.0) = 0 \), \( \log_2(0.5) = -1 \)  
- **FOIL Gain = 3.0**

👉 Interpretación: también es una condición fuerte para identificar empleados en formación.

---

## 📌 Conclusión
- Las condiciones con mayor FOIL Gain son:
  - `nivel_educativo = 'terciario'`
  - `edad ≤ 23`
- Ambas permiten inducir reglas que identifican correctamente a los empleados en formación.  
- El algoritmo FOIL muestra cómo a partir de ejemplos simples se pueden construir reglas lógicas útiles para clasificación.

---

## ✨ Autor
Estudiante: **Benjamín**  
Carrera: Tecnicatura Superior en Ciencia de Datos e IA  
Tema: Algoritmo FOIL y reglas de inducción
```
