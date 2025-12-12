---
nav_title: Criação de cercas geográficas
article_title: Criação de cercas geográficas
page_order: 1
page_type: reference
toc_headers: h2
description: "Este artigo de referência aborda o que são cercas geográficas e como criar e configurar eventos de cercas geográficas."
tool: 
  - Location
search_rank: 9
---

# Cercas geográficas

> No centro de nossa oferta de localização em tempo real está o conceito de geofence. Uma geofence é uma área geográfica virtual, representada como latitude e longitude combinadas com um raio, formando um círculo em torno de uma posição global específica. As cercas geográficas podem variar do tamanho de um prédio até o tamanho de uma cidade inteira.

## Como funciona

As cercas geográficas podem ser usadas para acionar campanhas em tempo real à medida que os usuários entram e saem de suas fronteiras, ou enviar campanhas de acompanhamento horas ou dias depois. Os usuários que entram ou saem de suas cercas geográficas adicionam uma nova camada de dados de usuário que pode ser usada para segmentação e redirecionamento.

As cercas geográficas são organizadas em conjuntos de cercas geográficas - um grupo de cercas geográficas que pode ser usado para segmentar ou envolver os usuários em toda a plataforma. Cada conjunto de cercas geográficas pode conter um máximo de 10.000 cercas geográficas.

Você pode criar ou carregar um número ilimitado de cercas geográficas.

- Os aplicativos Android só podem armazenar até 100 cercas geográficas localmente de cada vez. O Braze está configurado para armazenar apenas até 20 cercas geográficas localmente por aplicativo.
- Os dispositivos iOS podem monitorar até 20 cercas geográficas de cada vez por aplicativo. O Braze monitorará até 20 locais se houver espaço disponível. 
- Se o usuário estiver qualificado para receber mais de 20 cercas geográficas, o Braze fará o download da quantidade máxima de locais com base na proximidade do usuário no momento do início da sessão.
- Para que as cercas geográficas funcionem corretamente, você deve garantir que seu aplicativo não esteja usando todos os pontos de cercas geográficas disponíveis.

Consulte a tabela a seguir para obter termos comuns de geofence e suas descrições.

| Prazo | Descrição |
|---|---|
| Latitude e longitude | O centro geográfico da geocerca. |
| Raio | O raio da cerca geográfica em metros, medido a partir do centro geográfico. Recomendamos definir um raio mínimo de 100 a 150 metros para todas as cercas geográficas. |
| Resfriamento | Os usuários recebem notificações acionadas por geofences depois de realizar transições de entrada ou saída em geofences individuais. Após a ocorrência de uma transição, há um tempo predefinido durante o qual o usuário não pode realizar a mesma transição nessa geocerca individual novamente. Esse tempo é chamado de "cooldown" e é predefinido pelo Braze, e seu principal objetivo é evitar solicitações de rede desnecessárias. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Criar geofences manualmente

### Etapa 1: Criar um conjunto de cercas geográficas

Para criar uma geofence, primeiro você precisa criar um conjunto de geofence.

1. Vá para **Audience** > **Locations** ( **Público** > **Locais** ) no painel do Braze.
2. Selecione **Create Geofence Set (Criar conjunto de cercas geográficas**).
3. Em **Nome do conjunto**, digite um nome para o conjunto de cercas geográficas.
4. (Opcional) Adicione tags para filtrar seu conjunto.

### Etapa 2: Adicionar as cercas geográficas

Em seguida, você pode adicionar cercas geográficas ao seu conjunto de cercas geográficas.

1. Selecione **Draw Geofence** para clicar e arrastar o círculo no mapa. Repita para adicionar mais cercas geográficas ao seu conjunto, conforme necessário.
2. (Opcional) Você pode selecionar **Edit (Editar** ) e substituir a descrição da cerca geográfica por um nome.
3. Selecione **Save Geofence Set** para salvar.

{% alert tip %}
Recomendamos a criação de cercas geográficas com um raio de pelo menos 200 metros para otimizar a funcionalidade. Para obter mais informações sobre as opções configuráveis, consulte [Integrações móveis](#mobile-integrations).
{% endalert %}

\![Um conjunto de geofences com duas geofences "EastCoastGreaterNY" e "WesternRegion" com dois círculos no mapa.]({% image_buster /assets/img/geofence_example.png %})

## Carregamento em massa de cercas geográficas {#creating-geofence-sets-via-bulk-upload}

As cercas geográficas podem ser carregadas em massa como um objeto GeoJSON do tipo `FeatureCollection`. Cada geofence é um tipo de geometria `Point` na coleção de recursos. As propriedades de cada recurso exigem uma chave `radius` e uma chave `name` opcional para cada geofence. 

Para carregar seu GeoJSON, selecione **More** > **Upload GeoJSON**.

Ao criar suas cercas geográficas, considere os seguintes detalhes:

- O valor `coordinates` no GeoJSON é formatado como `[Longitude, Latitude]`.
- O raio máximo de geofence que pode ser carregado é de 10.000 metros (cerca de 10 quilômetros ou 6,2 milhas).

### Exemplo

O exemplo a seguir representa o GeoJSON correto para especificar duas cercas geográficas: uma para a sede do Braze em Nova York e outra para a Estátua da Liberdade ao sul de Manhattan.

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

## Uso de eventos de geofence

Depois que as cercas geográficas forem configuradas, você poderá usá-las para aprimorar e enriquecer a forma como se comunica com seus usuários.

### Campanhas de ativação e Canvases

Para usar os dados de geofence como parte dos acionadores de campanha e do Canvas, selecione **Entrega baseada em ação** para o método de entrega. Em seguida, adicione uma ação de acionamento de `Trigger a Geofence`. Por fim, escolha os tipos de evento de transição de geofence e de conjunto de geofence para sua mensagem. Também é possível avançar os usuários por um Canvas usando eventos de geofence.

Uma campanha baseada em ações com uma geocerca que será acionada quando um usuário entrar em aeroportos alemães.]({% image_buster /assets/img_archive/action_based_geofence_trigger.png %})

### Personalização de mensagens

Para usar dados de geofence para personalizar uma mensagem, você pode usar a seguinte sintaxe de personalização do Liquid:

{% raw %}
* `{{event_properties.${geofence_name}}}`
* `{{event_properties.${geofence_set_name}}}`
{% endraw %}

## Atualização de conjuntos de geofences

Para usuários ativos, o Braze SDK solicitará geofences apenas uma vez por dia no início da sessão. Isso significa que, se forem feitas alterações nos conjuntos de cercas geográficas após o início da sessão, você precisará aguardar 24 horas a partir do momento em que os conjuntos forem baixados pela primeira vez para receber o conjunto atualizado.

{% alert note %}
Se as cercas geográficas não forem carregadas localmente no dispositivo, o usuário não poderá acionar a cerca geográfica mesmo que entre na área.
{% endalert %}

## Integrações móveis {#mobile-integrations}

### Requisitos para várias plataformas

As campanhas acionadas por geofence estão disponíveis no iOS e no Android. Para oferecer suporte a cercas geográficas, é necessário que os seguintes itens estejam em vigor:

1. Sua integração deve suportar notificações push em segundo plano.
2. As cercas geográficas ou a coleta de localização do Braze devem estar ativadas.
3. Para dispositivos com iOS versão 11 ou superior, o usuário deve sempre permitir o acesso à localização para que o geofencing funcione.

{% alert important %}
A partir da versão 3.6.0 do Braze SDK, a coleta de locais do Braze é desativada por padrão. Para verificar se ele está ativado no Android, confirme se `com_braze_enable_location_collection` está definido como `true` em seu `braze.xml`.
{% endalert %}

Consulte a documentação [do Android](https://developer.android.com/develop/sensors-and-location/location/geofencing#choose-the-optimal-radius-for-your-geofence) ou [iOS](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LocationAwarenessPG/RegionMonitoring/RegionMonitoring.html#//apple_ref/doc/uid/TP40009497-CH9-SW5) para obter mais orientações com base em sua plataforma.

{% alert tip %}
Você também pode aproveitar as cercas geográficas com nossos parceiros de tecnologia, como o [Radar]({{site.baseurl}}/partners/message_personalization/location/radar/) e o [Foursquare]({{site.baseurl}}/partners/message_personalization/location/foursquare/)
{% endalert %}

## Perguntas frequentes

### Qual é a diferença entre cercas geográficas e rastreamento de localização?

No Braze, uma geofence é um conceito diferente do rastreamento de localização. As cercas geográficas são usadas como acionadores para determinadas ações. Uma geocerca é um limite virtual definido em torno de uma localização geográfica. Quando um usuário entra ou sai desse limite, ele pode acionar uma ação específica, como o envio de uma mensagem.

O rastreamento de localização é usado para coletar e armazenar os dados de localização mais recentes de um usuário. Esses dados podem ser usados para segmentar usuários com base no filtro `Most Recent Location`. Por exemplo, você pode usar o filtro `Most Recent Location` para segmentar uma região específica do seu público, como enviar uma mensagem para usuários localizados em Nova York.

### Qual é a precisão das cercas geográficas do Braze?

As cercas geográficas do Braze usam uma combinação de todos os provedores de localização disponíveis em um dispositivo para triangular a localização do usuário. Isso inclui Wi-Fi, GPS e torres de celular.

A precisão típica está na faixa de 20 a 50 m, e a melhor precisão possível estará na faixa de 5 a 10 m. Em áreas rurais, a precisão pode se degradar significativamente, podendo chegar a vários quilômetros. Braze recomenda a criação de cercas geográficas com raios maiores em locais rurais.

Para obter mais informações sobre a precisão das cercas geográficas, consulte a documentação [do Android](https://developer.android.com/develop/sensors-and-location/location/geofencing) e [do iOS](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LocationAwarenessPG/RegionMonitoring/RegionMonitoring.html#//apple_ref/doc/uid/TP40009497-CH9-SW1).

### Como as cercas geográficas afetam a duração da bateria?

Nossa solução de geofencing usa o serviço de sistema de geofence nativo no iOS e no Android e é ajustada para trocar precisão e energia de forma inteligente, economizando a vida útil da bateria e melhorando o desempenho à medida que o serviço subjacente é aprimorado.

### Quando as cercas geográficas estão ativas?

As cercas geográficas Braze funcionam em todas as horas do dia, mesmo quando seu aplicativo está fechado. Eles se tornam ativos assim que são definidos e carregados no painel de controle do Braze. No entanto, as cercas geográficas não podem funcionar se um usuário tiver desativado o rastreamento de localização.

Para que as cercas geográficas funcionem, os usuários devem ter os serviços de localização ativados no dispositivo e devem ter concedido permissão ao seu aplicativo para acessar a localização deles. Se um usuário tiver desativado o rastreamento de localização, seu aplicativo não poderá detectar quando ele entrar ou sair de uma geofence.

### Os dados de geofence são armazenados nos perfis de usuário?

Não, o Braze não armazena dados de geofence nos perfis de usuário. As geofences são monitoradas pelos serviços de localização da Apple e do Google, e o Braze só é notificado quando um usuário aciona uma geofence. Nesse momento, processamos todas as campanhas de acionamento associadas.

### Posso configurar uma geofence dentro de uma geofence?

Como prática recomendada, evite configurar cercas geográficas que se sobreponham umas às outras, pois isso pode causar problemas com o acionamento de notificações.

