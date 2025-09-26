---
nav_title: Campanhas de redirecionamento
article_title: Campanhas de redirecionamento
page_order: 2
page_type: reference
description: "Este artigo de referência aborda como e por que você deve considerar campanhas de redirecionamento com base nas mensagens que seus usuários recebem."
tool:
  - Campaigns
  
---

# campanhas de redirecionamento

> Ao utilizar campanhas de redirecionamento baseadas nas ações anteriores do usuário, como se ele abriu ou não um e-mail, você pode ajudar a reclassificar seus usuários, abrindo a porta para uma abordagem eficaz de marketing baseado em dados.

Braze fornece suporte para redirecionamento de usuários com base nas mensagens que eles receberam. É possível redirecionar os usuários com base nas interações deles com suas campanhas e Canvas. 

Cada um desses filtros de redirecionamento oferece várias opções depois que você os adiciona. Para mais informações sobre direcionamento de usuários, confira nosso [curso do Braze Learning](https://learning.braze.com/campaign-setup-delivery-targeting-conversions) sobre configuração de campanhas!

![Seção Segment Details (Detalhes do segmento) com o menu suspenso para os filtros disponíveis.]({% image_buster /assets/img_archive/retarget.png %}){: style="max-width:80%;"}

## Filtros de redirecionamento

É possível usar os filtros de redirecionamento nessa seção para seus usuários em suas campanhas e Canvas.

### Campanha clicada/aberta

Use este filtro para encontrar usuários que têm ou não têm:

- Clicou em um e-mail
- Clicou em uma mensagem no app
- Abriu diretamente uma notificação por push
- Abriu um e-mail
- Visualizou uma mensagem no app

![]({% image_buster /assets/img_archive/clickedopened.png %})

Isso pode ser especificado ainda mais selecionando qual campanha você deseja redirecionar.

### Clicou ou abriu a Campanha ou Canva com tag

Use este filtro para encontrar usuários que interagiram ou não com campanhas ou canvas com uma determinada tag:

- Clicou em um e-mail
- Clicou em uma mensagem no app
- Abriu diretamente uma notificação por push
- Abriu um e-mail
- Visualizou uma mensagem no app

![]({% image_buster /assets/img_archive/retarget_tag_filter.png %})

### Convertidos de uma campanha 

Use este filtro para encontrar usuários que se converteram ou não (com base na conversão primária) em sua campanha alvo. 

Para campanhas recorrentes, este filtro se refere a se os usuários converteram na mensagem mais recente da campanha.

![]({% image_buster /assets/img_archive/converted_from_campaign.png %})

### Convertidos de um canva 

Use este filtro para encontrar usuários que se converteram ou não (com base na conversão primária) no seu canva alvo.

Para Canvases recorrentes, este filtro se refere a se os usuários já converteram alguma vez que passaram pelo Canvas.

![]({% image_buster /assets/img_archive/converted_from_canvas.png %})

### No grupo de controle da campanha 

Use este filtro para encontrar usuários que estão ou não no grupo de controle da sua campanha alvo.

![]({% image_buster /assets/img_archive/campaign_control_group.png %})

### No grupo de controle do canva 

Use este filtro para encontrar usuários que estão ou não no grupo de controle do seu canva, que pode ser selecionado no menu suspenso.

![]({% image_buster /assets/img_archive/canvas_control_group.png %})

### Última mensagem recebida de campanha específica 

Use este filtro para encontrar usuários que receberam uma campanha específica antes ou depois de uma data ou número de dias especificado. Esse filtro não considera quando os usuários receberam outras campanhas.

![]({% image_buster /assets/img_archive/last_received_specific_campaign.png %})

### Última mensagem recebida de campanha específica ou canva com tag 

Use este filtro para encontrar usuários que receberam pela última vez uma campanha ou canva com uma tag específica antes ou depois de uma data ou número de dias especificado. Esse filtro não considera quando os usuários receberam outras campanhas ou Canvas.

![]({% image_buster /assets/img_archive/last_received_campaign_with_tag.png %})

### Mensagem recebida da campanha 

Use este filtro para encontrar usuários que receberam ou não sua campanha alvo.

![]({% image_buster /assets/img_archive/receivedcamp.png %})

### Mensagem recebida da campanha ou canva com tag 

Use este filtro para encontrar usuários que receberam ou não uma campanha ou canva que tenha sua tag alvo.

![]({% image_buster /assets/img_archive/received_campaign_with_tag.png %})

## Vantagens com campanhas de redirecionamento

Redirecionamento é particularmente eficaz quando o segmento original também incluía uma ação específica que você deseja que os usuários realizem. Por exemplo, digamos que você tenha um cartão direcionado a usuários que nunca fizeram uma compra. O cartão anuncia uma promoção para uma compra com desconto no app. O segmento inicial se parece com o seguinte:

- Dinheiro gasto no app é exatamente 0
- Último app usado há menos de 14 dias

O número total de usuários no segmento é 100.000 e você sabe, pelas estatísticas do cartão de conteúdo, que 60.000 usuários únicos visualizaram o cartão e 20.000 usuários únicos clicaram no cartão. Através do segmentador, podemos ver quantos desses usuários que clicaram no cartão realmente fizeram uma compra:

- Dinheiro gasto no app é mais que 0
- Cartão clicado é Nome do Cartão

Depois de examinar essas estatísticas, podemos fazer um segmento de usuários que clicaram no cartão, mas não fizeram uma compra:

- Dinheiro gasto no app é exatamente 0
- Cartão clicado é Nome do Cartão

Podemos redirecionar este segmento com envio de mensagens adicionais sobre a promoção ou outra compra in-app. O redirecionamento pode ser feito com uma campanha de mensagens. Uma abordagem multicanal permite alcançar os usuários onde eles são mais propensos a responder, aumentando assim a eficácia de suas campanhas.

