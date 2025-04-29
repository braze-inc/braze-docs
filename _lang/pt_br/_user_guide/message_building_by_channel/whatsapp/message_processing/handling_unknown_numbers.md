---
nav_title: Como lidar com números de telefone desconhecidos
article_title: Como lidar com números de telefone desconhecidos
description: "Este artigo de referência aborda como a Braze lidará com números de telefone desconhecidos para usuários do WhatsApp."
page_type: reference
channel:
  - WhatsApp
page_order: 50
---

# Como lidar com números de telefone desconhecidos

> É possível que, depois de colocar o WhatsApp em funcionamento com o Braze, você receba mensagens de usuários desconhecidos. As etapas a seguir descrevem como um usuário e um número não identificados são processados.

## Fluxo de trabalho de aceitação/saída e palavra-chave personalizada para números desconhecidos

O Braze tentará primeiro encontrar um usuário com um número correspondente. Se nenhum número for encontrado, a Braze endereça automaticamente um número desconhecido de uma das duas maneiras:

1. **Se uma palavra disparadora com uma [tela de aceitação]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/message_processing/opt-ins_and_opt-outs/) for configurada:**
- Braze cria um perfil anônimo
- Atribuímos um alias de usuário ao perfil com os seguintes detalhes:
  - Um `alias_name` com o valor sendo o número de telefone fornecido pelo usuário
  - Um `alias_label` com o valor `phone`
- Nosso sistema define a atribuição do telefone
- O usuário é inscrito no grupo de inscrições correspondente com base na lógica configurada no Canva.<br><br>
2. **Se nenhuma tela de aceitação estiver configurada:**
- Braze cria um perfil anônimo
- Atribuímos um alias de usuário ao perfil com os seguintes detalhes:
  - Um `alias_name` com o valor sendo o número de telefone fornecido pelo usuário
  - Um `alias_label` com o valor `phone`
- Nosso sistema define a atribuição do telefone
- O status de inscrição do usuário terá como padrão `unsubscribed` para todos os grupos de inscrições do WhatsApp<br><br>

