---
nav_title: Códigos promocionais
article_title: Códigos de promoção
page_order: 5
toc_headers: h2
alias: "/promotion_codes/"
description: "Aprenda sobre listas de códigos promocionais, para que você possa adicioná-los às suas campanhas e Canvases."
---

# Códigos promocionais

> Aprenda sobre listas de códigos promocionais, para que você possa adicioná-los às suas campanhas e Canvases.

## Sobre os códigos promocionais

Códigos promocionais permitem que você insira valores únicos e limitados no tempo em mensagens para impulsionar conversões. Cada lista pode conter até 20 milhões de códigos, e cada código pode durar até seis meses antes de expirar.

Quando a Braze envia uma mensagem com um código promocional, o código é deduzido antes que a mensagem seja enviada. Para garantir que os códigos sejam consistentes, únicos e nunca reutilizados:

- Uma mensagem falhada ainda consome o código.
- Em envios multicanal, o mesmo código é aplicado em todos os canais.
- Com Liquid condicional, todas as listas referenciadas têm códigos deduzidos, mesmo que apenas um ramo seja mostrado.
- Entrar ou reentrar em uma etapa do Canvas consome um novo código.

Se você colocar vários trechos da mesma lista em uma mensagem, a Braze aplicará o mesmo código em todos os trechos. Para evitar ficar sem códigos, recomendamos fazer o upload de mais códigos do que você espera usar.

{% tabs local %}
{% tab Example %}
Pense em códigos promocionais como cupons em um correio. Uma vez que o funcionário retira um cupom da pilha para sua carta, ele desaparece—mesmo que a carta nunca chegue.  

Por exemplo, no seguinte Liquid condicional, os códigos de ambas as listas (`vip-deal` e `regular-deal`) são deduzidos, mesmo que cada usuário veja apenas um ramo:

{% raw %}
```liquid
{% if user.is_vip %}
  {% promotion('vip-deal') %}
{% else %}
  {% promotion('regular-deal') %}
{% endif %}
```
{% endraw %}
{% endtab %}
{% endtabs %}

{% alert important %}
Códigos promocionais não podem ser enviados em mensagens dentro do aplicativo no Canvas.
{% endalert %}

## Próximos passos

Procurando os próximos passos? Comece aqui:

- [Criando uma lista de códigos promocionais]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes/create/)
- [Usando códigos promocionais]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes/manage/#using-promotion-codes)
- [Visualizando o uso de códigos promocionais]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes/manage/#viewing-promotion-code-usage)

## Perguntas frequentes

### Quais canais de envio de mensagens posso usar com códigos promocionais?

Os códigos de promoção são atualmente aceitos para e-mail, push móvel, web push, Cartões de Conteúdo, webhook, SMS e WhatsApp. As campanhas de e-mail de transação da Braze e as mensagens no app atualmente não suportam códigos promocionais.

### Os envios de teste e sementes contam para o uso?

Por padrão, os envios de teste e os envios de e-mail do grupo de teste usarão códigos de promoção por usuário, por envio de teste. No entanto, você pode entrar em contato com seu gerente de conta da Braze para atualizar esse comportamento e não usar códigos promocionais durante os testes.

### O que acontece quando vários canais de envio de mensagens usam o mesmo trecho de código promocional?

Se um usuário específico for elegível para receber um código através de vários canais, ele receberá o mesmo código em cada canal. Apenas um código promocional será usado, independentemente dos canais recebidos.

### Posso usar vários trechos Liquid para referenciar a mesma lista de códigos promocionais em uma mensagem?

Sim. A Braze aplicará o mesmo código promocional em todas as instâncias desse trecho na mensagem, garantindo que o usuário receba apenas um código único.

### O que acontece quando uma lista de códigos de promoção está expirada ou vazia?

Códigos expirados são excluídos após seis meses.

Se a mensagem deveria ter contido um código de promoção de uma lista vazia ou expirada, a mensagem será cancelada. 

Se a mensagem contiver lógica Liquid que insere condicionalmente um código de promoção, a mensagem só será cancelada se ela deveria ter contido um código de promoção. Se a mensagem não deveria conter um código promocional, a mensagem será enviada normalmente.

### Se eu carreguei os códigos promocionais errados, posso atualizá-los?

Sim. Você pode resolver isso descontinuando toda a lista ou usando um espaço reservado para excluir a lista. Para saber mais, veja [Atualizando uma lista de códigos promocionais]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes/create/#updating-a-promotion-code-list).

### Posso salvar um código promocional no perfil de um usuário para mensagens futuras?

Sim. Você pode salvar códigos promocionais no perfil de um usuário através de uma etapa de Atualização de Usuário. Para saber mais, veja [Salvando códigos promocionais em perfis de usuários]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes/manage/#save-to-profile).
