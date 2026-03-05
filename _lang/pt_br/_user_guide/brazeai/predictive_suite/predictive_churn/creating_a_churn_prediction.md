---
nav_title: Criar uma previsão de churn
article_title: Criar uma previsão de churn
description: "Este artigo aborda como criar uma previsão de churn no dashboard da Braze."
page_order: 1.1

---

# Criar uma previsão de churn

> Saiba como criar uma previsão de churn no dashboard da Braze.

## Etapa 1: Criar uma nova previsão

Na Braze, acesse **Análise de dados** > **Predictive Churn**.

Uma previsão é uma instância de um modelo de machine learning treinado e todos os parâmetros e dados que ele utiliza. Nesta página, você verá uma lista das previsões ativas atuais junto com algumas informações básicas sobre elas. Aqui, você pode renomear, arquivar e criar novas previsões. Previsões arquivadas ficam inativas e não atualizam as pontuações dos usuários.

Para criar uma nova previsão, selecione **Criar previsão** e escolha uma nova **Previsão de churn**.

{% alert note %}
Há um limite de cinco previsões de churn ativas simultaneamente. Antes de adquirir o Predictive Churn, o limite é de uma prévia ativa de previsão de churn. Uma prévia de previsão de churn não atualizará regularmente as pontuações nem permitirá que você direcione usuários com base no resultado da previsão. Fale com seu gerente de conta para mais informações.
{% endalert %}

Na página **Básico**, dê um nome exclusivo à sua nova previsão. Você também pode fornecer uma descrição opcional para registrar quaisquer observações sobre essa previsão específica.

Selecione **Avançar** para ir para a próxima etapa. Opcionalmente, você pode selecionar **Criar agora** para usar todas as configurações padrão e pular para a última etapa da criação. Você terá a oportunidade de revisar as configurações antes de iniciar o processo de criação. Você pode voltar a qualquer etapa posteriormente selecionando-a no indicador de progresso.

## Etapa 2: Definir o churn

No painel **Definição de churn**, use os filtros fornecidos para especificar como você define o churn de usuários para o seu negócio. Em outras palavras, o que um usuário precisa fazer em qual período para que você o considere um usuário desistente?

Lembre-se de que você não precisa explicar quais comportamentos podem preceder o churn — apenas o que torna um usuário um usuário desistente. Pense nisso em termos de algo que um usuário faz uma vez (`do`) ou para de fazer (`do not`) que constitui churn. Por exemplo, você pode considerar que usuários que não abriram seu app em 7 dias são usuários desistentes. Você pode considerar que desinstalar, ou eventos personalizados como cancelar inscrição, desativar uma conta, ou outros, fazem com que um usuário se torne um usuário desistente.

#### Período de churn

O período de churn é o intervalo em que a atividade de um usuário atende aos critérios de churn. Você pode defini-lo para até 60 dias, dependendo dos dados disponíveis. Esse período é usado para extrair dados históricos para treinar sua previsão. Depois que a previsão for criada, você verá se havia dados suficientes para resultados precisos.

Após a previsão ser criada e os usuários receberem pontuações, a _Pontuação de risco de churn_ mostra a probabilidade de um usuário apresentar churn dentro do período definido no período de churn.

Aqui está um exemplo de uma definição simples baseada em sessões inativas nos últimos 7 dias.

![Definição de churn em que um usuário é considerado desistente se não iniciar uma sessão em 7 dias]({% image_buster /assets/img/churn/churn1.png %})

Para este caso, selecionamos `do not` e `start a session`. Você pode combinar outros filtros com `AND` e `OR` conforme necessário para criar a definição desejada. Interessado em algumas definições de churn potenciais a considerar? Você pode encontrar inspiração na seção a seguir sobre [Exemplos de definições de churn](#sample-definitions).

{% alert note %}
Para `do`, assumimos que os usuários ativos não realizaram a ação que você especifica nesta linha antes de se tornarem usuários desistentes. Realizar a ação faz com que eles se tornem usuários desistentes. <br><br>Para `do not`, consideramos como usuários ativos aqueles que realizaram essa ação nos dias anteriores e depois pararam. <br><br>**Exemplo:** Se o churn é definido como "não fez uma compra nos últimos 60 dias", consideramos como usuários ativos aqueles que fizeram uma compra nos últimos 60 dias. Como resultado, qualquer pessoa que não fez uma compra nos últimos 60 dias não é considerada um usuário ativo. Isso significa que um público de churn criado a partir dessa definição incluiria apenas usuários que fizeram compras nos últimos 60 dias. Isso pode fazer com que o público resultante de previsão de churn pareça significativamente menor do que a população original — a maioria dos usuários em um espaço de trabalho pode já atender à definição de usuário desistente e, portanto, não estar ativa na previsão de churn.
{% endalert %}

Abaixo da definição, você verá estimativas de quantos usuários (no passado que apresentaram churn e que não apresentaram churn de acordo com sua definição) estão disponíveis. Você também verá os valores mínimos necessários. A Braze precisa dessa contagem mínima de usuários disponíveis nos dados históricos para que a previsão tenha dados suficientes para aprender.

## Etapa 3: Filtrar seu público de previsão

Seu público de previsão é o grupo de usuários para os quais você deseja prever o risco de churn. O público de previsão define o grupo de usuários que o modelo de machine learning analisa para aprender com o passado. Por padrão, isso é definido como **Todos os usuários**, o que significa que essa previsão criará pontuações de risco de churn para todos os seus usuários ativos (consulte a nota anterior sobre quem é considerado ativo para um modelo de churn).

Dependendo do seu caso de uso, você pode querer usar filtros para especificar os usuários que deseja avaliar para o modelo. Para isso, selecione **Definir meu próprio público de previsão** e escolha seus filtros de público. Por exemplo, se você é um app de viagem por aplicativo com motoristas e passageiros na sua base de usuários, e está criando um modelo de churn para passageiros, você vai querer filtrar seu público de previsão apenas para passageiros. Tenha em mente que muitos casos de uso não exigem que você selecione um público de previsão específico. Por exemplo, se seu caso de uso é direcionar usuários na região da UE com maior probabilidade de churn, você pode executar seu modelo em todos os usuários e simplesmente incluir um filtro para a região da UE no segmento da campanha.

A Braze mostrará o tamanho estimado do seu público de previsão. Se você especificar o público desejado e não atender ao mínimo necessário para executar o modelo, tente especificar um filtro mais amplo ou use a opção **Todos os usuários**. Observe que o tamanho do seu grupo "todos os usuários" não é estático e varia de modelo para modelo, pois leva em consideração sua definição de churn. Por exemplo, digamos que a definição de churn é **não** fazer uma compra em 30 dias; nesse caso, a Braze executa o modelo em usuários que **fizeram** uma compra nos últimos 30 dias (e prevê a probabilidade de que eles **não** façam uma compra nos próximos 30 dias), então esses são os usuários refletidos na métrica "todos os usuários".

{% alert note %}
O público de previsão não pode exceder 100 milhões de usuários.
{% endalert %}

Quando o período de previsão é de 14 dias ou menos, o período dos filtros que começam com "Último...", como "Último uso do app" e "Última compra realizada", **não pode exceder o período de churn especificado** na definição de churn. Por exemplo, se sua definição de churn tem um período de 14 dias, o período dos filtros "Último..." não pode exceder 14 dias.

O período de churn é avaliado olhando para trás o número de dias a partir do dia em que o modelo foi executado pela última vez, então se o período de churn é de 15 dias e o modelo foi executado pela última vez em 1º de dezembro, o modelo analisa de 16 de novembro a 30 de novembro para entender a atividade do usuário para elegibilidade de público e treinamento.

#### Modo de filtro completo

Para criar uma nova previsão imediatamente, apenas um subconjunto de filtros de segmentação da Braze é suportado. O Modo de filtro completo permite que você use todos os filtros da Braze, mas exigirá um período de churn para criar a previsão. Por exemplo, se o período de churn for definido como 15 dias, levará 15 dias para coletar os dados de usuários e criar a previsão ao usar filtros suportados apenas no Modo de filtro completo. Além disso, algumas estimativas sobre tamanhos de público não estarão disponíveis no Modo de filtro completo.

Para uma lista de exemplos de definições de público de previsão, confira nossos exemplos de definições na seção a seguir sobre [Exemplos de definições de churn](#sample-definitions).

![]({% image_buster /assets/img/churn/churn5.png %})

Assim como na página anterior, o painel inferior mostrará o número estimado de usuários históricos resultantes da sua definição de churn e definição de público de previsão. Essas estimativas devem atender aos requisitos mínimos mostrados para criar uma previsão.

## Etapa 4: Escolher a frequência de atualização para a previsão de churn

O modelo de machine learning gerará pontuações de probabilidade de eventos para os usuários, e essas pontuações serão atualizadas com base na programação que você selecionar aqui. Você poderá direcionar usuários com base na pontuação de probabilidade de eventos.

Selecione a **frequência máxima de atualizações** que você considerar útil. Por exemplo, se você vai enviar uma promoção semanal para evitar que os usuários apresentem churn, defina a frequência de atualização como **Semanal** no dia e horário de sua escolha.

![Programação de atualização da previsão definida para diariamente às 17h.]({% image_buster /assets/img/churn/churn2.png %})

{% alert note %}
Previsões de prévia e demonstração nunca atualizarão o risco de churn dos usuários. Além disso, atualizações diárias para previsões exigem uma compra adicional além das atualizações semanais ou mensais com o Predictive Churn. Para adquirir essa funcionalidade, fale com seu gerente de conta.
{% endalert %}

## Etapa 5: Criar a previsão

Verifique se os detalhes fornecidos estão corretos e selecione **Criar previsão**. Você também pode salvar suas alterações como rascunho selecionando **Salvar como rascunho** para retornar a esta página e criar o modelo posteriormente. Após selecionar **Criar previsão**, o processo que gera o modelo será iniciado. Isso pode levar de 30 minutos a algumas horas, dependendo do volume de dados. Para esta previsão, você verá uma página explicando que o treinamento está em andamento durante o processo de criação do modelo. O modelo da Braze leva em consideração eventos personalizados, eventos de compra, eventos de interação com campanhas e dados de sessão.

Após a conclusão, a página mudará automaticamente para a visualização de análise de dados, e você também receberá um e-mail informando que a previsão e os resultados estão prontos. Em caso de erro, a página retornará ao modo de edição com uma explicação do que deu errado.

A previsão será reconstruída ("retreinada") automaticamente a cada **duas semanas** para mantê-la atualizada com os dados mais recentes disponíveis. Observe que este é um processo separado de quando as _Pontuações de risco de churn_ dos usuários, o resultado da previsão, são produzidas. Este último é determinado pela frequência de atualização que você escolheu na Etapa 4.

## Exemplos de definições de churn e público de previsão {#sample-definitions}

**Exemplos de definições de churn**<br>
- "Entre 7 dias, realizar evento personalizado 'Cancelamento de inscrição'"<br>
- "Entre 30 dias, realizar evento personalizado 'Período de teste expirado'"<br>
- "Entre 1 dia, realizar desinstalação."<br>
- "Entre 14 dias, não realizar uma compra."<br>

Para as definições de churn que descrevemos, pode haver algumas definições de público de previsão correspondentes:<br>
- **Iniciou a inscrição há mais de 2 semanas OU Iniciou a inscrição há menos de duas semanas**<br>Você pode querer criar 2 previsões neste caso e então enviar mensagens diferentes para novos assinantes e assinantes de longo prazo. Você também pode definir isso como "Primeira compra realizada há mais de 30 dias."<br>
- **Desinstaladores**<br>Você pode focar em clientes que compraram algo recentemente ou usaram o app muito recentemente.<br>
- **Aqueles em risco de não comprar como definição de churn**<br>Você pode querer focar em clientes que estiveram navegando, pesquisando ou interagindo com seu app mais recentemente. Talvez a intervenção certa com desconto evite que esse grupo mais engajado apresente churn.

## Previsões arquivadas

Previsões arquivadas deixarão de atualizar as pontuações dos usuários. Qualquer previsão arquivada que for desarquivada continuará atualizando as pontuações dos usuários em sua programação predeterminada. Previsões arquivadas nunca são excluídas e permanecem na lista.