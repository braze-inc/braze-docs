---
nav_title: Transferência entre espaços de trabalho
article_title: Transferir números de telefone e grupos de assinatura entre espaços de trabalho
page_order: 4
description: "Este artigo de referência aborda como transferir seu número de telefone e grupos de assinatura do WhatsApp entre espaços de trabalho."
page_type: reference
channel:
  - WhatsApp
---

# Transferir números de telefone e grupos de assinatura do WhatsApp entre espaços de trabalho

> Esta página aborda como você pode mover um número de telefone da WhatsApp Business Account (WABA) e seu grupo de assinatura associado de um espaço de trabalho para outro no Braze. Esse processo simplifica sua experiência de uso do WhatsApp com o Braze e reduz a necessidade de ajuda da engenharia.

## Pré-requisitos

- Confirme que você tem a [permissão de usuário]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#list-of-permissions) "Manage Subscription Groups" (Gerenciar grupos de assinatura) nos espaços de trabalho original e novo.
- A WABA não pode cruzar vários [clusters Braze]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints). É improvável que isso aconteça se você estiver trabalhando em uma única empresa. 

## Transferência de um número de telefone e de um grupo de assinaturas

### Etapa 1: Arquivar o grupo de assinaturas

Para arquivar um grupo de assinaturas do WhatsApp, siga estas etapas:

1. Vá para o espaço de trabalho onde o grupo de assinaturas existe atualmente.
2. Vá para **Audience** > **Subscription Group Management** e localize o grupo de assinatura associado ao número de telefone do WhatsApp que você deseja mover.
3. Passe o mouse sobre o status do grupo de assinaturas e selecione <i class="fa-solid fa-box-archive"></i> **Archive**, que marcará o grupo de assinaturas como inativo, mas não o excluirá.

Exibição do botão "Arquivar" ao passar o mouse sobre o status "Ativo" de um grupo de assinatura.]({% image_buster /assets/img/whatsapp/archive_subscription_group.png %}){: style="max-width:70%;"}

### Etapa 2: Integrar o número de telefone do WhatsApp ao novo espaço de trabalho

1. Vá para o espaço de trabalho para o qual deseja mover o número de telefone do WhatsApp.
2. Vá para **Partner Integrations** > **Technology Partners** > **WhatsApp** e, em seguida, role até a seção **WhatsApp Messaging Integration**. 
3. Selecione a opção **Criar novo grupo de assinatura e número de telefone**
4. Inicie o processo de integração, durante o qual você pode selecionar o número de telefone do grupo de assinaturas arquivado.

### Etapa 3: Verificar a integração

1. Depois de concluir a integração, confirme que o número de telefone do WhatsApp agora está associado ao grupo de assinatura no novo espaço de trabalho.
2. Teste para confirmar que as mensagens podem ser enviadas e recebidas por meio desse número de telefone do WhatsApp.

## Considerações

- Se você precisar transferir o número de telefone do WhatsApp de volta para o espaço de trabalho original, repita as etapas. Arquive o grupo de assinaturas no espaço de trabalho de destino e, em seguida, integre-o ao espaço de trabalho original.
- Não é necessário remover o número de telefone do WhatsApp do Meta Business Manager durante a transferência.