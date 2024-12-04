---
nav_title: Configurações push
article_title: Configurações push para iOS
platform: Swift
page_order: 7
description: "Este artigo de referência aborda as configurações avançadas de notificação por push do iOS, como opções de alerta, sons, vencimento e muito mais, para o Swift SDK."
channel:
  - push

---

# Configurações push

> Ao criar uma campanha push por meio do dashboard, clique na guia **Settings (Configurações)** na etapa **Compose (Redigir** ) para visualizar as configurações avançadas disponíveis.

![]({% image_buster /assets/img_archive/ios_advanced_settings.png %})

## Pares chave-valor

A Braze permite que você envie pares de chave/valor de string personalizados, conhecidos como `extras`, juntamente com uma notificação por push para o seu app. Os extras podem ser definidos por meio do dashboard ou da API e estarão disponíveis como pares de valores-chave no dicionário `notification` passado para suas implementações de delegados push.

## Opções de alerta

Marque a caixa de seleção **Opções de alerta** para ver um menu suspenso de valores-chave disponíveis para ajustar como a notificação aparece nos dispositivos.

## Adição do sinalizador content-available

Marque a caixa de seleção **Adicionar sinalizador de conteúdo disponível** para instruir os dispositivos a baixar novos conteúdos em segundo plano. Geralmente, isso pode ser verificado se você estiver interessado em enviar [notificações silenciosas]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/silent_push_notifications/).

## Adição do sinalizador de conteúdo mutável

Marque a caixa de seleção **Add Mutable-Content Flag (Adicionar sinalizador de conteúdo mutável** ) para ativar a capacitação avançada do receptor. Esse sinalizador será enviado automaticamente ao criar uma [notificação Rich]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/customization/rich_notifications/), independentemente do valor dessa caixa de seleção.

## Atualizar o contador de avisos do app

Digite o número para o qual deseja atualizar a contagem de crachás ou use a sintaxe Liquid para definir condições personalizadas. Você também pode atualizar a contagem de emblemas de mensagens de forma programática: consulte nosso artigo dedicado à [contagem de emblemas]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/customization/badges/).

## Sons

Se quiser que a notificação por push seja acompanhada de um som personalizado quando for recebida, use o campo **Sound (Som)** para especificar o URL do protocolo do arquivo de som. Para obter mais informações sobre personalização, consulte nosso artigo sobre [sons personalizados]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/customization/custom_sounds/).

## ID de recolhimento

Especifique uma ID de recolhimento para agrupar notificações semelhantes. Se você enviar várias notificações com a mesma ID de colapso, o dispositivo mostrará apenas a notificação recebida mais recentemente. Consulte a documentação da Apple sobre [notificações agrupadas](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1).

## Expiração

Ao marcar a caixa de seleção **Vencimento**, você poderá definir um tempo de expiração para sua mensagem. Se o dispositivo de um usuário perder a conectividade, o Braze continuará a tentar enviar a mensagem até o horário especificado. Se isso não for definido, a plataforma terá como padrão uma expiração de 30 dias. Observe que as notificações por push que expiram antes da entrega não são consideradas falhas e não serão registradas como bounce.

