---
nav_title: Políticas de pôr do sol
article_title: Políticas do Sunset para e-mail
page_order: 8
page_type: reference
description: "Este artigo aborda as práticas recomendadas relacionadas às políticas de descontinuidade e à compreensão das situações em que é melhor descontinuar as mensagens para usuários não engajados."
channel: email

---

# Políticas de pôr do sol

> Embora você se sinta tentado a enviar campanhas para o maior número possível de usuários, há situações em que é realmente vantajoso interromper o envio de mensagens para usuários não engajados. 

Para e-mails, seu IP de envio tem uma pontuação de reputação que leva em conta o engajamento, relatórios de spam, listas de bloqueio e muito mais. Você pode usar ferramentas como o [Sender Score](https://www.senderscore.org/) ou [o Smart Network Data Service do Outlook](https://postmaster.live.com/snds/) para monitorar sua pontuação de reputação. Se sua pontuação de reputação for consistentemente baixa, os filtros do ISP e da caixa de correio poderão classificar automaticamente seus e-mails em uma pasta de spam ou de baixa prioridade para todos os destinatários, mesmo os engajados. A criação de uma política de descontinuidade ajuda a enviar seus e-mails somente para destinatários ativos. 

Os filtros de segmentação ajudam a evitar que suas mensagens apareçam como spam, permitindo que você implemente facilmente políticas de bloqueio para e-mails, notificações push e no aplicativo. Aqui estão alguns aspectos a serem considerados quando você criar uma política de descontinuidade:

- O que conta como um usuário "não engajado"? 
- O engajamento é definido por cliques, compras, uso do aplicativo ou uma combinação desses comportamentos? 
- Quanto tempo precisa durar o lapso de engajamento para que você pare de enviar mensagens?
- Você entregará alguma campanha especial aos usuários antes de excluí-los dos seus segmentos?
- A quais canais de mensagens a sua política de suspensão se aplicará? 

Por exemplo, se você tiver usuários que optam pela [MPP (Mail Privacy Protection) da Apple]({{site.baseurl}}/user_guide/message_building_by_channel/email/apple_mail/mpp/), considere como isso pode afetar suas campanhas de e-mail e as métricas de capacidade de entrega e determine a melhor forma de estruturar sua política de sunset.

Para incorporar políticas de sunset em suas campanhas, crie um [segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#creating-a-segment) que exclua automaticamente os usuários que marcaram seus e-mails como spam ou que não interagiram com suas mensagens por um determinado período de tempo.  

Para configurar esses segmentos, escolha os filtros `Has Marked You As Spam` e `Last Engaged With Message` localizados na seção **Retargeting** no menu suspenso de filtros. 

Ao aplicar o filtro `Last Engaged With Message`, especifique o tipo de mensagem (push, e-mail ou notificação in-app) com a qual o usuário interagiu ou não, bem como o número de dias desde a última interação do usuário. Depois de criar um segmento, opte por segmentar esse segmento com qualquer [canal de mensagens]({{site.baseurl}}/user_guide/message_building_by_channel/).

Página Segment Details (Detalhes do segmento) com o filtro "Last Engaged with Message" (Último envolvimento com mensagem) selecionado.]({% image_buster /assets/img_archive/email_sunset_policies_new.png %})

Embora o Braze pare automaticamente de enviar e-mails para usuários que marcaram você como spam, o filtro `Has Marked You As Spam` permite que você também envie a esses usuários mensagens push direcionadas e notificações no aplicativo. Esse filtro é útil para [campanhas de redirecionamento]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/retargeting_campaigns/#retargeting-campaigns). Por exemplo, você pode enviar aos usuários não engajados mensagens que os lembrem dos recursos e das ofertas que eles estão perdendo quando não abrem seus e-mails.

As políticas Sunset podem ser especialmente úteis em campanhas de e-mail direcionadas a usuários que estão perdendo a validade. Embora essas campanhas se concentrem em segmentos que não interagiram com seu aplicativo por um período de tempo, elas podem colocar em risco a capacidade de entrega de seus e-mails se incluírem repetidamente destinatários não engajados. As políticas do Sunset permitem que você direcione os usuários inativos sem que eles caiam na pasta de spam.

