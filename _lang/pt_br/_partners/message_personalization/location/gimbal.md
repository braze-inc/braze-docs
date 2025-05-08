---
nav_title: Gimbal
article_title: Gimbal
alias: /partners/gimbal/
description: "Este artigo de referência descreve a parceria entre a Braze e a Gimbal, que permite a você aperfeiçoar sua relevância de marketing usando dados de localização."
page_type: partner
search_tag: Partner

---

# Gimbal

> [O Gimbal](https://gimbal.com/) o capacita a aperfeiçoar sua relevância de marketing usando dados locais. Seu SDK local, combinado com software de geofencing e beacons, possibilita experiências móveis relevantes, personalizadas e com reconhecimento de proximidade.

Combine seu suporte a beacon ou geofence com os recursos de direcionamento e envio de mensagens do Braze para saber mais sobre as ações físicas do usuário e enviar as mensagens correspondentes. Essa integração de parceria abre uma série de casos de uso para:

- **Marketing:** Envie envios de mensagens contextualmente relevantes e crie jornadas experienciais para o consumidor.
- **Análise competitiva:** Defina disparos em locais competitivos para entender as tendências e os padrões dos consumidores.
- **Insights sobre o público:** Entenda os comportamentos de visitação de seus usuários e segmente mais com base nessas informações.

{% alert note %}
Essa integração funciona da mesma forma para os beacons da Gimbal e para as soluções de geofence da Gimbal.
{% endalert %}

## Pré-requisitos

| Requisito| Descrição|
| ---| ---|
| [Conta de gerente da Gimbal][1] | É necessário ter uma conta no Gimbal Manager para aproveitar essa parceria. |
|[Gimbal Location SDK](https://docs.gimbal.com/index.html) | O Gimbal Location SDK possibilita experiências móveis baseadas em macro e micro locais usando beacons de proximidade e geofences que permitem uma comunicação mais eficaz com os usuários do seu app. É necessário ter o SDK implementado e as geofences (ou beacons) configuradas. |
| Chave da API REST do Braze | Uma chave da API REST da Braze com permissões `users.track`. <br><br> Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## integração de SDK

Para integrar a Braze e a Gimbal, implemente o Gimbal Location SDK e crie uma conta de gerente da Gimbal. As seguintes integrações para Android, FireOS e iOS criarão um evento personalizado exclusivo para cada novo local em que um usuário entrar. Esses eventos podem ser usados para disparar e redirecionar suas campanhas e Canvas.

Se você prevê a criação de mais de 50 lugares, recomendamos a criação de um evento personalizado genérico `Places Entered` e a adição do nome do lugar como uma propriedade do evento. 

1. Integre o [Gimbal SDK][2] para Android e iOS ao seu app seguindo as instruções da [documentação da Gimbal][3].
2. Use a [place REST API][4] da Gimbal para obter o usuário `places`.
3. Vincule sua conta do Gimbal à Braze inserindo a [chave da API REST][5] da Braze.
4. Configure [eventos personalizados][6] no SDK do Braze. Você pode integrar a Gimbal com a Braze para [Android, FireOS][7] e [iOS][8].
5. Propriedades de registro para esses eventos (nome do local, tempo de permanência).
6. Use essas propriedades e eventos para disparar campanhas e Canvas no Braze. 

[1]: https://manager.gimbal.com/login/users/sign_in
[2]: https://manager.gimbal.com/sdk_downloads
[3]: https://docs.gimbal.com/
[4]: https://docs.gimbal.com/rest.html
[5]: https://manager.gimbal.com/apps
[6]: {{site.baseurl}}/user_guide/data_and_analytics/Custom_Data/custom_events/
[7]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/beacon_integration/#gimbal-beacons
[8]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/advanced_use_cases/beacon_integration/#gimbal-beacons