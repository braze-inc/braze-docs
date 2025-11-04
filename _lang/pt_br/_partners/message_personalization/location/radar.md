---
nav_title: Radar
article_title: Radar
alias: /partners/radar/
description: "Este artigo de referência descreve a parceria entre a Braze e a Radar, uma plataforma de geofencing, para adicionar contexto de local e rastreamento aos seus aplicativos para iOS e Android."
page_type: partner
search_tag: Partner

---

# Radar

> [Radar](https://www.onradar.com/) é a principal plataforma de geofencing e monitoramento de localização. A plataforma Radar possui três produtos principais: [Geofences](https://radar.io/product/geofencing), [Trip Tracking](https://radar.io/product/trip-tracking) e [Geo APIs](https://radar.io/product/api).  Isso inclui rastreamento de coleta e entrega, notificações acionadas por local, personalização contextual, verificação de local, localizadores de lojas, preenchimento automático de endereço e mais.



## Sobre a integração

A integração entre a Braze e a Radar permite acessar gatilhos sofisticados de campanhas baseadas em local e enriquecimento de perfil de usuário com dados primários de local. Quando eventos de geofence ou rastreamento de viagem da Radar são gerados, eventos personalizados e atributos de usuário são enviados para a Braze em tempo real. Esses eventos e atributos podem então ser usados para disparar campanhas baseadas em local, impulsionar operações de coleta e entrega na última milha, monitorar a logística de frotas e remessas, ou construir segmentos de usuários com base em padrões de local. 

Além disso, as APIs do Radar Geo podem ser aproveitadas para enriquecer ou personalizar suas campanhas de marketing através de [Conteúdo Conectado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/). 

## Pré-requisitos

| Requisito | Descrição |
|---|---|
| conta de radar | Uma conta Radar é necessária para aproveitar esta parceria. |
| Chave da API REST do Braze | Uma chave da API REST da Braze com permissões `users.track`. <br><br> Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**. |
| Identificador do app | Seu [identificador do app]({{site.baseurl}}/api/identifier_types/?tab=app%20ids) pode ser encontrado no dashboard do Braze em **Configurações** > **Chaves de API**. |
| chave de API do iOS<br>chave de API do Android | Essas chaves de API podem ser encontradas no dashboard do Braze em **Configurações** > **Configurações do app**. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Integração

Para mapear dados entre os SDKs do Braze e do Radar, você deve definir os mesmos IDs de usuário ou aliases de usuário em ambos os sistemas. Isso pode ser feito usando o método `changeUser()` no SDK da Braze e o método `setUserId()` no SDK da Radar.

Para ativar a integração:

1. No Radar na página [Integrações](https://radar.com/documentation/integrations), localize Braze.
1. Defina **Habilitado** para **Sim**.
3. Cole seu identificador de app e chaves de API.

{% alert note %}
Você pode definir chaves de API separadas para ambientes de teste e produção.
{% endalert %}

{:start="4"}
4\. Selecione seu endpoint Braze.
5\. Insira qualquer filtragem de evento ou atributo de evento para garantir que apenas dados relevantes sejam enviados para a Braze para marketing de engajamento. Sempre que eventos do Radar são gerados, o Radar enviará eventos personalizados e atributos de usuário para o Braze. Eventos de dispositivos iOS serão enviados usando suas chaves de API iOS; eventos e atributos de usuário de dispositivos Android serão enviados usando suas chaves de API Android.

{% alert note %}
Por padrão, o `userId` da Radar mapeia para o `external_id` da Braze para usuários logados. No entanto, você pode rastrear usuários desconectados ou especificar mapeamentos personalizados configurando o Radar `metadata.brazeAlias` ou `metadata.brazeExternalId`. Se você definir `metadata.brazeAlias`, também deverá adicionar um alias correspondente na Braze com o rótulo `radarAlias`.
{% endalert %}

## Casos de uso baseados em eventos e atributos

Você pode usar eventos personalizados e atributos de usuário para construir segmentos baseados em local ou disparar campanhas baseadas em local.

### Disparar uma notificação de chegada na loja para retirada na calçada 

Envie uma notificação por push para o usuário com instruções de chegada assim que ele chegar à sua loja para uma retirada na calçada.

![Uma campanha de entrega baseada em ação mostrando que a campanha será entregue quando o evento personalizado "arrived_at_trip_destination" ocorrer, e "trip_metadata" for igual a "curbside".]({% image_buster /assets/img_archive/radar-campaign.png %})

### Construa um segmento de público de visitantes recentes da loja

Por exemplo, mire em qualquer usuário que tenha visitado sua loja nos últimos 7 dias, independentemente de terem feito uma compra ou não.

![Um segmento onde "radar_geofence_tags" inclui o valor minha_loja e "radar_updated_at" foi há menos de 7 dias.]({% image_buster /assets/img_archive/radar-segment.png %})

## Conteúdo conectado

O exemplo a seguir mostra como executar uma promoção para atrair usuários próximos à loja com uma oferta digital. 



Para começar, você precisará ter sua chave de API publicável do Radar em mãos para usar nos URLs de suas solicitações.

Em seguida, dentro de uma tag `connected_content`, faça uma solicitação GET para a [API de pesquisa de lugares](https://radar.io/documentation/api#search-places). A API de busca de lugares retorna locais próximos com base em [Radar Places](https://radar.io/documentation/places): um banco de dados de locais para lugares, cadeias e categorias que fornece uma visão abrangente do mundo.

O snippet de código a seguir é um exemplo do que a Radar retornará como objeto JSON da chamada da API:

```json
{
  "meta": {
    "code": 200
  },
  "places": [
    {
      "_id": "5dc9b0fd2004860034bf2b06",
      "name": "Target",
      "location": {
        "type": "Point",
        "coordinates": [
          -74.42653983613333,
          40.548302893822985
        ]
      },
      "categories": [
        "shopping-retail",
        "department-store"
      ],
      "chain": {
        "slug": "target",
        "name": "Target",
        "domain": "target.com"
      }
    },
    {
      "_id": "5dc9b3d82004860034bfec54",
      "name": "Walmart",
      "location": {
        "type": "Point",
        "coordinates": [
          -74.44121885326864,
          40.554603296187224
        ]
      },
      "categories": [
        "shopping-retail"
      ],
      "chain": {
        "slug": "walmart",
        "name": "Walmart",
        "domain": "walmart.com"
      }
    }
  ]
}
```

Para construir a mensagem Braze direcionada e personalizada de Conteúdo Conectado, você pode aproveitar o atributo Braze `most_recent_location` como entrada para o parâmetro `near` na URL da solicitação da API. O atributo `most_recent_location` é coletado através da integração de eventos da Radar ou diretamente através do SDK da Braze.

No exemplo a seguir, o filtro da cadeia Radar é aplicado para as localizações do Target e Walmart, e o raio de busca para locais próximos é definido em 2 km.

{% raw %}
```
{% connected_content https://api.radar.io/v1/search/places?radius=2000&near={{${most_recent_location}.latitude}},{{${most_recent_location}.longitude}}&chains=target,walmart&limit=5 :method get :headers {"Authorization": "<yourRadarPublishableKey>"} :content_type application/json :save nearbyplaces %}
```
{% endraw %}

Como você pode ver na tag `connect_content`, o objeto JSON é armazenado na variável local `nearbyplaces` adicionando `:save nearbyplaces` após o URL.
Você pode testar qual deve ser a saída referenciando {% raw %}`{{nearbyplaces.places}}`{% endraw%}.

Reunindo nosso caso de uso, aqui está como seria a sintaxe da campanha. O código a seguir itera através do objeto `nearbyplaces.places`, extraindo valores únicos e concatenando-os com delimitadores legíveis para a mensagem.

{% raw %}
```
{% connected_content https://api.radar.io/v1/search/places?radius=2000&near={{${most_recent_location}.latitude}},{{${most_recent_location}.longitude}}&chains=target,walmart&limit=5 :method get :headers {"Authorization": "<yourRadarPublishableKey>"} :content_type application/json :save nearbyplaces %}
{% if nearbyplaces.**http_status_code** != 200 %}
{% abort_message('Connected Content returned a non-200 http status code') %}
{% endif %}
{% if nearbyplaces.meta.code != 200 %}
{% abort_message('Connected Content returned a non-200 meta code') %}
{% endif %}
{% if nearbyplaces.places.size == 0 %}
{% abort_message('Connected Content returned no nearby places') %}
{% else %}
{% assign delimiter = ", " %}
{% assign names = nearbyplaces.places | map: 'name' | uniq %}
{% if names.size == 2 %}
{{ names | join: ' and ' }} 
{% elsif names.size > 2 %}
{% assign names_final_str = "" %}
{% for name in names %}
{% if forloop.first == true %}
{% assign names_final_str = names_final_str  | append: name %}
{% elsif forloop.last == true %}
{% assign names_final_str = names_final_str | append: ", and "  | append: name %}
{% else %}
{% assign names_final_str = names_final_str | append: delimiter  | append: name %}
{% endif %}
{% endfor %}
{{ names_final_str }}
{% else %}
{{ names }} 
{% endif %}
near you!
```
{% endraw %}

{% alert tip %}
Visite a [documentação do Radar](https://radar.io/documentation/api) para todas as APIs do Radar que podem ser aproveitadas no Conteúdo Conectado.
{% endalert %}


