---
nav_title: Importação de sua lista de e-mails
article_title: Importação de sua lista de e-mails para o Braze
page_order: 4
page_type: reference
description: "Este artigo de referência aborda as práticas recomendadas para a importação de sua lista de e-mails para o Braze."
channel: email

---

# Importação de sua lista de e-mails para o Braze {#importing-email-lists}

> Uma etapa importante para se tornar um remetente de e-mail bem-sucedido é garantir que você tenha uma lista de e-mails de alta qualidade. O gerenciamento adequado da lista de e-mails pode melhorar a entregabilidade e fornecer resultados de campanha mais precisos e limpos.

## Considerações antes de importar

{% multi_lang_include email-via-sms-warning.md %}

### Valide suas listas de e-mail

Antes de importar sua lista de e-mails para o Braze, valide se sua lista inclui apenas endereços de e-mail genuínos. Uma alta taxa de bounce pode prejudicar a reputação de seu remetente de e-mail. 

Os serviços de limpeza de listas de e-mail podem fazer isso para você, determinando se o endereço de e-mail segue a sintaxe correta e tem as propriedades físicas de um endereço de e-mail, verificando o domínio do e-mail e conectando-se ao servidor de e-mail para autenticar se o endereço de e-mail existe lá.

### Identifique seus usuários engajados

Para identificar os usuários com maior engajamento, primeiro remova os usuários que estão profundamente desistentes. É uma prática recomendada não enviar e-mails a usuários que não tenham se engajado com um e-mail há mais de seis meses, pois isso pode prejudicar a reputação do remetente do e-mail. Ao importar sua lista de e-mails, certifique-se de incluir apenas os usuários que abriram um e-mail seu nos últimos seis meses.

A longo prazo, você também deve considerar a implementação de uma [política de sunsetting]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/sunset_policies/).

### Evitar listas de supressão

Se estiver fazendo a transição de um provedor de e-mail existente, certifique-se de não fazer a importação de usuários de uma lista de supressão. As listas de supressão apresentam endereços de e-mail que cancelaram a inscrição, marcaram seus e-mails como spam ou sofreram hard bounce.

## Métodos de importação

Depois de preparar sua lista de e-mails, há várias maneiras de importar usuários para o Braze, como por meio da API REST de e-mail do Braze ou de arquivos CSV. Leia mais em nosso artigo dedicado à [importação de usuários]({{site.baseurl}}/user_guide/data/user_data_collection/user_import/).

