---
nav_title: Rastreamento de cancelamentos de inscrição por push
article_title: Rastreamento de cancelamentos de inscrição por push
page_type: solution
description: "Este artigo de ajuda fornece algumas dicas para rastrear cancelamentos de inscrição por push."
channel: push
---

# Rastreamento de cancelamentos de inscrição por push

Os cancelamentos de inscrição por push dependem de atualizações no status de push de um usuário de provedores como a Apple ou o Google. Essas atualizações podem ser pouco frequentes e imprevisíveis. Como resultado, os cancelamentos de inscrição por push não são incluídos como uma métrica na análise de dados da campanha por push. 

No entanto, o rastreamento manual de cancelamentos de inscrição por push ainda pode fornecer insights valiosos sobre as respostas dos usuários à frequência das notificações e à relevância do conteúdo. Aqui estão duas opções para rastreamento de cancelamentos de inscrição por push.

## Opção 1: Usar filtros de segmento

Como solução alternativa, é possível criar um segmento para identificar os usuários que não estão ativados para push, o que significa que eles não estão inscritos ou não têm aceitação e não têm um [token de push em primeiro plano]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_registration/#push-tokens). Por exemplo, para ver o número de cancelamentos de inscrição em seu app para Android, você usaria a combinação dos seguintes segmentos: 

- `Background or Foreground Push Enabled for App "TEST (Android)" is false`
- `Has Uninstalled`

![A seção Criador de segmentos com o filtro "Background or Foreground Push Enabled for App" para o app TEST (Android) é falsa, e o filtro "Has Uninstalled" é selecionado para mostrar 2.393 usuários acessíveis.]({% image_buster /assets/img/push_unsub_segment_example.png %})

Note que os filtros de segmentação serão aproximados e não podem ser especificamente vinculados a uma data e campanha.

## Opção 2: Use um evento personalizado

{% alert important %}
Esteja ciente de que o registro de um evento personalizado para alteração de inscrição consumirá [pontos de dados]({{site.baseurl}}/user_guide/data_and_analytics/data_points#consumption-count). Como alternativa, use filtros de segmento para identificar e direcionar usuários que não estejam com a capacitação push ativada.
{% endalert %}

Para uma solução alternativa, também recomendamos a criação de um evento personalizado para cancelamentos de inscrição por push com base no fato de o status de capacitação por push de um usuário ser `true` ou `false` para rastrear essa métrica.

_Última atualização em 13 de junho de 2024_
