
# 🧑‍💻 Ejercicio de práctica: Clasificación aplicando AQ con Python

Este proyecto aplica el **algoritmo AQ** para inducir reglas de clasificación a partir de ejemplos positivos y negativos.  
El objetivo es identificar las características que diferencian a los casos positivos de los negativos y formular reglas que permitan clasificar nuevos ejemplos.

---

## 🚗 Ejercicio 1: Clasificación de clientes que compran un automóvil eléctrico

### 🎯 Objetivo
Encontrar qué atributos permiten identificar a los clientes que compran un automóvil eléctrico.

### 📊 Datos
- Atributos: `edad`, `ingreso`, `tiene_garaje`, `distancia_trabajo`.  
- Ejemplos positivos: clientes que sí compraron.  
- Ejemplos negativos: clientes que no compraron.

### 🔎 Resultado del análisis
- Los clientes positivos tienen **garaje = Si**.  
- Los clientes negativos tienen **garaje = No**.  
- Los demás atributos varían y no son determinantes.

### ✅ Regla inducida
```
SI tiene_garaje = "Si"
ENTONCES Compra_Auto_Electrico = "Sí"
```

---

## 🏋️ Ejercicio 2: Inferir qué significa ser Socio Activo de un Gimnasio

### 🎯 Objetivo
Inducir la regla que diferencia a los socios activos de los no activos.

### 📊 Datos
- Atributos: `edad`, `frecuencia`, `plan`.  
- Ejemplos positivos: socios activos.  
- Ejemplos negativos: socios no activos.

### 🔎 Resultado del análisis
- Los socios activos tienen **frecuencia = frecuente** y **plan = premium**.  
- Los socios no activos tienen frecuencias ocasional/rara y planes básicos/estándar.  
- La edad no es determinante.

### ✅ Regla inducida
```
SI frecuencia = "frecuente"
Y plan = "premium"
ENTONCES Socio_Activo = "Sí"
```

---

## 🎯 Conclusión general
- El algoritmo AQ permite **descubrir reglas simples y efectivas** comparando ejemplos positivos y negativos.  
- 🚗 En la concesionaria, la condición clave es **tener garaje**.  
- 🏋️ En el gimnasio, la condición clave es **frecuencia frecuente + plan premium**.  
- No siempre es necesario usar todos los atributos: la edad no fue útil en el segundo caso.  
- Las reglas inducidas clasifican correctamente todos los positivos y excluyen los negativos.

---

## 📂 Contenido del repo
- `01_aq_practica.ipynb` → Notebook con análisis, aplicación del algoritmo AQ y verificación de reglas.  
- `README.md` → Documento explicativo del proyecto.  

