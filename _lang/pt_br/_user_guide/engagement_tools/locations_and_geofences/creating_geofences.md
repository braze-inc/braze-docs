---
nav_title: Criando geofences
article_title: Criando geofences
page_order: 1
page_type: reference
toc_headers: h2
description: "Este artigo de referência aborda o que são geofences e como criar e configurar eventos de geofence."
tool: 
  - Location
search_rank: 9
---

# Geofences

> No centro de nossa oferta de local em tempo real está o conceito de geofence. Uma geofence é uma área geográfica virtual, representada como latitude e longitude combinadas com um raio, formando um círculo em torno de uma posição global específica. As geofences podem variar do tamanho de um prédio até o tamanho de uma cidade inteira.

## Como funciona?

As geofences podem ser usados para disparar campanhas em tempo real à medida que os usuários entram e saem de suas bordas, ou enviar campanhas de acompanhamento horas ou dias depois. Os usuários que entram ou saem de suas geofences adicionam uma nova camada de dados de usuários que podem ser usados para segmentação e direcionamento.

As geofences são organizadas em conjuntos de geofences - um grupo de geofences que pode ser usado para segmentar ou engajar usuários em toda a plataforma. Cada conjunto de geofences pode conter um máximo de 10.000 geofences.

Você pode criar ou fazer upload de um número ilimitado de geofences.

- Os apps para Android só podem armazenar até 100 geofences locais de cada vez. A Braze está configurado para armazenar apenas até 20 geofences localmente por app.
- Os dispositivos iOS podem monitorar até 20 geofences ao mesmo tempo por app. A Braze monitorará até 20 locais se houver espaço disponível. 
- Se o usuário for elegível para receber mais de 20 geofences, a Braze fará o download da quantidade máxima de locais com base na proximidade do usuário no início da sessão.
- Para que as geofences funcionem corretamente, você deve garantir que seu app não esteja usando todos os pontos de geofence disponíveis.

Consulte a tabela a seguir para termos comuns de geofence e suas descrições.

| Prazo | Descrição |
|---|---|
| Latitude e longitude | O centro geográfico da geofence. |
| Raio | O raio da geofence em metros, medido a partir do centro geográfico. Recomendamos definir um raio mínimo de 100 a 150 metros para todas as geofences. |
| Resfriamento | Os usuários recebem notificações disparadas por geofences depois de realizar transições de entrada ou saída em geofences individuais. Após a ocorrência de uma transição, há um tempo predefinido durante o qual o usuário não pode realizar a mesma transição nessa geofence individual novamente. Esse tempo é chamado de "cooldown" e é pré-definido pela Braze, e seu principal objetivo é evitar solicitações de rede desnecessárias. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Criar geofences manualmente

### Etapa 1: Criar um conjunto de geofences

Para criar um geofence, você precisará criar um conjunto de geofences primeiro.

1. Acessar **público** > **Locais** no dashboard da Braze.
2. Selecione **Criar Conjunto de Geofences**.
3. Para **Nome do conjunto**, insira um nome para seu conjunto de geofences.
4. (Opcional) Adicione tags para filtrar seu conjunto.

### Etapa 2: Adicione os geofences

Em seguida, você pode adicionar geofences ao seu conjunto de geofences.

1. Selecione **Desenhar Geofence** para clicar e arrastar o círculo no mapa. Repita para adicionar mais geofences ao seu conjunto conforme necessário.
2. (Opcional) Você pode selecionar **Editar** e substituir a descrição do geofence por um nome.
3. Selecione **Salvar Conjunto de Geofences** para salvar.

{% alert tip %}
Recomendamos a criação de geofences com um raio de pelo menos 200 metros para otimizar a funcionalidade. Para saber mais sobre opções configuráveis, consulte [Integrações móveis](#mobile-integrations).
{% endalert %}

![Um conjunto de geofences com dois geofences "EastCoastGreaterNY" e "WesternRegion" com dois círculos no mapa.]({% image_buster /assets/img/geofence_example.png %})

## Upload em massa de geofences {#creating-geofence-sets-via-bulk-upload}

As geofences podem ser feitas upload em massa como um objeto GeoJSON do tipo `FeatureCollection`. Cada geofence é um tipo de geometria `Point` na coleção de recursos. As propriedades de cada recurso exigem uma chave `radius` e uma chave `name` opcional para cada geofence. 

Para fazer upload do seu GeoJSON, selecione **Mais** > **Fazer upload do GeoJSON**.

Ao criar seus geofences, considere os seguintes detalhes:

- O valor `coordinates` no GeoJSON é formatado como `[Longitude, Latitude]`.
- O raio máximo do geofence que pode ser enviado é de 10.000 metros (cerca de 100 quilômetros ou 62 milhas).

### Exemplo

O seguinte exemplo representa o GeoJSON correto para especificar dois geofences: um para a sede da Braze em NYC e um para a Estátua da Liberdade ao sul de Manhattan.

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

Depois que os geofences forem configurados, você pode usá-los para melhorar e enriquecer a forma como se comunica com seus usuários.

### Disparando campanhas e Canvases

Para usar os dados de geofence como parte dos disparos da campanha e do canva, escolha **Entrega baseada em ação** para o método de entrega. Em seguida, adicione uma ação-gatilho de `Trigger a Geofence`. Por fim, escolha o conjunto de geofences e os tipos de eventos de transição de geofences para sua mensagem. Também é possível avançar os usuários em um Canva usando eventos de geofence.

![Uma campanha baseada em ação com um geofence que será disparado quando um usuário entrar em aeroportos alemães.]({% image_buster /assets/img_archive/action_based_geofence_trigger.png %})

### Personalizando mensagens

Para usar dados de geofence para personalizar uma mensagem, você pode usar a seguinte sintaxe de personalização do Liquid:

{% raw %}
* `{{event_properties.${geofence_name}}}`
* `{{event_properties.${geofence_set_name}}}`
{% endraw %}

## Atualização de conjuntos de geofences

Para usuários ativos, o SDK da Braze solicitará geofences apenas uma vez por dia no início da sessão. Isso significa que, se forem feitas alterações nos conjuntos de geofences após o início da sessão, você precisará aguardar 24 horas a partir do momento em que os conjuntos forem baixados pela primeira vez para receber o conjunto atualizado.

{% alert note %}
Se as geofences não forem carregadas localmente no dispositivo, o usuário não poderá disparar a geofence mesmo que entre na área.
{% endalert %}

## Integrações móveis {#mobile-integrations}

### Requisitos para várias plataformas

As campanhas disparadas por geofence estão disponíveis no iOS e no Android. Para oferecer suporte a geofences, os seguintes itens devem estar em vigor:

1. Sua integração deve suportar notificações por push em segundo plano.
2. As geofences do Braze ou a coleta de locais devem estar ativadas.
3. Para dispositivos com iOS versão 11 ou superior, o usuário deve sempre permitir o acesso ao local para que o geofencing funcione.

{% alert important %}
A partir da versão 3.6.0 do SDK do Braze, a coleta de locais do Braze é desativada por padrão. Para verificar se a capacitação está ativada no Android, confirme se `com_braze_enable_location_collection` está definido como `true` em seu `braze.xml`.
{% endalert %}

Consulte a documentação [Android](https://developer.android.com/develop/sensors-and-location/location/geofencing#choose-the-optimal-radius-for-your-geofence) ou [iOS](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LocationAwarenessPG/RegionMonitoring/RegionMonitoring.html#//apple_ref/doc/uid/TP40009497-CH9-SW5) para mais orientações com base na sua plataforma.

{% alert tip %}
Você também pode aproveitar os geofences com nossos Parceiros de Tecnologia, como [Radar]({{site.baseurl}}/partners/message_personalization/location/radar/) e [Foursquare]({{site.baseurl}}/partners/message_personalization/location/foursquare/)
{% endalert %}

## Perguntas frequentes

### Qual é a diferença entre geofences e monitoramento de localização?

Na Braze, uma geofence é um conceito diferente do monitoramento de localização. Os geofences são usados como disparadores para determinadas ações. Um geofence é um limite virtual estabelecido em um local geográfico. Quando um usuário entra ou sai desse limite, ele pode disparar uma ação específica, como o envio de uma mensagem.

O monitoramento de localização é usado para coletar e armazenar os dados de localização mais recentes de um usuário. Esses dados podem ser usados para segmentar usuários com base no filtro `Most Recent Location`. Por exemplo, é possível usar o filtro `Most Recent Location` para direcionamento a uma região específica do seu público, como o envio de mensagens a usuários localizados em Nova York.

### Qual é a precisão das geofences do Braze?

As geofences do Braze usam uma combinação de todos os provedores de localização disponíveis em um dispositivo para triangular a localização do usuário. Isso inclui Wi-Fi, GPS e torres de celular.

A precisão típica está na faixa de 20 a 50 m e a melhor precisão será na faixa de 5 a 10 m. Em áreas rurais, a precisão pode se degradar significativamente, podendo chegar a vários quilômetros. Braze recomenda a criação de geofences com raios maiores em locais rurais.

Para saber mais sobre a precisão das geofences, consulte a documentação do [Android](https://developer.android.com/develop/sensors-and-location/location/geofencing) e do [iOS](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LocationAwarenessPG/RegionMonitoring/RegionMonitoring.html#//apple_ref/doc/uid/TP40009497-CH9-SW1).

### Como o geofences afeta a duração da bateria?

Nossa solução de geofencing usa o serviço de sistema geofence nativo no iOS e Android e é ajustada para equilibrar inteligentemente precisão e consumo de energia, economizando a vida útil da bateria e melhorando o desempenho à medida que o serviço subjacente melhora.

### Quando as geofences estão ativas?

As geofences da Braze funcionam em todas as horas do dia, mesmo quando seu app está fechado. Eles se tornam ativos assim que são definidos e feitos upload no dashboard da Braze. No entanto, as geofences não podem funcionar se um usuário tiver desativado o monitoramento de localização.

Para que as geofences funcionem, os usuários devem ter os serviços de localização ativados no dispositivo e devem ter concedido permissão ao app para acessar o local. Se um usuário tiver desativado o monitoramento de localização, seu app não conseguirá detectar quando ele entrar ou sair de uma geofence.

### Os dados de geofence são armazenados nos perfis de usuários?

Não, a Braze não armazena dados de geofence nos perfis de usuários. As geofences são monitoradas pelos serviços de local da Apple e do Google, e o Braze só é notificado quando um usuário dispara uma geofence. Nesse ponto, processamos todas as campanhas de disparo associadas.

### Posso configurar uma geofence dentro de uma geofence?

Como prática recomendada, evite configurar geofences entre si, pois isso pode causar problemas com o disparo de notificações.

