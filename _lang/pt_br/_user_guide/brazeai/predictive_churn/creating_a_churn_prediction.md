---
nav_title: Criação de uma previsão de rotatividade
article_title: Criação de uma previsão de rotatividade
description: "Este artigo aborda como criar uma previsão de churn no painel do Braze."
page_order: 1.1

---

# Criação de uma previsão de rotatividade

> Saiba como criar uma previsão de churn no painel do Braze.

## Etapa 1: Criar uma nova previsão

No Braze, vá para **Analytics** > **Predictive Churn**.

Uma previsão é uma instância de um modelo de aprendizado de máquina treinado e todos os parâmetros e dados que ele usa. Nessa página, você verá uma lista das previsões ativas atuais, juntamente com algumas informações básicas sobre elas. Aqui, você pode renomear, arquivar e criar novas previsões. As previsões arquivadas são inativas e não atualizam as pontuações dos usuários. 

Para criar uma nova previsão, escolha **Criar previsão** e selecione uma nova **previsão de rotatividade**.

{% alert note %}
Há um limite de cinco previsões de rotatividade ativas simultaneamente. Antes de comprar o Predictive Churn, o limite é de uma previsão de churn de visualização ativa. Uma previsão prévia de rotatividade não atualizará regularmente as pontuações nem permitirá que você direcione os usuários com base no resultado da previsão. Entre em contato com o gerente da sua conta para obter detalhes.
{% endalert %}

Na página **Basics (Fundamentos)**, dê um nome exclusivo à sua nova previsão. Você também pode fornecer uma descrição opcional para fazer anotações sobre essa previsão específica.

Selecione **Forward (Avançar** ) para passar para a próxima etapa. Opcionalmente, você pode selecionar **Build Now** para usar todas as configurações padrão e pular para a última etapa da criação. Você terá a oportunidade de revisar as configurações antes de iniciar o processo de compilação. Você pode retornar a qualquer etapa posteriormente, selecionando-a no rastreador de progresso.

## Etapa 2: Definir churn

No painel **Churn Definition (Definição de** rotatividade), use os filtros fornecidos para especificar como definir a rotatividade de usuários para a sua empresa. Em outras palavras, o que um usuário precisa fazer em que período de tempo para que você o considere eliminado?

Lembre-se de que não é necessário explicar quais comportamentos podem preceder a rotatividade - apenas o que torna um usuário um usuário rotativo. Pense nisso em termos de algo que um usuário faz uma vez (`do`) ou deixa de fazer (`do not`) e que constitui churning. Por exemplo, você pode considerar que os usuários que não abriram seu aplicativo em 7 dias foram cancelados. Você pode considerar a desinstalação ou eventos personalizados, como cancelamento de assinatura, desativação de uma conta ou outros, para fazer com que um usuário se torne desistente. 

#### Janela de rotatividade

A janela de rotatividade é o período em que a atividade de um usuário atende aos critérios de rotatividade. Você pode configurá-lo para até 60 dias, dependendo dos dados disponíveis. Essa janela é usada para extrair dados históricos para treinar sua previsão. Depois que a previsão for criada, você verá se há dados suficientes para obter resultados precisos.

Depois que a previsão for criada e os usuários receberem pontuações, o _Churn Risk Score_ mostrará a probabilidade de um usuário se desligar dentro do período de tempo definido na janela de desligamento. 

Aqui está um exemplo de uma definição simples baseada em sessões de lapso nos últimos 7 dias.

Definição de rotatividade em que um usuário é considerado rotativo se não iniciar uma sessão em 7 dias]({% image_buster /assets/img/churn/churn1.png %})

Para esse caso, selecionamos `do not` e `start a session`. Você pode combinar outros filtros com `AND` e `OR` conforme achar necessário para criar a definição de que precisa. Interessado em algumas definições de churn em potencial a serem consideradas? Você pode encontrar alguma inspiração na seção a seguir sobre [Definições de churn de amostra](#sample-definitions).

{% alert note %}
Para `do`, presumimos que os usuários ativos não tomaram a ação que você especificou para essa linha antes de serem eliminados. A realização da ação faz com que eles se tornem agitados. <br><br>Para `do not`, consideramos usuários ativos aqueles que realizaram essa ação nos dias anteriores e depois pararam. <br><br>**Exemplo:** Se a rotatividade for definida como "não comprou nos últimos 60 dias", consideraremos usuários ativos aqueles que compraram nos últimos 60 dias. Como resultado, qualquer pessoa que não tenha feito uma compra nos últimos 60 dias não é considerada um usuário ativo. Isso significa que um público-alvo de rotatividade criado a partir dessa definição de rotatividade incluiria apenas usuários que compraram nos últimos 60 dias. Isso pode fazer com que o público resultante da previsão de rotatividade pareça significativamente menor do que a população original - a maioria dos usuários em um espaço de trabalho pode já atender à definição de rotatividade e, portanto, não estar ativa na previsão de rotatividade.
{% endalert %}

Abaixo da definição, você verá estimativas de quantos usuários (no passado, que se desligaram e que não se desligaram de acordo com sua definição) estão disponíveis. Você também verá os valores mínimos necessários. O Braze deve ter esse número mínimo de usuários disponíveis nos dados históricos para que a previsão tenha dados suficientes para aprender.

## Etapa 3: Filtrar seu público-alvo de previsão

Seu público-alvo de previsão é o grupo de usuários para o qual você deseja prever o risco de rotatividade. O público-alvo da previsão define o grupo de usuários que o modelo de aprendizado de máquina analisa para aprender com o passado. Por padrão, isso é definido como **All Users (Todos os usuários**), o que significa que essa previsão criará pontuações de risco de rotatividade para todos os seus usuários ativos (consulte a nota anterior para saber quem é considerado ativo para um modelo de rotatividade).

Dependendo do seu caso de uso, talvez você queira usar filtros para especificar os usuários que deseja avaliar para o modelo. Para isso, selecione **Definir meu próprio público de previsão** e escolha seus filtros de público. Por exemplo, se você for um aplicativo de compartilhamento de carona com motoristas e passageiros em sua base de usuários e estiver criando um modelo de rotatividade para passageiros, deverá filtrar seu público-alvo de previsão apenas para passageiros. Lembre-se de que muitos casos de uso não exigem que você selecione um público-alvo de previsão específico. Por exemplo, se o seu caso de uso for direcionar os usuários da região da UE com maior probabilidade de rotatividade, você poderá executar seu modelo em todos os usuários e, em seguida, simplesmente incluir um filtro para a região da UE no segmento da campanha.

O Braze mostrará o tamanho estimado do seu público-alvo de previsão. Se você especificar o público desejado e não atingir o mínimo necessário para executar o modelo, tente especificar um filtro mais amplo ou use a opção **Todos os usuários**. Observe que o tamanho do grupo "todos os usuários" não é estático e varia de modelo para modelo, pois leva em conta a definição de churn. Por exemplo, digamos que a definição de churn seja **não** fazer uma compra em 30 dias; nesse caso, o Braze executa o modelo em usuários que **compraram** nos últimos 30 dias (e prevê a probabilidade de que eles **não** comprarão nos próximos 30 dias), portanto, esses são os usuários refletidos na métrica "todos os usuários".

{% alert note %}
O público-alvo da previsão não pode exceder 100 milhões de usuários.
{% endalert %}

Quando a janela de previsão é de 14 dias ou menos, a janela de tempo para filtros que começam com "Last..." (Última...), como "Last Used App" (Último aplicativo usado) e "Last Made Purchase" (Última compra feita) **, não pode exceder a janela de rotatividade especificada** na definição de rotatividade. Por exemplo, se sua definição de rotatividade tiver uma janela de 14 dias, a janela de tempo para os filtros "Last..." não poderá exceder 14 dias.

#### Modo de filtro completo

Para criar uma nova previsão imediatamente, somente um subconjunto de filtros de segmentação do Braze é compatível. O modo de filtro completo permite que você use todos os filtros do Braze, mas exigirá uma janela de churn para criar a previsão. Por exemplo, se a janela de rotatividade for definida como 15 dias, serão necessários 15 dias para coletar os dados do usuário e criar a previsão ao usar filtros compatíveis apenas com o modo de filtro completo. Além disso, algumas estimativas sobre o tamanho do público não estarão disponíveis no modo de filtro completo.

Para obter uma lista de exemplos de definições de público-alvo de previsão, confira nossos exemplos de definições na seção a seguir sobre [Exemplos de definições de churn](#sample-definitions).

\![]({% image_buster /assets/img/churn/churn5.png %})

Assim como na página anterior, o painel inferior mostrará o número estimado de usuários históricos que resultam da definição de rotatividade e da definição de público-alvo de previsão. Essas estimativas devem atender aos requisitos mínimos mostrados para que seja possível criar uma previsão.

## Etapa 4: Escolha a frequência de atualização para a previsão de rotatividade

O modelo de aprendizado de máquina gerará pontuações de probabilidade de eventos para os usuários, e essas pontuações serão atualizadas com base na programação que você selecionar aqui. Você poderá segmentar usuários com base na pontuação de probabilidade de eventos. 

Selecione a **frequência máxima de atualizações** que você considera útil. Por exemplo, se for enviar uma promoção semanal para evitar a rotatividade de usuários, defina a frequência de atualização como **Weekly (Semanal** ) no dia e horário de sua escolha. 

\![Cronograma de atualização da previsão definido para diariamente às 17h.]({% image_buster /assets/img/churn/churn2.png %})

{% alert note %}
A previsão de visualização e demonstração nunca atualizará o risco de rotatividade dos usuários. Além disso, as atualizações diárias para previsões exigem uma compra adicional, além das atualizações semanais ou mensais com o Predictive Churn. Para adquirir essa funcionalidade, entre em contato com o gerente da sua conta.
{% endalert %}

## Etapa 5: Previsão de construção

Verifique se os detalhes que você forneceu estão corretos e selecione **Build Prediction (Criar previsão**). Você também pode salvar suas alterações no formato de rascunho selecionando **Save As Draft** para retornar a essa página e criar o modelo posteriormente. Depois que você selecionar **Criar previsão**, o processo que gera o modelo será iniciado. Isso pode levar de 30 minutos a algumas horas, dependendo do volume de dados. Para essa previsão, você verá uma página explicando que o treinamento está em andamento durante o processo de criação do modelo. O modelo Braze leva em conta eventos personalizados, eventos de compra, eventos de interação de campanha e dados de sessão.

Depois de concluída, a página mudará automaticamente para a exibição do Analytics, e você também receberá um e-mail informando que a previsão e os resultados estão prontos. No caso de um erro, a página retornará ao modo de edição com uma explicação do que deu errado.

A previsão será reconstruída ("retreinada") novamente a cada **duas semanas automaticamente** para mantê-la atualizada com os dados mais recentes disponíveis. Observe que esse é um processo separado de quando os _Churn Risk Scores_ dos usuários, o resultado da previsão, são produzidos. A última é determinada pela frequência de atualização que você escolheu na Etapa 4.

## Exemplo de definições de público-alvo de churn e previsão {#sample-definitions}

**Exemplos de definições de rotatividade**<br>
- "Dentro de 7 dias, faça o evento personalizado 'Cancelamento de assinatura'"<br>
- "Dentro de 30 dias, faça o evento personalizado 'Trial Expired'"<br>
- "Em um dia, faça a desinstalação." <br>
- "Dentro de 14 dias, não faça uma compra." <br>

Para as definições de rotatividade que descrevemos, pode haver algumas definições de público-alvo de previsão correspondentes:<br>
- **Iniciou a assinatura há mais de duas semanas OU Iniciou a assinatura há menos de duas semanas**<br>Talvez você queira criar duas previsões nesse caso e enviar mensagens aos novos assinantes de forma diferente dos assinantes de longo prazo. Você também poderia definir isso como "Primeira compra feita há mais de 30 dias".<br>
- **Desinstaladores**<br>Você pode se concentrar nos clientes que compraram algo no passado recente ou que usaram o aplicativo muito recentemente.<br>
- **Aqueles que correm o risco de não comprar como uma definição de rotatividade**<br>Talvez você queira se concentrar nos clientes que navegaram, pesquisaram ou se envolveram com seu aplicativo mais recentemente. Talvez a intervenção correta de desconto evite que esse grupo mais engajado se desfaça.

## Previsões arquivadas

As previsões arquivadas deixarão de atualizar as pontuações dos usuários. Qualquer previsão arquivada que não esteja arquivada continuará atualizando as pontuações dos usuários em sua programação predeterminada. As previsões arquivadas nunca são excluídas e permanecem na lista.


