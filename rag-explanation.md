# RAG

## ¿Cómo funciona la técnica RAG?

Los modelos LLMs mayormente son utilizados mayormente para resolver las preguntas que tenga un usuario (Q&A) con chatbots. Sin embargo, existe la limitación de querer hacer un chatbot personalizado, con información más especifica de, por ejemplo, una empresa. Para conseguir esto no es tan sencillo como parece, no se entrenará un nuevo LLM con la información en especifico de la empresa, o se reentrenará con esta nueva información, porque esto es un proceso muy demandante computacionalmente y puede no ser efectivo siempre; ni tampoco está muy bien hecho pasarle toda la información como se hizo en el ejemplo anterior ([aquí](./01-rag/rag.ipynb)), porque la información que se está pasando no toda es útil para responder la pregunta que hace el usuario, por lo que, es necesario optimizar este proceso, y aquí es donde la técnica RAG (Retrieval Augmented Generation) toma importancia.

De manera muy general, la forma más sencilla de saber cómo funciona esta técnica es como se ve en la imagen de abajo
<image src="./img/rag.png" alt="RAG Pipeline">

En la anterior imagen, se sigue el siguiente paso a paso: se hace la pregunta, se extrae la información relevante de todos la fuente de información y se les pasa al modelo, para así generar una respuesta al usuario.

Pero entonces, nacen las preguntas de, ¿cómo se logra que todo funcione bien? ¿Cómo se extrae la información? ¿Cómo se guarda la información?

De lo anterior, sacamos los dos siguientes componentes vítales: Indexación y Recuperación.

## Indexación

La indexación no es más que cómo se guardan los datos. Usualmente en esta fase se mencionan conceptos como "Document Loaders", "Text Splitters", "Vector Stores" y "Embeddings Models". En la siguiente imagen se ve un vistazo general de cómo sería el Pipeline que se sigue.
<image src="./img/rag-indexing-pipeline.png" alt="RAG Indexing pipeline">

De manera muy general, el primer paso que se hace es cargar todos los documentos, aquí es dónde se utilizan los "Document Loaders". Luego, con la intención de no pasarle información demás al modelo, la información extraida se divide en pequeños chunks, utilizando "Text Splitters". Finalmente, con ayuda de los modelos de Embedding, se convierten estos pedacitos de texto en vectores, los cuales son guardados en una base de datos de Vectores ("Vector Store").

## Recuperación

Para la "recuperación", se toman los vectores que están más asociados a la pregunta del usuario con ayuda de un "Retriever", para finalmente, con toda la información recopilada, se hace el prompt al LLM, y ahí es cuando se genera la respuesta. En la siguiente imagen, se puede ver el paso a paso que se sigue de manera visual.
<image src="./img/rag-retrieve_and_generation-pipeline.png" alt="RAG Retrieval and Generation pipeline">

Para la generación de la respuesta se usa un LLM ya entrenado previamente, ya sea el caso de GPT, Claude, Llama, etc.
