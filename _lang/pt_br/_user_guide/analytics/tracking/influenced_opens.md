---
nav_title: Aberturas influenciadas
article_title: Aberturas influenciadas
page_order: 7
page_type: reference
description: "Este artigo de referência explica as aberturas influenciadas e como você pode rastreá-las para fornecer um nível mais rico de detalhes em suas campanhas push."
channel: push

---

# Aberturas influenciadas

> Quando um usuário seleciona uma notificação por push e é enviado para o seu aplicativo, o Braze registra isso como uma abertura direta. Quando os usuários não selecionam a notificação, mas ainda assim podem ser influenciados pela notificação por push, o Braze registra isso como uma abertura influenciada. Isso proporciona um nível mais rico de detalhes sobre o efeito de suas campanhas push.

## Como funciona

Em sua base, as aberturas influenciadas medem o número de usuários que abrem o aplicativo após receber uma notificação sem selecioná-la. Como não há nenhuma ação direta que vincule a notificação à abertura do aplicativo, uma abertura influenciada é registrada se o usuário abrir o aplicativo menos de trinta minutos depois de receber a notificação por push ou menos da metade do tempo médio desde a última sessão do usuário.

Por exemplo, digamos que você envie uma notificação push para os usuários do seu aplicativo. Se um usuário que normalmente abre o aplicativo 30 vezes por dia abre seu aplicativo seis horas após receber o push, o push recebe pouco ou nenhum crédito por influenciar a abertura. No entanto, se um usuário que normalmente usa o aplicativo uma vez por mês abrir o aplicativo seis horas depois de receber o push, a abertura terá uma chance muito maior de ser contada como uma abertura influenciada. 

Isso difere da definição de aberturas de aplicativos como um evento de conversão para uma campanha push. Para conversões, todas as aberturas dentro da janela de conversão serão atribuídas à campanha. As aberturas influenciadas definem uma janela de tempo e crédito de atribuição com base no comportamento de um usuário individual.

## A visualização das influências de uma campanha abre

As aberturas influenciadas são adicionadas às aberturas diretas de uma campanha para obter um número total de aberturas. Isso é exibido na página **Campaign Analytics** de uma campanha de envio. O total de aberturas e as aberturas diretas são mostrados nas seções Desempenho de mensagens e **Desempenho histórico**. As aberturas influenciadas são a diferença entre as duas medidas.

O Influenciado abre estatísticas na página Detalhes da campanha para uma campanha]({% image_buster /assets/img_archive/Influenced_Opens2.png %})

Para obter mais informações sobre o rastreamento de aberturas, consulte a seção de rastreamento de conversões de nossas [práticas recomendadas para push]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/).

