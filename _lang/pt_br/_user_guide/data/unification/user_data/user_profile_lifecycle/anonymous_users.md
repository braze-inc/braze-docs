---
nav_title: Usuários anônimos
article_title: Usuários anônimos
page_order: 0
page_type: reference
description: "Este artigo fornece uma visão geral dos usuários anônimos e aliases de usuários, descrevendo sua importância e como eles podem ser aproveitados em suas mensagens."

---

# Usuários anônimos

> Os usuários que visitam seu site ou aplicativo sem fazer login, como um visitante convidado, são reconhecidos como usuários anônimos. Esses usuários não têm `external_ids`, que são usados para atualizar os perfis de usuário com a API do Braze, mas ainda têm [pontos de dados]({{site.baseurl}}/user_guide/data/data_points/) atribuídos a eles e podem ser direcionados em seus segmentos.

Quando um usuário anônimo visita seu site ou aplicativo, o Braze SDK cria e atribui a ele um perfil de usuário "anônimo". Enquanto o usuário navega, o SDK captura automaticamente dados para seu perfil de usuário anônimo, como informações de uso, informações do dispositivo e muito mais, se você tiver configurado atributos e eventos personalizados.

Você pode fazer o seguinte com usuários anônimos capturados:

- Envie mensagens aos usuários antes que eles façam login
- Colete o perfil de um usuário antes que ele faça login, para que você não perca dados relevantes
- Incentivar o preenchimento do perfil com uma mensagem quando um usuário preencher apenas parcialmente seu perfil
- Complete o perfil de um usuário quando ele fizer login, para que você possa cancelar o envio de mensagens em outras plataformas (por exemplo, não enviar uma mensagem de "frete grátis no primeiro pedido do aplicativo" quando o usuário já tiver feito pedidos do aplicativo)
- Envolva-se com os usuários que demonstram intenção de sair, incentivando-os a criar um perfil, fazer o checkout do carrinho ou realizar outra ação

## Como funciona

{% multi_lang_include anonymous_users/about_anonymous_users.md section='user_guide' %}

## Atribuição de aliases de usuário

{% multi_lang_include anonymous_users/about_user_aliases.md section='user_guide' %}

## Mesclando usuários anônimos  

Às vezes, os perfis de usuários anônimos são duplicatas que têm o mesmo número de telefone ou endereço de e-mail que outros perfis de usuários. Uma das duplicatas pode até ser um perfil de usuário identificado. Essas duplicatas podem ser mescladas em um único perfil de usuário usando o [POST: Mesclar Usuários do endpoint]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/) ou uma das ferramentas de mesclagem da plataforma Braze, como a [mesclagem baseada em regras]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users/#rules-based-merging).

## Casos de uso

### Segmente usuários anônimos no seu segmento

Como os usuários anônimos não têm um `external_id`, você pode segmentá-los em massa usando o filtro de segmentação **External User ID is blank**. Para maior precisão, você pode adicionar um atributo personalizado aos usuários anônimos que deseja segmentar e filtrar por ele.

Digamos que você atribua o atributo personalizado "is_lead_profile" a cada perfil de usuário anônimo. Você pode direcionar esses perfis com um ou ambos os filtros:

- **O ID do usuário externo está em branco**
- "is_lead_profile" **é verdadeiro**

\![Filtros de segmento para um ID de usuário externo em branco e um atributo personalizado "is_lead_profile" verdadeiro.]({% image_buster /assets/img/getting_started/anonymous_users.png %})

### Capturar dados de checkout de um usuário anônimo

É possível capturar dados de checkout de um usuário anônimo (ou visitante convidado) criando um perfil de usuário com alias durante o processo de checkout. Quando um usuário anônimo fizer o check-out usando um formulário de captura da Web, faça com que uma chamada de API seja acionada para criar um perfil de usuário com alias e registrar um evento de compra. Você poderá então atualizar o perfil de usuário criado por meio da API do Braze.

Aqui está um exemplo de carga útil que será gerada quando o formulário de captura da Web for enviado:

{% raw %}
```json
{
    "purchase":[
        {
            "user_alias": {"alias_name": "Joedoe", "alias_label": "full_name"},
            "app_id": "11dk3k9d-2183-3948-k02b-kw3938109k12od",
            "product_id": "jacket",
            "currency": "USD",
            "price": 80.00,
            "time": "2025-01-05T19:20:30+01:00",
            "properties": {
                "color": "brown",
                "monogram": "ABC",
                "checkout_duration": 180,
                "size": "Small",
                "brand": "Natural Essence"
            }
        }
    ]
}
```
{% endraw %}

