---
nav_title: Qualidade da previsão
title: Qualidade da previsão
description: "Este artigo de referência dá uma olhada detalhada na métrica de qualidade de previsão localizada na página de análises de previsão."
page_order: 1
Tool:
  - Dashboard
---

# Qualidade da previsão

> Para medir a precisão do seu modelo, a métrica de _Qualidade da Previsão_ mostrará quão eficaz este modelo específico de machine learning parece ser quando testado em dados históricos. O Braze extrai os dados de acordo com os grupos que você especificou na página de criação do modelo. O modelo é treinado em um conjunto de dados (o conjunto de "treinamento") e, em seguida, testado em um conjunto de dados novo e separado (o conjunto de "teste"). 

Nossa medida de _qualidade de previsão_ é a [qualidade de elevação](https://dl.acm.org/doi/10.1145/380995.381018). Você provavelmente conhece a "elevação", que geralmente mede o aumento, como uma proporção ou porcentagem, de algum resultado bem-sucedido, como uma conversão. Nesse caso, o resultado bem-sucedido é a identificação correta de um usuário que teria churn. A qualidade da elevação é a elevação média que a previsão fornece em todos os tamanhos possíveis de público para o envio de mensagens ao conjunto de teste. Essa abordagem mede o quanto o modelo é melhor do que a adivinhação aleatória. Com essa medida, 0% significa que o modelo não é melhor do que adivinhar aleatoriamente quem vai ter churn, e 100% indica conhecimento perfeito de quem vai ter churn.

Aqui está o que recomendamos para vários intervalos de _Qualidade da Previsão_:

| Qualidade da Previsão Faixa (%) | Recomendação |
| ---------------------- | -------------- |
| 60 - 100 | Excelente. Precisão exemplar. É improvável que a alteração das definições de público traga mais benefícios. |
| 40 - 60 | Bom. Este modelo produzirá previsões precisas, mas pode valer a pena testar outras configurações de público para tentar obter resultados melhores. |
| 20 - 40| Justo. Este modelo pode proporcionar precisão e benefícios, mas experimente diferentes definições de público para ver se a performance melhora. |
| 0 - 20 | Pobre. Recomendamos alterar suas definições de público e tentar novamente. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

A previsão será treinada novamente a cada duas semanas e atualizada juntamente com a métrica _Prediction Quality (Qualidade da previsão_ ) para manter suas previsões atualizadas sobre os padrões mais recentes de comportamento do usuário. Além disso, sempre que isso ocorrer, as duas últimas semanas de previsões serão testadas em relação aos resultados reais dos usuários. A _qualidade da previsão_ será então calculada com base nesses resultados reais (em vez de estimativas). Trata-se de um backtest automático (ou seja, testar um modelo de previsão em dados históricos) para garantir que a previsão seja precisa em cenários do mundo real. A última vez em que esse retreinamento e backtesting ocorreram será exibida na página **Previsões** e na página de análises preditivas de uma previsão individual. Mesmo uma previsão prévia realizará esse backtest uma vez após sua criação. Dessa forma, você pode ter certeza da precisão de sua previsão personalizada, mesmo com a versão gratuita do recurso.

{% details Detalhes da qualidade da previsão %}

Por exemplo, se 20% dos seus usuários costumam ter churn, em média, e você escolhe um subconjunto aleatório de 20% dos seus usuários e os rotula como "com churn" aleatoriamente (sejam eles realmente com churn ou não), você espera identificar corretamente apenas 20% dos usuários com churn reais. Isso é uma suposição aleatória. Se o modelo tivesse apenas esse desempenho, a elevação seria 1 para esse caso.

Se o modelo, por outro lado, permitisse o envio de mensagens para 20% dos usuários e, ao fazê-lo, capturasse todos os "verdadeiros" usuários com churn e mais ninguém, o aumento seria de 100% / 20% = 5. Se você traçar essa razão para cada proporção dos usuários com churn mais prováveis para quem poderia enviar mensagens, obterá a [curva de elevação](https://towardsdatascience.com/the-lift-curve-unveiled-998851147871). 

Outra maneira de pensar na qualidade da elevação (e também na _qualidade da previsão_) é a distância entre a adivinhação aleatória (0%) e a perfeição (100%) da curva de elevação da previsão na identificação de churners no conjunto de teste. Para obter o artigo original sobre qualidade de elevação, consulte [Measuring lift quality in database marketing](https://dl.acm.org/doi/10.1145/380995.381018).

{% enddetails %}
