---
nav_title: Criando geofences
article_title: Criando geofences
page_order: 1
page_type: reference
description: "Este artigo de referência aborda o que são geofences e como criar e configurar eventos de geofence."
tool: 
  - Location
search_rank: 9
---

# Geofences

> No centro de nossa oferta de local em tempo real está o conceito de geofence. Uma geofence é uma área geográfica virtual, representada como latitude e longitude combinadas com um raio, formando um círculo em torno de uma posição global específica. As geofences podem variar do tamanho de um prédio até o tamanho de uma cidade inteira.

É possível definir geofences no dashboard do Braze e usá-las para disparar campanhas em tempo real à medida que os usuários entram e saem de suas fronteiras, ou enviar campanhas de acompanhamento horas ou dias depois. Os usuários que entram ou saem de suas geofences adicionam uma nova camada de dados de usuários que podem ser usados para segmentação e direcionamento.

## Visão geral

Gerencie geofences em **Público** > **Locais**.

{% alert note %}
Se estiver usando a [navegação mais antiga]({{site.baseurl}}/navigation), poderá encontrar **os locais** em **Engajamento**.
{% endalert %}

As geofences são organizadas em conjuntos de geofences - um grupo de geofences que pode ser usado para segmentar ou engajar usuários em toda a plataforma. Cada conjunto de geofences pode conter um máximo de 10.000 geofences.

É possível criar ou fazer upload de uma quantidade ilimitada de geofences no dashboard, permitindo que sua equipe de marketing configure conjuntos de geofences e campanhas sem precisar calcular o número de geofences. A Braze ressincronizará dinamicamente os geofences que rastreia para cada usuário individual, garantindo que os geofences mais relevantes para eles estejam sempre disponíveis.

- Os apps para Android só podem armazenar até 100 geofences locais de cada vez. A Braze está configurado para armazenar apenas até 20 geofences localmente por app.
- Os dispositivos iOS podem monitorar até 20 geofences ao mesmo tempo por app. A Braze monitorará até 20 locais se houver espaço disponível. 
- Se o usuário for elegível para receber mais de 20 geofences, o Braze baixará a quantidade máxima de locais com base na proximidade do usuário no ponto de início da sessão/atualização silenciosa por push
- Para que as geofences funcionem corretamente, você deve garantir que seu app não esteja usando todos os pontos de geofence disponíveis.

## Criação de conjuntos de geofences

### Criação manual de conjuntos

Na página **Locais**, clique em **\+ Criar conjunto de geofences**.

![Conjunto de geofences de aeroportos alemães com um usuário desenhando um raio de dois mil metros no mapa para o Aeroporto de Hamburgo.][1]

Depois de criar um conjunto de geofences, você pode adicionar geofences manualmente, desenhando-as no mapa. Recomendamos a criação de geofences com um raio de pelo menos 200 metros para otimizar a funcionalidade. Para saber mais sobre as opções configuráveis, consulte [Configuração de geofences]({{site.baseurl}}/user_guide/engagement_tools/locations_and_geofences/mobile_integrations/).

### Criação de conjuntos via upload em massa {#creating-geofence-sets-via-bulk-upload}

As geofences podem ser feitas upload em massa como um objeto GeoJSON do tipo `FeatureCollection`. Cada geofence individual é um tipo de geometria `Point` na coleção de recursos. As propriedades de cada recurso exigem uma chave `"radius"` e uma chave `"name"` opcional para cada geofence. Para fazer upload de seu GeoJSON, clique em **\+ Criar conjunto de geofences** seguido de **Upload do GeoJSON**.

A amostra a seguir representa o GeoJSON correto para especificar duas geofences: uma para a sede do Braze em Nova York e outra para a Estátua da Liberdade ao sul de Manhattan. Recomendamos fazer upload de geofences com um raio de pelo menos 100 metros para otimizar a funcionalidade.

```
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [-73.992473, 40.755669]
      },
      "properties": {
        "radius": 200,
        "name": "Braze HQ"
      }
    },
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [-74.044468, 40.689225]
       },
      "properties": {
        "radius": 100,
        "name": "Statue of Liberty"
      }
    }
  ]
}
```

Ao criar suas geofences, tenha em mente os seguintes pontos:

- O valor `coordinates` no GeoJSON é formatado como [Longitude, Latitude].
- O raio máximo de geofence que pode ser feito upload é de 100.000 metros (cerca de 100 quilômetros ou 62 milhas).

## Atualização de conjuntos de geofences

Para usuários ativos, o SDK da Braze solicitará geofences apenas uma vez por dia no início da sessão. Isso significa que, se forem feitas alterações nos conjuntos de geofences após o início da sessão, você precisará aguardar 24 horas a partir do momento em que os conjuntos forem baixados pela primeira vez para receber o conjunto atualizado.

Para os usuários inativos, se o usuário estiver com a capacitação em segundo plano ativada, o Braze também enviará um push silencioso uma vez a cada 24 horas para baixar os locais mais recentes para o dispositivo.

{% alert note %}
Se as geofences não forem carregadas localmente no dispositivo, o usuário não poderá disparar a geofence mesmo que entre na área.
{% endalert %}

### Atualização para usuários individuais

A atualização de geofences para usuários individuais pode ser útil durante o teste. Para atualizar os conjuntos de geofences, navegue até a parte inferior da página **Locais** e clique em **Re-sync Geofences**. Em seguida, será solicitado que você digite `external_id` ou `email` dos usuários que deseja atualizar

## Uso de eventos de geofence

Depois que as geofences forem configuradas, você poderá usá-las para aprimorar e enriquecer a forma como se comunica com seus usuários.

### Como gerenciar os gatilhos

Para usar os dados de geofence como parte dos disparos da campanha e do canva, escolha **Entrega baseada em ação** para o método de entrega. Em seguida, adicione uma ação-gatilho de `Trigger a Geofence`. Por fim, escolha o conjunto de geofences e os tipos de eventos de transição de geofences para sua mensagem. Também é possível avançar os usuários em um Canva usando eventos de geofence.

![][2]

### Personalização

Para usar dados de geofence para personalizar uma mensagem, você pode usar a seguinte sintaxe de personalização do Liquid:

{% raw %}
* `{{event_properties.${geofence_name}}}`
* `{{event_properties.${geofence_set_name}}}`
{% endraw %}

## Perguntas frequentes

Acesse [Perguntas frequentes sobre geofences][3] para obter respostas às perguntas mais frequentes sobre geofences.


[1]: {% image_buster /assets/img_archive/locations_main_screen.png %}
[2]: {% image_buster /assets/img_archive/action_based_geofence_trigger.png %}
[3]: {{site.baseurl}}/user_guide/engagement_tools/locations_and_geofences/faqs/#geofences
