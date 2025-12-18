{% if include.section == "Variant distribution" %}

A distribuição entre as variantes nem sempre é uniforme. Veja como funciona a distribuição de variantes.

Toda vez que uma mensagem é enviada em uma campanha multivariante, o sistema seleciona independentemente uma opção aleatória de acordo com as porcentagens que você definiu e atribui uma variante com base no resultado. É como jogar uma moeda - anomalias são possíveis. Se você já jogou uma moeda 100 vezes, sabe que provavelmente não obterá uma divisão exata de 50-50 entre cara e coroa todas as vezes, mesmo que tenha apenas duas opções. Você pode obter 52 caras e 48 coroas.

Se você tiver várias variantes que deseja dividir igualmente, também precisará garantir que o número de variantes seja um múltiplo de 100. Caso contrário, algumas variantes terão uma porcentagem maior de usuários distribuídos para essa variante em comparação com outras. Por exemplo, se sua campanha tiver 7 variantes, não poderá haver uma distribuição uniforme de variantes, pois 7 não se divide igualmente por 100 como um número inteiro. Nesse caso, você teria 2 variantes de 15% e 5 variantes de 14%.

#### Nota sobre mensagens no app

Ao executar um teste A/B em mensagens dentro do app, sua análise de dados pode parecer mostrar uma distribuição de variantes mais alta entre uma variante e outra, mesmo que elas tenham uma divisão percentual igual. Por exemplo, considere o seguinte gráfico de *Destinatários Únicos* para a Variante A e a Variante C.

![Gráfico de Unique Recipients para duas variantes com uma forma semelhante entre a Variante A e a Variante C, em que a Variante A tem uma contagem maior de Unique Recipients por dia]({% image_buster /assets/img/variant_distribution_iam.png %})

A Variante A tem uma contagem consistentemente maior de *Destinatários Únicos* do que a Variante C. Isso não se deve à distribuição de variantes, mas sim à forma como *os Destinatários Únicos* são calculados para mensagens no app. Para mensagens no app, *os destinatários únicos* são, na verdade, *impressões únicas*, que é o número total de pessoas que receberam e visualizaram a mensagem no app. Isso significa que, se um usuário não receber a mensagem por qualquer motivo ou decidir não visualizá-la, ele não será incluído na contagem de *destinatários únicos*, e a distribuição de variantes poderá parecer distorcida.

{% endif %}