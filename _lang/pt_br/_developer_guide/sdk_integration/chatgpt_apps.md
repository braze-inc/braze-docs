---
page_order: 2.1
nav_title: ChatGPT apps
article_title: Integre o Braze com os aplicativos ChatGPT
description: "Aprenda a integrar o Braze com os aplicativos ChatGPT para ativar a análise de dados e o registro de eventos em aplicativos com tecnologia de IA."
platform:
  - ChatGPT Apps
---

# Integre o Braze com os aplicativos ChatGPT

> Este guia aborda como integrar o Braze com os aplicativos ChatGPT para ativar a análise de dados e o registro de eventos em aplicativos com tecnologia de IA.

![Um cartão de conteúdo integrado ao app ChatGPT.]({% image_buster /assets/img/chatgpt_app_integration.png %}){: style="float:right;max-width:30%;border:none;" }

## Visão geral

Os aplicativos ChatGPT oferecem uma plataforma poderosa para a criação de aplicativos conversacionais de IA. Ao integrar o Braze ao seu aplicativo ChatGPT, você pode continuar a manter o controle dos dados primários na era da IA, incluindo como:

- Acompanhe o engajamento e o comportamento dos usuários em seu app ChatGPT (por exemplo, identificando quais perguntas ou recursos de bate-papo seus clientes utilizam).
- Segmente e redirecione as campanhas da Braze com base em padrões de interação de IA (como o envio de e-mails para usuários que utilizaram o chat mais de três vezes por semana).

### Principais benefícios

- **Seja o dono da jornada do seu cliente:** Enquanto os usuários interagem com sua marca por meio do ChatGPT, você mantém visibilidade sobre o comportamento, as preferências e os padrões de engajamento deles. Esses dados fluem diretamente para os perfis de usuário da Braze, não apenas para a análise de dados da plataforma de IA.
- **Redirecionamento entre plataformas:** Acompanhe as interações dos usuários em seu aplicativo ChatGPT e redirecione-os em seus canais proprietários (e-mail, SMS, notificações por push, mensagens no app) com campanhas personalizadas com base em seus padrões de uso de IA.
- **Retorne conteúdo promocional 1:1 para conversas no ChatGPT:** Entregue [mensagens no app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages) Braze, [cartões de conteúdo]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards) e muito mais diretamente em sua experiência ChatGPT usando os componentes personalizados da interface de usuário conversacional que sua equipe criou para o seu app.
- **Atribuição de receita:** Acompanhe as compras e conversões originadas das interações com o app ChatGPT.

<!-- ### Practical Use Cases

- **E-commerce**: Track product inquiries, cart additions, and purchases made through ChatGPT conversations
- **SaaS**: Monitor feature requests, support interactions, and trial-to-paid conversions
- **Content/Media**: Understand what topics users are most interested in and create targeted content campaigns
- **Financial Services**: Track financial advice requests and product recommendations for compliance and optimization
- **Travel**: Monitor destination research, booking inquiries, and trip planning interactions

By integrating Braze with your ChatGPT App, you ensure that every AI interaction becomes a data point in your customer engagement strategy, not just a black box interaction on someone else's platform. -->

## Pré-requisitos

Antes de integrar o Braze ao seu aplicativo ChatGPT, você deve ter o seguinte:

- Um novo app web e uma chave de API em seu espaço de trabalho Braze
- Um [app ChatGPT](https://openai.com/index/introducing-apps-in-chatgpt/) criado na plataforma OpenAI ([app de amostra OpenAI](https://github.com/openai/openai-apps-sdk-examples))

{% multi_lang_include developer_guide/chatgpt_apps/sdk_integration.md %}

