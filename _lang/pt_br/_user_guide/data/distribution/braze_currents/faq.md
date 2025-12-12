---
nav_title: FAQ
article_title: FAQ de Currents
page_order: 9
page_type: reference
description: "Este artigo aborda algumas das perguntas mais frequentes que surgem ao configurar o Braze Currents."
tool: Currents
---

# Perguntas frequentes

> Esta página fornece respostas a algumas perguntas frequentes sobre Currents.

### Como obtenho dados históricos?

Currents é um fluxo de dados em tempo real, o que significa que os eventos não podem ser reproduzidos. No entanto, você pode armazenar os dados do Currents em um data warehouse como [Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3/) ou [Microsoft Azure Blob Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents/), para que você possa agir sobre eventos passados conforme achar necessário. Os dados são retidos por 30 dias, mas para mais dados históricos, você pode consultar [Snowflake]({{site.baseurl}}/user_guide/data/braze_currents/s3_to_snowflake/).

### Por que o Currents gera dados no formato Avro, e não em JSON?

Avro, ao contrário do JSON sem esquema, suporta nativamente a evolução do esquema. Você também se beneficiará da capacidade de enviar arquivos Avro com menos largura de banda e espaço de armazenamento economizado, pois o Avro é altamente compactável.

### Como o Braze lida com a sobrecarga de arquivos?

Construímos um processo de Extração, Transformação e Carga (ETL), que permite que você extraia grandes quantidades de dados de um banco de dados para colocar e armazenar em outro.

### Onde devo armazenar esses dados para consulta?

O Braze é parceiro de vários data warehouses onde você pode armazenar seus dados para consulta. Recomendamos usar:
- [Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3/)
- [Microsoft Azure Blob Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents/)
- [Google Cloud Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/google_cloud_storage_for_currents/).