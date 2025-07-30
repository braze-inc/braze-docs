---
nav_title: Como lidar com números de telefone desconhecidos
article_title: Como lidar com números de telefone desconhecidos
page_order: 4
description: "Este artigo de referência cobre como o Braze processa números de telefone desconhecidos de novos usuários."
page_type: reference
channel:
  - SMS
  - MMS
  - RCS
  
---

# Lidando com números de telefone desconhecidos - novos usuários

> Você pode descobrir que, depois de configurar SMS, MMS e RCS com o Braze, você recebe mensagens de usuários desconhecidos. As etapas a seguir descrevem como um usuário e um número não identificados são processados.

## Fluxo de trabalho de aceitação/saída e palavra-chave personalizada para números desconhecidos

Braze aborda automaticamente um número desconhecido de uma das três maneiras:

1. Se uma palavra-chave de aceitação for enviada por mensagem de texto:
  * Braze cria um perfil anônimo
  * Nosso sistema define o atributo do telefone
  * Inscreve o usuário no grupo de inscrições correspondente com base na palavra-chave de aceitação recebida pelo Braze.<br><br>
2. Se uma palavra-chave de exclusão for enviada por mensagem de texto:
  * Braze cria um perfil anônimo
  * Nosso sistema define o atributo do telefone
  * Cancela a inscrição do usuário do grupo de inscrições correspondente com base na palavra-chave de exclusão recebida pela Braze.<br><br>
3. Se qualquer outra palavra-chave personalizada for enviada por texto:
  * Braze ignora a mensagem de texto e não faz nada.

