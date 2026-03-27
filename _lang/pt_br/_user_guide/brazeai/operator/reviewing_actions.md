---
nav_title: Revisar ações
article_title: Revisando ações do BrazeAI Operator<sup>TM</sup>
page_order: 2
description: "Aprenda como revisar e aprovar ações quando o BrazeAI Operator propõe mudanças no dashboard."
---

# Revisando ações do BrazeAI Operator

> Aprenda como revisar e aprovar ações quando o BrazeAI Operator<sup>TM</sup> propõe mudanças no dashboard.

![Operator apresentando cartões de ação sugeridos para revisão.]({% image_buster /assets/img/operator/suggested_actions.png %}){: style="max-width:40%; border:none; float:right; margin-left:15px;"}

## Como funcionam os cartões de ação

Quando o Operator propõe mudanças no dashboard (como preencher campos de formulário, atualizar configurações ou gerar imagens), ele apresenta cada mudança como um cartão de ação para revisão.

1. **O Operator resume o plano:** o Operator explica o que planeja fazer antes de mostrar os cartões de ação.
2. **Cartões de ação individuais aparecem:** cada mudança proposta é apresentada como um cartão separado que mostra o que o Operator deseja alterar ou fazer no dashboard. Para mudanças em valores existentes, tanto o valor anterior quanto o valor proposto são mostrados lado a lado para comparação.
3. **Revisar e aprovar:** revise cada cartão e aprove ou recuse.
4. **Ação executada:** ações aprovadas são executadas na Braze. Ações recusadas não são aplicadas.

Se uma ação falhar após a aprovação, o Operator vai notificar você com detalhes sobre a falha.

### Disponibilidade

Os cartões de ação são compatíveis com os seguintes editores e páginas.

- **Editores de mensagem:**
    - Mensagens no app (apenas editor tradicional)
    - Cartões de conteúdo
    - E-mail (apenas editor de HTML)
    - Notificações por push
    - SMS/MMS/RCS
    - Webhooks
- Página [Criar agente personalizado]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/)
 
Em outras páginas, o Operator fornece uma lista de etapas a seguir na interface em vez de tomar a ação por conta própria. A funcionalidade do Operator está sendo aprimorada regularmente, e a expectativa é que a cobertura para ferramentas de criação seja expandida.

## Modificar um plano

Para modificar o plano do Operator, primeiro aprove ou rejeite as ações pendentes. Em seguida, descreva a alteração desejada em uma nova mensagem de chat.

Ações aprovadas não podem ser desfeitas pelo Operator. Descreva a nova alteração ao Operator ou faça as mudanças manualmente no dashboard.

## Aprovação automática de ações

O botão **Aprovação automática de ações** está localizado no painel de chat do Operator.

- **Ativado:** as ações sugeridas pelo Operator são executadas imediatamente sem exigir aprovação manual. Algumas ações ainda requerem aprovação explícita por segurança, como gerar imagens ou fazer modificações nas configurações do espaço de trabalho.
- **Desativado (padrão):** todas as ações propostas seguem o processo de revisão manual descrito.

![O botão de aprovação automática e o modal de confirmação no painel de chat do Operator.]({% image_buster /assets/img/operator/auto-approval_toggle.png %}){: style="max-width:50%;"}

A aprovação automática é redefinida quando você atualiza a página, abre uma nova guia ou faz logout e login novamente. Navegar entre páginas no dashboard não a redefine. A aprovação automática pode ser desativada a qualquer momento.