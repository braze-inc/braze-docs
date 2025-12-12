---
nav_title: Como lidar com números de telefone desconhecidos
article_title: Como lidar com números de telefone desconhecidos
description: "Este artigo de referência aborda como o Braze lidará com números de telefone desconhecidos para usuários do WhatsApp."
page_type: reference
channel:
  - WhatsApp
page_order: 50
---

# Como lidar com números de telefone desconhecidos

> É possível que, depois de colocar o WhatsApp em funcionamento com o Braze, você receba mensagens de usuários desconhecidos. As etapas a seguir descrevem como um usuário e um número não identificados são processados.

## Fluxo de trabalho de opt-in/out e palavra-chave personalizada para números desconhecidos

O Braze tentará primeiro encontrar um usuário com um número correspondente. Se não for encontrado nenhum número, o Braze automaticamente endereça um número desconhecido de duas maneiras:

1. **Se for configurada uma palavra de gatilho com um [Canvas opt-in]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/message_processing/opt-ins_and_opt-outs/):**
- O Braze cria um perfil anônimo
- Atribuímos um alias de usuário ao perfil com os seguintes detalhes:
  - Um `alias_name` com o valor sendo o número de telefone fornecido pelo usuário
  - Um `alias_label` com o valor `phone`
- Nosso sistema define o atributo de telefone
- O usuário é inscrito no grupo de assinatura correspondente com base na lógica configurada no Canvas<br><br>
2. **Se nenhum Canvas opt-in estiver configurado:**
- O Braze cria um perfil anônimo
- Atribuímos um alias de usuário ao perfil com os seguintes detalhes:
  - Um `alias_name` com o valor sendo o número de telefone fornecido pelo usuário
  - Um `alias_label` com o valor `phone`
- Nosso sistema define o atributo de telefone
- O status de assinatura do usuário terá como padrão `unsubscribed` para todos os grupos de assinatura do WhatsApp<br><br>

