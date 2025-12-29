---
nav_title: Abortar mensagens
article_title: Interrupção de mensagens líquidas
page_order: 7
description: "Este artigo de referência aborda a interrupção de mensagens Liquid e alguns exemplos de casos de uso."

---

# Abortar mensagens

> Opcionalmente, você pode usar a tag `abort_message("optional reason for aborting")` Liquid message nas condicionais para impedir o envio de uma mensagem a um usuário. Este artigo de referência lista alguns exemplos de como esse recurso pode ser usado em campanhas de marketing.

{% alert note %}
Se uma etapa de mensagem for abortada em um Canvas, o usuário **não sairá** do Canvas e **prosseguirá** para a próxima etapa.
{% endalert %}

## Mensagem de cancelamento se "Number Games Attended" = 0

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

## Mensagem Somente para clientes que falam inglês

Você pode enviar mensagens apenas para clientes que falam inglês criando uma instrução "if" que corresponderá quando o idioma do cliente for o inglês e uma instrução "else" que interromperá a mensagem para qualquer pessoa que não fale inglês ou não tenha um idioma em seu perfil.

{% raw %}
```liquid

{% if ${language} == 'en' %}
Send this message in English!
{% else %}
{% abort_message() %}
{% endif %}
```

Por padrão, o Braze registrará uma mensagem de erro genérica no seu Registro de Atividades de Mensagens:

```text
{% abort_message %} called
```

Também é possível fazer com que a mensagem de abortar registre algo no Message Activity Log incluindo uma cadeia de caracteres dentro dos parênteses:

```liquid
{% abort_message('language was nil') %}
```
{% endraw %}

\![Registro de erro de mensagem no Console do desenvolvedor com uma mensagem de interrupção de "o idioma era nulo".]({% image_buster /assets/img_archive/developer_console.png %})

## Consulta de mensagens de abortamento

Você pode usar o [Query Builder]({{site.baseurl}}/user_guide/analytics/query_builder/) ou seu próprio data warehouse, se ele estiver conectado ao Braze, para consultar mensagens de abortamento específicas que são acionadas quando a lógica do Liquid faz com que uma mensagem seja abortada.

## Considerações

A tag de mensagem `abort_message()` Liquid impede que as mensagens sejam enviadas aos usuários, o que significa que a mensagem não será exibida nos perfis dos usuários e não contará para entregas ou limite de frequência.
