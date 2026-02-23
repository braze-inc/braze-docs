---
page_order: 2.1
nav_title: Aplicativos ChatGPT
article_title: Integre Braze com Aplicativos ChatGPT
description: "Aprenda como integrar Braze com Aplicativos ChatGPT para ativar análise de dados e registro de eventos dentro de aplicativos impulsionados por IA."
platform:
  - ChatGPT Apps
---

# Integre Braze com aplicativos ChatGPT

> Este guia cobre como integrar Braze com aplicativos ChatGPT para ativar análise de dados e registro de eventos dentro de aplicativos impulsionados por IA.

![Um Cartão de Conteúdo integrado ao aplicativo ChatGPT.]({% image_buster /assets/img/chatgpt_app_integration.png %}){: style="float:right;max-width:30%;border:none;" }

## Visão geral

Os aplicativos ChatGPT fornecem uma plataforma poderosa para construir aplicativos de conversação com IA. Ao integrar Braze com seu aplicativo ChatGPT, você pode continuar a manter o controle dos dados primários na era da IA, incluindo como:

- Rastrear o engajamento e o comportamento do usuário dentro do seu aplicativo ChatGPT (como identificar quais perguntas ou recursos de chat seus clientes usam)
- Segmentar e redirecionar campanhas Braze com base em padrões de interação com IA (como enviar e-mails para usuários que usaram o chat mais de três vezes por semana)

### Principais benefícios

- **Possua a jornada do seu cliente:** Enquanto os usuários interagem com sua marca através do ChatGPT, você mantém visibilidade sobre seu comportamento, preferências e padrões de engajamento. Esses dados fluem diretamente para os perfis de usuários do Braze, não apenas para a análise da plataforma de IA.
- **Redirecionamento entre plataformas:** Rastreie interações do usuário em seu aplicativo ChatGPT e redirecione-os através de seus canais próprios (e-mail, SMS, notificações por push, envio de mensagens no aplicativo) com campanhas personalizadas com base em seus padrões de uso de IA.
- **Retorne conteúdo promocional 1:1 para conversas do ChatGPT:** Entregue mensagens [in-app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages) do Braze, [Cartões de Conteúdo]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards), e mais diretamente dentro da sua experiência ChatGPT usando os componentes de UI conversacional personalizados que sua equipe construiu para seu aplicativo.
- **Atribuição de receita:** Rastreie compras e conversões que se originam de interações no aplicativo ChatGPT.

<!-- ### Practical Use Cases

- **E-commerce**: Track product inquiries, cart additions, and purchases made through ChatGPT conversations
- **SaaS**: Monitor feature requests, support interactions, and trial-to-paid conversions
- **Content/Media**: Understand what topics users are most interested in and create targeted content campaigns
- **Financial Services**: Track financial advice requests and product recommendations for compliance and optimization
- **Travel**: Monitor destination research, booking inquiries, and trip planning interactions

By integrating Braze with your ChatGPT App, you ensure that every AI interaction becomes a data point in your customer engagement strategy, not just a black box interaction on someone else's platform. -->

## Pré-requisitos

Antes de integrar o Braze com seu app ChatGPT, você deve ter o seguinte:

- Um novo app web e chave de API no seu espaço de trabalho Braze
- Um [app ChatGPT](https://openai.com/index/introducing-apps-in-chatgpt/) criado na plataforma OpenAI ([app de exemplo OpenAI](https://github.com/openai/openai-apps-sdk-examples))

{% multi_lang_include developer_guide/chatgpt_apps/sdk_integration.md %}

