# 📊 Guía de Métricas para Evaluación de Traducción Automática

## 🔍 Métricas estadísticas: rápidas pero sin contextualización semántica, ayudan de complemento

### 1. **BLEU (Bilingual Evaluation Understudy)**
 **Descripción**: Evalúa la precisión de n-gramas (palabras o secuencias) comparando con traducciones de referencia. Basicamente, compara la traducción hecha por humanos y la nuestra y hace un cálculo. Sirve para textos cortos porque en el momento que ve un sinónimo falla

- **Caso de uso ideal**: Evaluación general de traducciones estándar.
- **Rango de valores**: `0.0` (pésimo) a `1.0` (perfecto).  
  - *Ejemplo típico*:  
    - < 0.3: Traducción inaceptable  
    - 0.3-0.5: Calidad básica  
    - 0.5-0.7: Buena calidad  
    - > 0.7: Excelente calidad
- **Requisitos**: Requiere texto de referencia.


### 2. **METEOR**
 **Descripción**: Es como BLEU pero más potente porque considera sinonimos, stems y alineación de palabras, además tiene más correlación con traduccione humanas.
- **Caso de uso ideal**: cuando queremos mas precision y recall.
- **Rango de valores**: `0.0` (pésimo) a `1.0` (perfecto).  
  - *Ejemplo típico*:  
    - < 0.3: Traducción inaceptable  
    - 0.3-0.5: Calidad básica  
    - 0.5-0.7: Buena calidad  
    - > 0.7: Excelente calidad
- **Requisitos**: Requiere texto de referencia.

### 3. **ROUGE-N**
 **Descripción**: Esta métrica mide la cobertura del contenido mediante la superposición de n-gramas.
- **Caso de uso ideal**: Medir la cobertura de palabras clave.
- **Rango de valores**: `0.0` (pésimo) a `1.0` (perfecto).  
  - *Ejemplo típico*:  
    - < 0.3: Traducción inaceptable  
    - 0.3-0.5: Calidad básica  
    - 0.5-0.7: Buena calidad  
    - > 0.7: Excelente calidad
- **Requisitos**: Requiere texto de referencia.


## 🔍 Métricas neuronales: modelos entrenados que miden la calidad de traducción 

### 1. **COMET**
**Descripción**: Modelo neuronal que evalua la calidad de la traducción teniendo en cuenta el contexto. Ideal en relación semántica
- **Caso de uso ideal**: evaluación profesional muy parecida al humano.
- **Rango de valores**: `0.0` (pésimo) a `1.5` (perfecto).  
  - *Ejemplo típico*:  
    - < 0.5: Traducción deficiente  
    - 0.5-0.8: Calidad aceptable  
    - 0.8-1.2: Buena calidad  
    - > 1.2: Excelente
- **Requisitos**: Puede funcionar con y sin referencia. Si es sin referencia el score maximo es 1.3 y con referencia 1.5 .


### 2. **BLEURT**
**Descripción**: Métrica basada en BERT fine-tuned para la evaluacion de metricas en traducción
- **Caso de uso ideal**: Evaluar la calidad semántica y naturalidad del texto
- **Rango de valores**: `-2.0` (pésimo) a `2.0` (perfecto).  
  - *Ejemplo típico*:  
    - < 0.0: Baja calidad
    - 0.0-1.0: Calidad media
    - 1.0: Alta calidad
- **Requisitos**: Funciona con referencia


### 2. **BERTscore**
working

