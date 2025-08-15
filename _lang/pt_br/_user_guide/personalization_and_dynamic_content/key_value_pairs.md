---
nav_title: Pares Chave-Valor
article_title: Pares Chave-Valor
page_order: 4
description: "Este artigo de referência cobre pares chave-valor e como usá-los para enviar cargas úteis de dados extras para dispositivos dos usuários."
channel:
  - push
  - in-app messages
  - content cards

---

# Pares chave-valor

> Esta página cobre como usar pares de chave-valor para enviar cargas úteis de dados extras para dispositivos de usuários. Este recurso está disponível nos canais de envio de mensagens push, in-app, e-mail e cartão de conteúdo.

Use pares de valores-chave para adicionar metadados estruturados às mensagens. Essas cargas úteis de dados extras podem enriquecer as mensagens com informações contextuais adicionais que podem influenciar a forma como uma mensagem é renderizada ou processada.

Como os pares chave-valor são metadados, esses dados não são necessariamente visíveis para o destinatário, mas podem ser usados por seus sistemas ou processos conectados para personalizar o envio de mensagens. 

Cada par é composto por:

- **Chave:** O identificador (Exemplo: `utm_source`)
- **Valor:** Os dados associados (Exemplo: `newsletter`)

## Casos de uso

Aqui estão alguns exemplos de casos de uso para adicionar metadados com pares de valores-chave:

1. **Parâmetros de rastreamento:** Anexar parâmetros UTM para fins de análise de dados
   - Chave: `utm_campaign`
   - Valor: `spring_sale`
2. **Tags personalizadas:** Adição de tags para roteamento interno ou categorização
   - Chave: `priority`
   - Valor: `high`
3. **Disparadores de comportamento:** Metadados usados para disparar ou personalizar comportamentos in-app
   - Chave: `deep_link`
   - Valor: `app://promo-page`

## Notificações por push

Os pares de valores-chave podem ser adicionados a notificações por push para Android, iOS e web push. Você pode usar pares de valores-chave para atualizar métricas internas e o conteúdo do app ou personalizar as propriedades da notificação por push, como priorização de alertas, localização e sons.

No criador de mensagem, selecione a guia **Configurações**, selecione **Adicionar novo par** e especifique seus pares de chave-valor.

### iOS

O serviço de Notificações por Push da Apple (APNs) suporta a definição de preferências de alerta e o envio de dados personalizados usando pares chave-valor. APNs faz uso da biblioteca reservada pela Apple ```aps```, que inclui chaves e valores predeterminados que governam as propriedades de alerta.

##### biblioteca APS

| Chave  | Tipo de Valor  | Descrição do valor |
|-------------------|-----------------------------|----------------------------------|
| alerta             | string ou objeto de dicionário | Para entradas de string, exibe um alerta com a string como mensagem com botões Fechar e Visualizar; para entradas não-string, exibe um alerta ou banner dependendo das propriedades filhas da entrada |
| ícone             | número                      | Governa o número que é exibido como o emblema no ícone do app                                                                                                                              |
| som             | string                      | O nome do arquivo de som a ser reproduzido como um alerta; deve estar no pacote do app ou na pasta ```Library/Sounds```                                                                                    |
| content-available | número                      | Valores de entrada de 1 sinalizam ao app a disponibilidade de novas informações ao iniciar ou retomar a sessão |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


##### Biblioteca de propriedades de alerta

| Chave            | Tipo de Valor               | Descrição do valor                                                                                                                             |
|----------------|--------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| title         | string                   | Uma string curta que o Apple Watch exibe brevemente como parte de uma notificação                                                                    |
| corpo         | string                   | O conteúdo da notificação por push                                                                                                                  |
| title-loc-key  | string ou nulo           | Uma chave que define a string de título para a localização atual do arquivo ```Localizable.strings```                                          |
| title-loc-args | array de strings ou nulo | Valores de string que podem aparecer no lugar dos especificadores de formato de localização de título em title-loc-key                                           |
| action-loc-key | array de string ou nulo  | Se presente, a string especificada define a localização dos botões Fechar e Visualizar                                                         |
| chave de localização        | string ou nulo           | Uma chave que define a mensagem de notificação para a localização atual do arquivo ```Localizable.strings```                                  |
| loc-args       | array de strings         | Valores de string que podem aparecer no lugar dos especificadores de formato de localização em loc-key                                                       |
| imagem de lançamento   | cordas                  | O nome de um arquivo de imagem no pacote do app que você deseja usar como imagem de lançamento quando os usuários tocarem no botão de ação ou moverem o slide de ação |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

O criador de mensagem da Braze lida automaticamente com a criação das seguintes chaves: **alert** e **suas propriedades**, **content-available**, **sound** e **category**. 

Esses valores podem ser inseridos na guia **Configurações** ao criar uma messagem de push. Selecione **Opções de Alerta** e selecione uma chave de dicionário de alerta para que a chave seja automaticamente preenchida em uma nova entrada de chave-valor.

![]({% image_buster /assets/img_archive/keyvalue_automatickeys.png %})
{% raw %}
Quando a Braze envia uma notificação por push para a APNs, a carga útil será formatada como um JSON.

**Simples carga útil**

```
{
    "aps" : { "alert" : "Message received from Spencer" },
}
```

**Carga Útil Complexa**

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

##### Pares de chave-valor personalizados

Além dos valores de carga útil da biblioteca ```aps```, você pode enviar pares de chave-valor personalizados para o dispositivo de um usuário. Os valores nesses pares são restritos a tipos primitivos: dicionário (objeto), array, string, número e booleano.

![]({% image_buster /assets/img_archive/keyvalue_enterpairs.png %})

Os casos de uso para pares de chave-valor personalizados incluem, mas não se limitam a, manter métricas internas e definir o contexto para a interface do usuário. O Braze permite que você envie pares de chave-valor adicionais junto com uma notificação por push para serem usados em seu aplicativo dentro da [chave extras]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/customization/advanced_settings/#extracting-data-from-push-key-value-pairs). Se você preferir usar outra chave, confirme que seu app pode lidar com essa chave personalizada.

{% alert warning %}
Você deve evitar lidar com uma chave de nível superior ou dicionário chamado ab em seu aplicativo.
{% endalert %}

A Apple aconselha os clientes a evitar incluir informações de clientes ou quaisquer dados sensíveis como dados de carga útil personalizados. Além disso, a Apple recomenda que qualquer ação associada a uma mensagem de alerta não deve excluir dados em um dispositivo.

{% alert warning %}
Se você estiver usando a API do provedor HTTP/2, qualquer carga útil individual que você enviar para APNs não pode exceder um tamanho de 4096 bytes. A interface binária legada, que em breve será depreciada, suporta apenas um tamanho de carga útil de 2048 bytes.
{% endalert %}

###### campanhas acionadas por API

A Braze permite que você envie pares de chave-valor de string definidos pelo usuário, conhecidos como `extras`. Para acessar seus extras em campanhas acionadas por API e campanhas acionadas por API agendadas, no dashboard defina uma chave como "example_key" e um valor como {% raw %}`"$json:{"foo": 1, "bar": 1}"`{% endraw %}. Isso resultará em um console de desenvolvedor de saída de `"extras": { "test": { "foo": 1, "bar": 1 }`

### Android

A Braze permite que você envie cargas de dados adicionais em notificações por push usando pares chave-valor.

##### Carga útil de dados

Semelhante ao push do iOS, você pode enviar pares de chave-valor personalizados para o dispositivo de um usuário.

Alguns casos de uso para pares chave-valor personalizados incluem a manutenção de métricas internas e a definição do contexto para a interface do usuário, mas podem ser usados para qualquer finalidade que você escolher.

{% alert important %}
O backend do seu app deve ser capaz de processar pares chave-valor personalizados para que a carga útil dos dados funcione corretamente.
{% endalert %}

###### campanhas acionadas por API

A Braze permite que você envie pares de chave-valor de string definidos pelo usuário, conhecidos como `extras`. Para acessar seus extras em campanhas acionadas por API e campanhas acionadas por API agendadas, no dashboard defina uma chave como "example_key" e um valor como {% raw %}`"$json:{"foo": 1, "bar": 1}"`{% endraw %}. Isso resultará em um console de desenvolvedor de saída de `"extras": { "test": { "foo": 1, "bar": 1 }`

##### Opções de envio de mensagens do FCM

As notificações por push do Android podem ser ainda mais personalizadas com as opções de mensagens do FCM. Estes incluem [prioridade de notificação]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/customization/advanced_settings/#notification-priority), [som]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/customization/advanced_settings/#sounds), postergação, vida útil e colapsabilidade. Esses valores podem ser inseridos na guia **Configurações** ao criar uma messagem de push. Consulte [Configurações avançadas de notificação por push]({{site.baseurl}}/developer_guide/push_notifications/customization/?sdktab=android#android_settings) para obter mais instruções sobre como definir essas opções no criador de mensagem do Braze.

![]({% image_buster /assets/img_archive/keyvalue_androidkeys.png %})

### Notificações por push silenciosas

Uma notificação por push silenciosa é uma notificação por push que não contém mensagem de alerta ou som, usada para atualizar a interface ou o conteúdo do seu app em segundo plano. Essas notificações utilizam pares de chave-valor para disparar essas ações de app em segundo plano. Notificações por push silenciosas também alimentam nosso [rastreamento de desinstalação]({{site.baseurl}}/user_guide/analytics/tracking/uninstall_tracking/).

Os profissionais de marketing devem testar esse comportamento esperado do disparo de notificações por push silenciosas antes de enviá-las aos usuários do app. Depois de compor sua [iOS]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift) ou [Android]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=android) notificação por push silenciosa, certifique-se de direcionar apenas um usuário teste filtrando pelo [ID de usuário externo]({{site.baseurl}}/developer_guide/rest_api/messaging/#external-user-id) ou [endereço de e-mail]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/).

Após o lançamento da campanha, você deve verificar se não recebeu nenhuma notificação por push visível no seu dispositivo de teste.

{% alert note %}
O sistema operacional iOS pode [bloquear notificações]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/silent_push_notifications/#ios-silent-notifications-limitations) para alguns recursos (rastreamento de desinstalação, geofences e stories por push). Se você estiver enfrentando dificuldades com esses recursos, o gate de notificações silenciosas do iOS pode ser a causa.
{% endalert %}

## Mensagem no app

Para adicionar um par de chave-valor a uma mensagem no app, selecione a guia **Configurações** no criador de mensagem, selecione **Adicionar novo par** e especifique seus pares de chave-valor.

![]({% image_buster /assets/img_archive/keyvalue_iam.png %})

#### campanhas acionadas por API

A Braze permite que você envie pares de chave-valor de string definidos pelo usuário, conhecidos como `extras`. Para acessar seus extras em campanhas acionadas por API e campanhas acionadas por API agendadas, no dashboard defina uma chave como "example_key" e um valor como {% raw %}`"$json:{"foo": 1, "bar": 1}"`{% endraw %}. Isso resultará em um console de desenvolvedor de saída de `"extras": { "test": { "foo": 1, "bar": 1 }`

## E-mails

Tanto o SparkPost quanto o SendGrid aceitas pares de chave/valor em e-mails. Se você usar o SendGrid, pares de chave/valor serão enviados como [argumentos únicos](https://docs.sendgrid.com/for-developers/sending-email/unique-arguments). SendGrid permite que você anexe um número ilimitado de pares chave-valor até 10.000 bytes de dados. Esses pares de chave-valor podem ser vistos em postagens do [Webhook de Eventos](https://sendgrid.com/docs/for-developers/tracking-events/event/) do SendGrid.

{% alert note %}
E-mails devolvidos não entregarão pares chave-valor para SparkPost ou SendGrid.
{% endalert %}

![Enviando a guia de informações do criador de mensagem de e-mail no Braze.]({% image_buster /assets/img_archive/keyvalue_email.png %})

## Cartões de conteúdo

Para adicionar um par de chave-valor a um cartão de conteúdo, acesse a guia **Configurações** no criador de mensagem do Braze e selecione **Adicionar novo par**.

![Adicionar par chave-valor ao cartão de conteúdo]({% image_buster /assets/img_archive/kvp_content_cards.png %}){: style="max-width:70%;"}


