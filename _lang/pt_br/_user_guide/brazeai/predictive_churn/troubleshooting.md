---
nav_title: Solução de problemas
article_title: Solução de problemas de previsão de churn
description: "Este artigo de referência aborda algumas etapas de solução de problemas e considerações que devem ser levadas em conta ao usar o Predictive Churn."
page_order: 3

---

# Solução de problemas

> A previsão do churn (e de qualquer modelo de machine learning) é tão boa quanto os dados disponíveis para o modelo. Também é altamente dependente da existência de determinados volumes de dados para trabalhar. 

## Erros potenciais

### Não há dados suficientes para treinar 

Essa mensagem de erro aparece quando a definição de churn é muito limitadora e retorna poucos usuários desistentes. 

Para corrigir isso, será necessário alterar o número de dias e/ou as ações que definem o churn para capturar mais usuários. Use corretamente os filtros `AND/OR` para não criar definições excessivamente restritivas. 

{% alert important %}
Embora o Predictive Churn esteja ativado no nível da empresa, alguns espaços de trabalho podem não ter usuários suficientes para criar previsões. Normalmente, são necessários 300.000 usuários ativos mensais em um único espaço de trabalho.
{% endalert %}

### Problemas com a previsão do tamanho do público

Ao criar seu público de previsão para ajustar o tipo de uso em relação ao qual deseja que seu modelo seja treinado, você poderá encontrar esta mensagem notificando que seu público de previsão tem muito poucos usuários: 

"Não há um número suficiente de não-canceladores anteriores para criar a previsão de forma confiável"

![Os requisitos de dados de previsão mostram 31 cancelamentos anteriores (atende ao requisito) e 0 não cancelamentos anteriores (abaixo do mínimo). Uma mensagem de aviso indica que não há número suficiente de não clientes para criar a previsão.]({% image_buster /assets/img/churn/audience_size_error.png %})

Se a definição do seu público-alvo de previsão for muito rigorosa, talvez não tenha um conjunto suficientemente grande de usuários históricos e ativos para trabalhar. Para corrigir isso, você precisará alterar o número de dias e o tipo de atribuições usadas nessa definição, alterar as ações que definem o churn ou ambos. 

Se o seu público de previsão continuar a ser um problema mesmo depois de mudar suas definições, talvez você tenha poucos usuários para suportar esse recurso opcional. Sugerimos que, em vez disso, tente criar uma previsão sem as camadas e os filtros extras. 

### O tamanho do público da previsão é muito grande

Uma definição de público de previsão não pode exceder 100 milhões de usuários. Se você vir uma mensagem dizendo que seu público é muito grande, recomendamos adicionar mais camadas ao seu público ou alterar a janela de tempo em que ele se baseia.

### A previsão tem qualidade ruim

![]({% image_buster /assets/img/churn/churn3.png %}){: style="float:right;max-width:40%;margin-left:15px;"}
Se o seu modelo tiver uma [qualidade de previsão]({{site.baseurl}}/user_guide/brazeai/predictive_churn/analytics/) de 40% ou mais, você está em um ótimo lugar! Mas se a qualidade da previsão cair para 39% ou menos, talvez seja necessário editar as definições de público do churn e da previsão para que sejam mais específicas ou tenham janelas de tempo diferentes. 

Se não for possível atender ao requisito de tamanho do público ao criar suas definições de previsão e obter uma qualidade de previsão superior a 40%, isso provavelmente significa que os dados enviados ao Braze não são ideais para esse caso de uso, que não há usuários suficientes para criar um modelo ou que o ciclo de vida do seu produto é mais longo do que nossa janela de lookback atual de 60 dias suporta. 

## Considerações sobre os dados

Veja a seguir as perguntas que você deve fazer a si mesmo ao configurar o Predictive Churn. Os modelos de machine learning são tão bons quanto os dados que os treinam, portanto, ter boas práticas de higiene de dados e entender o que entra no modelo fará uma grande diferença.

- Quais ações de alto valor levam à retenção e à fidelidade?
- Você configurou eventos personalizados que mapeiam essas ações específicas? O Predictive Churn funciona com eventos personalizados em vez de atributos personalizados.
- Você está pensando em janelas de tempo dentro das quais definirá o churn? Você pode definir churn como algo que acontece em até 60 dias.
- Você já considerou as épocas do ano que levam a comportamentos atípicos dos usuários, como os feriados? As rápidas mudanças no comportamento do consumidor afetarão suas previsões. 

