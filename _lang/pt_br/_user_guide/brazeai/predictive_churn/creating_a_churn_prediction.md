---
nav_title: Crie uma previsão de churn
article_title: Crie uma Previsão de Churn
description: "Este artigo aborda como criar uma previsão de churn no dashboard do Braze."
page_order: 1.1

---

# Crie uma previsão de churn

> Saiba como criar uma previsão de churn no dashboard do Braze.

## Etapa 1: Criar uma nova previsão

No Braze, acesse **Análises de dados** > **Predictive Churn**.

Uma previsão é uma instância de um modelo de machine learning treinado e todos os parâmetros e dados que ele usa. Nessa página, você verá uma lista das previsões ativas atuais, juntamente com algumas informações básicas sobre elas. Aqui, você pode renomear, arquivar e criar novas previsões. As previsões arquivadas são inativas e não atualizam as pontuações dos usuários. 

Para criar uma nova previsão, escolha **Criar previsão** e selecione uma nova **previsão de churn**.

{% alert note %}
Há um limite de cinco previsões de churn ativas simultaneamente. Antes de comprar a Previsão Preditiva de Churn, o limite é uma previsão de churn em prévia ativa. Uma previsão prévia de churn não atualizará regularmente as pontuações nem permitirá o direcionamento de usuários com base no resultado da previsão. Entre em contato com o gerente da sua conta para obter detalhes.
{% endalert %}

Na página **Noções básicas** ), dê um nome exclusivo à sua nova previsão. Você também pode fornecer uma descrição opcional para fazer anotações sobre essa previsão específica.

Selecione **Avançar** para ir para a próxima etapa. Opcionalmente, você pode selecionar **Construir Agora** para usar todas as configurações padrão e pular para a última etapa de criação. Você terá a oportunidade de revisar as configurações antes de iniciar o processo de construção. Você pode retornar a qualquer etapa mais tarde selecionando-a no rastreador de progresso.

## Etapa 2: Definir churn

No painel **Churn Definition (Definição de rotatividade** ), use os filtros fornecidos para especificar como definir a rotatividade de usuários para sua empresa. Em outras palavras, o que um usuário precisa fazer em que período de tempo para que você o considere com churn?

Lembre-se de que não é necessário explicar quais comportamentos podem preceder o churn - apenas o que torna um usuário um usuário desistente. Pense nisso em termos de algo que um usuário faz uma vez (`do`) ou deixa de fazer (`do not`) e que constitui churn. Por exemplo, você pode considerar como churn os usuários que não abriram seu app em 7 dias. Você pode considerar a desinstalação ou eventos personalizados, como cancelar inscrição, desativar uma conta ou outros, para fazer com que um usuário se torne churn. 

#### Janela de churn

A janela de churn é o período em que a atividade de um usuário atende aos critérios para churn. Você pode configurá-la para até 60 dias, dependendo dos dados disponíveis. Esta janela é usada para puxar dados históricos para treinar sua previsão. Uma vez que a previsão é construída, você verá se havia dados suficientes para resultados precisos.

Após a construção da previsão e os usuários receberem pontuações, o _Score de Risco de Churn_ mostra quão provável é que um usuário churne dentro do período que você definiu na janela de churn. 

Aqui está um exemplo de uma definição simples baseada em sessões de lapso nos últimos 7 dias.

![Churn Definition (Definição de rotatividade), em que um usuário é considerado churn se não iniciar uma sessão em 7 dias]({% image_buster /assets/img/churn/churn1.png %})

Para esse caso, selecionamos `do not` e `start a session`. Você pode combinar outros filtros com `AND` e `OR` conforme achar adequado para criar a definição de que precisa. Interessado em algumas definições potenciais de churn a serem consideradas? Você pode encontrar alguma inspiração na seção a seguir sobre [Definições de churn de amostra](#sample-definitions).

{% alert note %}
Para `do`, assumimos que os usuários ativos não tomaram a ação que você especifica para esta linha antes de se tornarem churned. A realização da ação faz com que eles se tornem com churn. <br><br>Para `do not`, consideramos usuários ativos aqueles que realizaram essa ação nos dias anteriores e depois pararam. <br><br>**Exemplo:** Se churn é definido como "não comprou nos últimos 60 dias", consideramos usuários ativos aqueles que compraram nos últimos 60 dias. Como resultado, qualquer um que não fez uma compra nos últimos 60 dias não é considerado um usuário ativo. Isso significa que um público de churn criado a partir dessa definição de churn incluiria apenas usuários que compraram nos últimos 60 dias. Isso pode fazer com que o público preditivo de churn resultante pareça significativamente menor do que a população original— a maioria dos usuários em um espaço de trabalho pode já atender à definição de churn e, portanto, não estar ativa na previsão de churn.
{% endalert %}

Abaixo da definição, você verá estimativas de quantos usuários (no passado, que churnaram e que não churnaram de acordo com sua definição) estão disponíveis. Você também verá os valores mínimos necessários. O Braze deve ter esse número mínimo de usuários disponíveis nos dados históricos para que a previsão tenha dados suficientes para aprender.

## Etapa 3: Filtrar seu público de previsão

Seu público de previsão é o grupo de usuários para os quais você deseja prever o risco de churn. O público de previsão define o grupo de usuários que o modelo de machine learning analisa para aprender com o passado. Por padrão, isso é definido como **Todos os Usuários**, o que significa que esta previsão criará pontuações de risco de churn para todos os seus usuários ativos (consulte a nota anterior para saber quem é considerado ativo para um modelo de churn).

Dependendo do seu caso de uso, você pode querer usar filtros para especificar os usuários que deseja avaliar para o modelo. Para fazer isso, selecione **Definir meu próprio público de previsão** e escolha seus filtros de público. Por exemplo, se você é um aplicativo de viagem por aplicativo com motoristas e passageiros em sua base de usuários, e está construindo um modelo de churn para passageiros, você vai querer filtrar seu público de previsão apenas para passageiros. Tenha em mente que muitos casos de uso não exigem que você selecione um público de previsão específico. Por exemplo, se seu caso de uso é direcionar usuários na região da UE que são mais propensos a churn, você pode executar seu modelo em todos os usuários e, em seguida, simplesmente incluir um filtro para a região da UE no segmento da campanha.

Braze mostrará o tamanho estimado do seu público de previsão. Se você especificar seu público desejado e não atender ao mínimo necessário para executar o modelo, tente especificar um filtro mais amplo ou use a opção **Todos os Usuários**. Observe que o tamanho do seu grupo "todos os usuários" não é estático e varia de modelo para modelo, pois leva em conta sua definição de churn. Por exemplo, digamos que a definição de churn é **não** fazer uma compra em 30 dias; neste caso, Braze executa o modelo em usuários que **fizeram** uma compra nos últimos 30 dias (e prevê a probabilidade de que eles **não** comprem nos próximos 30 dias), então esses são os usuários refletidos na métrica "todos os usuários".

{% alert note %}
O público da previsão não pode exceder 100 milhões de usuários.
{% endalert %}

Quando a janela de previsão é de 14 dias ou menos, a janela de tempo para filtros que começam com "Último...", como "Último Uso do App" e "Última Compra Feita" **não pode exceder a Janela de Churn especificada** na definição de churn. Por exemplo, se sua definição de churn tiver uma janela de 14 dias, a janela de tempo para os filtros "Últimos..." não poderá exceder 14 dias. 

A janela de churn é avaliada olhando para trás no número de dias a partir do dia em que o modelo foi executado pela última vez, então se a janela de churn é de 15 dias e o modelo foi executado pela última vez em 1º de dezembro, o modelo analisa de 16 de novembro a 30 de novembro para entender a atividade do usuário para elegibilidade do público e treinamento.

#### Modo “Todos os filtros”

Para construir uma nova previsão imediatamente, apenas um subconjunto de filtros de segmentação do Braze é suportado. O Modo de Filtro Completo permite que você use todos os filtros do Braze, mas exigirá uma janela de churn para construir a previsão. Por exemplo, se a janela de churn for definida como 15 dias, serão necessários 15 dias para coletar os dados de usuários e criar a previsão ao usar filtros compatíveis apenas com o modo de filtro completo. Além disso, algumas estimativas sobre o tamanho do público não estarão disponíveis no modo de filtro completo.

Para obter uma lista de exemplos de definições de público de previsão, confira nossos exemplos de definições na seção a seguir sobre [Exemplos de definições de churn](#sample-definitions).

![]({% image_buster /assets/img/churn/churn5.png %})

Assim como na página anterior, o painel inferior mostrará o número estimado de usuários históricos que resultam da definição de churn e da definição do público de previsão. Essas estimativas devem atender aos requisitos mínimos mostrados para que seja possível criar uma previsão.

## Etapa 4: Escolha a frequência de atualização para a previsão de churn

O modelo de machine learning gerará pontuações de probabilidade de eventos para os usuários, e essas pontuações serão atualizadas com base na programação que você selecionar aqui. Você poderá direcionar usuários com base em sua pontuação de probabilidade de eventos. 

Selecione a **frequência máxima de atualizações** que você considera útil. Por exemplo, se for enviar uma promoção semanal para evitar que os usuários desistam, defina a frequência de atualização como **Weekly (Semanal** ) no dia e hora de sua escolha. 

![Cronograma de atualização da previsão definido para diariamente às 17 horas.]({% image_buster /assets/img/churn/churn2.png %})

{% alert note %}
A previsão prévia e a demonstração nunca atualizarão o risco de churn dos usuários. Além disso, as atualizações diárias para previsões exigem uma compra adicional além das atualizações semanais ou mensais com o Predictive Churn. Para adquirir essa funcionalidade, entre em contato com o gerente da sua conta.
{% endalert %}

## Etapa 5: Previsão de construção

Verifique se os detalhes que você forneceu estão corretos e selecione **Criar previsão**. Você também pode salvar suas alterações no formato de rascunho selecionando **Save As Draft** para retornar a essa página e criar o modelo posteriormente. Depois de selecionar **Construir Previsão**, o processo que gera o modelo começará. Isso pode levar de 30 minutos a algumas horas, dependendo do volume de dados. Para esta previsão, você verá uma página explicando que o treinamento está em andamento durante a duração do processo de construção do modelo. O modelo Braze leva em conta eventos personalizados, eventos de compra, eventos de interação de campanha e dados de sessão.

Depois que terminar, a página mudará automaticamente para a visualização de análise, e você também receberá um e-mail informando que a previsão e os resultados estão prontos. No caso de um erro, a página retornará ao modo de edição com uma explicação do que deu errado.

A previsão será reconstruída ("retreinada") novamente a cada **duas semanas automaticamente** para mantê-la atualizada com os dados mais recentes disponíveis. Note que esse é um processo separado de quando as _pontuações de risco de churn_ dos usuários, o resultado da previsão, são produzidas. O último é determinado pela frequência de atualização que você escolheu na etapa 4.

## Exemplo de definições de público de churn e previsão {#sample-definitions}

**Exemplo de definições de churn**<br>
- "Dentro de 7 dias, faça o evento personalizado 'Cancelamento de inscrição'"<br>
- "Dentro de 30 dias, faça o evento personalizado "Período de teste expirou"<br>
- "Em um dia, faça a desinstalação." <br>
- "Dentro de 14 dias, não faça uma compra." <br>

Para as definições de churn que descrevemos, pode haver algumas definições de público de previsão correspondentes:<br>
- **Iniciou a inscrição há mais de duas semanas OU Iniciou a inscrição há menos de duas semanas**<br>Nesse caso, talvez você queira criar duas previsões e enviar mensagens aos novos assinantes de forma diferente dos assinantes de longo prazo. Você também poderia definir isso como "Primeira compra feita há mais de 30 dias".<br>
- **Desinstaladores**<br>Você pode se concentrar nos clientes que compraram algo no passado recente ou que usaram o app muito recentemente.<br>
- **Aqueles que correm o risco de não comprar como uma definição de churn**<br>Você pode querer se concentrar em clientes que têm navegado ou pesquisado, ou interagido com seu aplicativo mais recentemente. Talvez a intervenção correta de desconto impeça esse grupo mais engajado de churn.

## Previsões arquivadas

As previsões arquivadas deixarão de atualizar as pontuações dos usuários. Qualquer previsão arquivada que não esteja arquivada continuará atualizando as pontuações dos usuários em sua programação predeterminada. As previsões arquivadas nunca são excluídas e permanecem na lista.


