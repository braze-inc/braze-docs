---
nav_title: Criação de uma previsão de evento
article_title: Criação de uma previsão de evento
page_order: 1.1
description: "Este artigo aborda como criar uma previsão de evento no painel do Braze."

---

# Criação de uma previsão de evento

> Uma previsão é uma instância de um modelo de aprendizado de máquina treinado e todos os parâmetros e dados que ele usa. Para saber mais sobre os Predictive Events, consulte a [visão geral dos Predictive Events]({{site.baseurl}}/user_guide/brazeai//predictive_events/).

No Braze, vá para **Analytics** > **Predictive Events**.

Nessa página, você verá uma lista das previsões de eventos ativos atuais e algumas informações básicas sobre eles. Aqui, você pode renomear, arquivar e criar novas previsões. As previsões arquivadas são inativas e não atualizam as pontuações dos usuários.

## Etapa 1: Criar uma nova previsão

1. Selecione **Criar previsão** e marque uma nova **previsão de evento**.

{% alert note %}
Há um limite de cinco previsões ativas ao mesmo tempo. Antes de comprar eventos preditivos, o limite é uma previsão de visualização ativa. Uma previsão de visualização não atualizará regularmente as pontuações nem direcionará os usuários com base no resultado da previsão. Entre em contato com o gerente da sua conta para obter detalhes.
{% endalert %}

{: start="2"}
2\. Dê um nome exclusivo à sua previsão. Você também pode fornecer uma descrição para salvar quaisquer anotações relevantes.

\![]({% image_buster /assets/img/purchasePrediction/purchases_step1.png %})

{: start="3"}
3\. Clique em **Forward (Avançar** ) para passar para a próxima etapa. <br><br>Opcionalmente, você pode clicar em **Build Now** para usar todas as configurações padrão e pular para a última etapa da criação. Você terá a chance de revisar as configurações antes de iniciar o processo de compilação. Além disso, você pode retornar a qualquer etapa posteriormente clicando nela na barra superior.

## Etapa 2: Especificar o rastreamento de eventos {#event-tracking}

Especifique se os eventos de seus usuários são armazenados no Braze como [eventos de compra]({{site.baseurl}}/user_guide/data/custom_data/purchase_events/) ou [eventos personalizados]({{site.baseurl}}/user_guide/data/custom_data/custom_events/).

Aqui, você verá se o método selecionado fornece dados suficientes para que o Braze crie um modelo de aprendizado de máquina. Se o requisito não for atendido, tente selecionar o outro método de registro se ele também for usado pelo seu aplicativo. Infelizmente, se não for, o Braze não conseguirá criar uma previsão com a quantidade de dados disponíveis. Se achar que está vendo esse erro incorretamente, entre em contato com seu gerente de sucesso do cliente.

#### Janela de eventos

A janela do evento é o período de tempo em que se deseja prever se um usuário realizará o evento. Ele pode ser configurado para até 60 dias. Essa janela é usada para consultar dados históricos para treinar a previsão. Além disso, depois que a previsão é criada e os usuários recebem pontuações, a pontuação de probabilidade indica a probabilidade de um usuário realizar o evento dentro do número de dias especificado pela janela do evento.

### Etapa 3: Filtrar seu público-alvo de previsão (opcional) {#audience}

Seu público-alvo de previsão é o grupo de usuários cuja pontuação de probabilidade você gostaria de prever. Se desejar, você pode executar uma previsão em toda a sua população de usuários. Para fazer isso, deixe a opção padrão **All Users (Todos os usuários** ) selecionada.

Dependendo do seu caso de uso, talvez você queira usar filtros para especificar os usuários que deseja avaliar para o modelo. Para isso, selecione **Definir meu próprio público de previsão** e escolha seus filtros de público. Por exemplo, talvez você queira se concentrar nos usuários que usam seu aplicativo há pelo menos 30 dias, selecionando o filtro "First Used App" (Primeiro aplicativo usado) definido como 30 dias. A configuração desse público informa ao Braze que você deseja que seu modelo aprenda especificamente com os usuários que (no momento em que o modelo for executado) tenham usado o aplicativo por pelo menos 30 dias.

O público-alvo da previsão define o grupo de usuários que o modelo de aprendizado de máquina analisa para aprender com o passado. O Braze mostrará o tamanho estimado do seu público-alvo de previsão. Se você especificar o público desejado e não atingir o mínimo necessário para executar o modelo, tente especificar um filtro mais amplo ou use a opção **Todos os usuários**. Lembre-se de que muitos casos de uso não exigem que você selecione um público-alvo de previsão específico. Por exemplo, se o seu caso de uso for direcionar os usuários da região da UE com maior probabilidade de rotatividade, você poderá executar o modelo em todos os usuários e incluir um filtro para a região da UE no segmento da campanha.

{% alert note %}
O público-alvo da previsão não pode exceder 100 milhões de usuários.
{% endalert %}

Quando a janela de eventos é de 14 dias ou menos, a janela de tempo para filtros que começam com "Last..." (Última...), como "Last Used App" (Último aplicativo usado) e "Last Made Purchase" (Última compra feita), **não pode exceder a janela de eventos especificada no [rastreamento de eventos](#event-tracking)**. Por exemplo, se a janela de eventos estiver definida como 14 dias, a janela de tempo para os filtros "Last..." não poderá exceder 14 dias.

#### Modo de filtro completo

Para criar uma nova previsão imediatamente, somente um subconjunto de filtros de segmentação do Braze é compatível. O modo de filtro completo permite que você use todos os filtros do Braze, mas exigirá uma janela de eventos para criar a previsão. 

Por exemplo, se a janela de eventos for definida como 14 dias, serão necessários 14 dias para coletar os dados do usuário e criar a previsão ao usar filtros compatíveis apenas com o modo de filtro completo. Além disso, algumas estimativas sobre o tamanho do público não estarão disponíveis no modo de filtro completo.

### Etapa 4: Escolha o cronograma de atualização

O modelo de aprendizado de máquina gerará pontuações de probabilidade de eventos para os usuários, e essas pontuações serão atualizadas com base na programação que você selecionar aqui. Você poderá segmentar usuários com base na pontuação de probabilidade de eventos. 

Selecione a **frequência máxima de atualizações** que você considera útil. Por exemplo, se estiver prevendo compras e planejando enviar uma promoção semanal, defina a frequência de atualização como **Weekly (Semanal** ) no dia e hora de sua escolha.

{% alert note %}
A previsão de visualização e demonstração nunca atualizará as pontuações de probabilidade dos usuários.
{% endalert %}

### Etapa 5: Previsão de construção

Verifique se os detalhes que você forneceu estão corretos e selecione **Build Prediction (Criar previsão**). Você também pode salvar suas alterações no formato de rascunho selecionando **Save As Draft** para retornar a essa página e criar o modelo posteriormente. 

Depois de clicar em **Build Prediction (Criar previsão)**, o processo que gera o modelo será iniciado. Isso pode levar de 30 minutos a algumas horas, dependendo do volume de dados. Para essa previsão, você verá uma página explicando que o treinamento está em andamento durante o processo de criação do modelo. O modelo Braze leva em conta eventos personalizados, eventos de compra, eventos de interação de campanha e dados de sessão.

Quando concluída, a página mudará automaticamente para a exibição de análise, e você receberá um e-mail informando que a previsão e os resultados estão prontos. No caso de um erro, a página retornará ao modo de edição com uma explicação do que deu errado.

A previsão será automaticamente reconstruída ("retreinada") a cada **duas semanas** para mantê-la atualizada com os dados mais recentes disponíveis. Observe que esse é um processo separado de quando as pontuações de probabilidade dos usuários, o resultado da previsão, são produzidas. A última é determinada pela frequência de atualização que você escolheu na Etapa 4.

## Previsões arquivadas

As previsões arquivadas deixarão de atualizar as pontuações dos usuários. Qualquer previsão arquivada que não esteja arquivada continuará atualizando as pontuações dos usuários em sua programação predeterminada. As previsões arquivadas nunca são excluídas e permanecem na lista.


