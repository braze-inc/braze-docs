---
nav_title: Abortar o envio de mensagens
article_title: Abortar o envio de mensagens Liquid
page_order: 7
description: "Este artigo de referência aborda o cancelamento de mensagens Liquid e alguns exemplos de casos de uso."

---

# Abortar o envio de mensagens

> Opcionalmente, você pode abortar o envio de mensagens Liquid dentro de condicionais. Este artigo de referência lista alguns exemplos de como esse recurso pode ser usado em campanhas de marketing.

{% alert note %}
Se uma etapa de mensagens for abortada em um canva, o usuário **não sairá** do canva e **prosseguirá** para a próxima etapa.
{% endalert %}

## Abortar mensagem se "Number Games Attended" = 0

Por exemplo, digamos que você não queira enviar uma mensagem aos clientes que não compareceram a um jogo:

{% raw %}
```liquid
{% if custom_attribute.${Number_Game_Attended} == 1 %}
Loved the game? Get 10% off your second one with code SAVE10.
{% elsif custom_attribute.${Number_Game Attended} > 1 %}
Love the games? Get 10% off your next one with code SAVE10.
{% else %}
{% abort_message() %}
{% endif %}
```
{% endraw %}

Essa mensagem será enviada apenas para clientes que tenham participado de um jogo.

## Envio de mensagens apenas para clientes que falam inglês

Você pode enviar mensagens apenas para clientes que falam inglês criando uma instrução "if" que corresponderá quando o idioma do cliente for o inglês e uma instrução "else" que abortará a mensagem para qualquer pessoa que não fale inglês ou não tenha um idioma em seu perfil.

{% raw %}
```liquid

{% if ${language} == 'en' %}
Send this message in English!
{% else %}
{% abort_message() %}
{% endif %}
```

Por padrão, a Braze registrará uma mensagem de erro genérica no seu registro de atividades de mensagens:

```text
{% abort_message %} called
```

Também é possível fazer com que a mensagem de abortar registre algo no Registro de atividades, incluindo uma string dentro dos parênteses:

```liquid
{% abort_message('language was nil') %}
```
{% endraw %}

![Registro de erro de mensagem no console do desenvolvedor com uma mensagem de aborto de "language was nil".][26]

## Consulta de mensagens de aborto

Você pode usar o [Query Builder]({{site.baseurl}}/user_guide/analytics/query_builder/) ou seu próprio data warehouse, se ele estiver conectado ao Braze, para consultar mensagens de aborto específicas que são disparadas quando a lógica do Liquid faz com que uma mensagem seja abortada.

[15]: {% image_buster /assets/img_archive/liquid_abort.png %}
[26]: {% image_buster /assets/img_archive/developer_console.png %}
[31]:[31]:
[32]:[32]:
[34]:{% image_buster /assets/img_archive/personalized_iflogic_.png %}
[37]:\#accounting-for-null-attribute-values
