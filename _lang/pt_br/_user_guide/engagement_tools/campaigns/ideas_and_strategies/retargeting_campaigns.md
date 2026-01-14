---
nav_title: Campanhas de redirecionamento
article_title: Campanhas de redirecionamento
page_order: 2
page_type: reference
description: "Este artigo de referência explica como e por que você deve considerar campanhas de redirecionamento com base nas mensagens que seus usuários recebem."
tool:
  - Campaigns
  
---

# Campanhas de redirecionamento

> Ao redirecionar campanhas com base nas ações anteriores do usuário, como a abertura ou não de um e-mail, você pode ajudar a reclassificar seus usuários, abrindo a porta para uma abordagem de marketing eficaz e orientada por dados.

O Braze oferece suporte para redirecionamento de usuários com base nas mensagens que eles receberam. Você pode redirecionar os usuários com base nas interações deles com suas campanhas e Canvases. 

Cada um desses filtros de redirecionamento oferece várias opções depois de adicioná-los. Para saber mais sobre a segmentação de usuários, confira nosso [curso do Braze Learning](https://learning.braze.com/campaign-setup-delivery-targeting-conversions) sobre configuração de campanhas!

Seção Segment Details (Detalhes do segmento) com o menu suspenso para os filtros disponíveis.]({% image_buster /assets/img_archive/retarget.png %}){: style="max-width:80%;"}

## Filtros de redirecionamento

Você pode usar os filtros de redirecionamento nessa seção para seus usuários em suas campanhas e Canvases.

### Campanha clicada/aberta

Use esse filtro para encontrar usuários que têm ou não têm:

- Clicou em um e-mail
- Clicou em uma mensagem no aplicativo
- Abriu diretamente uma notificação por push
- Abriu um e-mail
- Visualizou uma mensagem no aplicativo

\![]({% image_buster /assets/img_archive/clickedopened.png %})

Isso pode ser especificado ainda mais selecionando a campanha que você deseja redirecionar.

### Clicou ou abriu a campanha ou o Canvas com a tag

Use esse filtro para encontrar usuários que tenham ou não interagido com campanhas ou Canvases com uma determinada tag:

- Clicou em um e-mail
- Clicou em uma mensagem no aplicativo
- Abriu diretamente uma notificação por push
- Abriu um e-mail
- Visualizou uma mensagem no aplicativo

\![]({% image_buster /assets/img_archive/retarget_tag_filter.png %})

### Convertido da campanha 

Use esse filtro para encontrar usuários que converteram ou não converteram (com base na conversão primária) em sua campanha de destino. 

Para campanhas recorrentes, esse filtro se refere ao fato de os usuários terem convertido na mensagem mais recente da campanha.

\![]({% image_buster /assets/img_archive/converted_from_campaign.png %})

### Convertido de tela 

Use esse filtro para encontrar usuários que converteram ou não converteram (com base na conversão primária) em seu Canvas de destino.

Para Canvases recorrentes, esse filtro se refere a se os usuários já converteram alguma vez que passaram pelo Canvas.

\![]({% image_buster /assets/img_archive/converted_from_canvas.png %})

### No grupo de controle da campanha 

Use esse filtro para encontrar usuários que estejam ou não no grupo de controle da sua campanha de destino.

\![]({% image_buster /assets/img_archive/campaign_control_group.png %})

### No grupo de controle do Canvas 

Use esse filtro para encontrar usuários que estejam ou não no grupo de controle do seu Canvas de destino, que pode ser selecionado no menu suspenso.

\![]({% image_buster /assets/img_archive/canvas_control_group.png %})

### Última mensagem recebida de uma campanha específica 

Use esse filtro para encontrar usuários que receberam uma campanha específica pela última vez antes ou depois de uma data ou número de dias especificados. Esse filtro não considera quando os usuários receberam outras campanhas.

\![]({% image_buster /assets/img_archive/last_received_specific_campaign.png %})

### Última mensagem recebida de uma campanha específica ou do Canvas com tag 

Use esse filtro para encontrar usuários que receberam pela última vez uma campanha específica ou um Canvas com uma determinada tag antes ou depois de uma data ou número de dias especificado. Esse filtro não considera quando os usuários receberam outras campanhas ou Canvases.

\![]({% image_buster /assets/img_archive/last_received_campaign_with_tag.png %})

### Mensagem recebida da campanha 

Use esse filtro para encontrar usuários que tenham ou não recebido sua campanha de destino.

\![]({% image_buster /assets/img_archive/receivedcamp.png %})

### Mensagem recebida da campanha ou do Canvas com tag 

Use esse filtro para encontrar usuários que tenham ou não recebido uma campanha ou Canvas que tenha sua tag de destino.

\![]({% image_buster /assets/img_archive/received_campaign_with_tag.png %})

## Vantagens das campanhas de retargeting

O retargeting é particularmente eficaz quando o segmento original também inclui uma ação específica que você deseja que os usuários realizem. Por exemplo, digamos que você tenha um cartão voltado para usuários que nunca fizeram uma compra. O cartão anuncia uma promoção para uma compra no aplicativo com desconto. O segmento inicial é parecido com o seguinte:

- O dinheiro gasto no aplicativo é exatamente 0
- Último aplicativo usado há menos de 14 dias

O número total de usuários no segmento é 100.000 e você sabe, pelas estatísticas do Content Card, que 60.000 usuários únicos visualizaram o cartão e 20.000 usuários únicos clicaram no cartão. Por meio do segmentador, podemos ver quantos dos usuários que clicaram no cartão realmente fizeram uma compra:

- O dinheiro gasto no aplicativo é maior que 0
- O cartão clicado é o nome do cartão

Depois de examinar essas estatísticas, podemos criar um segmento de usuários que clicaram no cartão, mas não fizeram uma compra:

- O dinheiro gasto no aplicativo é exatamente igual a 0
- O cartão clicado é o nome do cartão

Podemos redirecionar esse segmento com mensagens adicionais sobre a promoção ou outra compra no aplicativo. O retargeting pode ser feito com uma campanha de mensagens. Uma abordagem multicanal permite que você alcance os usuários onde eles têm maior probabilidade de responder, aumentando assim a eficácia de suas campanhas.

