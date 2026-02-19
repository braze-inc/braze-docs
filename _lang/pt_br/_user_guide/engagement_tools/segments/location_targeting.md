---
nav_title: Direcionamento do local
article_title: Direcionamento por local
page_order: 10
page_type: tutorial
tool: 
- Segments
- Location
description: "Este artigo explica como configurar o direcionamento por local, permitindo segmentar os usuários por local."

---

# Direcionamento do local

> Este artigo o orientará sobre como configurar o direcionamento por local, permitindo segmentar os usuários pelo local mais recente. Isso é perfeito para quem está procurando campanhas e estratégias baseadas em locais.

## Etapa 1: Crie seu segmento

Navegue até a página **Segments (Segmentos** ), em **Audience (Público**), para visualizar todos os segmentos de usuários atuais. Nesta página, você pode criar e nomear novos segmentos. Para começar, selecione **Create Segment (Criar segmento** ) e dê um nome ao seu segmento.

![Modal para criar um segmento.]({% image_buster /assets/img_archive/createsegment2.png %}){: style="max-width:70%;"}

## Etapa 2: Personalize seu local

Depois de criar seu segmento, adicione um filtro **Most Recent Location (Local mais recente** ) para direcionar os usuários pelo último local em que usaram seu app. Você tem a opção de destacar os usuários dentro ou fora de uma região circular padrão ou de uma região poligonal personalizável.

![Filtre o local mais recente em um círculo.]({% image_buster /assets/img_archive/filter_recent_location.png %})

{% tabs %}
{% tab Circular %}

### Regiões circulares

Para regiões circulares, você pode mover a origem e ajustar o raio do local para a segmentação.

![Um contorno circular de cidades entre Nova Jersey e Nova York.]({% image_buster /assets/img_archive/location_circle.png %}){: style="max-width:70%;"}

{% endtab %}
{% tab Polygonal %}

### Regiões poligonais

Para regiões poligonais, você pode designar mais especificamente quais áreas deseja incluir no seu segmento.

![Um contorno do estado de Nova York como a região poligonal selecionada.]({% image_buster /assets/img_archive/create_polygon.png %}){: style="max-width:70%;"}

{% endtab %}
{% endtabs %}

## Suporte de parceria para beacon e geofence

A combinação do suporte a beacon ou geofence existente com nossos recursos de direcionamento e envio de mensagens fornece mais informações sobre as ações físicas dos usuários para que você possa enviar mensagens de acordo com elas. Você pode aproveitar o monitoramento de localização com alguns de nossos parceiros: 

- [Radar]({{site.baseurl}}/partners/message_personalization/location/radar/)
- [Infillion]({{site.baseurl}}/partners/message_personalization/location/infillion/)
- [Foursquare]({{site.baseurl}}/partners/message_personalization/location/foursquare/)

