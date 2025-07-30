---
nav_title: Criação de uma previsão de churn
article_title: Criação de uma previsão de churn
description: "Este artigo aborda como criar uma previsão de churn no dashboard do Braze."
page_order: 1.1

---

# Criação de uma previsão de churn

> Saiba como criar uma previsão de churn no dashboard do Braze.

## Etapa 1: Criar uma nova previsão

No Braze, acesse **Análises de dados** > **Predictive Churn**.

Uma previsão é uma instância de um modelo de machine learning treinado e todos os parâmetros e dados que ele usa. Nessa página, você verá uma lista das previsões ativas atuais, juntamente com algumas informações básicas sobre elas. Aqui, você pode renomear, arquivar e criar novas previsões. As previsões arquivadas são inativas e não atualizam as pontuações dos usuários. 

Para criar uma nova previsão, escolha **Criar previsão** e selecione uma nova **previsão de churn**.

{% alert note %}
Há um limite de cinco previsões de churn ativas simultaneamente. Antes da compra do Predictive Churn, o limite é de uma previsão prévia ativa de churn. Uma previsão prévia de churn não atualizará regularmente as pontuações nem permitirá o direcionamento de usuários com base no resultado da previsão. Entre em contato com o gerente da sua conta para obter detalhes.
{% endalert %}

Na página **Noções básicas** ), dê um nome exclusivo à sua nova previsão. Você também pode fornecer uma descrição opcional para fazer anotações sobre essa previsão específica.

Clique em **Avançar** para passar para a próxima etapa. Opcionalmente, você pode clicar em **Build Now** para usar todas as configurações padrão e pular para a última etapa da criação. Você terá a chance de revisar as configurações antes de iniciar o processo de compilação. Você pode retornar a qualquer etapa mais tarde, selecionando-a no rastreador de progresso na parte superior.

## Etapa 2: Definir churn

No painel **Churn Definition (Definição de rotatividade** ), use os filtros fornecidos para especificar como definir a rotatividade de usuários para sua empresa. Em outras palavras, o que um usuário precisa fazer em que período de tempo para que você o considere com churn?

Lembre-se de que não é necessário explicar quais comportamentos podem preceder o churn - apenas o que torna um usuário um usuário desistente. Pense nisso em termos de algo que um usuário faz uma vez (`do`) ou deixa de fazer (`do not`) e que constitui churn. Por exemplo, você pode considerar como churn os usuários que não abriram seu app em 7 dias. Você pode considerar a desinstalação ou eventos personalizados, como cancelar inscrição, desativar uma conta ou outros, para fazer com que um usuário se torne churn. 

#### Janela de churn

A janela de churn é o período de tempo em que um usuário executa o comportamento especificado para constituir churn. Ele pode ser configurado para até 60 dias. Essa janela é usada para consultar dados históricos para treinar a previsão. Além disso, depois que a previsão é criada e os usuários recebem pontuações, a _Pontuação de risco de churn_ indica a probabilidade de um usuário desistir dentro do número de dias especificado pela janela de churn. 

Aqui está um exemplo de uma definição simples baseada em sessões de lapso nos últimos 7 dias.

![Churn Definição em que um usuário é considerado churn se não iniciar uma sessão em 7 dias]({% image_buster /assets/img/churn/churn1.png %})

Para esse caso, selecionamos `do not` e `start a session`. Você pode combinar outros filtros com `AND` e `OR` conforme achar adequado para criar a definição de que precisa. Interessado em algumas definições potenciais de churn a serem consideradas? Você pode encontrar alguma inspiração na seção a seguir sobre [Definições de churn de amostra](#sample-definitions).

{% alert note %}
Para `do`, presumimos que os usuários ativos não tomaram a ação especificada para essa linha antes de serem churnados. A realização da ação faz com que eles se tornem com churn. <br><br>Para `do not`, consideramos usuários ativos aqueles que realizaram essa ação nos dias anteriores e depois pararam.
{% endalert %}

Abaixo da definição, você verá estimativas de quantos usuários (no passado, que churnaram e que não churnaram de acordo com sua definição) estão disponíveis. Você também verá os valores mínimos necessários. O Braze deve ter esse número mínimo de usuários disponíveis nos dados históricos para que a previsão tenha dados suficientes para aprender.

## Etapa 3: Filtrar seu público de previsão

Seu público de previsão é o grupo de usuários para o qual deseja prever o risco de churn. Por padrão, isso será definido como **All Users (Todos os usuários**), o que significa que essa previsão criará pontuações de risco de churn para todos os seus usuários ativos. Normalmente, o modelo provavelmente terá uma performance melhor se você restringir e filtrar o grupo de usuários que deseja evitar o churn com alguns critérios. Pense nos usuários específicos que são mais importantes para você e que gostaria de manter e defina-os aqui. Por exemplo, talvez você queira reter os usuários que usaram o app pela primeira vez há mais de um mês ou que já fizeram uma compra.

{% alert note %}
O público da previsão não pode exceder 100 milhões de usuários.
{% endalert %}

Quando a janela de previsão é de 14 dias ou menos, a janela de tempo para filtros que começam com "Última...", como "Último aplicativo usado" e "Última compra feita", **não pode exceder a janela de churn especificada** na definição de churn. Por exemplo, se sua definição de churn tiver uma janela de 14 dias, a janela de tempo para os filtros "Últimos..." não poderá exceder 14 dias.

#### Modo “Todos os filtros”

Para criar uma nova previsão imediatamente, somente um subconjunto de filtros de segmentação da Braze é possível. O modo de filtro completo permite que você use todos os filtros da Braze, mas exigirá uma janela de churn para criar a previsão. Por exemplo, se a janela de churn for definida como 15 dias, serão necessários 15 dias para coletar os dados de usuários e criar a previsão ao usar filtros compatíveis apenas com o modo de filtro completo. Além disso, algumas estimativas sobre o tamanho do público não estarão disponíveis no modo de filtro completo.

Para obter uma lista de exemplos de definições de público de previsão, confira nossos exemplos de definições na seção a seguir sobre [Exemplos de definições de churn](#sample-definitions).

![]({% image_buster /assets/img/churn/churn5.png %})

Assim como na página anterior, o painel inferior mostrará o número estimado de usuários históricos que resultam da definição de churn e da definição do público de previsão. Essas estimativas devem atender aos requisitos mínimos mostrados para que seja possível criar uma previsão.

## Etapa 4: Escolha a frequência de atualização para a previsão de churn

O modelo de machine learning criado quando você concluir esta página será usado em uma programação selecionada aqui para gerar novas pontuações de risco de churn. Selecione a **frequência máxima de atualizações** que você considera útil. Por exemplo, se for enviar uma promoção semanal para evitar que os usuários desistam, defina a frequência de atualização como **Weekly (Semanal** ) no dia e hora de sua escolha. 

![Cronograma de atualização da previsão definido para diariamente às 17 horas.]({% image_buster /assets/img/churn/churn2.png %})

{% alert note %}
A previsão prévia e a demonstração nunca atualizarão o risco de churn dos usuários. Além disso, as atualizações diárias para previsões exigem uma compra adicional além das atualizações semanais ou mensais com o Predictive Churn. Para adquirir essa funcionalidade, entre em contato com o gerente da sua conta.
{% endalert %}

## Etapa 5: Previsão de construção

Verifique se os detalhes que você forneceu estão corretos e selecione **Criar previsão**. Você também pode salvar suas alterações no formato de rascunho selecionando **Save As Draft** para retornar a essa página e criar o modelo posteriormente. Depois de clicar em **Criar previsão**, o processo que gera o modelo será iniciado. Isso pode levar de 30 minutos a algumas horas, dependendo do volume de dados. Para essa previsão, você verá uma página explicando que o treinamento está em andamento durante o processo de construção do modelo.

Quando isso for feito, a página mudará automaticamente para a exibição de análises de dados, e você também receberá um envio de e-mail informando que a previsão e os resultados estão prontos. No caso de um erro, a página retornará ao modo de edição com uma explicação do que deu errado.

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
- **Aqueles que correm o risco de não comprar como uma definição de churn**<br>Talvez você queira se concentrar nos clientes que navegaram, pesquisaram ou se engajaram com seu app mais recentemente. Talvez a intervenção correta de desconto impeça esse grupo mais engajado de churn.

## Previsões arquivadas

As previsões arquivadas deixarão de atualizar as pontuações dos usuários. Qualquer previsão arquivada que não esteja arquivada continuará atualizando as pontuações dos usuários em sua programação predeterminada. As previsões arquivadas nunca são excluídas e permanecem na lista.


