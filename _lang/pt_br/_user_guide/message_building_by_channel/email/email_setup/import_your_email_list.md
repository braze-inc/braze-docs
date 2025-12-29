---
nav_title: Importando sua lista de e-mails
article_title: Importando sua lista de e-mails para o Braze
page_order: 4
page_type: reference
description: "Este artigo de referência cobre as melhores práticas para importar sua lista de e-mails para o Braze."
channel: email

---

# Importando sua lista de e-mails para o Braze {#importing-email-lists}

> Uma etapa importante para se estabelecer como um remetente de e-mails bem-sucedido é garantir que você tenha uma lista de e-mails de alta qualidade. Uma gestão adequada da lista de e-mails pode melhorar sua entregabilidade e fornecer resultados de campanha mais precisos e limpos.

## Considerações antes de importar

{% multi_lang_include alerts/important_alerts.md alert='Email via SMS' %}

### Valide suas listas de e-mails

Antes de importar sua lista de e-mails para o Braze, valide se sua lista inclui apenas endereços de e-mail genuínos. Uma alta taxa de rejeição pode prejudicar sua reputação como remetente de e-mails. 

Serviços de limpeza de listas de e-mails podem fazer isso por você, determinando se o endereço de e-mail segue a sintaxe correta e possui as propriedades físicas de um endereço de e-mail, verificando o domínio do e-mail e conectando-se ao servidor de e-mail para autenticar se o endereço de e-mail existe lá.

### Verifique se um endereço de e-mail já está associado a um usuário

Antes de criar um usuário através da API ou SDK, chame o [`/users/export/ids`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) endpoint e especifique o `email_address` do usuário. Se retornar um perfil de usuário, esse usuário do Braze já está associado a esse endereço de e-mail.

Recomendamos fortemente que você procure endereços de e-mail únicos quando novos usuários forem criados e evite passar ou importar usuários com o mesmo endereço de e-mail. Caso contrário, você pode ter consequências indesejadas que impactam o envio de mensagens, segmentação, relatórios e outros recursos.

Por exemplo, digamos que você tenha perfis duplicados, mas certos atributos ou eventos personalizados residem em apenas um perfil. Quando você tenta acionar campanhas ou Canvases com múltiplos critérios, o Braze não consegue identificar o usuário como elegível porque existem dois perfis de usuário. Ou, se uma campanha segmenta um endereço de e-mail compartilhado por dois usuários, a página **Buscar Usuários** mostrará ambos os perfis de usuário como tendo recebido a campanha.

### Identifique seus usuários engajados

Para identificar seus usuários mais engajados, primeiro remova os usuários que estão inativos há muito tempo. É uma boa prática não enviar e-mails para usuários que não interagiram com um e-mail em mais de seis meses, pois isso pode prejudicar sua reputação como remetente de e-mails. Ao importar sua lista de e-mails, certifique-se de incluir apenas usuários que abriram um e-mail seu nos últimos seis meses.

A longo prazo, você também deve considerar implementar uma [política de descontinuação]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/sunset_policies/).

### Evite listas de supressão

Se você estiver mudando de um provedor de e-mail existente, certifique-se de não importar usuários de uma lista de supressão. Listas de supressão contêm endereços de e-mail que se desinscreveram, marcaram seus e-mails como spam ou retornaram como erro permanente.

## Métodos para importação

Uma vez que você tenha sua lista de e-mails preparada, existem várias maneiras de importar usuários para o Braze, como via API REST do Braze ou arquivos CSV. Leia mais em nosso artigo dedicado [Importação de Usuários]({{site.baseurl}}/user_guide/data/user_data_collection/user_import/).

