---
nav_title: Migrando do feed de notícias
article_title: Migrando do feed de notícias
page_order: 10
description: "Este artigo de referência fornece orientação sobre a migração do Feed de notícias para os cartões de conteúdo do Braze."
channel:
  - content cards
  - news feed
  
---

# Migração do feed de notícias para cartões de conteúdo

{% alert note %}
O feed de notícias será descontinuado. A Braze recomenda que os clientes que usam nossa ferramenta de feed de notícias migrem para o canal de envio de mensagens Content Cards - é mais flexível, personalizável e confiável.
{% endalert %}

> A mudança do Feed de notícias para os cartões de conteúdo leva tempo, mas fácil de adotar. Não é possível migrar automaticamente o conteúdo do Feed de notícias para os cartões de conteúdo - você deve integrar os cartões de conteúdo do zero. No entanto, com a nova flexibilidade dos cartões de conteúdo, não achamos que você sentirá falta ou se importará com isso.

Entre em contato com seu gerente de conta da Braze para saber mais.

## Recursos e funcionalidade

Os cartões de conteúdo oferecem muitos recursos que não são compatíveis com o feed de notícias, como opções adicionais de entrega, como entrega baseada em ação e API, e análise de dados aprimorada, como rastreamento de conversões.

Ao planejar sua migração do Feed de notícias para os cartões de conteúdo, será importante notar as principais diferenças entre os cartões de conteúdo e o Feed de notícias:

- **Segmentação:** A segmentação dos cartões de conteúdo pode ser avaliada no momento em que as mensagens são enviadas ou no momento em que o cartão é visualizado pela primeira vez. A segmentação do Feed de notícias é avaliada no momento em que os cartões do Feed de notícias são visualizados.
- **Personalização:** A personalização dos cartões de conteúdo pode ser modelada no momento em que as mensagens são enviadas ou no momento em que o cartão é visualizado pela primeira vez. A personalização do cartão do Feed de notícias é modelada no momento em que os cartões do Feed de notícias são visualizados.

A tabela a seguir descreve mais detalhadamente a diferença nos recursos suportados entre o Feed de notícias e os cartões de conteúdo:

| Recurso | Feed de notícias | Cartões de conteúdo |
|---|---|---|
| Campanhas multivariantes e multicanais | <i class="fas fa-times" title="Não compatível"></i> | <i class="fas fa-check" title="Com suporte"></i> |
| Entrega programada, baseada em ação e baseada em API | <i class="fas fa-times" title="Não compatível"></i> | <i class="fas fa-check" title="Com suporte"></i> |
| Envios de mensagens criadas pela API | <i class="fas fa-times" title="Não compatível"></i> | <i class="fas fa-check" title="Com suporte"></i> |
| Testes A/B | <i class="fas fa-times" title="Não compatível"></i> | <i class="fas fa-check" title="Com suporte"></i> |
| [Descarte e fixação de cartões][4] | <i class="fas fa-times" title="Não compatível"></i> | <i class="fas fa-check" title="Com suporte"></i> |
| [Análise avançada de dados][3] (por exemplo, rastreamento de conversões) | <i class="fas fa-times" title="Não compatível"></i> | <i class="fas fa-check" title="Com suporte"></i> |
| [Disponível em canvas][2] | <i class="fas fa-times" title="Não compatível"></i> | <i class="fas fa-check" title="Com suporte"></i> |
| [Conteúdo conectado][5] | <i class="fas fa-times" title="Não compatível"></i> | <i class="fas fa-check" title="Com suporte"></i> |
| Personalização e segmentação | Modelo na impressão | Modelado no envio ou na primeira impressão |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Implementação

- Os cartões de conteúdo e o feed de notícias são produtos separados, portanto, é necessária uma integração simples com seu app ou site para usar os cartões de conteúdo.
- Se desejar, os cartões de feed de notícias existentes precisarão ser migrados manualmente para campanhas de cartão de conteúdo quando você mudar.
- Os cartões de conteúdo não se destinam a ser usados ao mesmo tempo que o feed de notícias, pois substituem o feed de notícias.
- Atualmente, os cartões de conteúdo não oferecem suporte a categorias. As categorias podem ser obtidas por meio de [personalização e pares de valores-chave][1].


[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/content_cards/multiple_feeds/
[2]: {{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/content-cards_in_canvas/
[3]: {{site.baseurl}}/user_guide/message_building_by_channel/content_cards/reporting/
[4]: {{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/#step-2-compose-a-content-card
[5]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/
