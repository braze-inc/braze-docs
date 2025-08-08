---
nav_title: Alteração do atributo personalizado ou do tipo de dados do evento
article_title: Alteração do atributo personalizado ou do tipo de dados do evento
page_order: 1

page_type: solution
description: "Este artigo de ajuda o orienta sobre como alterar o tipo de dados de um atributo personalizado ou evento personalizado e as implicações disso."
---

# Alteração do atributo personalizado ou do tipo de dados do evento

Para alterar o tipo de dados de um atributo personalizado ou evento, no dashboard do Braze, navegue até **Configurações de dados** e selecione **Atributos personalizados** ou **Eventos personalizados**.

![Guia de Atributos Personalizados para editar atributo ou tipo de dado]({% image_buster /assets/img/change_custom_attribute.png %})

Se você precisar alterar o tipo de dados de um atributo personalizado ou evento (por exemplo, alterar `time` para `string`), considere o seguinte:

- Os filtros relevantes em segmentos, campanhas, Canvas ou outros locais que usam o atributo ou evento alterado não são atualizados automaticamente. Antes de modificar as atribuições, você deve interromper todas as campanhas ou telas que estejam usando os atributos em segmentos ou filtros e remover os atributos dos filtros que os referenciam.
- Os dados de usuários não serão atualizados retroativamente. Se a atribuição alterada estava em um perfil de usuário antes da alteração do tipo de dados, então esse valor ainda será o tipo de dados antigo. Isso pode fazer com que os usuários saiam dos segmentos que contêm a atribuição alterada. O filtro procurará ativamente o novo tipo de dados, mas se um perfil ainda tiver o tipo de dados anterior, esse usuário será excluído do segmento. Esses usuários devem ser atualizados para voltarem aos segmentos adequados. Você pode fazer isso com o [endpoint `users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/).
- Novos dados não serão aceitos se não forem do novo tipo de dados. Por exemplo, uma chamada de API para o endpoint `users/track` que contenha o tipo de dados anterior para uma atribuição alterada não será aceita. Você deve chamar o novo tipo de dados.

{% alert important %}
A capacidade de impedir que a detecção automática atualize o tipo de dados de atributo personalizado está atualmente em acesso antecipado. Entre em contato com seu gerente de sucesso do cliente se tiver interesse em participar desse acesso antecipado.
{% endalert %}

_Última atualização em 8 de fevereiro de 2024_

