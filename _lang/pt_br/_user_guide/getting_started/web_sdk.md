---
nav_title: Visão geral do SDK
article_title: Visão geral do SDK 
page_order: 9
page_type: reference
description: "Este artigo de referência aborda os conceitos básicos do Braze SDK."
---

# Visão geral do SDK 

> O Braze SDK facilita a coleta de dados de sessão, a identificação de usuários e o registro de compras e eventos personalizados por meio do seu site ou aplicativo. Você também pode usar o SDK para interagir com seus usuários, enviando mensagens no aplicativo e notificações push diretamente do painel do Braze.

Em resumo, o Braze SDK:
* Coleta e sincroniza os dados do usuário em um perfil de usuário consolidado
* Captura dados de engajamento de marketing e dados personalizados específicos de sua empresa
* Potencializa as notificações push, as mensagens no aplicativo e os canais de mensagens do Content Card

## O que é um SDK?
Um kit de desenvolvimento de software (SDK) é um conjunto de ferramentas pré-fabricadas - apenas pequenos blocos de código - que podem ser adicionadas aos aplicativos digitais para oferecer suporte a novos recursos. O Braze SDK é usado para enviar e obter informações de e para seu aplicativo ou site. Ele foi projetado para fornecer a funcionalidade essencial desde o início: criação de perfis de usuário, registro de eventos personalizados, acionamento de notificações por push, etc. 

Como essa funcionalidade vem por padrão do Braze, seus desenvolvedores ficam livres para se concentrar em seu negócio principal. Sem um SDK, cada cliente Braze teria que criar toda a infraestrutura e as ferramentas para processamento de dados, lógica de segmentação, opções de entrega, tratamento de usuários anônimos, análise de campanhas e muito mais, completamente do zero. Isso levaria muito mais tempo e seria muito mais trabalhoso do que a hora ou mais que leva para incorporar nosso SDK.

## Implementação

Para incorporar um SDK em seu aplicativo ou site, alguém precisará adicionar o código do SDK à base de código geral mais ampla que alimenta o aplicativo. Isso significa que a sua equipe de engenharia estará envolvida, essencialmente unindo nossos aplicativos para que as informações e ações fluam entre eles. Mas, embora seus desenvolvedores estejam envolvidos, o SDK foi projetado para ser leve e de fácil integração. 

Para economizar seu tempo e garantir uma integração tranquila, recomendamos que você e sua equipe de engenharia configurem seus eventos personalizados, atributos personalizados e o SDK ao mesmo tempo. Saiba mais sobre as etapas que suas equipes de marketing e engenharia precisarão pensar juntas lendo nosso [artigo sobre implementação]({{site.baseurl}}/user_guide/getting_started/integration/). 

## Agregação de dados

O Braze SDK captura automaticamente imensas quantidades de dados no nível do usuário, facilitando a visualização das principais métricas do seu aplicativo e da sua base de usuários. Você agrupará aplicativos semelhantes em um único espaço de trabalho no seu painel. Por exemplo, você agrupará as versões para iOS e Android do seu aplicativo no mesmo espaço de trabalho, o que lhe permitirá ver os dados coletados dos usuários em ambas as plataformas. Isso lhe dá uma visão mais completa dos seus usuários nos canais da Web e móveis. Consulte o artigo na [página inicial]({{site.baseurl}}/user_guide/analytics/dashboard/home_dashboard/) para obter mais informações.

## Mensagens no aplicativo

O SDK facilita a composição e o envio de mensagens no aplicativo para interagir diretamente com os usuários. Você pode optar por enviar mensagens em slideup, modal ou tela cheia com base na sua estratégia de campanha. Para obter mais informações sobre como compor uma mensagem in-app, consulte nossa página sobre como [criar uma mensagem in-app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/create/).

\![Push exibido em um navegador da Web]({% image_buster /assets/img_archive/web_push_macbook.png %}){: style="float:right;max-width:45%;margin-left:20px;border:0;"}

## Notificações push

As notificações push são outra ótima opção para interagir com os usuários e são especialmente úteis para lidar com chamadas à ação sensíveis ao tempo. As notificações push para celular são exibidas nos dispositivos dos usuários e as notificações push para web são exibidas mesmo quando o site não está aberto. Para obter informações específicas sobre o uso de notificações por push, consulte nosso [artigo sobre notificações por push]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/).

Os usuários do seu site ou aplicativo precisam optar por receber notificações por push. Para obter mais detalhes, consulte a [preparação por pressão]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/). 

## Regras de segmentação e entrega

Por padrão, uma campanha contendo mensagens in-app será enviada para todas as versões do aplicativo nesse espaço de trabalho. Por exemplo, a mensagem será enviada para usuários da Web e de dispositivos móveis. Para enviar uma mensagem in-app exclusivamente para a Web ou para dispositivos móveis, você precisará segmentar sua campanha de acordo, o que é suportado por padrão pelo SDK do Braze. 

Você pode criar um segmento de seus usuários da Web definindo **aplicativos e sites direcionados** a **usuários de aplicativos específicos** e, em seguida, selecionar apenas o seu site para os **aplicativos específicos**.

\![Página de detalhes do segmento com o aplicativo da Web em foco]({% image_buster /assets/img_archive/web-users-segment.png %}){:style="max-width:60%"}

Isso permitirá que você direcione os usuários com base no comportamento deles de forma inteligente. Se você quisesse segmentar usuários da Web para incentivá-los a baixar seu aplicativo móvel, criaria esse segmento como seu público-alvo. Se você quisesse enviar uma campanha de mensagens que incluísse uma mensagem móvel no aplicativo, mas não uma mensagem da Web, desmarcaria o ícone do site no seu segmento.

## Plataformas suportadas

O Braze fornece SDKs para várias plataformas, como Web, Android e Swift. Para obter a lista completa, consulte o [Guia do Desenvolvedor do Braze]({{site.baseurl}}/developer_guide/home).
