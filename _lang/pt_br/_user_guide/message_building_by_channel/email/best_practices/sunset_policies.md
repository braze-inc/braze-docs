---
nav_title: Políticas de Pôr do Sol
article_title: Políticas de Pôr do Sol para e-mail
page_order: 8
page_type: reference
description: "Este artigo cobre as melhores práticas em torno das políticas de descontinuação e a compreensão das situações em que é melhor descontinuar mensagens para usuários desengajados."
channel: email

---

# Políticas de pôr do sol

> Embora você possa ser tentado a enviar campanhas para o maior número de usuários possível, há situações em que é realmente vantajoso parar de enviar mensagens para usuários desengajados. 

Para e-mails, seu IP de envio tem uma pontuação de reputação que leva em consideração o engajamento, o relatório de spam, a lista de bloqueio e mais. Você pode usar ferramentas como o [Sender Score](https://www.senderscore.org/) ou [o Smart Network Data Service do Outlook](https://postmaster.live.com/snds/) para monitorar sua pontuação de reputação. Se sua pontuação de reputação estiver consistentemente baixa, provedores de acesso à internet e filtros de caixa de correio podem automaticamente classificar seus e-mails em uma pasta de spam ou de baixa prioridade para todos os destinatários, até mesmo os engajados. Criar uma política de sunset ajuda a entregar seus e-mails apenas para destinatários ativos. 

Os filtros de segmentação ajudam a evitar que seu envio de mensagens pareça spam, permitindo que você implemente facilmente políticas de sunset para emails, push e notificações no app. Aqui estão algumas coisas a considerar ao criar uma política de descontinuação:

- O que conta como um usuário "desengajado"? 
- O engajamento é definido por cliques, compras, uso de app ou uma combinação desses comportamentos? 
- Quanto tempo precisa durar o lapso no engajamento para você parar de enviar mensagens?
- Você entregará alguma campanha especial aos usuários antes de excluí-los de seus segmentos?
- A quais canais de envio de mensagens sua política de descontinuação se aplicará? 

Por exemplo, se você tem usuários que optam pela [proteção de privacidade de e-mail (MPP) da Apple]({{site.baseurl}}/user_guide/message_building_by_channel/email/apple_mail/mpp/), considere como isso pode impactar suas campanhas de e-mail e métricas de entregabilidade e determine a melhor forma de estruturar sua política de sunset.

Para incorporar políticas de sunset em suas campanhas, crie um [segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#creating-a-segment) que exclua automaticamente os usuários que marcaram seus e-mails como spam ou que não interagiram com suas mensagens por um determinado período de tempo.  

Para configurar esses segmentos, escolha os filtros `Has Marked You As Spam` e `Last Engaged With Message`, localizados na seção **Redirecionamento**, no menu suspenso de filtros. 

Quando você aplica o filtro `Last Engaged With Message`, especifique o tipo de envio de mensagens (push, e-mail ou notificação no app) com o qual o usuário interagiu ou não, bem como o número de dias desde a última interação do usuário. Depois de criar um segmento, escolha segmentar este segmento com qualquer [canal de envio de mensagens]({{site.baseurl}}/user_guide/message_building_by_channel/).

![Página Detalhes do segmento com o filtro "Último engajamento com mensagem" selecionado.]({% image_buster /assets/img_archive/email_sunset_policies_new.png %})

Embora o Braze pare automaticamente de enviar e-mails para usuários que marcaram você como spam, o filtro `Has Marked You As Spam` permite que você também envie mensagens push direcionadas e notificações no app para esses usuários. Esse filtro é útil para [campanhas de redirecionamento]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/retargeting_campaigns/#retargeting-campaigns). Por exemplo, você pode enviar mensagens para usuários desengajados que os lembrem dos recursos e ofertas que estão perdendo quando não abrem seus e-mails.

Políticas de descontinuação podem ser especialmente úteis em campanhas de e-mail que visam usuários inativos. Embora essas campanhas se concentrem em segmentos que não interagiram com seu app por um período de tempo, elas podem colocar a entregabilidade de seus e-mails em risco se incluírem repetidamente destinatários não engajados. As políticas de sunset permitem que você mire em usuários que estão deixando de usar o serviço sem cair na pasta de spam.

