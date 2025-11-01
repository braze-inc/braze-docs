---
nav_title: Grupos de assinatura
article_title: Grupos de assinatura
page_order: 1
description: "Este artigo aborda os grupos de assinatura de mensagens LINE."
page_type: reference
channel:
 - LINE
alias: /line/subscription_groups/
---

# Grupos de assinatura LINE

> Há dois estados de assinatura para os usuários do LINE: inscrito e não inscrito. O LINE pode ter até 100 grupos de assinatura por espaço de trabalho, com cada grupo de assinatura conectado ao seu próprio canal LINE.

| Estado | Definição |
| --- | --- |
| Assinatura | O usuário seguiu o canal LINE a partir de seu aplicativo LINE. Os usuários são inscritos automaticamente quando os seguem após a conclusão das etapas de integração. |
| Cancelamento da inscrição | O usuário não seguiu o canal LINE no aplicativo LINE ou deixou explicitamente de seguir o canal LINE. <br><br> Os usuários que cancelarem a assinatura de um grupo de assinatura LINE não receberão mais nenhuma mensagem LINE dos canais de envio que pertencem ao grupo de assinatura. |
{: .reset-td-br-1 .reset-td-br-2 }

## Definição do grupo de assinatura LINE de um usuário

O LINE hospeda o status da assinatura dos usuários. O Braze processa os eventos de seguir e deixar de seguir que atualizam o status da assinatura.