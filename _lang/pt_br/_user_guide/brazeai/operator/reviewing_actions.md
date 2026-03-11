---
nav_title: Revisar ações
article_title: Revisando ações do BrazeAI Operator<sup>TM</sup>
page_order: 2
description: "Aprenda como revisar e aprovar ações quando o BrazeAI Operator propõe mudanças no dashboard."
---

# Revisando ações do BrazeAI Operator

> Aprenda como revisar e aprovar ações quando o BrazeAI Operator<sup>TM</sup> propõe mudanças no dashboard.

![Operador apresentando cartões de ação sugeridos para revisão.]({% image_buster /assets/img/operator/suggested_actions.png %}){: style="max-width:40%; border:none; float:right; margin-left:15px;"}

## Como funcionam os cartões de ação

Quando o Operador propõe mudanças no dashboard (como preencher campos de formulário, atualizar configurações ou gerar imagens), ele apresenta cada mudança como um cartão de ação para revisão.

1. **Operador resume o plano:** O Operador explica o que planeja fazer antes de mostrar os cartões de ação.
2. **Cartões de ação individuais aparecem:** Cada mudança proposta é apresentada como um cartão separado que mostra o que o Operador deseja mudar ou fazer no dashboard. Para mudanças em valores existentes, tanto o valor anterior quanto o valor proposto são mostrados lado a lado para comparação.
3. **Revisar e aprovar:** Revise cada cartão e aprove ou recuse.
4. **Ação executa:** Ações aprovadas são executadas no Braze. Ações recusadas não são aplicadas.

Se uma ação falhar após a aprovação, o Operador notificará com detalhes sobre a falha.

### Disponibilidade

Os cartões de ação são suportados nos seguintes editores:

- Mensagens no aplicativo (apenas editor tradicional)
- Cartões de conteúdo
- E-mail (apenas editor de HTML)
- Notificações por push
- SMS/MMS/RCS
- Webhooks

Em outras páginas, o Operador fornece uma lista de etapas a seguir na interface em vez de tomar a ação por conta própria. A funcionalidade do Operador está sendo regularmente aprimorada, e uma cobertura expandida para ferramentas de criação é esperada.

## Modificar um plano

Para modificar o plano do Operador, primeiro aprove ou rejeite as ações pendentes. Em seguida, descreva a alteração desejada em uma nova mensagem de chat.

Ações aprovadas não podem ser desfeitas através do Operador. Descreva a nova alteração ao Operador ou faça alterações manualmente no dashboard.

## Ações com aprovação automática

O botão **Auto-aprovar ações** está localizado no painel de chat do Operador.

- **Ativado:** As ações sugeridas pelo Operador são executadas imediatamente sem exigir aprovação manual. Algumas ações ainda requerem aprovação explícita por segurança, como gerar imagens ou fazer modificações nas configurações de nível de espaço de trabalho.
- **Desativado (padrão):** Todas as ações propostas seguem o processo de revisão manual descrito.

![O botão de auto-aprovação e o modal de confirmação no painel de chat do Operador.]({% image_buster /assets/img/operator/auto-approval_toggle.png %}){: style="max-width:50%;"}

A auto-aprovação é redefinida quando você atualiza a página, abre uma nova guia ou faz logout e login novamente. Navegar entre páginas no dashboard não a redefine. A auto-aprovação pode ser desativada a qualquer momento.
