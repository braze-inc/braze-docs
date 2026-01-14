---
nav_title: Como lidar com números de telefone desconhecidos
article_title: Como lidar com números de telefone desconhecidos
page_order: 4
description: "Este artigo de referência aborda como o Braze processa números de telefone desconhecidos de novos usuários."
page_type: reference
channel:
  - SMS
  - MMS
  - RCS
  
---

# Como lidar com números de telefone desconhecidos - novos usuários

> Talvez você descubra que, depois de colocar SMS, MMS e RCS em funcionamento com o Braze, receberá mensagens de usuários desconhecidos. As etapas a seguir descrevem como um usuário e um número não identificados são processados.

## Fluxo de trabalho de opt-in/out e palavra-chave personalizada para números desconhecidos

O Braze endereça automaticamente um número desconhecido de uma das três maneiras:

1. Se uma palavra-chave opt-in for enviada por texto:
  * O Braze cria um perfil anônimo
  * Nosso sistema define o atributo de telefone
  * Inscreve o usuário no grupo de assinaturas correspondente com base na palavra-chave opt-in recebida pelo Braze.<br><br>
2. Se uma palavra-chave de recusa for enviada por mensagem de texto:
  * O Braze cria um perfil anônimo
  * Nosso sistema define o atributo de telefone
  * Cancela a assinatura do usuário do grupo de assinatura correspondente com base na palavra-chave de cancelamento recebida pelo Braze.<br><br>
3. Se qualquer outra palavra-chave personalizada for digitada:
  * Braze ignora a mensagem de texto e não faz nada.

