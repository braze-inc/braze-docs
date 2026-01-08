---
nav_title: Migration von WhatsApp-Telefonnummern
article_title: WhatsApp-Telefonnummern-Migration
page_order: 2
description: "In diesem Referenzartikel erfahren Sie, wie Sie Ihre WhatsApp-Telefonnummer migrieren können."
page_type: reference
channel:
  - WhatsApp
---

# Migration von WhatsApp-Telefonnummern

> Migrieren Sie Ihre WhatsApp-Telefonnummer zwischen WhatsApp Business-Konten, indem Sie Meta's Embedded Signup verwenden.

## Voraussetzungen

Ihre Telefonnummer muss die Anforderungen von Meta erfüllen, um für die Migration in Frage zu kommen:

- Ihr Meta Business-Konto ist verifiziert.
- Ihr bestehendes WhatsApp Business-Konto ist genehmigt.
- Ihr bestehendes WhatsApp Business-Konto hat eine gültige Zahlungsmethode in den **Zahlungseinstellungen**.
- Bei Ihrer geschäftlichen Telefonnummer ist die zweistufige Verifizierung ausgeschaltet. Wenn Sie ein WhatsApp Business-Konto besitzen, können Sie die zweistufige Verifizierung für ihre Nummer im WhatsApp Manager deaktivieren. Andernfalls müssen Sie Ihren Anbieter der Lösung bitten, sie für Sie zu deaktivieren.

Informationen zur Migration Ihrer WhatsApp-Telefonnummer finden Sie in der Dokumentation von Meta zur [Migration von Telefonnummern zwischen WhatsApp Business-Konten über Embedded Signup](https://developers.facebook.com/docs/whatsapp/business-management-api/guides/migrate-phone-to-different-waba/).

## Migration Ihrer WhatsApp-Telefonnummer

1. Wählen Sie im WhatsApp Manager das WhatsApp Business-Konto (WABA), das mit Ihrer Telefonnummer verknüpft ist, und gehen Sie dann zu **Konto-Tools** > **Telefonnummern**.
2. Wählen Sie **Zwei-Schritt-Verifizierung aus** schalten und führen Sie die folgenden Schritte aus.<br><br>![WhatsApp Business Manager:in öffnete die Seite "Telefonnummern".]({% image_buster /assets/img/whatsapp/waba_manager.png %}){: style="max-width:80%;"} <br><br> Wenn Sie eine Telefonnummer zu einer anderen WhatsApp Business Group migrieren und die eingebettete Anmeldung von Meta erfordert, dass der Anzeigename übereinstimmt, notieren Sie sich den bestehenden Anzeigenamen auf der Seite **Telefonnummern**. Sie werden diesen Namen im nächsten Schritt eingeben.<br><br>![Die Seite Telefonnummern des WhatsApp Business Managers mit einem Anzeigenamen "Braze" neben einer Telefonnummer.]({% image_buster /assets/img/whatsapp/phone_numbers.png %}){: style="max-width:80%;"}<br><br>
3. Setzen Sie den in Meta eingebetteten Anmeldevorgang bis zum Abschluss fort. 

