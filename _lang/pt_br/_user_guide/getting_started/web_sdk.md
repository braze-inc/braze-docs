---
nav_title: Visão geral do SDK 
article_title: Visão geral do SDK 
page_order: 9
page_type: reference
description: "Este artigo de referência aborda os conceitos básicos do SDK da Braze."
---

# Visão geral do SDK 

> O Braze SDK facilita a coleta de dados de sessão, a identificação de usuários e o registro de compras e eventos personalizados por meio do seu site ou app. Também é possível usar o SDK para interagir com seus usuários, enviando mensagens no app e notificações por push diretamente do dashboard da Braze.

Em resumo, o SDK da Braze:
* Coleta e sincroniza dados de usuários em um perfil de usuário consolidado
* Captura dados de engajamento de marketing e dados personalizados específicos de sua empresa
* Potencializa as notificações por push, as mensagens no app e os canais de envio de mensagens do cartão de conteúdo

## O que é um SDK?
Um kit de desenvolvimento de software (SDK) é um conjunto de ferramentas pré-fabricadas - apenas pequenos blocos de código - que podem ser adicionadas aos aplicativos digitais para oferecer suporte a novos recursos. O SDK da Braze é usado para enviar e obter informações de e para seu app ou site. Ele foi projetado para oferecer funcionalidades essenciais desde o início: criação de perfis de usuário, registro de usuários de eventos personalizados, disparo de notificações por push, etc. 

Como essa funcionalidade vem por padrão do Braze, seus desenvolvedores ficam livres para se concentrar em seu negócio principal. Sem um SDK, cada cliente Braze teria que criar toda a infraestrutura e as ferramentas para processamento de dados, lógica de segmentação, opções de entrega, tratamento de usuários anônimos, análise de campanhas e muito mais completamente do zero. Isso levaria muito mais tempo e seria muito mais trabalhoso do que a hora ou mais que leva para incorporar nosso SDK.

## Implementação

Para incorporar um SDK em seu app ou site, alguém precisará adicionar o código do SDK à base de código geral maior que alimenta o aplicativo. Isso significa que a sua equipe de engenharia estará envolvida, essencialmente unindo nossos apps para que as informações e ações fluam entre eles. Mas, embora seus desenvolvedores estejam envolvidos, o SDK foi projetado para ser leve e de fácil integração. 

Para economizar seu tempo e garantir uma integração tranquila, recomendamos que você e sua equipe de engenharia configurem seus eventos personalizados, atributos personalizados e o SDK ao mesmo tempo. Saiba mais sobre as etapas que as equipes de marketing e engenharia precisarão pensar juntas, lendo nosso [artigo sobre implementação][4]. 

## Agregação de dados

O Braze SDK captura automaticamente imensas quantidades de dados no nível do usuário, facilitando a visualização das principais métricas do seu app e da sua base de usuários. Você agrupará aplicativos semelhantes em um único espaço de trabalho em seu dashboard. Por exemplo, você agrupará as versões para iOS e Android do seu app no mesmo espaço de trabalho, o que lhe permitirá ver os dados coletados de usuários em ambas as plataformas. Isso lhe dá uma visão mais completa dos seus usuários nos canais da Web e móveis. Consulte o artigo na [página inicial][3] para obter mais informações.

## Envio de mensagens no app

O SDK facilita a criação e o envio de mensagens no app para o engajamento direto com os usuários. É possível optar pelo envio de mensagens slideup, modal ou em tela cheia com base na sua estratégia de campanha. Para saber mais, consulte nossa página sobre [criar uma mensagem no app][8].

![Push exibido em um navegador da Web][11]{: style="float:right;max-width:45%;margin-left:20px;border:0;"}

## Notificações por push

As notificações por push são outra ótima opção para engajamento com seus usuários e são especialmente úteis para lidar com chamadas à ação sensíveis ao tempo. As notificações por push para mobile aparecem nos dispositivos dos usuários, e as notificações por web push aparecem mesmo quando o site não está aberto. Para obter informações específicas sobre o uso de notificações por push, consulte nosso [artigo sobre notificações por push][5].

Os usuários do seu site ou app precisam fazer a aceitação para receber notificações por push. Consulte [push priming][13] para obter mais detalhes. 

## Regras de segmentação e entrega

Por padrão, uma campanha contendo mensagens no app será enviada para todas as versões do app nesse espaço de trabalho. Por exemplo, a mensagem será enviada tanto para usuários da Internet quanto para usuários móveis. Para enviar uma mensagem no app exclusivamente para a Web ou para dispositivos móveis, você precisará segmentar sua campanha de acordo, o que é suportado por padrão por meio d o SDK da Braze. 

É possível criar um segmento dos seus usuários da Web selecionando apenas o ícone do aplicativo do seu site na seção **Apps usados** de um segmento.

![Página Detalhes do segmento com o app da Web selecionado][10]

Isso permitirá direcionar os usuários com base em seu comportamento de forma inteligente. Se quisesse direcionar os usuários da Web para incentivá-los a baixar seu app móvel, você criaria esse segmento como seu público-alvo. Se você quisesse enviar uma campanha de mensagens que incluísse uma mensagem no app para celular, mas não uma mensagem na Internet, desmarcaria o ícone do seu site no segmento de mensagens.

## Quais são as integrações do Braze?
A Braze oferece uma versão de nosso SDK para muitas plataformas (Web, Android, iOS, Flutter, React Native e outras), mas todas elas funcionam essencialmente da mesma maneira. Portanto, se você vir uma referência a, digamos, "Web SDK", essa é apenas a versão do SDK da Braze destinada ao seu site.

<style>
table th:nth-child(1) {
width: 33%;
}
table th:nth-child(2) {
width: 33%;
}
table th:nth-child(3) {
width: 33%;
}
table td {
word-break: break-word;
text-align: center;
}
</style>
Integrações em destaque   |    |   
----------- |---------------- | --------------------
[![Android]({% image_buster /assets/img/braze_icons/android.svg %})]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/){: style="max-width:40%;margin-right:15px;border:0" class="noimgborder"}  [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/) |[![iOS]({% image_buster /assets/img/braze_icons/apple.svg %})]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/overview/){: style="max-width:20%;margin-right:15px;border:0" class="noimgborder"} [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/overview/) |[![Web]({% image_buster /assets/img/braze_icons/globe-02.png %})]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/){: style="max-width:25%;margin-right:15px;border:0" class="noimgborder"} [Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/)  

Todas as integrações   |    |   
----------- |---------------- | --------------------
[![Cordova Android]({% image_buster /assets/img/cordova.png %})]({{site.baseurl}}/developer_guide/platform_integration_guides/cordova/initial_sdk_setup/android/){: style="max-width:40%;margin-right:15px;border:0" class="noimgborder"}  [Cordova Android]({{site.baseurl}}/developer_guide/platform_integration_guides/cordova/initial_sdk_setup/android/) | [![Cordova iOS]({% image_buster /assets/img/cordova.png %})]({{site.baseurl}}/developer_guide/platform_integration_guides/cordova/initial_sdk_setup/ios/){: style="max-width:40%;margin-right:15px;border:0" class="noimgborder"}  [Cordova iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/cordova/initial_sdk_setup/ios/) | [![Flutter Android e iOS]({% image_buster /assets/img/flutter_icon.png %})]({{site.baseurl}}/developer_guide/platform_integration_guides/flutter/flutter_sdk_integration/){: style="max-width:20%;margin-top:5%;border:0" class="noimgborder"}  [Flutter para Android e iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/flutter/flutter_sdk_integration/)
[![React Native]({% image_buster /assets/img/reactnative_icon.png %})]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/react_sdk_setup/){: style="max-width:40%;margin-right:15px;border:0" class="noimgborder"}  [React Native]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/react_sdk_setup/) | [![tvOS]({% image_buster /assets/img/tvos_icon.png %})]({{site.baseurl}}/developer_guide/platform_integration_guides/tvos/initial_sdk_setup/){: style="max-width:40%;margin-top:5%;border:0" class="noimgborder"}  [tvOS]({{site.baseurl}}/developer_guide/platform_integration_guides/tvos/initial_sdk_setup/) | [![MacOS]({% image_buster /assets/img/macOS_icon.png %})]({{site.baseurl}}/developer_guide/platform_integration_guides/macOS/initial_sdk_setup/){: style="max-width:40%;margin-top:15%;border:0" class="noimgborder"}  [MacOS]({{site.baseurl}}/developer_guide/platform_integration_guides/macOS/initial_sdk_setup/)
[![Unity Android]({% image_buster /assets/img/unity.png %})]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/sdk_integration/android/){: style="max-width:40%;margin-right:15px;border:0" class="noimgborder"}  [Unity Android]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/sdk_integration/android/) | [![Unity iOS]({% image_buster /assets/img/unity.png %})]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/sdk_integration/ios/){: style="max-width:40%;margin-right:15px;border:0" class="noimgborder"}  [Unity iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/sdk_integration/ios/) | [![Xamarin]({% image_buster /assets/img/xamarin.png %})]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/initial_sdk_setup/){: style="max-width:35%;margin-top:5%;border:0" class="noimgborder"}  [Xamarin]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/initial_sdk_setup/) 
[![Roku]({% image_buster /assets/img/roku.png %})]({{site.baseurl}}/developer_guide/platform_integration_guides/roku/initial_sdk_setup/){: style="max-width:40%;margin-top:5%;border:0" class="noimgborder"}  [Roku]({{site.baseurl}}/developer_guide/platform_integration_guides/roku/initial_sdk_setup/) | [![Unreal Engine]({% image_buster /assets/img/unreal.png %})]({{site.baseurl}}/developer_guide/platform_integration_guides/unreal_engine/initial_sdk_setup/){: style="max-width:30%;margin-right:15px;border:0" class="noimgborder"}  [Unreal Engine]({{site.baseurl}}/developer_guide/platform_integration_guides/unreal_engine/initial_sdk_setup/)

[3]: {{site.baseurl}}/user_guide/data_and_analytics/your_analytics_dashboards/understanding_your_app_usage_data/
[4]: {{site.baseurl}}/user_guide/onboarding_with_braze/integration/#the-technical-side-of-the-integration-process
[5]: {{site.baseurl}}/user_guide/message_building_by_channel/push/about/
[7]: {% image_buster /assets/img_archive/app_group_list.png %}
[8]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/
[10]: {% image_buster /assets/img_archive/web-users-segment.png %}
[11]: {% image_buster /assets/img_archive/web_push_macbook.png %}
[13]: {{site.baseurl}}/user_guide/message_building_by_channel/push/push_primer_messages/
