---
nav_title: Guia de fazer upgrade do iOS 16
article_title: Guia de fazer upgrade do iOS 16
page_order: 7
platform: 
  - iOS
description: "Este artigo de referência abrange o iOS 16, como fazer upgrade, atualizações do SDK e mais."
hidden: true
noindex: true
---

# Guia de atualização do SDK para iOS 16

> Este guia descreve mudanças relevantes introduzidas pelo iOS 16 (2022) e o impacto na sua integração de SDK da Braze para iOS. Consulte um guia completo de migração nas [notas de versão do iOS 16](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-16-release-notes).

## Mudanças no iOS 16

### Web push do Safari {#safari-web-push}

A Apple anunciou duas mudanças em sua funcionalidade de web push.

#### Web push para desktop (MacOS) {#macos-push}

Antes, a Apple aceitava notificações por push no MacOS (desktop) usando suas próprias APIs de push do Safari.

A partir do macOS Ventura (lançado em 24 de outubro de 2022), [o Safari passou a ser compatível com APIs de web push](https://webkit.org/blog/12824/news-from-wwdc-webkit-features-in-safari-16-beta/#web-push-for-macos) além do push do Safari. Esse é um padrão de API existente entre navegadores usado em outros navegadores populares.

Se você já envia web push para o Safari pela Braze, nenhuma mudança é necessária.

#### Web push para dispositivos móveis (iOS e iPadOS) {#ios-push}

Antes, o Safari no iPhone e iPad não aceitava o recebimento de notificações por push.

Em 2023, a Apple adicionará suporte para web push em dispositivos iPhone e iPad através do Safari.

A Braze será compatível com esse novo web push do iOS e iPadOS sem exigir alterações ou atualizações adicionais.

## Como se preparar para o iOS 16 {#next-steps}

Embora você não precise fazer upgrade do SDK da Braze para iOS 16, há duas outras atualizações interessantes:

1. A Braze lançou um [novo Swift SDK](https://github.com/braze-inc/braze-swift-sdk). Ele traz melhor performance, novos recursos e muitos aprimoramentos.
2. Nosso SDK SWIFT da Braze suporta um novo recurso de primer de push ["sem código"]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_primer_messages/)!

