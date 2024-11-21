---
nav_title: Grupos de inscrições
article_title: Grupos de inscrições
page_order: 1
description: "Este artigo aborda os grupos de inscrições de mensagens LINE."
page_type: reference
channel:
 - LINE
alias: /line/subscription_groups/
---

# Grupos de inscrições LINE

> Há dois estados de inscrição para usuários do LINE: inscrito e cancelado inscrição. O LINE pode ter até 100 grupos de inscrições por espaço de trabalho, com cada grupo de inscrições conectado a seu próprio canal LINE.

| Status | Definição |
| --- | --- |
| Inscreveu-se | O usuário seguiu o canal do LINE em seu app do LINE. Os usuários são automaticamente inscritos quando seguem o site após a conclusão das etapas de integração. |
| Cancelou inscrição | O usuário não seguiu o canal LINE em seu app LINE ou deixou explicitamente de seguir o canal LINE. <br><br> Os usuários que cancelarem a inscrição em um grupo de inscrições LINE não receberão mais mensagens LINE dos canais de envio de mensagens que pertencem ao grupo de inscrições. |
{: .reset-td-br-1 .reset-td-br-2 }

## Configuração do grupo de inscrições LINE de um usuário

O LINE hospeda o status da inscrição dos usuários. O Braze processa os eventos de seguir e deixar de seguir que atualizam o status da inscrição.