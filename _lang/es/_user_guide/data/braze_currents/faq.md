---
nav_title: Preguntas frecuentes
article_title: Currents FAQ
page_order: 9
page_type: reference
description: "Este artículo aborda algunas de las preguntas más frecuentes que surgen al configurar Braze Currents."
tool: Currents
---

# Preguntas más frecuentes

> Esta página ofrece respuestas a algunas preguntas frecuentes sobre Currents.

### ¿Cómo obtengo datos históricos?

Currents es una transmisión de datos en vivo y en tiempo real, lo que significa que los acontecimientos no pueden repetirse. Sin embargo, puedes almacenar los datos de Currents en un almacén de datos como [Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3/) o [Microsoft Azure Blob Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents/), para que puedas actuar sobre eventos pasados según te convenga. Los datos se conservan durante 30 días, pero para obtener más datos históricos, puedes consultar [Snowflake]({{site.baseurl}}/user_guide/data/braze_currents/s3_to_snowflake/).

### ¿Por qué Currents emite los datos en formato Avro y no JSON?

Avro, a diferencia de JSON sin esquema, admite de forma nativa la evolución del esquema. También te beneficiarás de la posibilidad de enviar archivos Avro con menos ancho de banda y ahorrando espacio de almacenamiento, porque Avro es altamente compresible.

### ¿Cómo gestiona Braze la sobrecarga de archivos?

Creamos un proceso de Extraer, Transformar, Cargar (ETL), que te permite extraer grandes cantidades de datos de una base de datos para colocarlos y almacenarlos en otra.

### ¿Dónde debo almacenar estos datos para su consulta?

Braze está asociado con varios almacenes de datos en los que puedes guardar tus datos para realizar consultas. Recomendamos utilizar:
- [Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3/)
- [Almacenamiento Blob de Microsoft Azure]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents/)
- [Google Cloud Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/google_cloud_storage_for_currents/).