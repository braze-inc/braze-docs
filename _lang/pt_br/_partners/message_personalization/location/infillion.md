---
nav_title: Infillion
article_title: Infillion
alias: /partners/infillion/
description: ""
page_type: partner
search_tag: Partner

---

# Infillion

>  Seu SDK local, combinado com software de geofencing e beacons, possibilita experiências móveis relevantes, personalizadas e com reconhecimento de proximidade.

 Essa integração de parceria abre uma série de casos de uso para:

- **Marketing:** Envie envios de mensagens contextualmente relevantes e crie jornadas experienciais para o consumidor.
- **Análise competitiva:** Defina disparos em locais competitivos para entender as tendências e os padrões dos consumidores.
- **Insights sobre o público:** Entenda os comportamentos de visitação de seus usuários e segmente mais com base nessas informações.

{% alert note %}

{% endalert %}

## Pré-requisitos

| Requisito| Descrição|
| ---| ---|
|  |  |
| |  É necessário ter o SDK implementado e as geofences (ou beacons) configuradas. |
| Chave da API REST do Braze | Uma chave da API REST da Braze com permissões `users.track`. <br><br> Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## integração de SDK

 As seguintes integrações para Android, FireOS e iOS criarão um evento personalizado exclusivo para cada novo local em que um usuário entrar. Esses eventos podem ser usados para disparar e redirecionar suas campanhas e Canvas.

Se você prevê a criação de mais de 50 lugares, recomendamos a criação de um evento personalizado genérico `Places Entered` e a adição do nome do lugar como uma propriedade do evento. 

1. 
2. 
3. 
4.  
5. Propriedades de registro para esses eventos (nome do local, tempo de permanência).
6. Use essas propriedades e eventos para disparar campanhas e Canvas no Braze. 

