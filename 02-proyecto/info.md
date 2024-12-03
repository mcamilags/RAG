# NEBULA

## Roadmap

### Purpose and Scope of the SAD

El SAD tiene como objetivo documentar la arquitectura de Nebula, detallando los componentes estructurales y sus interacciones para cumplir con los requisitos de desarrollo, escalabilidad y seguridad. En este documento se incluye toda la informaci�n sobre la arquitectura de software de Nebula, destacando aquellos aspectos que influyen en el rendimiento y la adaptabilidad del sistema. Las decisiones de dise�o documentadas en el SAD son aquellas que tienen un impacto arquitect�nico relevante en la estructura general del sistema, mientras que los detalles de implementaci�n espec�ficos se documentan en otros informes t�cnicos.

### How the SAD Is Organized

El SAD de Nebula est� estructurado en las siguientes secciones:  
Sección 1: Documentation Roadmap - Proporciona una visi�n general del SAD, el prop�sito del documento y una gu�a sobre c�mo est� organizado.  
Sección 2: Antecedentes de la Arquitectura - Explica los objetivos y el contexto de desarrollo de Nebula, los requerimientos que impulsan las decisiones arquitect�nicas y los enfoques de soluci�n adoptados, as� como un resumen de los cambios entre versiones.  
Sección 3: Vistas de Arquitectura - Presenta diversas vistas de la arquitectura del software (m�dulos, componentes y conectores, y asignaci�n) que detallan la organizaci�n, relaci�n y comportamiento de los elementos en el sistema.  
Sección 4: Relaciones entre Vistas - Describe c�mo se relacionan e integran las diferentes vistas arquitect�nicas del sistema, proporcionando una visi�n coherente de la arquitectura de Nebula.  
Sección 5: Materiales Referenciados - Cita los documentos de referencia y bibliograf�a utilizados en el SAD, proporcionando una base documental para futuras consultas.  
Sección 6: Directorio - Incluye un �ndice de t�rminos, glosario y lista de acr�nimos, facilitando la navegaci�n y comprensi�n de t�rminos clave empleados en el documento.

### Stakeholder Representation

Esta secci�n describe los stakeholders de Nebula y sus principales preocupaciones, organizando el SAD para responder a las necesidades de cada uno. Entre los stakeholders considerados estan:

* Usuarios.
* Desarrolladores.
* Administradores del sistema.
* Gerentes de proyecto.
* Analistas de datos.

La estructura y contenido del SAD aseguran que cada stakeholder pueda acceder f�cilmente a la informaci�n relevante para sus intereses espec�ficos.

### Viewpoint Definitions

Para abordar de manera efectiva los intereses de los stakeholders, se han seleccionado diferentes puntos de vista arquitect�nicos, que se desarrollan en la Secci�n 3. Estos puntos de vista permiten entender la arquitectura de Nebula desde distintas perspectivas, como la estructura de m�dulos, la interacci�n de componentes y la asignaci�n de recursos. Cada vista facilita el an�lisis de aspectos espec�ficos del sistema y permite una representaci�n detallada de la arquitectura.

### How a View is Documented

Cada vista arquitect�nica en la Secci�n 3 sigue una estructura uniforme que incluye una descripci�n de la vista, su prop�sito, los elementos y relaciones que la componen, un diagrama de contexto, y cualquier mecanismo de variabilidad relevante. Este enfoque estandarizado facilita la lectura y comprensi�n de cada vista, proporcionando una referencia clara y consistente para los lectores.

## Architecture Background

### Problem Background

#### System Overview

Nebula es una plataforma basada en web que permite a los usuarios cargar archivos CSV, seleccionar caracter�sticas y etiquetas, y generar autom�ticamente modelos de regresi�n y clasificaci�n. El sistema tiene como objetivo simplificar el proceso de creaci�n, evaluaci�n de modelos para usuarios con diversos niveles de experiencia en ciencia de datos y sin necesidad de configurar infraestructuras locales complejas.

##### Funcionalidades Principales

* Carga de Datos: Los usuarios pueden cargar conjuntos de datos en formato CSV que el sistema procesar� para an�lisis.
* Selecci�n de Caracter�sticas y Etiquetas: La plataforma permite definir las caracter�sticas (variables independientes) y las etiquetas (variable objetivo) que ser�n utilizadas para el entrenamiento.
* Entrenamiento Autom�tico de Modelos: Nebula entrena modelos autom�ticamente para tareas de regresi�n o clasificaci�n, utilizando algoritmos de machine learning comunes.
* Evaluaci�n de Modelos en Tiempo Real: Los modelos generados son evaluados autom�ticamente, y se presentan m�tricas como precisi�n, error cuadr�tico medio, o puntuaci�n F1, seg�n corresponda.
* Visualizaci�n de Resultados: Gr�ficas e informes muestran la precisi�n del modelo y la importancia de cada caracter�stica en el modelo.
* Gesti�n de Usuarios y Seguridad: La aplicaci�n incluye un sistema de autenticaci�n y autorizaci�n para garantizar el manejo seguro de los datos de los usuarios.
Componentes Principales del Sistema
* Frontend (Interfaz de Usuario): Desarrollado en Next.js y React, provee una interfaz intuitiva y responsiva, adecuada para dispositivos de diferentes tama�os.
* Backend (API de Alto Rendimiento): Basado en FastAPI, se encarga de procesar las solicitudes del cliente, gestionar el entrenamiento de modelos y coordinar las interacciones con la base de datos.
* Base de Datos: Se utiliza PostgreSQL para el almacenamiento seguro y eficiente de los datos, como los conjuntos de datos de usuario y los modelos generados.
* M�dulo de Aprendizaje Autom�tico: Implementado con Scikit-learn, este m�dulo se encarga de la selecci�n de algoritmos y del entrenamiento de modelos de regresi�n o clasificaci�n.
* Capa de Contenedorizaci�n: Docker se utiliza para asegurar que cada componente del sistema se implemente de manera consistente en diferentes entornos.
Tecnolog�as Clave
* Frontend: Next.js, React
* Backend: FastAPI
* Base de Datos: PostgreSQL
* Machine Learning: Scikit-learn
* Autenticaci�n y Manejo de Sesiones: Auth.js
* Proxy Inverso: Nginx
* Contenedorizaci�n: Docker

Nebula est� dise�ado para ser escalable y modular, permitiendo una f�cil integraci�n de nuevas funcionalidades y mejoras a medida que evolucionen las necesidades de los usuarios.

#### Goals and Context

##### Objetivos del Proyecto

El objetivo principal de Nebula es proporcionar un sistema SaaS accesible y eficiente para la creaci�n y evaluaci�n de modelos de aprendizaje autom�tico, espec�ficamente para tareas de regresi�n y clasificaci�n. La plataforma est� dise�ada para usuarios con diversos niveles de experiencia en ciencia de datos, brindando una experiencia intuitiva y automatizada que permite crear modelos precisos sin necesidad de conocimientos avanzados en machine learning.

##### Objetivos Espec�ficos

* Simplificar el Proceso de Machine Learning: Automatizar la carga de datos, selecci�n de caracter�sticas y etiquetas, as� como el entrenamiento y evaluaci�n de modelos de regresi�n y clasificaci�n.
* Proveer una Interfaz Intuitiva y Eficaz: Dise�ar una interfaz de usuario intuitiva, adaptable a diferentes dispositivos, que permita a los usuarios interactuar f�cilmente con el sistema y obtener resultados visuales claros.
* Automatizar la Evaluaci�n de Modelos: Incorporar herramientas de visualizaci�n de resultados y de importancia de caracter�sticas, de forma que los usuarios puedan interpretar y mejorar los modelos sin complicaciones.
* Garantizar la Seguridad de los Datos: Implementar un sistema de autenticaci�n y gesti�n de sesiones que asegure el almacenamiento seguro de los datos del usuario y los modelos generados.
* Ofrecer Escalabilidad y Flexibilidad: Permitir la escalabilidad del sistema mediante el uso de contenedores y tecnolog�as modulares, facilitando el crecimiento y la adaptaci�n de la plataforma a nuevos requerimientos y funcionalidades.

##### Contexto del Proyecto

Nebula surge en un contexto donde la demanda por herramientas accesibles de machine learning est� en crecimiento. En la actualidad, el uso de machine learning es com�n en sectores como el financiero, sanitario, retail, y de tecnolog�a, donde se requiere tanto la predicci�n de valores continuos (regresi�n) como la clasificaci�n en categor�as.
La plataforma busca posicionarse como una herramienta que, adem�s de ser f�cil de usar, brinde un alto grado de flexibilidad y precisi�n. El proyecto utiliza tecnolog�as de desarrollo web modernas (React, FastAPI, PostgreSQL) y herramientas de aprendizaje autom�tico (Scikit-learn), lo cual permite que Nebula mantenga un rendimiento �ptimo y una experiencia de usuario fluida.

##### Usuarios Objetivo

* Analistas de Datos: Profesionales que desean utilizar modelos predictivos sin involucrarse en la complejidad de la programaci�n y el ajuste de modelos.
* Cient�ficos de Datos Principiantes: Usuarios que est�n aprendiendo machine learning y necesitan una plataforma que les permita experimentar con regresi�n y clasificaci�n de manera guiada.
* Empresas Peque�as y Medianas: Organizaciones que buscan integrar modelos de machine learning sin necesidad de desarrollar una infraestructura avanzada.

##### Alcance del Sistema en el Contexto Organizacional

Nebula est� dise�ado para servir tanto a usuarios individuales como a organizaciones. Permite la creaci�n de modelos en la nube, por lo que facilita la colaboraci�n y el acceso remoto a los modelos y resultados. En este contexto, la plataforma se posiciona como una soluci�n que combina el poder del machine learning con la accesibilidad de una aplicaci�n web intuitiva, de modo que organizaciones y usuarios puedan beneficiarse de sus capacidades predictivas con una inversi�n m�nima en infraestructura y experiencia t�cnica.

##### Significant Driving Requirements

Esta secci�n describe los requerimientos de comportamiento y atributos de calidad que influyeron directamente en la arquitectura de Nebula. Estos requerimientos son fundamentales para cumplir con los objetivos del sistema y proporcionar una experiencia de usuario �ptima en el contexto de creaci�n de modelos de regresi�n y clasificaci�n.

##### Requerimientos de Comportamiento

* Carga y Preprocesamiento de Datos: El sistema debe permitir a los usuarios cargar archivos CSV y realizar un preprocesamiento autom�tico de datos, garantizando que las caracter�sticas seleccionadas est�n listas para el entrenamiento.
* Entrenamiento de Modelos de Machine Learning: El sistema debe entrenar autom�ticamente modelos de regresi�n y clasificaci�n utilizando las caracter�sticas y etiquetas seleccionadas, con soporte para algoritmos populares y un proceso de entrenamiento optimizado para obtener resultados en tiempo real.
* Evaluaci�n de Modelos: Debe incluir una funcionalidad para evaluar el rendimiento de los modelos generados, proporcionando m�tricas clave como precisi�n, error cuadr�tico medio, y puntuaci�n F1.
* Visualizaci�n de Resultados: El sistema debe presentar los resultados del modelo de manera visual, incluyendo gr�ficos de precisi�n y visualizaci�n de la importancia de caracter�sticas, para facilitar la interpretaci�n y an�lisis por parte del usuario.
* Gesti�n de Usuarios y Seguridad de Datos: El sistema debe incluir autenticaci�n y autorizaci�n de usuarios, garantizando que los datos y modelos sean accesibles solo para los usuarios autorizados, cumpliendo con las normas de privacidad.

##### Requerimientos de Calidad

* Rendimiento y Escalabilidad: La arquitectura debe ser capaz de manejar m�ltiples solicitudes de entrenamiento de modelos de manera simult�nea sin afectar el rendimiento, siendo escalable para soportar un aumento en la base de usuarios.
* Usabilidad: La interfaz de usuario debe ser intuitiva y f�cil de navegar, permitiendo que usuarios con diferentes niveles de experiencia en machine learning puedan utilizar la plataforma sin dificultad.
* Confiabilidad y Disponibilidad: La plataforma debe estar disponible para los usuarios en todo momento y debe manejar de manera eficaz errores durante la carga de datos, preprocesamiento y entrenamiento de modelos.
* Mantenibilidad y Flexibilidad: La arquitectura debe estar dise�ada para permitir actualizaciones y mejoras en los algoritmos y funcionalidades de visualizaci�n, con un c�digo modular y bien documentado.
* Seguridad: La plataforma debe contar con medidas de seguridad, tanto en la autenticaci�n de usuarios como en el manejo de datos, protegiendo la informaci�n contra accesos no autorizados.

### Solution Background

#### Architectural Approaches

Para garantizar que Nebula cumpla con sus objetivos de rendimiento, escalabilidad y usabilidad, se han adoptado los siguientes enfoques arquitect�nicos:

* Arquitectura Basada en Servicios: La arquitectura del sistema se organiza en m�dulos funcionales separados, como el frontend, backend, base de datos y motor de machine learning. Estos m�dulos funcionan de manera independiente, comunic�ndose a trav�s de una API de alto rendimiento desarrollada en FastAPI, lo que permite una escalabilidad y mantenibilidad mejoradas.
* Contenedorizaci�n: Utilizando Docker, todos los componentes del sistema est�n contenedorizados para facilitar el despliegue y la consistencia en diversos entornos. Esto tambi�n permite que el sistema se escale horizontalmente, permitiendo ejecutar instancias adicionales de servicios en funci�n de la demanda.
* Componentizaci�n con Next.js y React en el Frontend: La interfaz de usuario se ha construido con Next.js y React, lo que permite una experiencia de usuario fluida y adaptable a diferentes dispositivos. La arquitectura basada en componentes hace que la interfaz sea modular, facilitando la implementaci�n de actualizaciones o nuevas funcionalidades.
* Machine Learning Modular con Scikit-Learn: Para el entrenamiento de modelos, se utiliza Scikit-Learn, una biblioteca modular y flexible de Python que permite implementar algoritmos de regresi�n y clasificaci�n. Esta elecci�n garantiza que el sistema pueda incorporar f�cilmente nuevos algoritmos en el futuro, manteniendo una arquitectura extensible y f�cilmente actualizable.
* Seguridad y Manejo de Sesiones: La autenticaci�n y la gesti�n de sesiones se implementan utilizando Redis para asegurar una gesti�n r�pida y eficiente de sesiones de usuario. La arquitectura est� dise�ada para proteger los datos de usuario y las credenciales con autenticaci�n segura, integrando tambi�n HTTPS y seguridad en las comunicaciones.

#### Requirements Coverage

La arquitectura de Nebula aborda los requisitos fundamentales del sistema en las siguientes �reas:

* Rendimiento: La arquitectura modular y escalable permite manejar un n�mero creciente de usuarios y solicitudes, garantizando tiempos de respuesta eficientes.
* Escalabilidad y Mantenibilidad: Gracias al uso de contenedores y una arquitectura orientada a servicios, el sistema puede actualizarse y ampliarse sin interrumpir la experiencia del usuario.
* Seguridad: Los mecanismos de autenticaci�n, manejo de sesiones y la implementaci�n de HTTPS protegen los datos de los usuarios.
* Usabilidad: La interfaz intuitiva construida con Next.js y React permite a los usuarios, sin importar su nivel de experiencia, navegar y utilizar la plataforma f�cilmente.

#### Summary of Background Changes Reflected in Current Version

Desde la versi�n inicial, Nebula ha experimentado una serie de mejoras arquitect�nicas y funcionales, en gran parte centradas en la optimizaci�n de la experiencia de usuario en el frontend, la integraci�n efectiva con el backend y el aseguramiento de una arquitectura escalable y eficiente. Estos cambios incluyen:

* Experiencia de Usuario Guiada e Intuitiva en el Frontend: Se ha mejorado la interfaz del usuario para guiarlo paso a paso en la carga de datos, selecci�n de variables y visualizaci�n de resultados. El flujo de trabajo permite que cualquier usuario, independientemente de sus conocimientos en ciencia de datos, pueda navegar de manera intuitiva. Gracias a Next.js y Material Design 3 en combinaci�n con componentes personalizados de Shadcn, la interfaz es atractiva y familiar, asegurando que los usuarios puedan concentrarse en los resultados sin sentirse abrumados por la complejidad del modelo.
* Optimizaci�n de Rendimiento con Next.js y Zustand: La estructura optimizada de Next.js mejora la carga de p�ginas y componentes. Adicionalmente, Zustand ha sido implementado para la gesti�n de estados, permitiendo una manipulaci�n eficiente de datos sin una jerarqu�a compleja de componentes. Esto reduce el tiempo de respuesta en la interfaz y asegura que la experiencia de usuario sea r�pida y sin interrupciones.
* Comunicaci�n As�ncrona con el Backend: Para optimizar la comunicaci�n entre el frontend y el backend (desarrollado en FastAPI), se integraron funciones as�ncronas (async/await) en el servidor de Next.js, lo cual facilita una interacci�n fluida con los datos y evita bloqueos en la interfaz. Esta implementaci�n asegura que la carga y procesamiento de datos se realice en tiempo real, con una visualizaci�n continua de los resultados.
* Soporte para Modelos de Evaluaci�n de M�tricas: Se a�adi� soporte para generar m�tricas de rendimiento avanzadas, tales como precisi�n, error cuadr�tico medio, y puntuaci�n F1, que permiten a los usuarios evaluar la efectividad de sus modelos y ajustar sus an�lisis seg�n sea necesario. Estas m�tricas se generan en el backend y se env�an al frontend para su visualizaci�n en tiempo real.
* Visualizaci�n Interactiva de la Importancia de Variables: Se ha incorporado una funcionalidad para que los usuarios puedan visualizar gr�ficamente la importancia de las variables predictoras en sus modelos, permitiendo una comprensi�n m�s profunda de c�mo cada factor influye en las predicciones. Los elementos interactivos en los gr�ficos ofrecen detalles espec�ficos de la importancia de cada variable, lo que permite a los usuarios explorar los resultados de manera m�s din�mica.
* Automatizaci�n del Entrenamiento de Modelos: El backend integra Scikit-Learn para el entrenamiento de modelos de machine learning, enfoc�ndose en algoritmos de regresi�n y clasificaci�n. El proceso de entrenamiento es completamente automatizado, permitiendo a los usuarios entrenar modelos sin configuraci�n manual. Los resultados se generan en tiempo real y se env�an al frontend para su visualizaci�n.
* Desaf�os T�cnicos y Dockerizaci�n de la Aplicaci�n: Uno de los mayores retos en esta versi�n fue la dockerizaci�n del frontend, asegurando as� que el entorno de desarrollo y producci�n sean consistentes. Docker se utiliz� para contenedorizaci�n, permitiendo una escalabilidad sencilla y un despliegue r�pido en distintos entornos, facilitando tambi�n la integraci�n con otros componentes de la arquitectura.
* Dockerizaci�n del Backend: Al igual que el frontend, el backend fue dockerizado para permitir una implementaci�n uniforme en distintos entornos, facilitando la gesti�n del sistema y mejorando la flexibilidad de la arquitectura para actualizaciones futuras.

### Product Line Reuse Considerations

La arquitectura de AG Nebula est� dise�ada para permitir la reutilizaci�n en una l�nea de productos de aplicaciones de machine learning, facilitando la creaci�n de variantes orientadas a diferentes tipos de usuarios o necesidades espec�ficas. La modularidad del sistema, que abarca componentes frontend y backend altamente desacoplados, permite la adaptaci�n de funcionalidades como la selecci�n de algoritmos, m�tricas de evaluaci�n y visualizaci�n de resultados sin impactar otros m�dulos. Esta flexibilidad permite integrar nuevos modelos de machine learning y a�adir caracter�sticas educativas para usuarios menos experimentados, adaptando as� la plataforma a mercados o sectores espec�ficos con m�nimos ajustes. Adem�s, el uso de tecnolog�as como Docker y Redis permite replicar y escalar f�cilmente la soluci�n en distintos entornos, optimizando el proceso de despliegue y asegurando consistencia y confiabilidad en cada versi�n de producto.

## Views

La arquitectura de software de Nebula se documenta a trav�s de varias vistas, cada una de las cuales describe un aspecto particular del sistema desde diferentes perspectivas. Estas vistas se estructuran de acuerdo con los puntos de vista identificados en la Secci�n 1.5, y est�n dise�adas para abordar los intereses y preocupaciones de los distintos stakeholders involucrados en el desarrollo y uso de Nebula.

### Vista de M�dulos

#### View Description - 1

La Vista de M�dulos representa la organizaci�n estructural del sistema en t�rminos de m�dulos o componentes principales. Cada m�dulo agrupa una funcionalidad espec�fica, lo que facilita la mantenibilidad y la escalabilidad del sistema al permitir que cada m�dulo pueda evolucionar independientemente.

#### View Packet Overview - 1

Los paquetes en esta vista representan las agrupaciones principales de funcionalidad en Nebula:

* M�dulo de Interfaz de Usuario: Gestiona la presentaci�n y la interacci�n con el usuario en el frontend, proporcionando una interfaz guiada e intuitiva.
* M�dulo de API Backend: Proporciona los servicios de backend a trav�s de FastAPI, gestionando la l�gica de negocio y las interacciones con la base de datos y el m�dulo de machine learning.
* M�dulo de Machine Learning: Implementa los algoritmos de clasificaci�n y regresi�n utilizando Scikit-Learn y gestiona los procesos de entrenamiento y evaluaci�n de modelos.
* M�dulo de Base de Datos: Almacena los datos del usuario, configuraciones y modelos en PostgreSQL, asegurando un acceso r�pido y seguro a la informaci�n persistente.

#### Variability Mechanisms - 1

Cada m�dulo es contenedorizado con Docker, lo que permite despliegues independientes y escalabilidad en funci�n de la demanda. Adem�s, la arquitectura permite la adici�n de nuevos algoritmos de machine learning en el M�dulo de Machine Learning sin impactar el resto del sistema.

### Vista de Componentes y Conectores

#### View Description - 2

La Vista de Componentes y Conectores muestra los elementos que interact�an en tiempo de ejecuci�n y los canales de comunicaci�n entre ellos. Esto incluye tanto componentes de frontend y backend como los conectores que permiten la comunicaci�n y flujo de datos entre ellos.

#### View Packet Overview - 2

Los principales paquetes en esta vista son:

* Componente de Interfaz de Usuario: Gestiona la interacci�n con el usuario, enviando solicitudes al backend y mostrando los resultados de los modelos.
* Conector de API REST: Act�a como un puente entre el frontend y el backend, facilitando las solicitudes HTTP y asegurando que la comunicaci�n se realice de forma segura.
* Componente de Entrenamiento de Modelos: Responsable de ejecutar los procesos de machine learning y gestionar los algoritmos de Scikit-Learn.
* Conector de Base de Datos: Permite que el backend acceda y actualice la informaci�n almacenada en PostgreSQL de manera segura.

#### Variability Mechanisms - 2

El diagrama de clases en esta vista ilustra c�mo est�n estructurados los principales componentes l�gicos del sistema y las relaciones entre ellos. Este diagrama muestra las clases clave, sus atributos, m�todos, y las asociaciones que existen entre ellas, proporcionando una visi�n clara de c�mo est�n organizados los datos y la l�gica del sistema. Adem�s, se detalla c�mo las diferentes clases colaboran para cumplir con las funcionalidades requeridas.

### Vista de Asignaci�n

#### View Description - 3

La Vista de Asignaci�n muestra la relaci�n entre los elementos de software de Nebula y los recursos f�sicos o virtuales donde se implementan, destacando la distribuci�n de los m�dulos en contenedores Docker y su despliegue en un entorno escalable en la nube.

#### View Packet Overview - 3

Los principales paquetes de esta vista incluyen:

* Asignaci�n de Contenedores Docker: Cada m�dulo se implementa en un contenedor Docker independiente, lo cual permite escalar el sistema horizontalmente y realizar actualizaciones sin afectar a otros componentes.
* Asignaci�n de Recursos en la Nube: Los contenedores Docker se implementan en un entorno de nube que permite una asignaci�n flexible de recursos seg�n la carga del sistema, optimizando el uso de CPU y memoria.

#### Variability Mechanisms - 3

La arquitectura de asignaci�n permite escalar o reducir los recursos de manera din�mica seg�n la demanda, facilitando el balanceo de carga en entornos de alta concurrencia.

## Relations Among Views

Las vistas presentadas en el SAD de Nebula proporcionan diferentes perspectivas del sistema, y aunque cada una de ellas presenta una parte distinta de la arquitectura, todas est�n interrelacionadas y deben ser entendidas de manera conjunta. En esta secci�n, se describen las relaciones entre las vistas seleccionadas y se abordan cualquier inconsistencia que pueda existir entre ellas, asegurando que las diferentes representaciones del sistema sean coherentes y complementarias.

### General Relations Among Views

Las vistas documentadas en este SAD est�n relacionadas de la siguiente manera:

* Vista de M�dulos y Vista de Componentes y Conectores: La vista de m�dulos describe la estructura est�tica del sistema, dividiendo la funcionalidad del sistema en unidades modulares. Estas unidades, definidas en la vista de m�dulos, se implementan como componentes en la vista de componentes y conectores.
* Vista de Componentes y Conectores y Vista de Asignaci�n: La vista de componentes y conectores se complementa con la vista de asignaci�n, que muestra c�mo los componentes del sistema se distribuyen y se ejecutan en el hardware y otros recursos del entorno. Los componentes representados en la vista de componentes y conectores est�n asignados a unidades de procesamiento (como servidores o contenedores) en la vista de asignaci�n.
* Vista de M�dulos y Vista de Asignaci�n: Aunque la vista de m�dulos se centra en la estructura l�gica del sistema, la vista de asignaci�n proporciona informaci�n sobre c�mo esa estructura se distribuye en la infraestructura f�sica. La relaci�n entre ambas vistas asegura que los m�dulos definidos en el sistema se asignen correctamente a los recursos de hardware, garantizando el rendimiento y la escalabilidad.
* Vista de Variabilidad: Las vistas de variabilidad en el sistema permiten modificar ciertos aspectos de la arquitectura seg�n las necesidades del entorno o del usuario final. Estas variaciones pueden afectar tanto a la vista de m�dulos como a la de componentes y conectores, permitiendo adaptar la arquitectura para nuevos requisitos sin afectar la estructura fundamental del sistema.

### View-to-View Relations

Para proporcionar una visi�n coherente de la arquitectura, es crucial entender c�mo las diferentes vistas se relacionan entre s�. Las principales relaciones entre las vistas del sistema Nebula son las siguientes:

* Relaci�n entre la Vista de M�dulos y la Vista de Componentes y Conectores: La vista de m�dulos se enfoca en la estructura l�gica y la divisi�n de las funcionalidades en unidades aut�nomas, mientras que la vista de componentes y conectores describe c�mo esas unidades de software interact�an en tiempo de ejecuci�n. Los m�dulos definidos en la vista de m�dulos se representan como componentes en la vista de componentes, y las relaciones entre ellos se modelan como conectores, que representan los puntos de interacci�n entre los componentes. Esta relaci�n permite entender c�mo la estructura l�gica se materializa en la arquitectura de ejecuci�n.
* Relaci�n entre la Vista de Componentes y Conectores y la Vista de Asignaci�n: Los componentes definidos en la vista de componentes y conectores son asignados a los recursos del sistema en la vista de asignaci�n. Esto incluye la asignaci�n de componentes a servidores, contenedores y otros elementos de infraestructura. La relaci�n entre ambas vistas asegura que cada componente est� bien distribuido en el entorno de ejecuci�n, de modo que el sistema pueda escalar y ejecutarse eficientemente en diferentes plataformas.
* Relaci�n entre la Vista de M�dulos y la Vista de Asignaci�n: Aunque ambas vistas abordan aspectos diferentes de la arquitectura (la vista de m�dulos se enfoca en la estructura l�gica y la vista de asignaci�n en la distribuci�n f�sica), es crucial que exista una correspondencia entre los m�dulos y los recursos de hardware en los que se ejecutan. Esto asegura que los m�dulos sean implementados correctamente y que el sistema sea capaz de cumplir con los requisitos de rendimiento y escalabilidad.
* Relaci�n entre la Vista de Variabilidad y las Otras Vistas: Las vistas de variabilidad permiten adaptar la arquitectura a diferentes contextos y necesidades. Las variaciones pueden incluir la elecci�n de algoritmos de machine learning, el n�mero de servidores, o la configuraci�n de modelos de entrenamiento. Estas variaciones se reflejan tanto en la vista de m�dulos como en la de componentes y conectores, permitiendo que el sistema sea flexible y pueda ajustarse a diferentes entornos de ejecuci�n sin necesidad de redise�ar la arquitectura completa.

## Directory

### Index

Este �ndice proporciona una lista completa de todos los nombres de elementos, relaciones y propiedades definidas a lo largo del Documento de Arquitectura de Software (SAD) de Nebula. Para cada entrada, se incluye la ubicaci�n en el documento donde se define y los lugares en los que se utiliza, permitiendo una navegaci�n eficiente hacia cualquier parte del contenido relacionado.
Elementos

### Frontend

* Definici�n: El componente de la arquitectura encargado de la interfaz de usuario, desarrollado con Next.js.
* Ubicaci�n en el SAD: Secci�n 2.1.1 (Componentes del Sistema)
* Usado en: Secci�n 3.1 (Vista de Arquitectura de Frontend)

### Backend

* Definici�n: El componente encargado de la l�gica de negocio, el procesamiento de datos y la interacci�n con la base de datos, desarrollado en FastAPI.
* Ubicaci�n en el SAD: Secci�n 2.1.1 (Componentes del Sistema)
* Usado en: Secci�n 3.2 (Vista de Arquitectura del Backend)

### API

* Definici�n: Interfaz que conecta el frontend con el backend y permite la comunicaci�n entre los diferentes m�dulos del sistema.
* Ubicaci�n en el SAD: Secci�n 2.2.1 (Enfoques Arquitect�nicos)
* Usado en: Secci�n 3.2.2 (Interacci�n entre Componentes)

### Relaciones

#### Comunicaci�n Frontend-Backend

* Definici�n: Relaci�n de interacci�n entre el frontend y el backend a trav�s de llamadas a la API usando funciones as�ncronas.
* Ubicaci�n en el SAD: Secci�n 2.2.1 (Enfoques Arquitect�nicos)
* Usado en: Secci�n 3.2.2 (Interacci�n entre Componentes)

#### Escalabilidad

* Definici�n: Relaci�n que asegura que el sistema pueda soportar un mayor n�mero de usuarios y solicitudes de forma eficiente.
* Ubicaci�n en el SAD: Secci�n 2.2.1 (Enfoques Arquitect�nicos)
* Usado en: Secci�n 3.1 (Vista de Arquitectura del Frontend) y Secci�n 3.2 (Vista de Arquitectura del Backend)

#### Modularidad

* Definici�n: Propiedad del sistema que permite que sus componentes sean independientes y f�cilmente actualizables sin afectar el sistema en su totalidad.
* Ubicaci�n en el SAD: Secci�n 2.2.1 (Enfoques Arquitect�nicos)
* Usado en: Secci�n 3.1.1 (Descripci�n de la Vista del Frontend) y Secci�n 3.2.1 (Descripci�n de la Vista del Backend)

#### Interactividad

* Definici�n: Propiedad del sistema que permite a los usuarios interactuar con la interfaz de manera din�mica, especialmente en la visualizaci�n de resultados y la selecci�n de variables.
* Ubicaci�n en el SAD: Secci�n 2.1.3 (Componentes del Sistema)
* Usado en: Secci�n 3.1.4 (Mecanismos de Variabilidad en el Frontend)

### Glossary

* API (Interfaz de Programaci�n de Aplicaciones) se definen como conjunto de reglas y protocolos que permiten que diferentes software se comuniquen entre s�. En Nebula, las APIs permiten la interacci�n entre el frontend y el backend.
* Contenerizaci�n. Proceso de encapsular una aplicaci�n y sus dependencias en un contenedor para garantizar que se ejecute de manera consistente en diferentes entornos, como desarrollo, pruebas y producci�n. En Nebula, Docker se utiliza para contenerizar tanto el frontend como el backend.
* FastAPI. Framework web de Python utilizado para construir APIs r�pidas y de alto rendimiento. Es utilizado en Nebula para gestionar las solicitudes del frontend y procesar las operaciones de machine learning.
* Machine Learning (ML) Subcampo de la inteligencia artificial que permite a las m�quinas aprender patrones y realizar predicciones sin necesidad de programaci�n expl�cita. Nebula permite la creaci�n y entrenamiento de modelos de ML para tareas de clasificaci�n y regresi�n.
* Next.js. Framework de React para la creaci�n de aplicaciones web optimizadas. Se utiliza en Nebula para construir la interfaz de usuario, aprovechando sus capacidades de renderizado en el lado del servidor y la optimizaci�n autom�tica del rendimiento.
* PostgreSQL. Sistema de gesti�n de bases de datos relacional que se utiliza para almacenar datos persistentes en Nebula, como los conjuntos de datos cargados por los usuarios y los modelos generados.
* Redis. Sistema de almacenamiento en cach� en memoria que se usa para mejorar el rendimiento del backend, especialmente en la gesti�n de sesiones de usuarios en Nebula.
* Scikit-learn. Biblioteca de Python para la creaci�n y entrenamiento de modelos de machine learning. En Nebula, se utiliza para entrenar y evaluar modelos de regresi�n y clasificaci�n.
* Zustand. Librer�a de gesti�n de estado para aplicaciones React que permite gestionar de manera eficiente el estado global de la aplicaci�n en Nebula sin necesidad de pasar datos a trav�s de propiedades entre componentes.
* Docker. Plataforma para el desarrollo, env�o y ejecuci�n de aplicaciones en contenedores. Se utiliza en Nebula para garantizar que los componentes del sistema funcionen de manera consistente en diferentes entornos.
* Modelos de Regresi�n y Clasificaci�n. Tipos de modelos de machine learning utilizados para predecir valores continuos (regresi�n) o para asignar etiquetas a entradas (clasificaci�n). Nebula est� dise�ado para entrenar y evaluar estos tipos de modelos.
* API As�ncrona (Async API). Un tipo de API que permite que las solicitudes se gestionen sin bloquear la ejecuci�n del resto del sistema. En Nebula, se utiliza para permitir una comunicaci�n fluida y eficiente entre el frontend y el backend.
* Material Design 3. Un sistema de dise�o desarrollado por Google que proporciona directrices sobre la apariencia y el comportamiento de las interfaces de usuario. Nebula implementa este dise�o en su frontend para garantizar una interfaz limpia y coherente.

### Acronym List

* API. Application Programming Interface; Application Program Interface; Application Programmer Interface(Interfaz de Programaci�n de Aplicaciones)
* JSON. JavaScript Object Notation (Notaci�n de Objetos de JavaScript)
* ML. Machine Learning (Aprendizaje Autom�tico)
* SAD. Software Architecture Document (Documento de Arquitectura de Software)
