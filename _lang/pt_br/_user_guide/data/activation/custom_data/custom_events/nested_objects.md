---
nav_title: Objetos aninhados
article_title: Objetos aninhados em eventos personalizados
page_order: 1
page_type: reference
description: "Este artigo descreve como enviar dados JSON aninhados como propriedades de eventos e compras personalizados e como usar esses objetos aninhados em suas mensagens."
---

# Objetos aninhados em eventos personalizados

> Esta página aborda como enviar dados JSON aninhados como propriedades de eventos e compras personalizados e como usar esses objetos aninhados em suas mensagens.

Você pode usar objetos aninhados - objetos que estão dentro de outro objeto - para enviar dados JSON aninhados como propriedades de eventos e compras personalizados. Esses dados aninhados podem ser usados para criar modelos de informações personalizadas em mensagens, acionar envios de mensagens e segmentar usuários.

## Limitações

- Os dados aninhados são compatíveis com [eventos personalizados]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) e [eventos de compra]({{site.baseurl}}/user_guide/data/custom_data/purchase_events/), mas não com outros tipos de eventos.
- Os objetos de propriedade de evento que contêm valores de matriz ou objeto podem ter uma carga útil de propriedade de evento de até 100 KB.
- Os esquemas de propriedades de eventos não podem ser gerados para eventos de compra.
- Os esquemas de propriedades de eventos são gerados por meio da amostragem de eventos personalizados das últimas 24 horas.

### Versões mínimas do SDK

As seguintes versões do SDK oferecem suporte a objetos aninhados:

{% sdk_min_versions swift:5.0.0 android:1.0.0 web:3.3.0 %}

## Etapa 1: Gerar um esquema

Você pode acessar os dados aninhados em seu evento personalizado gerando um esquema para cada evento com propriedades de evento aninhadas. Para gerar um esquema:

1. Vá para **Configurações de dados** > **Eventos personalizados**.
2. Selecione **Manage Properties (Gerenciar propriedades** ) para os eventos com propriedades aninhadas.
3. Selecione o botão <i class="fas fa-arrows-rotate"></i> para gerar o esquema. Para visualizar o esquema, selecione o botão <i class="fas fa-plus"></i> plus.

\![]({% image_buster /assets/img_archive/schema_generation_example.png %}){: style="max-width:80%;"}

Se novas propriedades forem enviadas no futuro, elas não estarão no esquema até que ele seja gerado novamente. Os esquemas podem ser regenerados a cada 24 horas.

## Etapa 2: Use o objeto aninhado

Você pode fazer referência aos dados aninhados durante a segmentação e a personalização. Observe que não é necessário ter um esquema. Consulte as seções a seguir para obter exemplos de uso:

- [Corpo da solicitação de API](#api-request-body)
- [Modelo líquido](#liquid-templating)
- [Acionamento de mensagens](#message-triggering)
- [Segmentação](#segmentation)
- [Personalização](#personalization)

### Corpo da solicitação de API

{% tabs %}
{% tab Music Example %}

A seguir, um exemplo do site `/users/track` com um evento personalizado "Created Playlist". Depois que uma lista de reprodução for criada, capture as propriedades da lista de reprodução enviando-as:
- Uma solicitação de API que lista "songs" como uma propriedade
- Uma matriz das propriedades aninhadas das músicas

```
...
"properties": {
  "songs": [
    {
      "title": "Smells Like Teen Spirit",
      "artist": "Nirvana",
      "album": {
        "name": "Nevermind",
        "yearReleased": "1991"
      }
    },
    {
      "title": "While My Guitar Gently Weeps",
      "artist": "the Beatles",
      "album": {
        "name": "The Beatles",
        "yearReleased": "1968"
      }
    }
  ]
}
...
```
{% endtab %}
{% tab Restaurant Example%}

A seguir, um exemplo do site `/users/track` com um evento personalizado "Ordered". Depois que um pedido for concluído, capture as propriedades desse pedido enviando-as:
- Uma solicitação de API que lista "r_details" como uma propriedade
- As propriedades aninhadas dessa ordem

```
...
"properties": {
  "r_details": {
    "name": "McDonalds",
    "identifier": "12345678",
    "location" : {
      "city": "Montclair",
      "state": "NJ"
    }
  }
}
...
```
{% endtab %}
{% endtabs %}

{% alert note %}
Para propriedades de eventos personalizados aninhados, se o ano for menor que 0 ou maior que 3000, o Braze não armazenará esses valores no usuário.
{% endalert %}

### Modelo líquido

A seguir, mostramos como criar um modelo Liquid que faz referência às propriedades aninhadas solicitadas na [solicitação de API anterior](#api-request-body).

{% tabs %}
{% tab Music Example %}
Criação de modelos no Liquid em uma mensagem acionada pelo evento "Created Playlist":

{% raw %}
`{{event_properties.${songs}[0].album.name}}`: "Nevermind" (Não importa)<br>
`{{event_properties.${songs}[1].title}}`: "While My Guitar Gently Weeps" (Enquanto minha guitarra chora suavemente)
{% endraw %}

{% endtab %}
{% tab Restaurant Example %}
Modelagem no Liquid em uma mensagem acionada pelo evento "Ordered":

{% raw %}
`{{event_properties.${r_details}.location.city}}`: "Montclair"
{% endraw %}

{% endtab %}
{% endtabs %}

### Acionamento de mensagens

Para usar essas propriedades para acionar uma campanha, selecione seu evento ou compra personalizada e, em seguida, adicione um filtro de **propriedade aninhada**. Observe que o acionamento de mensagens ainda não é compatível com mensagens in-app, mas as propriedades aninhadas na personalização Liquid nas mensagens ainda serão exibidas.

{% tabs %}
{% tab Music Example %}

Acionamento de uma campanha com propriedades aninhadas a partir do evento "Created Playlist":

\![Um usuário escolhendo uma propriedade aninhada para filtros de propriedade em um evento personalizado.]({% image_buster /assets/img/nested_object2.png %})

A condição de acionamento `songs[].album.yearReleased` "is" "1968" corresponderá a um evento em que qualquer uma das músicas tenha um álbum lançado em 1968. Usamos a notação de colchetes `[]` para percorrer as matrizes e combinamos se **algum** item da matriz percorrida corresponde à propriedade do evento.

{% alert important %}
O filtro **does not equal** só corresponde se nenhuma das propriedades em sua matriz for igual ao valor fornecido. <br><br>Por exemplo, digamos que o Canvas A tenha o filtro de propriedade aninhada de evento personalizado baseado em ação **igual a** "smartwatch", e o Canvas B tenha o filtro de propriedade aninhada de evento personalizado baseado em ação **não igual a** "simphone". Se você tiver "smartwatch" e "simphone" em suas propriedades, ambos os Canvases serão acionados. Mas se você tiver "simphone" ou "sim only" em qualquer propriedade, nenhum dos Canvas será acionado.
{% endalert %}

{% endtab %}
{% tab Restaurant Example %}

Acionamento de uma campanha com propriedades aninhadas a partir do evento "Ordered":

\![Um usuário adicionando o filtro de propriedade r_details.name é McDonalds para um evento personalizado.]({% image_buster /assets/img/nested_object1.png %})

`r_details.name`: "Mcdonalds"<br>
`r_details.location.city`: "Montclair"
{% endtab %}
{% endtabs %}

{% alert note %}
Se a propriedade do evento contiver os caracteres `[]` ou `.`, escape-os colocando o bloco entre aspas duplas. Por exemplo, `"songs[].album".yearReleased` corresponderá a um evento com a propriedade literal `"songs[].album"`.
{% endalert %}

### Segmentação

Para segmentar usuários com base em propriedades de eventos aninhados, é necessário usar [Segment Extensions]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/). Depois de gerar um esquema, o explorador de objetos aninhados será exibido na seção de segmentação. 

\![]({% image_buster /assets/img_archive/nested_event_properties_segmentation.png %})

A segmentação usa a mesma notação do acionamento (consulte [Acionamento de mensagens](#message-triggering)).

Para editar ou criar Extensões de Segmento, você precisará da permissão "Edit Segments" (Editar Segmentos).

### Personalização

Usando o modal **Add Personalization**, selecione **Advanced Event Properties** como o tipo de personalização. Isso permite a opção de adicionar propriedades de eventos aninhados depois que um esquema tiver sido gerado.

\![]({% image_buster /assets/img_archive/nested_event_properties_personalization.png %}){: style="max-width:70%;"}

## Perguntas frequentes

### O uso de objetos aninhados registra pontos de dados adicionais?

Não há nenhuma alteração na forma como registramos os pontos de dados como resultado da adição desse recurso. A segmentação com base em objetos aninhados usa Segment Extensions, que não usa pontos de dados adicionais.

### Quantos dados aninhados podem ser enviados?

Se uma ou mais propriedades do evento contiverem dados aninhados, a carga útil máxima para todas as propriedades combinadas em um evento será de 100 KB. Qualquer solicitação acima desse limite de tamanho será rejeitada.

