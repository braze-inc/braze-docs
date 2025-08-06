---
nav_title: Setembro
page_order: 5
noindex: true
page_type: update
description: "Este artigo contém notas de versão de setembro de 2018."
---
# Setembro de 2018

## Grupos de notificação do iOS 12: Habilidades adicionais

Agora você pode acessar [os recursos do Grupo de Notificação da Apple]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#notification-groups) usando o Braze! É possível adicionar argumentos e grupos resumidos, utilizar alertas críticos, filtrar usuários autenticados provisoriamente e visualizar o status de autenticação provisória nos perfis de usuário.

## Horário de silêncio

Os clientes agora podem especificar o [Horário de silêncio]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-5-select-your-send-settings) (o tempo durante o qual suas mensagens não serão enviadas) para o Canva. Basta acessar **as Configurações de envio dos canvas** e marcar a opção "Ativar horário de silêncio". Em seguida, selecione o Horário de silêncio no fuso local do usuário e a ação a ser seguida se a mensagem for disparada dentro desse Horário de silêncio.

As campanhas de mensagens agora também usam o "horário de silêncio" em vez de "enviar esta mensagem durante uma parte específica do dia".

## Ajustar clientes

Os clientes do Braze que usam [o Adjust]({{site.baseurl}}/partners/message_orchestration/attribution/adjust/) agora podem ver sua chave de API do Braze e o URL da instância do Braze, que serão usados na plataforma Adjust para integração.

## Não está no filtro de segmento

Os clientes agora podem criar um segmento a partir de usuários que [não]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#retargeting) estão [incluídos em um determinado segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#retargeting).

## Exportações CSV do destinatário da tela

Os clientes agora podem [exportar dados]({{site.baseurl}}/user_guide/data/export_braze_data/export_canvas_data/) de usuários que entraram em um Canva. O CSV gerado será semelhante ao CSV da campanha.

## Filtro de segmento do iOS 12 autorizado provisoriamente

Foi adicionado um [filtro de segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#other) que permite encontrar usuários que estão autorizados provisoriamente no iOS 12 para um determinado app.

## Upload de imagens para mensagens no app

O criador de imagens para mensagens no app foi transferido do painel de design para o painel de criação.

## Permissões somente leitura na página Perfil do usuário

Antes desta versão, os clientes podiam alterar o status da inscrição e o endereço de e-mail no perfil do usuário com [permissões somente de leitura]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#available-limited-and-team-role-permissions). Renomeamos a permissão `import_user` para `import_and_update_user` e restringimos o acesso de edição ao status da inscrição e ao endereço de e-mail. Agora, quando um desenvolvedor está em simulação de somente leitura ou não tem essa permissão, ele não pode alterar o status da inscrição ou o endereço de e-mail.
