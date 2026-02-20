Você pode escolher uma das seguintes opções:

- **Mais populares:** Esse é o horário mais popular em que seu app é usado entre todos os usuários.
- **Personalizado:** Esse é um fallback personalizado de sua escolha. A mensagem será entregue com base no fuso local de cada usuário individual.

{% subtabs local %}
{% subtab most popular %}
O horário de app mais popular é determinado pelo horário médio de início da sessão para o seu espaço de trabalho (em fuso local). Esse tempo é exibido em vermelho no gráfico de prévia.

No caso improvável de seu aplicativo não ter dados de sessão suficientes para calcular quando o aplicativo é mais usado (um aplicativo completamente novo sem dados), a mensagem será enviada às 17h no fuso local do usuário. Se o fuso local do usuário for desconhecido, ele será enviado às 17h no fuso horário da sua empresa.

É importante estar ciente das limitações de usar Intelligent Timing no início do ciclo de vida de um usuário quando dados limitados estão disponíveis. Ainda pode ser valioso, pois mesmo usuários com poucas sessões registradas podem oferecer insights sobre seu comportamento. No entanto, a Braze pode calcular de forma mais eficaz o momento ideal para envio mais tarde no ciclo de vida de um usuário.

{% if include.type == "campaigns" %}
{% alert note %}
Para campanhas, se você especificou uma [janela de entrega](#sending-within-specific-hours) e o horário mais popular para usar seu app estiver fora dessa janela, a mensagem será enviada o mais próximo possível da borda da janela de entrega. Por exemplo, se seu período de entrega for das 13h às 20h e o horário mais popular do app for às 22h, a mensagem será enviada às 20h.
{% endalert %}
{% endif %}
{% endsubtab %}

{% subtab custom %}
Use o tempo de fallback personalizado para escolher um horário diferente para enviar a mensagem. Similar ao tempo do app mais popular, a mensagem será enviada no horário de fallback no fuso local do usuário. Se o fuso local do usuário for desconhecido, ele será enviado no fuso horário da sua empresa.

Para campanhas com um tempo de fallback personalizado especificado, se você lançar a campanha dentro de 24 horas da data de envio, os usuários cujos horários ideais já passaram receberão a campanha no tempo de fallback personalizado. Se o tempo de fallback personalizado já tiver passado no fuso horário deles, a mensagem será enviada imediatamente.
{% endsubtab %}
{% endsubtabs %}