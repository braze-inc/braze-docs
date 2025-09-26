---
nav_title: Uso do registro de eventos
article_title: Uso do registro de eventos
page_order: 6
page_type: solution
description: "Este artigo de ajuda descreve como usar o registro de eventos para solucionar problemas com a integração do Braze."
---

# Usando o registro de eventos

Para ajudar a solucionar problemas com a integração do Braze, é possível configurar um perfil de usuário anônimo e um [registro de usuários de eventos]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/event_user_log_tab). Para ver um passo a passo para configurar um perfil anônimo, consulte [Adição de usuários teste]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#adding-test-users).

## Sobre o registro

Use o registro de usuários de eventos para testar como é o comportamento de um usuário anônimo. Isso pode ser particularmente útil para identificar o ID do usuário se o app que estiver sendo testado não coletar e-mails. Você pode usar o Braze e o endereço IP do seu dispositivo para adicioná-lo como usuário teste.

Essa é uma ótima maneira de encontrar usuários anônimos. Você também pode usar essas informações para testar quais dados estão sendo enviados ao Braze e verificar se há discrepâncias. Nessa visualização, é possível identificar se os deltas dos seus dados estão sendo enviados para o Braze. Se um endereço de e-mail ou token por push for enviado com cada evento registrado, todos os dados serão enviados ao Braze.

Ainda precisa de ajuda? Abra um [tíquete de suporte]({{site.baseurl}}/braze_support/).

_Última atualização em 16 de novembro de 2022_

