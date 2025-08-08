---
nav_title: Verificação de dados locais
article_title: Verificação de dados locais
page_order: 1
page_type: solution
description: "Este artigo de ajuda o orienta em verificações rápidas que podem ajudá-lo se nenhum usuário tiver locais disponíveis."
tool: Location
---

# Verificação de dados locais

A Braze captura o local mais recente de um usuário por padrão por meio de seu SDK. Isso normalmente significa que o "local recente" é o local em que o usuário usou o app mais recentemente. Se você enviar dados de localização em segundo plano à Braze, poderá ter dados mais granulares disponíveis.

Se nenhum usuário tiver locais disponíveis, duas verificações rápidas podem ajudá-lo a confirmar a coleta de dados e a transferência de datas.

## Coleta de dados

Confirme se o seu app está coletando dados locais:

- Para o iOS, isso significa que os usuários aceitam compartilhar seus dados de local por meio de um pedido de aceitação em algum ponto da jornada do usuário. 
- Para Android, confirme se seu app solicita permissões de localização fina ou bruta na instalação.

Para ver se os dados de usuários estão sendo enviados ao Braze, use o filtro **Localização disponível**. Esse filtro permite ver a porcentagem de usuários com um "local mais recente".

![]({% image_buster /assets/img_archive/trouble7.png %})

## Transferência de dados

Confirme se seus desenvolvedores estão passando dados de local para o Braze. Normalmente, a passagem de dados de localização é tratada automaticamente pelo SDK depois que o usuário dá permissões, mas seus desenvolvedores podem ter desativado o monitoramento de localização na Braze. Mais informações sobre o monitoramento de localização podem ser encontradas em:
- [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/location_tracking/)
- [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/location_tracking/)
- [Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/location_tracking/)

Ainda precisa de ajuda? Abra um [tíquete de suporte]({{site.baseurl}}/braze_support/).

_Última atualização em 16 de novembro de 2022_

