---
nav_title: Pares de valores-chave
article_title: Pares de chave-valor
page_order: 4
description: "Este artigo de referência aborda os pares de valores-chave e como usá-los para enviar cargas extras de dados para dispositivos de usuários."
channel:
  - push
  - in-app messages
  - content cards

---

# Pares de valores-chave

> Esta página aborda como usar pares de valores-chave para enviar cargas extras de dados para dispositivos de usuários. Esse recurso está disponível nos canais de mensagens push, no aplicativo, por e-mail e Content Card.

Use pares de valores-chave para adicionar metadados estruturados às mensagens. Esses payloads de dados extras podem enriquecer as mensagens com informações contextuais adicionais que podem influenciar a forma como uma mensagem é renderizada ou processada.

Como os pares de valores-chave são metadados, esses dados não são necessariamente visíveis para o destinatário, mas podem ser usados por seus sistemas ou processos conectados para personalizar o tratamento de mensagens. 

Cada par é composto por:

- **Chave:** O identificador (Exemplo: `utm_source`)
- **Valor:** Os dados associados (Exemplo: `newsletter`)

## Casos de uso

Aqui estão alguns exemplos de casos de uso para adicionar metadados com pares de valores-chave:

1. **Parâmetros de rastreamento:** Anexar parâmetros UTM para fins de análise
   - Chave: `utm_campaign`
   - Valor: `spring_sale`
2. **Etiquetas personalizadas:** Adição de tags para roteamento interno ou categorização
   - Chave: `priority`
   - Valor: `high`
3. **Acionadores de comportamento:** Metadados usados para acionar ou personalizar comportamentos in-app
   - Chave: `deep_link`
   - Valor: `app://promo-page`

## Notificações push

Os pares de valores-chave podem ser adicionados a notificações push para Android, iOS e Web. Você pode usar pares de valores-chave para atualizar métricas internas e o conteúdo do aplicativo ou personalizar as propriedades da notificação por push, como priorização de alertas, localização e sons.

No compositor de mensagens, selecione a guia **Settings (Configurações** ), selecione **Add New Pair (Adicionar novo par**) e especifique seus pares de valores-chave.

### iOS

O serviço de notificação por push da Apple (APNs) permite definir preferências de alerta e enviar dados personalizados usando pares de valores-chave. Os APNs usam a biblioteca ```aps```, reservada pela Apple, que inclui chaves e valores predeterminados que controlam as propriedades do alerta.

##### Biblioteca da APS

| Chave  | Tipo de valor  | Descrição do valor |
|-------------------|-----------------------------|----------------------------------|
| alerta             | string ou objeto de dicionário | Para entradas de cadeia de caracteres, exibe um alerta com a cadeia de caracteres como a mensagem com os botões Fechar e Exibir; para entradas que não sejam de cadeia de caracteres, exibe um alerta ou um banner, dependendo das propriedades secundárias do input |
| crachá             | número                      | Controla o número que é exibido como o emblema no ícone do aplicativo                                                                                                                              |
| som             | string                      | O nome do arquivo de som a ser reproduzido como um alerta; deve estar no pacote do aplicativo ou na pasta ```Library/Sounds```.                                                                                    |
| disponível para conteúdo | número                      | Valores de entrada de 1 sinalizam para o aplicativo a disponibilidade de novas informações na inicialização ou na retomada da sessão |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


##### Biblioteca de propriedades de alerta

| Chave            | Tipo de valor               | Descrição do valor                                                                                                                             |
|----------------|--------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| título         | string                   | Uma sequência curta que o Apple Watch exibe brevemente como parte de uma notificação                                                                    |
| corpo         | string                   | O conteúdo da notificação por push                                                                                                                  |
| chave de localização do título  | string ou nulo           | Uma chave que define a string de título para a localização atual do arquivo ```Localizable.strings```                                           |
| title-loc-args | matriz de cadeias de caracteres ou nula | Valores de cadeia de caracteres que podem aparecer no lugar dos especificadores de formato de localização do título em title-loc-key                                           |
| chave de localização de ação | matriz de string ou nula  | Se presente, a cadeia de caracteres especificada define a localização dos botões Fechar e Exibir                                                         |
| chave de localização        | string ou nulo           | Uma chave que define a mensagem de notificação para a localização atual do arquivo ```Localizable.strings```                                   |
| loc-args       | matriz de cadeias de caracteres         | Valores de cadeia de caracteres que podem aparecer no lugar dos especificadores de formato de localização em loc-key                                                       |
| imagem de lançamento   | cadeias de caracteres                  | O nome de um arquivo de imagem no pacote de aplicativos que você deseja que seja usado como imagem de inicialização quando os usuários tocarem no botão de ação ou moverem o slide de ação |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

O compositor de mensagens do Braze lida automaticamente com a criação das seguintes chaves: **alert** e **suas propriedades**, **content-available**, **sound** e **category**. 

Esses valores podem ser inseridos na guia **Configurações** ao criar uma mensagem push. Selecione **Opções de alerta** e selecione uma chave de dicionário de alerta para que a chave seja preenchida automaticamente em uma nova entrada de valor-chave.

\![]({% image_buster /assets/img_archive/keyvalue_automatickeys.png %})
{% raw %}
Quando o Braze envia uma notificação push para APNs, o payload será formatado como JSON.

**Carga útil simples**

```
{
    "aps" : { "alert" : "Message received from Spencer" },
}
```

**Carga útil complexa**

```
{
    "aps" : {
        "alert" : {
            "body" : "Hi, welcome to our app!",
            "loc-key" : "France",
            "loc-args" : ["Bonjour", "bienvenue"],
            "action-loc-key" : "Button_Type_1",
            "launch-image" : "Paris"
      },
        "content-available" : 1
    },
}
```

{% endraw %}

##### Pares de valores-chave personalizados

Além dos valores de carga útil da biblioteca ```aps```, você pode enviar pares de valores-chave personalizados para o dispositivo de um usuário. Os valores nesses pares são restritos a tipos primitivos: dicionário (objeto), matriz, cadeia de caracteres, número e booleano.

\![]({% image_buster /assets/img_archive/keyvalue_enterpairs.png %})

Os casos de uso de pares de valores-chave personalizados incluem, entre outros, a manutenção de métricas internas e a definição do contexto da interface do usuário. O Braze permite que você envie pares de valores-chave adicionais junto com uma notificação push a ser usada por meio do seu aplicativo dentro da [chave extra]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/customization/advanced_settings/#extracting-data-from-push-key-value-pairs). Se preferir usar outra chave, confirme se seu aplicativo pode lidar com essa chave personalizada.

{% alert warning %}
Evite manipular uma chave de nível superior ou um dicionário chamado ab em seu aplicativo.
{% endalert %}

A Apple aconselha os clientes a evitarem incluir informações de clientes ou quaisquer dados confidenciais como dados de carga personalizada. Além disso, a Apple recomenda que qualquer ação associada a uma mensagem de alerta não exclua dados em um dispositivo.

{% alert warning %}
Se você estiver usando a API do provedor HTTP/2, qualquer carga útil individual enviada aos APNs não poderá exceder o tamanho de 4096 bytes. A interface binária legada, que em breve será depreciada, suporta apenas um tamanho de carga útil de 2048 bytes.
{% endalert %}

###### Campanhas acionadas por API

O Braze permite que você envie pares de valores-chave de cadeia de caracteres personalizados, conhecidos como `extras`. Para acessar seus extras em campanhas acionadas por API e campanhas acionadas por API programadas, no painel, defina uma chave como "example_key", e um valor como {% raw %}`"$json:{"foo": 1, "bar": 1}"`{% endraw %}. Isso resultará em uma saída do console do desenvolvedor de `"extras": { "test": { "foo": 1, "bar": 1 }`

### Android

O Braze permite que você envie cargas úteis de dados adicionais em notificações push usando pares de valores-chave.

##### Carga útil de dados

Semelhante ao iOS push, você pode enviar pares de valores-chave personalizados para o dispositivo de um usuário.

Alguns casos de uso de pares de valores-chave personalizados incluem a manutenção de métricas internas e a definição do contexto da interface do usuário, mas eles podem ser usados para qualquer finalidade que você escolher.

{% alert important %}
O back-end do seu aplicativo deve ser capaz de processar pares de valores-chave personalizados para que a carga de dados funcione corretamente.
{% endalert %}

###### Campanhas acionadas por API

O Braze permite que você envie pares de valores-chave de cadeia de caracteres personalizados, conhecidos como `extras`. Para acessar seus extras em campanhas acionadas por API e campanhas acionadas por API programadas, no painel, defina uma chave como "example_key", e um valor como {% raw %}`"$json:{"foo": 1, "bar": 1}"`{% endraw %}. Isso resultará em uma saída do console do desenvolvedor de `"extras": { "test": { "foo": 1, "bar": 1 }`.

##### Opções de mensagens FCM

As notificações push do Android podem ser ainda mais personalizadas com opções de mensagens FCM. Isso inclui [prioridade de notificação]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/customization/advanced_settings/#notification-priority), [som]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/customization/advanced_settings/#sounds), atraso, vida útil e colapsabilidade. Esses valores podem ser especificados na guia **Configurações** ao criar uma mensagem push. Consulte [Configurações avançadas de notificação por push]({{site.baseurl}}/developer_guide/push_notifications/customization/?sdktab=android#android_settings) para obter mais instruções sobre como definir essas opções no compositor de mensagens do Braze.

\![]({% image_buster /assets/img_archive/keyvalue_androidkeys.png %})

### Notificações push silenciosas

Uma notificação push silenciosa é uma notificação push sem mensagem de alerta ou som, usada para atualizar a interface ou o conteúdo do seu aplicativo em segundo plano. Essas notificações usam pares de valores-chave para acionar essas ações do aplicativo em segundo plano. As notificações push silenciosas também alimentam nosso [rastreamento de desinstalação]({{site.baseurl}}/user_guide/analytics/tracking/uninstall_tracking/).

Os profissionais de marketing devem testar se as notificações push silenciosas acionam o comportamento esperado antes de enviá-las aos usuários do aplicativo. Depois de redigir a notificação por push silenciosa [para iOS]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift) ou [Android]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=android), certifique-se de que o alvo seja apenas um usuário de teste, filtrando o [ID do usuário externo]({{site.baseurl}}/developer_guide/rest_api/messaging/#external-user-id) ou [o endereço de e-mail]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/).

Após o lançamento da campanha, você deve verificar se não recebeu nenhuma notificação push visível em seu dispositivo de teste.

{% alert note %}
O sistema operacional iOS pode [bloquear as notificações]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/silent_push_notifications/#ios-silent-notifications-limitations) de alguns recursos (rastreamento de desinstalação, cercas geográficas e Push Stories). Observe que, se você estiver tendo dificuldades com esses recursos, a porta de notificações silenciosas do iOS pode ser a causa.
{% endalert %}

## Mensagens no aplicativo

Para adicionar um par de valores-chave a uma mensagem in-app, selecione a guia **Configurações** no compositor de mensagens, selecione **Adicionar novo par** e especifique seus pares de valores-chave.

\![]({% image_buster /assets/img_archive/keyvalue_iam.png %})

#### Campanhas acionadas por API

O Braze permite que você envie pares de valores-chave de cadeia de caracteres personalizados, conhecidos como `extras`. Para acessar seus extras em campanhas acionadas por API e campanhas acionadas por API programadas, no painel, defina uma chave como "example_key", e um valor como {% raw %}`"$json:{"foo": 1, "bar": 1}"`{% endraw %}. Isso resultará em uma saída do console do desenvolvedor de `"extras": { "test": { "foo": 1, "bar": 1 }`.

## E-mails

Tanto o SparkPost quanto o SendGrid suportam pares de valores-chave em e-mails. Se você usar o SendGrid, os pares de valores-chave serão enviados como [argumentos exclusivos](https://docs.sendgrid.com/for-developers/sending-email/unique-arguments). O SendGrid permite que você anexe um número ilimitado de pares de valores-chave de até 10.000 bytes de dados. Esses pares de valores-chave podem ser vistos nas postagens do [Webhook de evento](https://sendgrid.com/docs/for-developers/tracking-events/event/) da SendGrid.

{% alert note %}
Os e-mails devolvidos não entregarão pares de valores-chave ao SparkPost ou SendGrid.
{% endalert %}

\![Guia Informações de envio do compositor de mensagens de e-mail no Braze.]({% image_buster /assets/img_archive/keyvalue_email.png %})

## Cartões de conteúdo

Para adicionar um par chave-valor a um Content Card, vá para a guia **Settings (Configurações** ) no compositor de mensagens do Braze e selecione **Add New Pair (Adicionar novo par**).

\![Adicionar par chave-valor ao cartão de conteúdo]({% image_buster /assets/img_archive/kvp_content_cards.png %}){: style="max-width:70%;"}


