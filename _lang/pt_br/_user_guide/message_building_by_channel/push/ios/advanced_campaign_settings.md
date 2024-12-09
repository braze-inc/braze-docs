---
nav_title: "Configurações avançadas de campanhas push"
article_title: Configurações avançadas de campanhas push
page_type: reference
page_order: 6
description: "Este artigo de referência aborda várias configurações avançadas de campanhas push, como opções de alerta, sinalizadores, sons, vencimento e muito mais."
platform: iOS
channel:
  - push
tool:
  - Campaigns

---

# Configurações avançadas de campanhas push

> Este artigo de referência aborda várias configurações avançadas de campanhas push, como opções de alerta, sinalizadores, sons, vencimento e muito mais.

Ao criar um engajamento com mensagem push, na etapa **Compose (Criar** ), você pode selecionar o ícone de engrenagem <i class="fas fa-cog"></i> para visualizar as configurações avançadas da mensagem.

![][1]

## Opções de alerta

Ao marcar a caixa de seleção aqui, você verá um menu suspenso de valores-chave disponíveis para ajustar como a notificação será exibida nos dispositivos.

## Adição do sinalizador content-available

O sinalizador `content-available` instrui os dispositivos a baixar novos conteúdos em segundo plano. Geralmente, isso pode ser verificado se você estiver interessado em enviar [notificações silenciosas][2].

## Adição do sinalizador de conteúdo mutável

O sinalizador `mutable-content` ativa a capacitação avançada do receptor em dispositivos iOS 10+. Esse sinalizador será enviado automaticamente ao criar uma [notificação Rich][3], independentemente do valor dessa caixa de seleção.

## Sons

Aqui, você pode inserir uma jornada para um arquivo de som no pacote do seu app para especificar um som a ser reproduzido quando a mensagem no app for recebida. Se o arquivo de som especificado não existir ou se a palavra-chave "default" for inserida, a Braze usará o som de alerta padrão do dispositivo.

## ID de recolhimento
Especifique um ID de recolhimento para aglutinar notificações semelhantes. Caso você envie diversas notificações com o mesmo ID de recolhimento, o dispositivo mostrará apenas a notificação recebida por último. Para saber mais, consulte a [documentação da Apple][4].

## Expiração

A seleção de **Expirar** oferecerá a opção de definir um horário de expiração da sua mensagem. Se o dispositivo de um usuário perder a conectividade, a Braze continuará tentando enviar a mensagem até o horário especificado. Se isso não for definido, a plataforma terá como padrão uma expiração de 30 dias. Observe que as notificações por push que expiram antes da entrega não são consideradas como falha e não serão registradas como bounce.

[1]: {% image_buster /assets/img_archive/ios_advanced_settings.gif %}
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/silent_push_notifications/
[3]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#ios-10-rich-notifications
Daqui a [4]: https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1
