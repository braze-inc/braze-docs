---
nav_title: Exportación de grandes segmentos
article_title: Exportación de grandes segmentos
page_order: 4

page_type: solution
description: "Este artículo de ayuda te guía a través de varios métodos para exportar grandes segmentos de usuarios."
tool: Segments
---

# Exportación de grandes segmentos

Existen varios métodos para exportar un gran segmento de usuarios. Para los segmentos que contengan más de 500.000 usuarios, puedes desglosar este segmento mayor en segmentos más pequeños para capturar a estos usuarios, y exportar cada uno de los segmentos más pequeños desde el panel Braze. 

También puedes considerar el uso de [números de contenedor aleatorios]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/ab_testing_with_random_buckets/#step-1-segment-your-users-by-the-random-bucket-attribute) para dividir tu base de usuarios en varios segmentos, y combinarlos después de la exportación. Por ejemplo, si necesitas dividir tu segmento en dos segmentos diferentes, puedes hacerlo con los siguientes filtros:
- Segmento 1: El número de contenedor aleatorio es inferior a 5000 (incluye 0-4999)
- Segmento 2: El número de contenedor aleatorio es superior a 4999 (incluye 5000-9999)

También puedes aprovechar los siguientes puntos finales para exportar datos de usuario de un segmento específico. Ten en cuenta que estos puntos finales están sujetos a límites de datos.
- [`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/)
- [`/users/export/global_control_group`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group/)

¿Aún necesitas ayuda? Abre un [ticket de soporte]({{site.baseurl}}/braze_support/).

_Última actualización: 24 de octubre de 2022_
