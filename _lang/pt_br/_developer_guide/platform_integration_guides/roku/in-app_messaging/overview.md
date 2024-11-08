---
nav_title: Visão geral
article_title: Visão geral das mensagens no app para Roku
platform: Roku
channel: in-app messages
page_order: 0
page_type: reference
description: "Este artigo aborda uma visão geral das mensagens no app da Roku, incluindo práticas recomendadas e casos de uso."

---

# Visão geral das mensagens no app

> [As mensagens no app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/) ajudam a levar o conteúdo ao usuário sem interromper o dia dele com uma notificação por push. Mensagens no app personalizadas e sob medida aprimoram a experiência do usuário e ajudam o público a obter o máximo valor do seu app. Com uma variedade de layouts e ferramentas de personalização para escolher, as mensagens no app engajam seus usuários mais do que nunca.

Confira nossos [estudos de caso](https://www.braze.com/customers) para ver exemplos de mensagens no app.

![Três imagens de possíveis mensagens no app da Roku que um usuário poderia criar. Esses exemplos incluem "captura de tela cheia", "banner da página inicial" e "notificador de canto".]({% image_buster /assets/img/roku/Docs-Imagery.png %})

## Tipos de mensagens no app

Crie uma mensagem no app para o Roku selecionando **Dispositivos Roku** como a plataforma de mensagem no app.

![]({% image_buster /assets/img/roku/1-Platform-Selector.png %})

## Documentação técnica

Visite nosso [guia de integração]({{ site.baseurl }}/developer_guide/platform_integration_guides/roku/in-app_messaging/integration) para instruções sobre como exibir mensagens no aplicativo e registrar impressões e análise de dados.

![Um exemplo de "banner da página inicial" mostrando os diferentes componentes necessários para criar o banner personalizado. Os componentes listados incluem o componente de composição de mensagem (mostrando o corpo, texto do botão, imagem, comportamento do botão atribuído (deep link) e pares chave-valor), os detalhes do backend (público listado como "usuários que assistiram à temporada 1", interações pretendidas (botão deeplinks para app, fechar a mensagem descarta a mensagem e descarte automático após 10 segundos), o disparador (início da sessão) e o par chave-valor (modelo = homepage_banner)).]({% image_buster /assets/img/roku/Roku-In-App-Messages-Example.png %})

## Testes e controle de qualidade

O recurso de envio de teste não é compatível com as mensagens no app do Roku. Para testar uma mensagem, inicie a campanha filtrada apenas para o seu ID de usuário.

