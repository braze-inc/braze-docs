---
nav_title: Exportação de grandes segmentos
article_title: Exportação de grandes segmentos
page_order: 4

page_type: solution
description: "Este artigo de ajuda o orienta por vários métodos de exportação de grandes segmentos de usuários."
tool: Segments
---

# Exportação de grandes segmentos

Há vários métodos para exportar um grande segmento de usuários. Para segmentos que contêm mais de 500.000 usuários, é possível dividir esse segmento maior em segmentos menores para capturar esses usuários e exportar cada um dos segmentos menores do dashboard do Braze. 

Você também pode considerar o uso de [números aleatórios]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/ab_testing_with_random_buckets/#step-1-segment-your-users-by-the-random-bucket-attribute) para dividir sua base de usuários em vários segmentos e, em seguida, combiná-los após a exportação. Por exemplo, se você precisar dividir seu segmento em dois segmentos diferentes, poderá fazer isso com os seguintes filtros:
- Segmento 1: O número do intervalo aleatório é menor que 5000 (inclui 0-4999)
- Segmento 2: O número do intervalo aleatório é maior que 4999 (inclui 5000-9999)

Também é possível aproveitar os seguintes pontos de extremidade para exportar dados de usuários para um segmento específico. Note que esses endpoints estão sujeitos a limites de dados.
- [`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/)
- [`/users/export/global_control_group`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group/)

Ainda precisa de ajuda? Abra um [tíquete de suporte]({{site.baseurl}}/braze_support/).

_Última atualização em 24 de outubro de 2022_
