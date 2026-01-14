Os IDs de usuário devem ser definidos para cada um de seus usuários. Esses devem ser imutáveis e acessíveis quando um usuário abre o app. Nomear seus IDs de usuário corretamente desde o início é uma das etapas mais **cruciais** na configuração de IDs de usuário. Sugerimos enfaticamente o uso do padrão Braze de UUIDs e GUIDs (detalhado abaixo). Também recomendamos enfaticamente que você forneça esse identificador, pois isso lhe permitirá:

- Acompanhe seus usuários em dispositivos e plataformas, melhorando a qualidade de seus dados comportamentais e demográficos.
- Importe dados de seus usuários usando nossa [API de dados de usuários]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data).
- Direcione-se a usuários específicos com nossa [API de envio de mensagens]({{site.baseurl}}/api/endpoints/messaging/), tanto para mensagens gerais quanto transacionais.

{% alert note %}
Se tal identificador não estiver disponível, a Braze atribuirá um identificador único aos seus usuários, mas você não terá as capacidades listadas para IDs de usuário. Você deve evitar definir IDs de usuário para usuários para os quais você não possui um identificador exclusivo que esteja vinculado a eles como indivíduos. Passar um identificador de dispositivo não oferece nenhum benefício em comparação com o rastreamento anônimo automático de usuários que o Braze oferece por padrão.
{% endalert %}

{% alert warning %}
Se quiser incluir um valor identificável como ID de usuário, para aumentar a segurança, é **altamente recomendável** adicionar o recurso de [autenticação do SDK]({{site.baseurl}}/developer_guide/authentication/) para evitar a simulação do usuário.
{% endalert %}

