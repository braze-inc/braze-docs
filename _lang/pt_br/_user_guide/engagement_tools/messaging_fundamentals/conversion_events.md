---
nav_title: Eventos de conversão
article_title: Eventos de conversão
page_order: 4
page_type: reference
description: "Este artigo de referência define eventos de conversão, como usá-los para definir suas métricas de sucesso no Braze e como usar esses eventos para ver o grau de engajamento de seus usuários."
tool:
    - Campaigns
    - Canvas
---

# Eventos de conversão

> Um evento de conversão é um tipo de métrica de sucesso que rastreia se um destinatário de seu envio de mensagens realiza uma ação de alto valor em um determinado período de tempo após receber seu engajamento. Use esses eventos para se certificar de que está coletando informações relevantes e úteis que poderão ser usadas posteriormente para obter insight para sua campanha ou Canva.

## Como funciona?

Digamos que você esteja criando uma campanha de férias personalizada para usuários ativos, um evento de conversão de **Iniciar uma sessão** dentro de dois ou três dias pode ser apropriado, pois permitirá que você obtenha um senso de engajamento do usuário ao receber sua mensagem. Eventos adicionais como **Make Purchase**, **Upgrade App ** ou qualquer um de seus eventos personalizados podem ser selecionados como eventos de conversão.

{% alert tip %}
Para saber mais sobre conversões, confira nosso [curso do Braze Learning](https://learning.braze.com/campaign-setup-delivery-targeting-conversions) sobre configuração de campanhas.
{% endalert %}

### Regras de rastreamento de conversões

Os eventos de conversão permitem atribuir a ação do usuário a um ponto de engajamento. Dito isso, há alguns aspectos a serem notados com relação ao modo como a Braze lida com várias conversões. Confira os cenários a seguir para entender como o Braze rastreia essas conversões:

- As conversões ocorrem por usuário, não por dispositivo. Isso significa que um usuário só pode converter uma vez, mesmo que uma mensagem seja enviada para vários dispositivos. Como outro exemplo, suponha que uma campanha tenha apenas um evento de conversão, que é "Faz qualquer compra". Se um usuário que receber essa campanha fizer duas compras separadas dentro do prazo de conversão, apenas uma conversão será contabilizada.
- Se um usuário realizar um evento de conversão dentro dos prazos de conversão de duas campanhas ou Canvas separados que ele recebeu, a conversão será registrada em ambos.
- Um usuário será contado como convertido se tiver realizado o evento de conversão específico na janela, mesmo que não tenha aberto ou clicado na mensagem.

### Evento de conversão primária

O evento de conversão primária é o primeiro evento adicionado durante a criação da campanha ou do Canva. Esse evento é o que mais influencia seu engajamento e seus relatórios. Seu evento de conversão primária é usado para:

- Calcule a variação da mensagem vencedora em campanhas [multivariantes]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/#multivariate-and-ab-testing) ou Canvas.
- Determine a janela em que a receita é calculada para a campanha ou o Canva.
- Ajuste as distribuições de mensagens para campanhas e Canvas usando o [Intelligent Selection]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/).

{% alert note %}
Se as mensagens forem abortadas usando a tag Liquid `abort`, apenas os usuários que passam pelas variantes são potencialmente abortados. Isso significa que as mensagens para os usuários que passam pelo grupo de controle não serão abortadas, o que pode levar a porcentagens de conversão distorcidas entre variantes e grupos de controle. Como solução alternativa, use [a segmentação]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment) para direcionar seus usuários na entrada da campanha e do Canva.
{% endalert %}

## Criação de uma campanha com rastreamento de conversões

### Etapa 1: Configure sua campanha

[Crie uma campanha]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/creating_campaign) para seu canal de envio de mensagens desejado. Depois de configurar as mensagens e a programação da campanha, você terá a opção de adicionar até quatro eventos de conversão para rastreamento.

Recomendamos o uso de tantos eventos de conversão quantos forem necessários, pois a adição de um segundo (ou terceiro) evento de conversão pode enriquecer significativamente seus relatórios. Por exemplo, digamos que você tenha uma campanha que direciona os usuários inativos. Nesse caso, a adição de um evento de conversão secundário e do evento de conversão primária **Starts Session** pode aumentar sua compreensão sobre a eficácia da campanha em trazer os usuários de volta ao aplicativo. 

### Etapa 2: Adicionar os eventos de conversão

Primeiro, selecione o tipo geral de evento que você gostaria de usar:

| Tipo de evento de conversão         | Descrição                                                                                                                                                                                                                                                                                                                                 |
|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Inicia sessão**      | Um usuário é contado como convertido quando abre qualquer um dos apps que você especificar (o padrão é todos os apps no espaço de trabalho).                                                                                                                                                                                                         |
| **Faz compra**      | Um usuário é contado como convertido quando compra o produto que você especificar (o padrão é qualquer produto).                                                                                                                                                                                                                                 |
| **Realiza evento personalizado** | Um usuário é contado como convertido quando realiza um de seus eventos personalizados existentes (não há padrão, é necessário especificar o evento).                                                                                                                                                                                                        |
| **Faz upgrade de app**         | Um usuário é contado como convertido quando faz upgrade da versão do aplicativo em qualquer um dos aplicativos que você especificar (o padrão é todos os aplicativos no espaço de trabalho). O Braze realiza uma comparação numérica de melhores esforços para determinar se a alteração foi um upgrade. Versões não numéricas são contadas como conversões se a versão for alterada.              |
| **Abre e-mail**         | Um usuário é contado como convertido quando abre o e-mail (somente para campanhas de e-mail).                                                                                                                                                                                                                                                 |
| **Clica no e-mail**        | Um usuário é contado como convertido quando clica em um link dentro do e-mail (somente para campanhas de e-mail).                                                                                                                                                                                                                                  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

Defina seu prazo de conversão. Esse é o tempo máximo que pode passar para considerar uma conversão. Você tem a opção de permitir uma janela de até 30 dias durante a qual a conversão será contada se o usuário realizar a ação especificada.

![O tipo de evento de conversão "Makes Purchase" como exemplo para registrar conversões para usuários que fazem qualquer compra. Esse prazo de conversão é de 12 horas.]({% image_buster /assets/img_archive/conversion_event_selection.png %})

Depois de selecionar seus eventos de conversão, continue o processo de criação da campanha e comece a enviar sua campanha.

### Etapa 3: Veja seus resultados

Acesse a página **Detalhes** para visualizar os detalhes de cada evento de conversão associado à campanha que você acabou de criar. Independentemente dos eventos de conversão selecionados, também é possível ver a receita total que pode ser atribuída a essa campanha específica, bem como a variantes específicas, durante a janela do evento de conversão primária.

{% alert note %}
Se não houver eventos de conversão selecionados durante a criação da campanha, o tempo padrão será de três dias.
{% endalert %}

Além disso, para mensagens multivariantes, é possível ver o número de conversões e as porcentagens de conversão do grupo de controle e de cada variante.

![Quatro eventos de conversão que rastreiam as conversões com base em quando uma compra foi feita dentro de três horas, fez uma compra dentro de duas horas, iniciou uma sessão dentro de 30 minutos e iniciou uma sessão dentro de 25 minutos.]({% image_buster /assets/img_archive/conversion_event_details.png %})


