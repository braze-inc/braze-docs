---
nav_title: Compatibilidade com o visionOS
article_title: Compatibilidade com o visionOS
page_order: 7.2
platform: 
  - iOS
description: "Este artigo aborda os recursos compatíveis com o visionOS."
---

# Compatibilidade com o visionOS

> A partir do [Braze Swift SDK 8.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#800), é possível usar a Braze com o [visionOS](https://developer.apple.com/visionos/), a plataforma de computação espacial da Apple para o Apple Vision Pro. Para ver um exemplo de app do visionOS utilizando a Braze, consulte [Apps de amostra]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/sample_apps/).

## Recursos totalmente compatíveis

A maioria dos recursos disponíveis no iOS também está disponível no visionOS, tais como:

- Análise de dados (sessões, eventos personalizados, compras, etc.)
- Envio de mensagens no app (modelos de dados e UI)
- Cartões de Conteúdo (modelos de dados e UI)
- Notificações por push (visíveis ao usuário com botões de ação e notificações silenciosas)
- Feature Flags
- Análise de dados do local

## Recursos parcialmente suportados

Alguns recursos são compatíveis apenas parcialmente com o visionOS, mas é provável que a Apple resolva esses problemas no futuro:

- Notificações por push avançadas
  - Há suporte para imagens.
  - GIFs e vídeos exibem a miniatura de pré-visualização, mas não podem ser reproduzidos.
  - A reprodução de áudio não é suportada.
- Stories por push
  - Há suporte para rolagem e seleção da página do Story por push.
  - Não há suporte para a navegação entre as páginas do Story por push usando **Next**.

## Recursos incompatíveis

- Não há suporte para o monitoramento de geofences. A Apple não disponibilizou as APIs principais de localização para monitoramento de região no visionOS.
- Não há suporte para atividades ao vivo. No momento, o ActivityKit está disponível apenas para iOS e iPadOS.
