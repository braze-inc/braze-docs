---
nav_title: Perguntas frequentes
article_title: Perguntas frequentes sobre Currents
page_order: 9
page_type: reference
description: "Este artigo aborda algumas das perguntas mais frequentes que surgem ao configurar o Braze Currents."
tool: Currents
---

# Perguntas frequentes

> Esta página fornece respostas a algumas perguntas frequentes sobre o Currents.

### Como faço para obter dados históricos?

O Currents é um fluxo de dados ao vivo e em tempo real, o que significa que os eventos não podem ser reproduzidos. No entanto, é possível armazenar os dados do Currents em um data warehouse, como o [Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3/) ou [o Microsoft Azure Blob Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents/), para que você possa agir com base em eventos passados conforme achar necessário. Os dados são retidos por 30 dias, mas para obter mais dados históricos, você pode consultar [o Snowflake]({{site.baseurl}}/user_guide/data/braze_currents/s3_to_snowflake/).

### Por que o Currents gera dados no formato Avro, e não em JSON?

O Avro, ao contrário do JSON sem esquema, suporta nativamente a evolução do esquema. Você também se beneficiará da capacidade de enviar arquivos Avro com menos largura de banda e economizar espaço de armazenamento, pois o Avro é altamente compactável.

### Como o Braze lida com a sobrecarga de arquivos?

Criamos um processo de extração, transformação e carga (ETL), que permite extrair grandes quantidades de dados de um banco de dados para colocá-los e armazená-los em outro.

### Onde devo armazenar esses dados para consulta?

O Braze tem parceria com vários data warehouses nos quais você pode armazenar seus dados para consulta. Recomendamos o uso:
- [Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3/)
- [Armazenamento de Blob do Microsoft Azure]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents/)
- [Google Cloud Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/google_cloud_storage_for_currents/).