{% if include.page == "testing" %}Enquanto [compondo sua mensagem de Banner]({{site.baseurl}}/user_guide/message_building_by_channel/banners/create/#compose-a-banner), selecione{% elsif include.page == "campaigns" %}Selecionar{% endif %} **Prévia** para visualizar seu Banner ou enviar uma mensagem de teste.

![A guia de prévia do compositor de Banner.]({% image_buster /assets/img/banners/select_preview.png %}){: style="max-width:50%;"}

Tenha em mente que sua prévia pode não ser idêntica ao render final no dispositivo de um usuário devido a diferenças de hardware.

Para enviar uma mensagem de teste, adicione um grupo de teste de conteúdo ou um ou mais usuários individuais como **Destinatários de Teste**, em seguida, selecione **Enviar Teste**. Você poderá visualizar sua mensagem de teste no dispositivo por até 5 minutos. Você pode então selecionar **Copiar link de prévia** para gerar e copiar um link de prévia compartilhável que mostra como o banner ficará para um usuário aleatório. O link durará sete dias antes de precisar ser regenerado.

![A guia de prévia do compositor de Banner.]({% image_buster /assets/img/banners/preview_banner.png %})

Enquanto revisa seu Banner de teste, verifique o seguinte:

- Sua campanha de Banner está atribuída a um local?
- As imagens e mídias aparecem e agem como esperado nos tipos de dispositivos e tamanhos de tela que você segmentou?
- Seus links e botões direcionam o usuário para onde deveriam ir?
- O Liquid funciona conforme o esperado? Você considerou um valor de atribuição padrão no caso de o Liquid não retornar nenhuma informação?
- Seu texto é claro, conciso e correto?
