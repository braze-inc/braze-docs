---
nav_title: RudderStack
article_title: RudderStack
description: "Este artigo descreve a parceria entre o Braze e o RudderStack, uma infraestrutura de dados de clientes de código aberto que oferece integração perfeita da Braze para seus aplicativos Android, iOS e Web. Com o RudderStack, você pode enviar seus dados de eventos de clientes no app diretamente para o Braze para análise contextual."
page_type: partner
search_tag: Partner

---

# RudderStack

> [RudderStack](https://rudderstack.com/) é uma infraestrutura de dados de cliente de código aberto para coletar e direcionar dados de eventos de clientes para o seu data warehouse preferido e dezenas de outros provedores de análise, como Braze. Ele está pronto para empresas e oferece uma estrutura de transformação robusta para processar seus dados de eventos em tempo real.

A integração entre a Braze e o RudderStack oferece uma integração de SDK nativo para seus aplicativos Android, iOS e Web e uma integração de servidor para servidor de seus serviços de back-end.

## Pré-requisitos

| Requisito | Descrição |
| --- | --- |
| Conta do RudderStack | É necessário ter uma [conta RudderStack](https://app.rudderstack.com/) para usar a parceria. |
| Fonte configurada | Uma [source](https://www.rudderstack.com/docs/dashboard-guides/sources/) é essencialmente a origem de qualquer dado enviado para o RudderStack, como websites, aplicativos móveis ou servidores de backend. É necessário configurar a fonte antes de configurar o Braze como um destino no RudderStack. |
| chave da API REST Braze | Uma chave da API REST da Braze com as permissões `users.track`, `users.identify`, `users.delete` e `users.alias.new`.<br><br>Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**. |
| Chave do app da Braze | Para obter sua chave de aplicativo no dashboard do Braze, vá para **Configurações** > **Configurações do aplicativo** > **Identificação** e encontre o nome do seu aplicativo. Salva a string de identificador associada.
| Centro de dados | Seu data center se alinha com sua dashboard Braze [instance]({{site.baseurl}}/api/basics/#endpoints).  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Integração

### Etapa 1: Adicionar uma fonte

Para começar a enviar dados para a Braze, primeiro você precisa confirmar se há uma fonte configurada no seu app da RudderStack. Visite [RudderStack](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#getting-started) para aprender como configurar sua fonte de dados.

### Etapa 2: configure os destinos

Agora que sua fonte de dados está configurada, no dashboard do RudderStack, selecione **ADD DESTINATION (Adicionar destino** ) em **Destinations (Destinos**). Na lista de destinos disponíveis, selecione **Braze** e clique em **Next**.

No destino da Braze, forneça a chave do app, a chave da API REST da Braze, o cluster de dados e a opção de SDK nativo (somente no modo dispositivo). Se ativada, a opção de SDK nativo usará o SDK nativo da Braze para enviar eventos. 

![]({% image_buster /assets/img/RudderStack/braze_settings.png %}){: style="max-width:70%;margin-bottom:15px;border:none;"}

### Etapa 3: Escolha o tipo de integração

Você pode optar por integrar as bibliotecas web e nativas do lado do cliente do RudderStack com o Braze usando uma das seguintes abordagens:

- [Modo lado a lado / dispositivo](#device-mode)**:** O RudderStack enviará os dados do evento para a Braze diretamente do seu cliente (navegador ou aplicativo móvel).
- [Modo de servidor para servidor / nuvem](#cloud-mode)**:** O SDK da Braze envia os dados do evento diretamente para o RudderStack, onde são transformados e reencaminhados para a Braze.
- [Modo híbrido](#hybrid-mode)**:** Use o modo híbrido para enviar eventos gerados automaticamente pelo usuário e pelo iOS e Android para o Braze usando uma única conexão.

{% alert note %}
Saiba mais sobre os [modos de conexão](https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/) do RudderStack e os benefícios de cada um.
{% endalert %}

#### Integração lado a lado (modo dispositivo) {#device-mode}

Com esse modo, você pode enviar seus eventos para a Braze usando o SDK da Braze configurado em seu site ou app móvel.

Configure os mapeamentos para o SDK do RudderStack para sua plataforma no repositório do GitHub do Braze, conforme descrito em [supported methods](#supported-methods):

- [Android](https://github.com/rudderlabs/rudder-integration-braze-android)
- [iOS](https://github.com/rudderlabs/rudder-integration-braze-ios/tree/master)
- [Swift](https://github.com/rudderlabs/rudder-integration-braze-swift)
- [Web](https://github.com/rudderlabs/rudder-sdk-js/tree/production/src/integrations/Braze)
- [React Native](https://github.com/rudderlabs/rudder-sdk-react-native/tree/develop/libs/rudder-integration-braze-react-native)
- [Flutter](https://github.com/rudderlabs/rudder-sdk-flutter/tree/develop/packages/integrations/rudder_integration_braze_flutter)

Para concluir a integração do modo de dispositivo, consulte as instruções detalhadas do RudderStack para [adicionar o Braze ao seu projeto](https://rudderstack.com/docs/destinations/marketing/braze/#adding-device-mode-integration).

#### Integração de servidor para servidor (modo de nuvem) {#cloud-mode}

Nesse modo, o SDK envia os dados de evento diretamente para o servidor do RudderStack. Em seguida, o RudderStack transforma esses dados e os encaminha para os destinos desejados. Essa transformação é feita no backend do RudderStack usando o módulo de transformação do RudderStack.

Para ativar a integração, você precisará mapear os métodos do RudderStack para o Braze, conforme descrito em [métodos suportados](#supported-methods).

{% alert note %}
Os SDKs do lado do servidor do RudderStack (Java, Python, Node.js, Go, Ruby) suportam apenas o modo de nuvem. Isso ocorre porque seus SDKs do lado do servidor operam no back-end do RudderStack e não podem carregar nenhum SDK específico da Braze.
{% endalert %}

{% alert important %}
A integração de servidor para servidor não oferece suporte aos recursos da UI do Braze, como notificações por push ou envio de mensagens no app. Esses recursos são, no entanto, suportados pela integração do modo dispositivo.
{% endalert %}

#### Modo híbrido {#hybrid-mode}

Use o modo híbrido para enviar todos os eventos para o Braze a partir de suas fontes iOS e Android. 

Quando você escolhe o modo híbrido para enviar eventos para a Braze, o RudderStack:
1. Inicializa o SDK do Braze.
2. Envia todos os eventos gerados pelo usuário (identificar, rastrear, página, tela e grupo) para o Braze somente pelo modo de nuvem e impede que sejam enviados pelo modo de dispositivo.
3. Envia os eventos gerados automaticamente (mensagens no app, notificações por push que requerem o SDK do Braze) por meio do modo dispositivo.

Para [enviar eventos por meio do modo híbrido](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#send-events-in-hybrid-mode), use a opção de modo híbrido ao conectar sua origem ao destino do Braze. Em seguida, adicione a integração da Braze ao seu projeto.

## Etapa 4: Configurar definições adicionais

Após concluir a configuração inicial, defina as seguintes configurações para receber corretamente seus dados no Braze:

- **Ativar grupos de inscrições em chamadas em grupo**: Ative essa configuração para enviar o status do grupo de inscrições em seus eventos de grupo. Para saber mais, consulte [Grupo](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#group).
- **Use a operação de atributos personalizados**: Ative essa capacitação se quiser usar a funcionalidade de [atributos personalizados aninhados]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/array_of_objects/) no Braze para criar segmentos e personalizar suas mensagens usando um objeto de atributo personalizado. Para saber mais, consulte [Enviar características de usuário como atributos personalizados aninhados](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#send-user-traits-as-nested-custom-attributes).
- **Rastreamento de eventos para usuários anônimos**: Ative essa configuração para rastrear a atividade anônima do usuário e enviar essas informações ao Braze.

### Configurações do modo do dispositivo

As configurações a seguir são aplicáveis somente se você estiver enviando eventos para o Braze por meio do [modo dispositivo](https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode):

- **Filtragem de eventos no lado do cliente**: Essa configuração permite que você especifique quais eventos devem ser bloqueados ou autorizados a fluir para o Braze. Para saber mais sobre essa configuração, consulte [Filtragem de eventos no lado do cliente](https://www.rudderstack.com/docs/sources/event-streams/sdks/event-filtering/).
- **Desduplicar características**: Ative essa configuração para desduplicar as características do usuário na [`identify`](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#identify) chamada.
- **Mostrar os registros do Braze**: Essa configuração é aplicável somente ao usar o [SDK para JavaScript](https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/) como fonte. Ative-a para mostrar os registros do Braze aos seus usuários.
- **Categorias de cookies da OneTrust**: Essa configuração permite que você associe os grupos de consentimento de cookies [da OneTrust](https://www.rudderstack.com/docs/sources/event-streams/sdks/onetrust/javascript/) ao Braze.

## Métodos suportados

A Braze oferece suporte a estes métodos do RudderStack: identificar, rastrear, tela, página, grupo e alias.

{% tabs %}
{% tab Identificar %}

O [método `identify` do RudderStack](https://rudderstack.com/docs/destinations/marketing/braze/#identify) associa os usuários às suas ações. O RudderStack captura um ID de usuário exclusivo e características opcionais associadas a esse usuário, como nome, e-mail, endereço IP etc.

**Gerenciamento de diferenciais para identificar chamadas**<br>
Se enviar eventos para a Braze usando o modo dispositivo, você poderá economizar custos ao desduplicar suas chamadas para `identify`. Para fazer isso, ative a configuração de desduplicação de características no dashboard. O RudderStack envia apenas os atributos alterados ou modificados (traits) para a Braze.

**Exclusão de um usuário**<br>
É possível excluir um usuário no Braze usando a [regulamentação Suppression with Delete](https://www.rudderstack.com/docs/api/data-regulation-api/#adding-a-suppression-with-delete-regulation) da [API de regulamentação de dados](https://www.rudderstack.com/docs/api/data-regulation-api/) do RudderStack.

{% endtab %}
{% tab Rastrear %}

O [método`track` ](https://rudderstack.com/docs/destinations/marketing/braze/#track) do RudderStack captura todas as atividades do usuário e as propriedades associadas a essas atividades.

**Pedido concluído**<br>
Ao usar a [RudderStack eCommerce API](https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/) para chamar o método track para um evento com o nome `Order Completed`, o RudderStack envia os produtos listados nesse evento para o Braze como [`purchases`]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data/#revenue-data).

{% endtab %}
{% tab Tela %}

O [método`screen` ](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#screen) do RudderStack permite gravar as visualizações de tela móvel dos usuários com qualquer informação adicional sobre a tela visualizada.

{% endtab %}
{% tab Página %}

O [método `page`](https://rudderstack.com/docs/destinations/marketing/braze/#page) do RudderStack permite que você registre as visualizações de página do seu site. Ele também captura qualquer outra informação relevante sobre essa página.

{% endtab %}
{% tab Grupo %}

O [método `group`](https://rudderstack.com/docs/destinations/marketing/braze/#group) do RudderStack permite que você associe um usuário a um grupo.

**Status do grupo de inscrições**<br>
Para atualizar o status do grupo de inscrições, ative a configuração "Ativar grupos de inscrições na chamada de grupo" no dashboard do RudderStack e envie o status do grupo de inscrições na chamada de grupo.

{% endtab %}
{% tab Alias %}

O [método `alias`](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#alias) do RudderStack permite mesclar diferentes identidades de um usuário conhecido. Observe que o RudderStack oferece suporte à chamada de alias para a Braze somente no modo nuvem.

{% endtab %}
{% endtabs %}

## Enviar características do usuário como atributos personalizados aninhados

É possível enviar as características do usuário para o Braze como atributos personalizados aninhados e realizar operações de adição, atualização e remoção sobre eles. Para fazer isso, ative a configuração "Use Custom Attributes Operation dashboard" (Usar dashboard de operação de atributos personalizados) no RudderStack ao configurar o destino da Braze. Esse recurso só está disponível no modo de nuvem.

É possível enviar as características do usuário como atributos personalizados aninhados em seus eventos `identify` no seguinte formato:
```javascript
rudderanalytics.identify("1hKOmRA4GRlm", {
  "cars": {
    "add": [{
      "age": 27,
      "id": 1,
      "name": "Alex Keener"
    }],
    "update": [{
        "age": 30,
        "id": 2,
        "identifier": "id",
        "name": "Rowan"
      },
      {
        "age": 27,
        "id": 1,
        "identifier": "id",
        "name": "Mike"
      }
    ]
  },
  "country": "USA",
  "email": "alex@example.com",
  "firstName": "Alex",
  "gender": "M",
  "pets": [{
      "breed": "beagle",
      "id": 1,
      "name": "Scooby",
      "type": "dog"
    },
    {
      "breed": "calico",
      "id": 2,
      "name": "Garfield",
      "type": "cat"
    }
  ]
})
```

Para enviar as características de usuário como atributos personalizados de usuário por meio das chamadas `track`, `page` ou `screen`, passe `traits` como um campo contextual no evento:
```javascript
rudderanalytics.track("Product Viewed", {
    revenue: 8.99,
    currency: "USD",
 },{
  "traits": {
    "cars": {
      "add": [{
        "age": 27,
        "id": 1,
        "name": "Alex Keener"
      }],
      "update": [{
          "age": 30,
          "id": 2,
          "identifier": "id",
          "name": "Mike"
        },
        {
          "age": 27,
          "id": 1,
          "identifier": "id",
          "name": "Rowan"
        }
      ]
    },
    "city": "Disney",
    "country": "USA",
    "email": "alexa@example.com",
    "firstName": "Alexa",
    "gender": "woman",
    "pets": [{
        "breed": "beagle",
        "id": 1,
        "name": "Scooby",
        "type": "dog"
      },
      {
        "breed": "calico",
        "id": 2,
        "name": "Garfield",
        "type": "cat"
      }
    ]
  }
});
```

{% alert note %}
Para as operações de atualização e remoção, `identifier` é uma chave obrigatória. Se as operações de adição, atualização ou remoção não estiverem presentes na matriz aninhada, o RudderStack usará a operação de criação para criar as propriedades por padrão. Consulte [Vetor de objetos]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/array_of_objects/) para saber mais sobre o envio de atributos personalizados aninhados.
{% endalert %}

