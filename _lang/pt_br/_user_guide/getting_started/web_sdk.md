---
nav_title: Visão geral do SDK
article_title: Visão geral do SDK 
page_order: 9
page_type: reference
description: "Este artigo de referência aborda os conceitos básicos do SDK da Braze."
---

# Visão geral do SDK 

> O SDK do Braze coleta dados de sessão, identifica usuários e registra compras e eventos personalizados através do seu site ou app. Você também pode usar o SDK para engajar usuários enviando mensagens no app e notificações por push diretamente do dashboard do Braze.

Em resumo, o SDK da Braze:
* Coleta e sincroniza dados de usuários em um perfil de usuário consolidado
* Captura dados de engajamento de marketing e dados personalizados específicos de sua empresa
* Potencializa as notificações por push, as mensagens no app e os canais de envio de mensagens do cartão de conteúdo

## O que é um SDK?
Um kit de desenvolvimento de software (SDK) é um conjunto de ferramentas pré-fabricadas - apenas pequenos blocos de código - que podem ser adicionadas aos aplicativos digitais para oferecer suporte a novos recursos. O SDK da Braze é usado para enviar e obter informações de e para seu app ou site. Ele foi projetado para oferecer funcionalidades essenciais desde o início: criação de perfis de usuário, registro de usuários de eventos personalizados, disparo de notificações por push, etc. 

Como essa funcionalidade vem por padrão do Braze, seus desenvolvedores ficam livres para se concentrar em seu negócio principal. Sem um SDK, cada cliente Braze teria que criar toda a infraestrutura e as ferramentas para processamento de dados, lógica de segmentação, opções de entrega, tratamento de usuários anônimos, análise de campanhas e muito mais completamente do zero. Isso levaria muito mais tempo e seria muito mais trabalhoso do que a hora ou mais que leva para incorporar nosso SDK.

## Implementação

Para incorporar um SDK em seu app ou site, alguém precisará adicionar o código do SDK à base de código geral maior que alimenta o aplicativo. Isso significa que a sua equipe de engenharia estará envolvida, essencialmente unindo nossos apps para que as informações e ações fluam entre eles. Mas, embora seus desenvolvedores estejam envolvidos, o SDK foi projetado para ser leve e de fácil integração. 

Para economizar seu tempo e garantir uma integração tranquila, recomendamos que você e sua equipe de engenharia configurem seus eventos personalizados, atributos personalizados e o SDK ao mesmo tempo. Saiba mais sobre as etapas que as equipes de marketing e engenharia precisarão pensar juntas, lendo nosso [artigo sobre implementação]({{site.baseurl}}/user_guide/getting_started/integration/). 

## Agregação de dados

O SDK do Braze captura automaticamente dados em nível de usuário, fornecendo métricas chave para seu app e base de usuários. Agrupe aplicativos semelhantes em um único espaço de trabalho (por exemplo, versões iOS e Android juntas) para visualizar os dados coletados em várias plataformas e construir uma imagem completa da atividade do usuário. Consulte o artigo na [página inicial]({{site.baseurl}}/user_guide/analytics/dashboard/home_dashboard/) para obter mais informações.

## Envio de mensagens no app

Use o SDK para compor e enviar mensagens no app diretamente. Você pode escolher mensagens slideup, modais ou em tela cheia com base na sua estratégia de campanha. Para detalhes de composição, consulte [Criar uma mensagem no app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/create/).

![Push exibido em um navegador da Web]({% image_buster /assets/img_archive/web_push_macbook.png %}){: style="float:right;max-width:45%;margin-left:20px;border:0;"}

## Notificações por push

As notificações por push são outra ótima opção para engajamento com seus usuários e são especialmente úteis para lidar com chamadas à ação sensíveis ao tempo. As notificações por push para mobile aparecem nos dispositivos dos usuários, e as notificações por web push aparecem mesmo quando o site não está aberto. Para obter informações específicas sobre o uso de notificações por push, consulte nosso [artigo sobre notificações por push]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/).

Os usuários do seu site ou app precisam fazer a aceitação para receber notificações por push. Veja [preparação de push]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/) para mais detalhes. 

## Regras de segmentação e entrega

Por padrão, uma campanha contendo mensagens no app será enviada para todas as versões do app nesse espaço de trabalho. Por exemplo, a mensagem será enviada tanto para usuários da Internet quanto para usuários móveis. Para enviar uma mensagem no app exclusivamente para a Web ou para dispositivos móveis, você precisará segmentar sua campanha de acordo, o que é suportado por padrão por meio d o SDK da Braze. 

Você pode criar um segmento de seus usuários da web definindo **Aplicativos e sites direcionados** para **Usuários de aplicativos específicos**, e então selecionar apenas seu site para os **Aplicativos Específicos**.

![Página de Detalhes do Segmento com o app web em foco]({% image_buster /assets/img_archive/web-users-segment.png %}){:style="max-width:60%"}

Isso permitirá direcionar os usuários com base em seu comportamento de forma inteligente. Se quisesse direcionar os usuários da Web para incentivá-los a baixar seu app móvel, você criaria esse segmento como seu público-alvo. Se você quisesse enviar uma campanha de mensagens que incluísse uma mensagem no app para celular, mas não uma mensagem na Internet, desmarcaria o ícone do seu site no segmento de mensagens.

## Plataformas suportadas

O Braze fornece SDKs para várias plataformas, como Web, Android e Swift. Para a lista completa, consulte o [Guia do Desenvolvedor do Braze]({{site.baseurl}}/developer_guide/home).
