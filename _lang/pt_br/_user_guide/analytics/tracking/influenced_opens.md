---
nav_title: Aberturas por influência
article_title: Aberturas por influência
page_order: 7
page_type: reference
description: "Este artigo de referência explica as aberturas por influência e como você pode rastreá-las para fornecer um nível mais rico de detalhes em suas campanhas push."
channel: push

---

# Aberturas por influência

> Quando um usuário seleciona uma notificação por push e é enviado para o seu app, o Braze registra isso como uma abertura direta. Quando os usuários não selecionam a notificação, mas ainda podem ser influenciados pela notificação por push, o Braze registra como uma abertura influenciada. Isso fornece um nível mais rico de detalhes sobre o efeito de suas campanhas push.

## Como funciona?

Em sua base, as aberturas por influência medem o número de usuários que abrem o app depois de receber uma notificação sem selecioná-la. Como não há nenhuma ação direta que vincule a notificação à abertura do aplicativo, uma abertura influenciada é registrada se o usuário abrir o aplicativo menos de trinta minutos após receber a notificação por push ou menos da metade do tempo médio desde a última sessão do usuário.

Por exemplo, digamos que você envie uma notificação por push para os usuários do seu app. Se um usuário que normalmente abre o aplicativo 30 vezes por dia abrir seu aplicativo seis horas depois de receber o push, o push recebe pouco ou nenhum crédito por aberturas por influência. No entanto, se um usuário que normalmente usa o aplicativo uma vez por mês abrir o aplicativo seis horas depois de receber o push, a abertura terá uma chance muito maior de ser contada como uma abertura por influência. 

Isso difere da definição de aberturas de aplicativos como um evento de conversão para uma campanha push. Para conversões, todas as aberturas dentro da janela de conversão serão atribuídas à campanha. As aberturas por influência definem uma janela de tempo e crédito de atribuição com base no comportamento de um usuário individual.

## A visualização das aberturas por influência de uma campanha

As aberturas por influência são adicionadas às aberturas diretas de uma campanha para obter um número total de aberturas. Isso é exibido em uma página de **análise de dados** da **campanha** push. O total de aberturas e as aberturas diretas são mostrados nas seções Desempenho de mensagens e **Desempenho histórico**. As aberturas por influência são a diferença entre as duas medidas.

![As aberturas por influência das estatísticas na página Detalhes da campanha para uma campanha]({% image_buster /assets/img_archive/Influenced_Opens2.png %})

Para saber mais sobre o rastreamento de aberturas, confira a seção de rastreamento de conversões de nossas [práticas recomendadas para push]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/).

