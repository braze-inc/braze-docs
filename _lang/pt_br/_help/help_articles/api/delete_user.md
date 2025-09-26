---
nav_title: Remoção de usuários via API
article_title: Remoção de usuários via API
page_order: 0

page_type: reference
description: "Este artigo de ajuda descreve as implicações da remoção de um perfil de usuário por meio da API REST do Braze."
tool: Dashboard
platform: API
---

# Remoção de usuários via API

Quando você [remove um usuário por meio da Braze REST API]({{site.baseurl}}/api/endpoints/user_data/#user-delete-endpoint/), os seguintes dados são excluídos (nulled):
- Quaisquer atribuições que o usuário tenha
- Endereço de e-mail
- Número de telefone
- ID de usuário externo 
- Gênero
- País
- Idioma

Quando você [remove um usuário por meio da Braze REST API]({{site.baseurl}}/api/endpoints/user_data/#user-delete-endpoint/), ocorrem os seguintes eventos:
- O perfil do usuário é excluído (anulado).
- A contagem de [usuários vitalícios]({{site.baseurl}}/user_guide/data_and_analytics/analytics/understanding_your_app_usage_data/#lifetime-users) será atualizada para contabilizar os usuários recém-removidos.	
- O usuário removido ainda será contabilizado na porcentagem de conversão agregada. As contagens de eventos personalizados e de compras não serão atualizadas para usuários removidos.

## Vários perfis com um endereço de e-mail compartilhado

Digamos que você queira mesclar vários perfis de usuário que compartilham o mesmo endereço de e-mail. 

Para mesclar esses perfis de usuário:

 1. Identifique todos os usuários com endereços de e-mail duplicados. 
 2. Exportar todas as atribuições de um único perfil. 
 3. Importe essas atribuições para o perfil do usuário via API ou CSV. 
 4. Remova os usuários via API, essencialmente excluindo esses usuários duplicados e os dados descritos acima.

_Última atualização em 13 de setembro de 2023_

