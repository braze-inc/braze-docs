---
nav_title: Eventos de conversão
article_title: Eventos de conversão
page_order: 5
page_type: tutorial
description: "Este artigo define os eventos de conversão, como usá-los e definir suas métricas de sucesso no Braze, e como usar essas ferramentas para ver o grau de engajamento dos seus usuários."
tool: Campaigns

---
# Eventos de conversão

> Os eventos de conversão podem ser usados para garantir que você esteja coletando informações relevantes e úteis que possam ser usadas posteriormente para obter insight para sua campanha. 

Para rastrear as métricas de engajamento e os detalhes necessários sobre como o envio de mensagens impulsiona seus KPIs, o Braze permite que você defina eventos de conversão para cada uma de suas campanhas e Canvases.

Um evento de conversão é um tipo de métrica de sucesso que rastreia se um destinatário de seu envio de mensagens realiza uma ação de alto valor em um determinado período de tempo após receber seu engajamento. Com isso, você pode começar a atribuir essas ações valiosas aos diferentes pontos de engajamento que atingem o usuário. 

Por exemplo, se estiver criando uma campanha de férias personalizada para usuários ativos, um evento de conversão de **Iniciar uma sessão** dentro de dois ou três dias pode ser apropriado, pois permitirá que você obtenha um senso de engajamento do usuário ao receber sua mensagem. Eventos adicionais como **Make Purchase**, **Upgrade App ** ou qualquer um de seus eventos personalizados podem ser selecionados como eventos de conversão.

Para saber mais sobre conversões, confira nosso [curso do Braze Learning](https://learning.braze.com/campaign-setup-delivery-targeting-conversions) sobre configuração de campanhas!

## Evento de conversão primária

O evento de conversão primária é o primeiro evento adicionado durante a criação da campanha ou do Canva. Esse evento é o que mais influencia seu engajamento e seus relatórios. Seu evento de conversão primária é usado para:

- Calcule a variação da mensagem vencedora em [campanhas][4] multivariantes ou Canvas.
- Determine a janela em que a receita é calculada para a campanha ou o Canva.
- Ajuste as distribuições de mensagens para campanhas e canvas usando a [seleção inteligente][5].

{% alert note %}
Se as mensagens forem abortadas usando a tag Liquid `abort`, apenas os usuários que passam pelas variantes são potencialmente abortados. Isso significa que as mensagens para os usuários que passam pelo grupo de controle não serão abortadas, o que pode levar a porcentagens de conversão distorcidas entre variantes e grupos de controle. Como solução alternativa, use [a segmentação]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment) para direcionar seus usuários na entrada da campanha e do Canva.
{% endalert %}

## Etapa 1: Crie uma campanha com rastreamento de conversões

[Crie uma campanha]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/creating_campaign) para seu canal de envio de mensagens desejado. Depois de configurar as mensagens e a programação da campanha, você terá a opção de adicionar até quatro eventos de conversão para rastreamento.

É altamente recomendável usar tantos eventos de conversão quantos forem necessários, pois a adição de um segundo (ou terceiro) evento de conversão pode enriquecer significativamente seus relatórios. Por exemplo, digamos que você tenha uma campanha que direciona os usuários inativos. Nesse caso, a adição de um evento de conversão secundário e do evento de conversão primária **Starts Session** pode aumentar sua compreensão sobre a eficácia da campanha em trazer os usuários de volta ao aplicativo. 

## Etapa 2: Adicionar eventos de conversão

Para cada evento de conversão que deseja rastrear, selecione o evento e o prazo de conversão.

1. Selecione o tipo geral de evento que você gostaria de usar:
  - **Inicia a sessão**: Um usuário é contado como convertido quando abre qualquer um dos apps que você especificar (o padrão é todos os apps no espaço de trabalho).
  - **Faz a compra**: Um usuário é contado como convertido quando compra o produto que você especificar (o padrão é qualquer produto).
  - **Executa o evento personalizado**: Um usuário é contado como convertido quando realiza um de seus eventos personalizados existentes (não há padrão, é necessário especificar o evento).
  - **Faça upgrade do app**: Um usuário é contado como convertido quando faz upgrade da versão do aplicativo em qualquer um dos aplicativos que você especificar (o padrão é todos os aplicativos no espaço de trabalho). O Braze realizará uma comparação numérica de melhores esforços para determinar se a mudança de versão foi um upgrade. Por exemplo, um usuário seria convertido se fizesse upgrade da versão 1.2.3 para a 1.3.0 do aplicativo, mas a Braze não registraria uma conversão se um usuário fizesse downgrade da 1.2.3 para a 1.2.2. No entanto, se o nome da versão do app contiver strings, como "1.2.3-beta2", a Braze não poderá determinar se uma alteração de versão foi um upgrade. Nessa situação, o Braze contará como uma conversão quando a versão mais recente do app do usuário for alterada.
  - **Abre e-mail**: Um usuário é contado como convertido quando abre o e-mail (somente para campanhas de e-mail).
  - **Clica no e-mail**: Um usuário é contado como convertido quando clica em um link dentro do e-mail (somente para campanhas de e-mail).<br><br>
2. Defina seu prazo de conversão. Esse é o tempo máximo que pode passar para considerar uma conversão. Você tem a opção de permitir uma janela de até 30 dias durante a qual a conversão será contada se o usuário realizar a ação especificada.  

![O tipo de evento de conversão "Makes Purchase" como exemplo para registrar conversões para usuários que fazem qualquer compra. Esse prazo de conversão é de 12 horas.][2]

Depois de selecionar seus eventos de conversão, continue o processo de criação da campanha e comece a enviar sua campanha.

## Etapa 3: Ver resultados

Acesse a página **Detalhes** para visualizar os detalhes de cada evento de conversão associado à campanha que você acabou de criar. Independentemente dos eventos de conversão selecionados, também é possível ver a receita total que pode ser atribuída a essa campanha específica, bem como a variantes específicas, durante a janela do evento de conversão primária.

{% alert note %}
Se não houver eventos de conversão selecionados durante a criação da campanha, o tempo padrão será de três dias.
{% endalert %}

Além disso, para mensagens multivariantes, é possível ver o número de conversões e as porcentagens de conversão do grupo de controle e de cada variante.

![][3]

## Regras de rastreamento de conversões

Os eventos de conversão permitem atribuir a ação do usuário a um ponto de engajamento. Dito isso, há alguns aspectos a serem notados com relação ao modo como a Braze lida com várias conversões. Confira os cenários a seguir para entender como o Braze rastreia essas conversões:

- As conversões ocorrem por usuário, não por dispositivo. Isso significa que um usuário só pode converter uma vez, mesmo que uma mensagem seja enviada para vários dispositivos. Como outro exemplo, suponha que uma campanha tenha apenas um evento de conversão, que é "Faz qualquer compra". Se um usuário que receber essa campanha fizer duas compras separadas dentro do prazo de conversão, apenas uma conversão será contabilizada.
- Se um usuário realizar um evento de conversão dentro dos prazos de conversão de duas campanhas ou Canvas separados que ele recebeu, a conversão será registrada em ambos.
- Um usuário será contado como convertido se tiver realizado o evento de conversão específico na janela, mesmo que não tenha aberto ou clicado na mensagem.

[2]: {% image_buster /assets/img_archive/conversion_event_selection.png %}
[3]: {% image_buster /assets/img_archive/conversion_event_details.png %}
[4]: {{site.baseurl}}/user_guide/engajamento_tools/testing/multivariant_testing/#multivariate-and-ab-testing
[5]: {{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/
