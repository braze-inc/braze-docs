---
nav_title: Revisar ações
article_title: Revisar ações do BrazeAI Operator<sup>TM</sup>
page_order: 2
description: "Saiba como revisar e aprovar ações quando o BrazeAI Operator sugere alterações no dashboard."
---

# Revisar ações do BrazeAI Operator

> Saiba como revisar e aprovar ações quando o BrazeAI Operator<sup>TM</sup> sugere alterações no dashboard.

![O Operator exibe cartões de ação sugeridos para revisão.]({% image_buster /assets/img/operator/suggested_actions.png %}){: style="max-width:40%; border:none; float:right; margin-left:15px;"}

## Como funcionam os cartões de ação

Quando o Operator sugere alterações no dashboard (por exemplo, preencher campos de formulário, ajustar configurações ou gerar imagens), cada alteração é exibida como um cartão de ação para revisão.

1. **O Operator resume o plano:** O Operator explica o que fará antes dos cartões de ação.
2. **Cartões de ação individuais aparecem:** Cada alteração sugerida é exibida em seu próprio cartão. Para alterações em valores existentes, o valor antigo e o novo aparecem lado a lado.
3. **Revisar e aprovar:** Revise cada cartão e aprove ou rejeite.
4. **Ação é executada:** Ações aprovadas são executadas na Braze. Ações rejeitadas não são aplicadas.

Se uma ação falhar após aprovação, o Operator informa com detalhes do erro.

### Disponibilidade

Os cartões de ação são suportados nos seguintes editores:

- Mensagens in-app (apenas editor clássico)
- Content Cards
- E-mail (apenas editor HTML)
- Notificações push
- SMS/MMS/RCS
- Webhooks

Em outras páginas, o Operator fornece uma lista de etapas para executar na interface em vez de executar ações diretamente. A funcionalidade do Operator está em expansão contínua; maior cobertura das ferramentas de criação está planejada.

## Ajustar um plano

Para alterar o plano do Operator, primeiro aprove ou rejeite as ações pendentes. Em seguida, descreva a alteração desejada em uma nova mensagem no chat.

Ações aprovadas não podem ser desfeitas pelo Operator. Descreva a nova alteração ao Operator ou faça as alterações manualmente no dashboard.

## Aprovar ações automaticamente

O interruptor **Aprovar ações automaticamente** fica no painel de chat do Operator.

- **Ligado:** As ações sugeridas pelo Operator são executadas imediatamente, sem aprovação manual. Por segurança, algumas ações ainda exigem aprovação explícita, por exemplo geração de imagens ou alterações em nível de espaço de trabalho.
- **Desligado (padrão):** Todas as ações sugeridas passam pelo processo de revisão manual descrito.

![O interruptor de aprovação automática e a caixa de confirmação no painel de chat do Operator.]({% image_buster /assets/img/operator/auto-approval_toggle.png %}){: style="max-width:50%;"}

A aprovação automática é redefinida quando você atualiza a página, abre uma nova aba ou faz logout e login novamente. Navegar entre páginas no dashboard não a redefine. Você pode desligar a aprovação automática a qualquer momento.
