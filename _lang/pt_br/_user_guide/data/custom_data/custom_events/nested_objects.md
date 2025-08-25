---
nav_title: Objetos Aninhados
article_title: Objetos Aninhados em Eventos Personalizados
page_order: 1
page_type: reference
description: "Este artigo descreve como enviar dados JSON aninhados como propriedades de eventos personalizados e compras, e como usar esses objetos aninhados no seu envio de mensagens."
---

# Objetos aninhados em eventos personalizados

> Esta página aborda como enviar dados JSON aninhados como propriedades de eventos personalizados e compras, e como usar esses objetos aninhados em seu envio de mensagens.

Você pode usar objetos aninhados—objetos que estão dentro de outro objeto—para enviar dados JSON aninhados como propriedades de eventos personalizados e compras. Esses dados aninhados podem ser usados para modelar informações personalizadas em mensagens, disparar envios de mensagens e segmentar usuários.

## Limitações

- Dados aninhados são suportados tanto para [eventos personalizados]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) quanto para [eventos de compra]({{site.baseurl}}/user_guide/data/custom_data/purchase_events/), mas não para outros tipos de eventos.
- Objetos de propriedades de evento que contêm valores de array ou objeto podem ter uma carga útil de propriedade de evento de até 100 KB.
- Os esquemas de propriedades de eventos não podem ser gerados para eventos de compra.
- Os esquemas de propriedades de eventos são gerados através da amostragem de eventos personalizados das últimas 24 horas.

### Versões mínimas do SDK

As seguintes versões do SDK suportam objetos aninhados:

{% sdk_min_versions swift:5.0.0 android:1.0.0 web:3.3.0 %}

## Etapa 1: Gerar um esquema

Você pode acessar os dados aninhados em seu evento personalizado gerando um esquema para cada evento com propriedades de evento aninhadas. Para gerar um esquema:

1. Acessar **Configurações de Dados** > **Eventos Personalizados**.
2. Selecione **Gerenciar Propriedades** para os eventos com propriedades aninhadas.
3. Selecione o botão <i class="fas fa-arrows-rotate"></i> para gerar o esquema. Para visualizar o esquema, selecione o botão <i class="fas fa-plus"></i> de adição.

![]({% image_buster /assets/img_archive/schema_generation_example.png %}){: style="max-width:80%;"}

Se novas propriedades forem enviadas no futuro, elas não estarão no esquema até que seja regenerado. Os esquemas podem ser regenerados a cada 24 horas.

## Etapa 2: Use o objeto aninhado

Você pode referenciar os dados aninhados durante a segmentação e personalização. Observe que um esquema não é necessário. Consulte as seguintes seções para exemplos de uso:

- [Corpo da solicitação da API](#api-request-body)
- [Modelos do Liquid](#liquid-templating)
- [Mensagem de gatilho](#message-triggering)
- [Segmentação](#segmentation)
- [Personalização](#personalization)

### Corpo da solicitação da API

{% tabs %}
{% tab Exemplo de Música %}

Veja a seguir um `/users/track` exemplo com um evento personalizado "Criou playlist". Depois que uma playlist foi criada, capture as propriedades da playlist enviando:
- Uma solicitação de API que lista "músicas" como uma propriedade
- Um array das propriedades aninhadas das músicas

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
{% tab Exemplo de Restaurante%}

O seguinte é um `/users/track` exemplo com um evento personalizado "Comprou". Após um pedido ter sido concluído, capture as propriedades desse pedido enviando:
- Uma solicitação de API que lista "r_details" como uma propriedade
- As propriedades aninhadas daquela ordem

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
Para propriedades de evento personalizado aninhadas, se o ano for menor que 0 ou maior que 3000, o Braze não armazena esses valores no usuário.
{% endalert %}

### Modelos do Liquid

O seguinte mostra como criar um modelo Liquid que referencia as propriedades aninhadas solicitadas da [solicitação de API anterior](#api-request-body).

{% tabs %}
{% tab Exemplo de Música %}
Modelagem em Liquid em uma mensagem acionada pelo evento "Created Playlist": 

{% raw %}
`{{event_properties.${songs}[0].album.name}}`: "Deixa pra lá"<br>
`{{event_properties.${songs}[1].title}}`: Enquanto Minha Guitarra Gentilmente Chora
{% endraw %}

{% endtab %}
{% tab Exemplo de Restaurante %}
Modelagem em Liquid em uma mensagem acionada pelo evento "Ordered": 

{% raw %}
`{{event_properties.${r_details}.location.city}}`: Montclair
{% endraw %}

{% endtab %}
{% endtabs %}

### Mensagem de gatilho

Para usar essas propriedades para disparar uma campanha, selecione seu evento personalizado ou compra, e então adicione um filtro de **Propriedade aninhada**. Nota que o disparo de mensagens ainda não é suportado para mensagens no app, mas as propriedades aninhadas na personalização Liquid nas mensagens ainda serão exibidas.

{% tabs %}
{% tab Exemplo de Música %}

Acionando uma campanha com propriedades aninhadas do evento "Playlist Criada": 

![Um usuário escolhendo uma propriedade aninhada para filtros de propriedade em um evento personalizado.]({% image_buster /assets/img/nested_object2.png %})

A condição de disparo `songs[].album.yearReleased` "é" "1968" corresponderá a um evento onde qualquer uma das músicas tenha um álbum lançado em 1968. Usamos a notação de colchetes `[]` para percorrer matrizes e correspondemos se **qualquer** item na matriz percorrida corresponder à propriedade do evento.

{% alert important %}
O filtro **does not equal** só corresponde se nenhuma das propriedades em sua matriz for igual ao valor fornecido. <br><br>Por exemplo, digamos que o Canvas A tenha o filtro de propriedade aninhada de evento personalizado baseado em ação **igual a** "smartwatch" e o Canvas B tenha o filtro de propriedade aninhada de evento personalizado baseado em ação **não igual a** "simphone". Se você tiver "smartwatch" e "simphone" em suas propriedades, ambas as telas serão disparadas. Mas se você tiver "simphone" ou "sim only" em qualquer propriedade, nenhum dos Canvas será disparado.
{% endalert %}

{% endtab %}
{% tab Exemplo de Restaurante %}

Acionando uma campanha com propriedades aninhadas do evento "Ordered": 

![Um usuário adicionando o filtro de propriedade r_details.name é McDonalds para um evento personalizado.]({% image_buster /assets/img/nested_object1.png %})

`r_details.name`: Mcdonalds<br>
`r_details.location.city`: Montclair
{% endtab %}
{% endtabs %}

{% alert note %}
Se a propriedade do seu evento contiver os caracteres `[]` ou `.`, escape-os colocando o trecho entre aspas duplas. Por exemplo, `"songs[].album".yearReleased` corresponderá a um evento com a propriedade literal `"songs[].album"`.
{% endalert %}

### Segmentação

Para segmentar usuários com base em propriedades de eventos aninhados, você deve usar [extensões de segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/). Depois de gerar um esquema, o explorador de objetos aninhados será exibido na seção de segmentação. 

![]({% image_buster /assets/img_archive/nested_event_properties_segmentation.png %})

A segmentação usa a mesma notação que o gatilho (veja [Gatilho de mensagem](#message-triggering)).

Para editar ou criar extensões de segmento, você precisará da permissão "Editar Segmentos".

### Personalização

Usando o modal **Adicionar Personalização**, selecione **Propriedades Avançadas do Evento** como o tipo de personalização. Isso permite a opção de adicionar propriedades de eventos aninhados após um esquema ter sido gerado.

![]({% image_buster /assets/img_archive/nested_event_properties_personalization.png %}){: style="max-width:70%;"}

## Perguntas frequentes

### O uso de objetos aninhados consome pontos de dados adicionais?

Não há mudança na forma como cobramos pontos de dados como resultado da adição dessa capacidade. Segmentar com base em objetos aninhados usa extensões de segmento, o que não gera uso adicional de pontos de dados.

### Quantos dados aninhados podem ser enviados?

Se uma ou mais propriedades do evento contiverem dados aninhados, a carga útil máxima para todas as propriedades combinadas em um evento é de 100 KB. Qualquer solicitação acima desse limite de tamanho será rejeitada.

