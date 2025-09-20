### **QABasedOnMedicaKnowledgeGraph**

Implementación propia de un grafo médico centrado en enfermedades desde cero, para servir como base de un sistema de preguntas y respuestas.

---

### **Introducción del Proyecto**

Los grafos de conocimiento son actualmente una dirección popular en el procesamiento del lenguaje natural. Para obtener información más completa, puedes revisar mi resumen de participación en la CCKS2018 ([enlace](https://github.com/liuhuanyong/CCKS2018Summary)).

Otra variante relacionada con los grafos de conocimiento es el grafo de eventos o razonamiento, en el que también he acumulado algunos trabajos exploratorios. Puedes consultar más detalles aquí: ([enlace](https://github.com/liuhuanyong/ComplexEventExtraction)).

No me extenderé en la introducción conceptual de los grafos de conocimiento. Actualmente, los grafos de conocimiento están floreciendo en múltiples campos como la educación, la medicina, la justicia y las finanzas. Este proyecto se enfoca en el ámbito médico, utilizando datos de sitios web médicos especializados como fuente de información. Con las enfermedades como núcleo, se construye un grafo de conocimiento que incluye alrededor de 44,000 entidades de conocimiento de 7 categorías y aproximadamente 300,000 relaciones entre estas entidades de 11 categorías.

El proyecto incluirá dos partes principales:
1. Construcción de un grafo de conocimiento médico basado en datos de sitios web especializados.
2. Sistema de preguntas y respuestas automáticas basado en el grafo de conocimiento médico.

---

### **Resultado Final del Proyecto**

Sin más preámbulos, aquí están las capturas de pantalla del proceso de preguntas y respuestas en acción:

![imagen](https://github.com/liuhuanyong/QABasedOnMedicalKnowledgeGraph/blob/master/img/chat1.png)
![imagen](https://github.com/liuhuanyong/QABasedOnMedicalKnowledgeGraph/blob/master/img/chat2.png)

---

### **Forma de Ejecución del Proyecto**

1. **Requisitos de Configuración:** Se requiere configurar la base de datos neo4j y las dependencias de Python correspondientes. Recuerda el nombre de usuario y contraseña de la base de datos neo4j y modifica los archivos correspondientes.
2. **Importación de Datos del Grafo de Conocimiento:** Ejecuta `python build_medicalgraph.py`. La importación de datos puede tardar varias horas debido a la gran cantidad de información.
3. **Iniciar el Sistema de Preguntas y Respuestas:** Ejecuta `python chat_graph.py`.

---

### **Esquema Detallado del Proyecto**

#### **1. Construcción del Grafo de Conocimiento Médico**

##### **1.1 Marco de Construcción del Grafo de Conocimiento Basado en Negocios**
![imagen](https://github.com/liuhuanyong/QABasedOnMedicalKnowledgeGraph/blob/master/img/kg_route.png)

##### **1.2 Directorio de Scripts**
- `prepare_data/datasoider.py`: Script para la recolección de información en línea.
- `prepare_data/max_cut.py`: Script para la segmentación máxima hacia adelante/atrás basada en diccionario.
- `build_medicalgraph.py`: Script para la importación de datos al grafo de conocimiento.

##### **1.3 Escala del Grafo de Conocimiento Médico**

###### **1.3.1 Escala de Almacenamiento en la Base de Datos Neo4j**
![imagen](https://github.com/liuhuanyong/QABasedOnMedicalKnowledgeGraph/blob/master/img/graph_summary.png)

###### **1.3.2 Tipos de Entidades en el Grafo de Conocimiento**



| Tipo de Entidad  | Significado en Español | Cantidad de Entidades | Ejemplo                     |
|------------------|------------------------|-----------------------|-----------------------------|
| Check            | Prueba de Diagnóstico  | 3,353                 | Broncografía; Artroscopia    |
| Department       | Departamento Médico    | 54                    | Cirugía Plástica; Quemados   |
| Disease          | Enfermedad             | 8,807                 | Tromboangeítis Obliterante; Aneurisma de la aorta torácica descendente |
| Drug             | Medicamento            | 3,828                 | Ungüento Jingwanhem; Gotas de Brinzolamida |
| Food             | Comida                 | 4,870                 | Sopa de albóndigas de carne con tomate; Estofado de brotes de bambú con carne de cordero |
| Producer         | Producto en Venta      | 17,201                | Tabletas de Penicilina V Potásica Tongyao; Tabletas de Dexametasona QiYang |
| Symptom          | Síntoma                | 5,998                 | Hiperplasia del tejido mamario; Hemorragia cerebral profunda |
| **Total**        | **Total**              | **44,111**            | Aprox. 44,000 entidades     |

###### **1.3.3 Tipos de Relaciones entre Entidades en el Grafo de Conocimiento**



| Tipo de Relación       | Significado en Español       | Cantidad de Relaciones | Ejemplo                                      |
|------------------------|-------------------------------|------------------------|----------------------------------------------|
| belongs_to             | Pertenece a                   | 8,844                  | <Ginecología, pertenece a, Obstetricia y Ginecología> |
| common_drug            | Medicamento Común             | 14,649                 | <Priapismo, común, Tabletas dispersables de Fenoxibenzamina> |
| do_eat                 | Alimento Recomendado          | 22,238                 | <Fractura de vértebra torácica, comer, Pez negro> |
| drugs_of               | Medicamento en Venta          | 17,315                 | <Tabletas de Penicilina V Potásica, en venta, Tabletas de Penicilina V Potásica Tongyao> |
| need_check             | Prueba Necesaria              | 39,422                 | <Enfisema pulmonar unilateral, prueba necesaria, Broncografía> |
| no_eat                 | Alimento no Recomendado       | 22,247                 | <Enfermedad labial, evitar, Almendras>       |
| recommand_drug         | Medicamento Recomendado       | 59,467                 | <Hemorroides mixtas, medicamento recomendado, Ungüento Jingwanhem> |
| recommand_eat          | Dieta Recomendada             | 40,221                 | <Hidrocele, dieta recomendada, Sopa de albóndigas de carne con tomate> |
| has_symptom            | Síntoma de Enfermedad         | 5,998                  | <Cáncer de mama en etapa temprana, síntoma, Hiperplasia del tejido mamario> |
| acompany_with          | Enfermedad Concurrent         | 12,029                 | <Insuficiencia valvular de vena comunicante de extremidad inferior, enfermedad concurrent, Tromboangeítis Obliterante> |
| **Total**              | **Total**                     | **294,149**            | Aprox. 300,000 relaciones                    |

### 1.3.4 Tipos de Atributos del Grafo de Conocimiento



| Tipo de Atributo | Significado en Español       | Ejemplo                     |
|------------------|------------------------------|-----------------------------|
| name             | Nombre de la enfermedad      | Bronquitis asmatiforme      |
| desc             | Descripción de la enfermedad | También conocida como bronquitis asmática... |
| cause            | Causa de la enfermedad       | Comúnmente causada por el virus sincitial respiratorio... |
| prevent          | Medidas preventivas          | Prestar atención a los antecedentes alérgicos familiares y del niño... |
| cure_lasttime    | Duración del tratamiento     | 6-12 meses                  |
| cure_way         | Método de tratamiento        | "Tratamiento farmacológico", "Tratamiento de soporte" |
| cured_prob       | Probabilidad de curación     | 95%                         |
| easy_get         | Grupos susceptibles           | No hay un grupo específico  |

---

### 2. Sistema de Preguntas y Respuestas Basado en el Grafo de Conocimiento Médico

### 2.1 Arquitectura Técnica
![imagen](https://github.com/liuhuanyong/QABasedOnMedicalKnowledgeGraph/blob/master/img/qa_route.png)

### 2.2 Estructura de Scripts
- `question_classifier.py`: Script para clasificar el tipo de pregunta.
- `question_parser.py`: Script para analizar la pregunta.
- `chatbot_graph.py`: Script del programa de preguntas y respuestas.

### 2.3 Tipos de Preguntas Soportadas



| Tipo de Pregunta         | Significado en Español               | Ejemplo de Pregunta                     |
|--------------------------|---------------------------------------|-----------------------------------------|
| disease_symptom          | Síntomas de la enfermedad             | ¿Cuáles son los síntomas del cáncer de mama? |
| symptom_disease          | Encontrar posibles enfermedades por síntomas | Últimamente tengo mucho moco nasal, ¿qué puedo hacer? |
| disease_cause            | Causa de la enfermedad                | ¿Por qué algunas personas sufren de insomnio? |
| disease_acompany         | Complicaciones de la enfermedad      | ¿Qué complicaciones tiene el insomnio? |
| disease_not_food         | Alimentos que deben evitarse          | ¿Qué no deben comer las personas con insomnio? |
| disease_do_food          | Alimentos recomendados                | ¿Qué debo comer si tengo acúfenos? |
| food_not_disease         | Enfermedades que deben evitar ciertos alimentos | ¿Quiénes no deben comer miel? |
| food_do_disease          | Beneficios de un alimento para enfermedades | ¿Qué beneficios tiene la carne de ganso? |
| disease_drug             | Medicamentos para enfermedades        | ¿Qué medicamentos debo tomar para enfermedades del hígado? |
| drug_disease             | Enfermedades que trata un medicamento | ¿Qué enfermedades trata Banlangen Kulili? |
| disease_check            | Pruebas necesarias para una enfermedad | ¿Cómo se detecta la meningitis? |
| check_disease            | Enfermedades detectables por una prueba | ¿Qué enfermedades puede detectar un hemograma completo? |
| disease_prevent          | Medidas preventivas                   | ¿Cómo puedo prevenir la deficiencia renal? |
| disease_lasttime         | Duración del tratamiento              | ¿Cuánto tiempo tarda en curarse un resfriado? |
| disease_cureway          | Método de tratamiento                 | ¿Cómo se trata la hipertensión? |
| disease_cureprob         | Probabilidad de curación              | ¿Se puede curar la leucemia? |
| disease_easyget          | Grupos susceptibles                   | ¿Qué personas son más propensas a tener hipertensión? |
| disease_desc             | Descripción de la enfermedad          | Diabetes                                   |

---

### Ejemplos de Resultados de Preguntas y Respuestas

**Usuario:** ¿Cuáales son los síntomas del cáncer de mama?
**Respuesta:** Los síntomas del cáncer de mama incluyen: metástasis a distancia del cáncer de mama, dolor en el pecho, secreción del pezón, grietas en el pezón, hepatomegalia, trastornos en la lactancia, retracción del pezón, bultos en el pecho, dolor intenso.

---

**Usuario:** Últimamente tengo mucho moco nasal, ¿qué puedo hacer?
**Respuesta:** El síntoma de moco nasal puede estar asociado con las siguientes enfermedades: fiebre del heno, gripe secundaria, infección aguda del tracto respiratorio superior, intoxicación por sulfuro de hidrógeno, neumonía por clamidia infantil, resfriado por viento-frío, sinusitis frontal crónica, cefalea de origen nasal, gripe aviar, neumonía obstructiva bronquial infantil, gripe viral, rinitis crónica, viento-calor atacando el pulmón, resfriado común, asfixia, infección aguda del tracto respiratorio superior infantil, rinitis eosinofílica no alérgica, sinusitis caseosa, infección del tracto respiratorio inferior, sarampión.

---

**Usuario:** ¿Por qué algunas personas sufren de insomnio?
**Respuesta:** Las posibles causas del insomnio incluyen: enfermedades físicas y el uso de medicamentos que pueden afectar el sueño, como indigestión, dolor de cabeza, dolor de espalda, artritis, enfermedades cardíacas, diabetes, asma, sinusitis, úlceras o el uso de ciertos medicamentos que afectan el sistema nervioso central. También es común que los problemas de sueño sean causados por el estilo de vida, como consumir café o té, beber alcohol por la noche, comer antes de dormir o cenar tarde, fumar en exceso, hacer ejercicio intenso antes de dormir, actividad mental excesiva antes de dormir, trabajar en turnos nocturnos, dormir siestas durante el día, horarios irregulares para acostarse y levantarse. Otras causas pueden ser estrés, preocupación excesiva, tensión o ansiedad, tristeza o depresión, enojo. Un ambiente ruidoso para dormir, un ambiente demasiado brillante, contaminación y hacinamiento también pueden causar problemas de sueño.

---

**Usuario:** ¿Qué complicaciones tiene el insomnio?
**Respuesta:** Las complicaciones del insomnio incluyen: desarmonía entre el corazón y el riñón, acúfenos neurológicos, disfunción anormal de la trompa de Eustaquio, paranoia, reflujo duodenal gástrico y gastritis por reflujo biliar, bromhidrosis, melasma, arteritis de células gigantes, enfermedad de Stargardt, depresión, infarto cerebral lacunar, trastorno mental asociado con hipertiroidismo, cefalea tensional, gastroptosis, deficiencia de sangre cardíaca, conmoción laberíntica, úlceras bucales tuberculosas, retención de líquidos, paniculitis nodular migratoria, conmoción cerebral infantil.

---

**Usuario:** ¿Qué no deben comer las personas con insomnio?
**Respuesta:** Los alimentos que deben evitarse en caso de insomnio incluyen: youtiao (tira de masa frita), almejas de río, manteca de cerdo (grasa de cerdo), mejillones frescos.

---

**Usuario:** ¿Qué debo comer si tengo acúfenos?
**Respuesta:** Los alimentos recomendados para el acúfeno incluyen: semillas de calabaza, alas de pollo, sésamo, anacardos. Las recetas recomendadas incluyen: sopa de tofu y col china, fideos con sopa de carne de cordero, tofu frito con col china, sopa de huevo con algas y hierbas de loto, sopa de carne de cordero con lindera, alas de pollo con Coca-Cola, alas de pollo con castañas, brócoli con corazón de col china.

---

**Usuario:** ¿Quiénes no deben comer miel?
**Respuesta:** Las personas que padecen encefalitis esporádica con trastorno mental asociado, trastorno afectivo del estado de ánimo, picadura de escorpión, linfedema de las extremidades, trastorno mental causado por intoxicación con pesticidas, tumor hepático disembrioplásico, neumonía bacteriana, mal de altura agudo, tumor de la fosa posterior craneal infantil, exantema por virus Coxsackie, hemangioma venoso orbital, trastorno mental asociado con encefalitis japonesa, hemorragia posparto tardía, neumonía por aspiración, lesión del nervio peroneo, enfermedades de la piel causadas por berilio y sus compuestos, enfermedad coronaria con muerte súbita, anomalía de Peter, nefritis tubulointersticial aguda alérgica, distensión abdominal infantil no deben comer miel.

---

**Usuario:** ¿Qué beneficios tiene la carne de ganso?
**Respuesta:** Se recomienda que las personas con engrosamiento del endometrio, enfermedades respiratorias, enfermedades anorrectales, amenorrea, trastorno adaptativo tras la viudez, ectropión cervical, macroglobulinemia, sialoadenitis submaxilar aguda, daño extrapiramidal, adenoides, tos, hamartoma, enfermedades dentales, endometritis, síndrome de enclaustramiento, conjuntivitis, linfoma maligno, pie valgo, neuritis, miopía patológica prueben la carne de ganso.

---

**Usuario:** ¿Qué medicamentos debo tomar para enfermedades del hígado?
**Respuesta:** Los alimentos recomendados para enfermedades del hígado incluyen: carne de ganso, carne de pollo, hígado de pollo, muslos de pollo. Las recetas recomendadas incluyen: gachas de mijo con azúcar moreno, gachas de mijo con huevo y leche, gachas de mijo con frijoles mungo, gachas de mijo con soja, gachas de mijo con ginseng, gachas de harina de mijo, gachas de mijo con champiñones, gachas de mijo con sésamo. Los medicamentos comúnmente utilizados para enfermedades del hígado incluyen: tabletas dispersables de entecavir, tabletas de vitamina C, píldoras Wuwei Songshi, cápsulas de lamivudina, tabletas de adefovir dipivoxil.

---

**Usuario:** ¿Qué enfermedades trata Banlangen Kulili?
**Respuesta:** Banlangen Kulili se utiliza principalmente para tratar paperas epidémicas, amigdalitis, laringitis, sensación de cuerpo extraño en la faringe, faringitis aguda simple, infección del espacio parotídeo, faringitis alérgica, inflamación de la bolsa faríngea, nasofaringitis aguda, edema de laringe, parotiditis purulenta crónica, faringitis crónica, laringitis aguda, sensación de cuerpo extraño en la faringe, nasofaringitis, forúnculo de la garganta, faringolaringitis infantil, lesión del nervio laríngeo recurrente, parotiditis purulenta, hemangioma laríngeo.

---

**Usuario:** ¿Cómo se detecta la meningitis?
**Respuesta:** La meningitis generalmente se puede detectar mediante las siguientes pruebas: sodio en el líquido cefalorraquídeo, análisis de orina, prueba del dedo de Fisher, rigidez de nuca, cultivo bacteriano del líquido cefalorraquídeo, glutamina en la orina, potasio en el líquido cefalorraquídeo, aspartato aminotransferasa en el líquido cefalorraquídeo, examen de patógenos en el líquido cefalorraquídeo, prueba de reducción de nitrato.

---

**Usuario:** ¿Cómo puedo prevenir la deficiencia renal?
**Respuesta:** Las posibles causas de la deficiencia renal incluyen: 1. Exceso de actividad sexual o masturbación frecuente en la adolescencia. 2. Preocupación y melancolía que dañan el corazón y el bazo, afectando los vasos Chong y Yangming. 3. Miedo que daña los riñones. 4. El hígado controla los tendones, y los genitales son la convergencia de los tendones ancestrales. Si las emociones no se satisfacen, la tristeza, la preocupación y la ira afectan la capacidad del hígado para dispersar y drenar, lo que lleva a la disfunción de los tendones ancestrales. 5. Humedad-calor descendente, relajación de los tendones ancestrales. La deficiencia renal es un concepto integral que abarca varias afecciones causadas por la insuficiencia de la esencia, el qi, el yin y el yang de los riñones, como fatiga mental, mareos, tinnitus, pérdida de memoria, caída del cabello, dolor lumbar, emisiones nocturnas, impotencia, infertilidad masculina, infertilidad femenina y síndrome menopáusico. Las causas de la deficiencia renal se pueden dividir en dos aspectos: insuficiencia congénita y factores adquiridos. Desde la perspectiva de los factores congénitos que causan deficiencia renal, primero está la debilidad congénita. Según el capítulo "Shou Tian Gang Rou" de Ling Shu, "las personas al nacer pueden ser fuertes o débiles". Debido a que los padres están débiles y enfermos, y la esencia y la sangre son deficientes durante el embarazo, o debido a relaciones sexuales bajo la influencia del alcohol durante el embarazo, o cuando ambos padres tienen más de cincuenta años y su fuerza vital está significativamente reducida, o cuando la edad de los padres es demasiado joven y sus cuerpos no están completamente desarrollados, o debido a múltiples embarazos que agotan en gran medida la esencia y la sangre, o a la falta de cuidado durante el embarazo, lo que lleva a una insuficiencia de qi fetal, todo esto puede causar deficiencia de la esencia y el qi de los riñones, convirtiéndose en una causa importante de la deficiencia renal. En segundo lugar, si la función de los riñones para almacenar esencia es anormal, esto llevará a disfunción sexual, disminución de la función reproductiva y afectará la capacidad reproductiva, lo que resultará en que la próxima generación tenga cuerpos débiles, o defectos congénitos, discapacidad intelectual, defectos físicos, los hombres tendrán poca esperma e infertilidad, eyaculación precoz, y las mujeres tendrán amenorrea, infertilidad, abortos espontáneos o abortos habituales.

Las medidas preventivas para la deficiencia renal incluyen:
1. La vida sexual debe ser moderada, sin forzarse ni ser indulgente.
2. En la dieta: cuando haya fatiga, consumir más alimentos ricos en hierro y proteínas, como hongos negros, dátiles chinos, gallina negra; para quienes tienen indigestión, beber más yogur y comer más hawthorn; para el cuidado diario de los riñones, comer más puerros, pepino de mar, ginseng, gallina negra y palomas.
3. Realizar actividades de la zona lumbar con frecuencia, estos movimientos pueden fortalecer la puerta de la vida y tonificar los riñones. También se pueden hacer más masajes que estimulen la planta del pie. Según la medicina tradicional china, el punto Yongquan en la planta del pie es donde desciende el qi turbio. Masajear frecuentemente el punto Yongquan puede beneficiar la esencia y tonificar los riñones, fortalecer el cuerpo, prevenir el envejecimiento prematuro, además de aliviar el hígado, aclarar la visión, calmar la garganta, estabilizar la mente, promover el sueño y mejorar el apetito.
4. Dormir lo suficiente también es una garantía importante para recuperar la energía. No importa cuán ocupado esté el trabajo o cuántas preocupaciones domésticas tenga, debe descansar a tiempo cuando sea hora de dormir.
5. Evitar el consumo excesivo de alimentos amargos, fríos o helados, como aloe vera, melón amargo, helado, carne de ganso y cerveza, que pueden dañar los riñones. Se deben consumir más alimentos con alto contenido de melanina y propiedades cálidas y tónicas, como el arroz negro y los frijoles negros.
6. Los hombres que entran en contacto con demasiados detergentes también pueden dañar los riñones. Las familias deben reducir el uso de detergentes para lavar utensilios y verduras para evitar la ingesta excesiva de residuos de detergentes.
7. El ejercicio adecuado puede retrasar el envejecimiento, pero la intensidad no debe ser demasiado alta. Deben elegir actividades físicas acorde a sus capacidades para promover la circulación sanguínea y mejorar condiciones como estasis de sangre y daño de qi. Caminar, trotar, caminar rápido o caminar descalzo sobre piedras de río pueden promover la circulación sanguínea y tienen un efecto terapéutico auxiliar para la deficiencia renal.
8. Mantener buenos hábitos de sueño y evitar trasnochar.
9. Participar activamente en actividades al aire libre y relajarse.
10. No ponerse demasiada presión y aprender a aliviar el estrés de manera razonable.

---

**Usuario:** ¿Cuánto tiempo tarda en curarse un resfriado?
**Respuesta:** El tratamiento del resfriado puede durar: 7-14 días.

---

**Usuario:** ¿Cómo se trata la hipertensión?
**Respuesta:** La hipertensión puede tratarse con los siguientes métodos: tratamiento farmacológico, tratamiento quirúrgico, tratamiento de soporte.

---

**Usuario:** ¿Se puede curar la leucemia?
**Respuesta:** La probabilidad de curación de la leucemia es (solo como referencia): 50%-70%.

---

**Usuario:** ¿Qué personas son más propensas a tener hipertensión?
**Respuesta:** Los grupos susceptibles a la hipertensión incluyen: personas con antecedentes familiares de hipertensión, personas con malos hábitos de vida y falta de ejercicio.

---

**Usuario:** Diabetes
**Respuesta:** La diabetes es una enfermedad endocrina y metabólica relativamente común. Las causas de esta enfermedad se deben principalmente a la secreción insuficiente de insulina y la secreción excesiva inapropiada de glucagón. Es más común en pacientes mayores de 40 años que consumen muchos dulces y tienen sobrepeso. Es más frecuente en áreas urbanas que en rurales y a menudo tiene antecedentes familiares, por lo que está relacionada con la genética. Algunos pacientes están relacionados con infecciones virales y reacciones autoinmunes. Los síntomas principales incluyen sed excesiva, polidipsia, poliuria, polifagia, fatiga y pérdida de peso. Es una enfermedad común que amenaza la vida y a menudo se acompaña de hipertensión, enfermedad coronaria, hiperlipidemia, etc., y puede ser potencialmente mortal en casos graves. Según la medicina tradicional china, el hígado regula la dispersión y está relacionado con el ascenso y descenso del mecanismo de recepción del cuerpo. Si el qi del hígado está estancado, el mecanismo de qi ascendente y descendente se desordena. Cuando el hígado pierde su capacidad de dispersión, sustancias esenciales como el azúcar en la sangre no pueden distribuirse por todo el cuerpo junto con el qi claro yang, lo que lleva a un estancamiento en la sangre o una distribución desordenada de sustancias esenciales, lo que resulta en un aumento del azúcar en la sangre. Esto, a su vez, causa desórdenes en otras sustancias esenciales como los lípidos en sangre y las proteínas, lo que lleva a otras complicaciones. El tratamiento se centra en aliviar el qi del hígado y regular el qi. Siguiendo la naturaleza dispersante y reguladora del hígado para restaurar su función fisiológica, cuando el qi del hígado fluye sin obstáculos y el mecanismo de qi está armonizado, las sustancias esenciales pueden distribuirse y el azúcar puede ser utilizado, reduciendo naturalmente los niveles de azúcar en la sangre. Además, la aparición de la diabetes está relacionada con la dieta. El efecto del control dietético afecta directamente los resultados del tratamiento. Junto con el ejercicio y prestando atención a la regulación emocional, combinado con un tratamiento adecuado con medicina tradicional china, se pueden obtener buenos resultados terapéuticos.

---

**Usuario:** ¿Qué enfermedades puede detectar un hemograma completo?
**Respuesta:** Generalmente, las siguientes enfermedades pueden detectarse mediante un hemograma completo: escleritis reumatoide del adulto, síndrome vulvovaginal-gingival, lesión por descarga eléctrica, hipertensión sistólica en ancianos, cirrosis infantil, hemoglobinopatía, síndrome demencial, trastorno mental asociado con hipertensión, linfoma testicular, anemia por deficiencia de folato, endoftalmitis, hemoglobinopatía inestable, síndrome carcinoide, demencia senil, linfangitis aguda, embarazo cervical, úlcera corneal corrosiva, leucemia aguda hipoplásica, oftalmía simpática, enfermedad por inmunodeficiencia primaria.

---

### Resumen

1. Este proyecto logró construir desde cero un grafo de conocimiento médico centrado en enfermedades, utilizando datos de sitios web verticales. El grafo incluye 44,000 entidades y 300,000 relaciones entre ellas. Sobre esta base, se desarrolló un pequeño sistema de preguntas y respuestas capaz de responder 18 tipos de preguntas, todo en un período de 3 días. La recolección y organización de datos tomó 1 día, la construcción e importación del grafo de conocimiento tomó medio día, y el desarrollo del sistema de preguntas y respuestas tomó un día y medio. En general, fue un proceso relativamente rápido.

2. Este proyecto se guió por las necesidades del negocio para construir el grafo de conocimiento médico. El diseño del esquema de conocimiento se basó en los datos estructurados recolectados (analizando los datos estructurados de las páginas web mediante xpath).

3. Este proyecto utiliza neo4j como almacenamiento y completa el servicio de preguntas y respuestas basado en reglas tradicionales, utilizando finalmente consultas en lenguaje Cypher como SQL de búsqueda para preguntas y respuestas.

4. Este proyecto se puede implementar rápidamente. Los datos ya están disponibles en `data/medical.json`. Si los datos de este proyecto infringen los derechos de alguna unidad, por favor contácteme para eliminarlos. Los datos de este proyecto no deben usarse con fines comerciales para evitar disputas innecesarias. Para la implementación de este proyecto, se pueden seguir los pasos de ejecución del proyecto para construir la base de datos y proporcionar servicios de búsqueda.

5. Este proyecto aún tiene deficiencias: en cuanto a las causas y prevención de enfermedades, actualmente devuelve un gran bloque de texto. Aquí se podría introducir el concepto de extracción de eventos para representar estructuralmente las causas. Esto se puede intentar en el futuro.

Si tienes alguna pregunta sobre el proyecto o sobre mí, visita [mi página de GitHub](https://liuhuanyong.github.io/).

Para preguntas o colaboraciones sobre procesamiento de lenguaje natural, grafos de conocimiento, grafos de eventos, computación social y construcción de recursos lingüísticos, puedes contactarme:
1. Mis proyectos en GitHub: [liuhuanyong.github.io](https://liuhuanyong.github.io)
3. Acerca de mí: Liu Huanyong, lhy_in_blcu@126.com.
4. Mi cuenta pública en WeChat: Lao Liu habla sobre PLN (Procesamiento de Lenguaje Natural), escanea el código para seguirme:
![imagen](https://github.com/liuhuanyong/QABasedOnMedicalKnowledgeGraph/blob/master/img/wechat.jpg)

