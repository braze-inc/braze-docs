---
nav_title: Reconciliação de usuários do Shopify
article_title: Reconciliação de usuários do Shopify
permalink: "/shopify_user_reconciliation/"
description: "Este artigo de referência aborda como reconciliar o ID do dispositivo e as informações pessoais do usuário quando ele chega ao fluxo de checkout."
hidden: true
---

# Reconciliação de usuários do Shopify fora do fluxo de checkout 

> A integração com o Shopify reconcilia o ID do dispositivo e as informações pessoais do usuário quando ele chega ao fluxo de checkout e executa qualquer evento de webhook do Shopify lá.

{% alert note %}
Esse recurso está em beta. Se estiver interessado, entre em contato com seu gerente de sucesso do cliente ou gerente de conta.
{% endalert %}

Para dar suporte à reconciliação do usuário por meio do fluxo de inscrição e login do Shopify, podemos implementar uma função JavaScript automaticamente em sua loja do Shopify fora do fluxo de checkout. A Braze implementará automaticamente uma função sempre que virmos um formulário com `type="email"` na loja da Shopify, como no exemplo abaixo.

![1]{:style="max-width:60%;"}

Quando essa função é chamada, o usuário anônimo na Web passa a ser associado ao endereço de e-mail fornecido. No futuro, todos os eventos do Shopify que fizerem referência a qualquer um dos identificadores que usamos (por exemplo, ID do cliente do Shopify, endereço de e-mail, número de telefone) serão atribuídos ao mesmo usuário do Braze se houver uma correspondência.

## Considerações

{% alert important %}
O Braze não está familiarizado com todos os formulários que contêm `type="email"` no site Shopify de um cliente. Isso significa que existe a possibilidade de a função não detectar alguns campos de entrada que deveriam ser utilizados para a reconciliação do usuário ou detectar campos incorretos que definiriam o endereço de e-mail errado (por exemplo, formulário de indicação) no perfil do usuário.
{% endalert %}

Recomendamos que você explore todos os formulários compatíveis com o site da Shopify e avalie como essa solução beta pode atender às suas necessidades de forma eficaz. Ao aceitar utilizar esse recurso beta, você entende que há um comportamento potencialmente inesperado ao fazer alterações manuais em seus formulários da Shopify.

[1]: {% image_buster /assets/img/shopify_type_email.png %}
