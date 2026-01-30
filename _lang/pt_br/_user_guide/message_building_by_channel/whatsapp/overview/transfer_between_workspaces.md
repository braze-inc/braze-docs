---
nav_title: Transferência entre espaços de trabalho
article_title: Transfira números de telefone e grupos de inscrições entre espaços de trabalho
page_order: 5
description: "Este artigo de referência aborda como transferir seu número de telefone e grupos de inscrições do WhatsApp entre espaços de trabalho."
page_type: reference
channel:
  - WhatsApp
---

# Transfira números de telefone e grupos de inscrições do WhatsApp entre espaços de trabalho

> Esta página aborda como você pode mover um número de telefone da WhatsApp Business Account (WABA) e seu grupo de inscrições associado de um espaço de trabalho para outro no Braze. Esse processo simplifica sua experiência de uso do WhatsApp com o Braze e reduz a necessidade de ajuda da engenharia.

## Pré-requisitos

- Confirme que você tem a [permissão de usuário]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#list-of-permissions) "Gerenciar grupos de inscrições" nos espaços de trabalho original e novo.
- A WABA não pode cruzar vários [clusters de Braze]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints). É improvável que isso aconteça se você estiver trabalhando em uma única empresa. 

## Transferência de um número de telefone e de um grupo de inscrições

### Etapa 1: Arquivar o grupo de inscrições

Para arquivar um grupo de inscrições do WhatsApp, siga estas etapas:

1. Acesse o espaço de trabalho onde o grupo de inscrições existe atualmente.
2. Acesse **Público** > **Gerenciamento de grupos de inscrições** e localize o grupo de inscrições associado ao número de telefone do WhatsApp que deseja mover.
3. Passe o mouse sobre o status do grupo de inscrições e selecione <i class="fa-solid fa-box-archive"></i> **Archive**, que marcará o grupo de inscrições como inativo, mas não o excluirá.

![O botão "Arquivar" aparece ao passar o mouse sobre o status "Ativo" de um grupo de inscrições.]({% image_buster /assets/img/whatsapp/archive_subscription_group.png %}){: style="max-width:70%;"}

### Etapa 2: Integrar o número de telefone do WhatsApp ao novo espaço de trabalho

1. Acesse o espaço de trabalho para o qual você deseja mover o número de telefone do WhatsApp.
2. Acesse **Partner Integrations** > **Technology Partners** > **WhatsApp** e, em seguida, role até a seção **WhatsApp Messaging Integration**. 
3. Selecione a opção **Criar novo grupo de inscrições e número de telefone**
4. Inicie o processo de integração, durante o qual você pode selecionar o número de telefone do grupo de inscrições arquivado.

### Etapa 3: Verificar a integração

1. Depois de concluir a integração, confirme que o número de telefone do WhatsApp agora está associado ao grupo de inscrições no novo espaço de trabalho.
2. Teste para confirmar que as mensagens podem ser enviadas e recebidas por meio desse número de telefone do WhatsApp.

## Considerações

- Se precisar transferir o número de telefone do WhatsApp de volta para o espaço de trabalho original, repita as etapas. Arquive o grupo de inscrições no espaço de trabalho de destino e, em seguida, integre-o ao espaço de trabalho original.
- Não é necessário remover o número de telefone do WhatsApp do Meta Business Manager durante a transferência.