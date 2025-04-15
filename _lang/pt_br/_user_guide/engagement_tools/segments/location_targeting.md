---
nav_title: Direcionamento por local
article_title: Direcionamento por local
page_order: 6.5
page_type: tutorial
tool: 
- Segments
- Location
description: "Este artigo explica como configurar o direcionamento por local, permitindo segmentar os usuários por local."

---

# Direcionamento do local

> Este artigo o orientará sobre como configurar o direcionamento por local, permitindo segmentar os usuários pelo local mais recente. Isso é perfeito para quem está procurando campanhas e estratégias baseadas em locais.

## Etapa 1: Crie seu segmento

Navegue até a página **Segments (Segmentos** ), em **Audience (Público**), para visualizar todos os segmentos de usuários atuais. Nessa página, você pode criar e nomear novos segmentos. Para começar, clique em **Create Segment (Criar segmento** ) e dê um nome ao seu segmento.

{% alert note %}
Se estiver usando a [navegação mais antiga]({{site.baseurl}}/navigation), **Segments** está localizado em **Engagement (Engajamento**).
{% endalert %}

![][1]{: style="max-width:70%;"}

## Etapa 2: Personalize seu local

Depois de criar seu segmento, adicione um filtro **Most Recent Location (Local mais recente** ) para direcionar os usuários pelo último local em que usaram seu app. Você tem a opção de destacar os usuários em uma região circular padrão ou em uma região poligonal personalizável.

![][2]

### Regiões circulares

Para regiões circulares, você pode mover a origem e ajustar o raio do local para a segmentação.

![Um contorno circular de cidades entre Nova Jersey e Nova York.][3]{: style="max-width:70%;"}

### Regiões poligonais

Para regiões poligonais, você pode designar mais especificamente quais áreas deseja incluir no seu segmento.

![Um contorno do estado de Nova York como a região poligonal selecionada.][4]{: style="max-width:70%;"}

## Suporte de parceria para beacon e geofence

A combinação do suporte a beacon ou geofence existente com nossos recursos de direcionamento e envio de mensagens fornece mais informações sobre as ações físicas dos usuários para que você possa enviar mensagens de acordo com elas. Você pode aproveitar o monitoramento de localização com alguns de nossos parceiros: 

- [Radar]({{site.baseurl}}/partners/message_personalization/location/radar/)
- [Infillion]({{site.baseurl}}/partners/message_personalization/location/infillion/)
- [Foursquare]({{site.baseurl}}/partners/message_personalization/location/foursquare/)

[1]: {% image_buster /assets/img_archive/createsegment2.png %}
[2]: {% image_buster /assets/img_archive/filter_recent_location.png %}
[3]: {% image_buster /assets/img_archive/location_circle.png %}
[4]: {% image_buster /assets/img_archive/create_polygon.png %}
