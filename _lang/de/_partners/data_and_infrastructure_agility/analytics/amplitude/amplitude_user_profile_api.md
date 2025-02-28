---
nav_title: Amplitude und vernetzte Inhalte
article_title: Amplitude und vernetzte Inhalte
page_order: 0
alias: /partners/amplitude_api_endpoints/
page_type: partner
description: "Die Benutzerprofil-API von Amplitude dient den Benutzerprofilen von Amplitude. Dazu gehören Benutzereigenschaften, berechnete Benutzereigenschaften, eine Liste von Kohorten-IDs von Kohorten, die den Benutzer enthalten, und Empfehlungen."
search_tag: Partner

---

# Amplitude und vernetzte Inhalte

> Die Benutzerprofil-API von Amplitude dient den Benutzerprofilen von Amplitude. Dazu gehören Benutzereigenschaften, berechnete Benutzereigenschaften, eine Liste von Kohorten-IDs von Kohorten, die den Benutzer enthalten, und Empfehlungen. Im Folgenden finden Sie eine Liste gängiger Amplitude-API-Endpunkte, die mit Connected Content verwendet werden können.

## Endpunkt-Parameter

In der folgenden Tabelle finden Sie die Parameter, die Sie in Ihren Aufrufen der Benutzerprofil-API verwenden können.

| Parameter | Erforderlich | Beschreibung |
| --------- | -------- | ----------- |
| `user_id` | Optional | Benutzerkennung (externe Datenbankkennung), die abgefragt werden soll, erforderlich, wenn nicht `device_id` eingestellt ist. |
| `device_id` | Optional | Geräte-ID (anonyme ID), die abgefragt werden soll, erforderlich, sofern nicht `user_id` eingestellt ist. |
| `get_recs` | Optional<br>(Standardwert ist false) | Gibt ein Empfehlungsergebnis für diesen Benutzer zurück. |
| `rec_id` | Optional | Empfehlung(en), die abgerufen werden sollen, erforderlich, wenn `get_recs` true ist. Sie können mehrere Empfehlungen abrufen, indem Sie die `rec_ids` mit Kommas trennen. |
| `rec_type` | Optional | Setzt die Standardeinstellung für die experimentelle Kontrolle außer Kraft. `rec_type=model` liefert modellierte Empfehlungen und `rec_type=random` liefert zufällige Empfehlungen. Möglicherweise gibt es in Zukunft weitere Optionen. |
| `get_amp_props` | Optional<br>(Standardwert ist false) | Gibt einen vollständigen Satz von Benutzereigenschaften für diesen Benutzer zurück, ohne Berechnungen. |
| `get_cohort_ids` | Optional<br>(Standardwert ist false) | Gibt eine Liste aller Kohorten-IDs zurück, zu denen dieser Benutzer gehört und die für die Nachverfolgung eingerichtet wurden. Standardmäßig wird die Kohortenzugehörigkeit von Benutzern für keine Kohorte verfolgt. |
| `get_computations` | Optional<br>(Standardwert ist false) | Gibt eine Liste aller Berechnungen zurück, die für diesen Benutzer aktiviert sind. |
| `comp_id` | Optional | Gibt eine einzelne Berechnung zurück, die für diesen Benutzer aktiviert sein könnte. Es wird ein Nullwert zurückgegeben, wenn es nicht existiert. Wenn `get_computations` wahr ist, werden alle Werte abgerufen, einschließlich dieses einen (sofern er nicht archiviert oder gelöscht wurde).|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Die folgende Tabelle enthält die Parameter, die Sie in den meisten Fällen in den Antworten von Amplitude erwarten können.

| Antwort Parameter | Beschreibung |
| ------------------ | ----------- |
| `rec_id` | Die Empfehlung id, die angefordert wurde. |
| `child_rec_id` | Eine detailliertere Empfehlung, die Amplitude im Rahmen eines internen Experiments zur Verbesserung der Modellleistung im Backend verwenden kann. In den meisten Fällen wird dies dasselbe sein wie `rec_id`. |
| `items` | Liste der Empfehlungen für diesen Benutzer. |
| `is_control` | true, wenn dieser Benutzer Teil der Kontrollgruppe ist. |
| `recommendation_source` | Name des Modells, das zur Erstellung dieser Empfehlung verwendet wurde |
| `last_updated` | Zeitstempel, wann diese Empfehlung zuletzt erstellt und synchronisiert wurde. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Gemeinsame Endpunkte der Amplitude

### Erhalten Sie eine Empfehlung

#### Endpunkt
{% raw %}
`https://profile-api.amplitude.com/v1/userprofile?user_id=testUser&get_recs=true&rec_id=testRecId`
{% endraw %}
#### Beispielhafte Antwort
```json
{
  "userData": {
    "recommendations": [
      {
        "rec_id": "testRecId",
        "child_rec_id": "testRecId",
        "items": [
          "cookie",
          "cracker",
          "chocolate milk",
          "donut",
          "croissant"
        ],
        "is_control": false,
        "recommendation_source": "model",
        "last_updated": 1608670720
      }
    ],
    "user_id": "testUser",
    "device_id": "ffff-ffff-ffff-ffff",
    "amp_props": null,
    "cohort_ids": null
  }
}
```

### Erhalten Sie mehrere Empfehlungen

#### Endpunkt
{% raw %}
`https://profile-api.amplitude.com/v1/userprofile?user_id=testUser&get_recs=true&rec_id=testRecId,testRecId2`
{% endraw %}
#### Beispielhafte Antwort
```json
{
  "userData": {
    "recommendations": [
      {
        "rec_id": "testRecId",
        "child_rec_id": "testRecId",
        "items": [
          "cookie",
          "cracker",
          "chocolate milk",
          "donut",
          "croissant"
        ],
        "is_control": false,
        "recommendation_source": "model",
        "last_updated": 1608670720
      },
            {
        "rec_id": "testRecId2",
        "child_rec_id": "testRecId2",
        "items": [
          "bulgogi",
          "bibimbap",
          "kimchi",
          "croffles",
          "samgyeopsal"
        ],
        "is_control": false,
        "recommendation_source": "model2",
        "last_updated": 1608670658
      }
    ],
    "user_id": "testUser",
    "device_id": "ffff-ffff-ffff-ffff",
    "amp_props": null,
    "cohort_ids": null
  }
}
```

### Benutzereigenschaften abrufen

#### Endpunkt
{% raw %}
`https://profile-api.amplitude.com/v1/userprofile?user_id=testUser&get_amp_props=true`
{% endraw %}
#### Beispielhafte Antwort
```json
{
  "userData": {
    "recommendations": null,
    "user_id": "testUser",
    "device_id": "ffff-ffff-ffff-ffff",
    "amp_props": {
      "library": "http/1.0",
      "first_used": "2020-01-13",
      "last_used": "2021-03-24",
      "number_property": 12,
      "boolean_property": true
    },
    "cohort_ids": null
  }
}
```

### Kohorten-IDs abrufen

#### Endpunkt
{% raw %}
`https://profile-api.amplitude.com/v1/userprofile?user_id=testUser&get_cohort_ids=true`
{% endraw %}
#### Beispielhafte Antwort
```json
{
  "userData": {
    "recommendations": null,
    "user_id": "testUser",
    "device_id": "ffff-ffff-ffff-ffff",
    "amp_props": null,
    "cohort_ids": ["cohort1", "cohort3", "cohort7"]
  }
}
```

### Erhalten Sie eine einzelne Berechnung

#### Endpunkt
{% raw %}
`https://profile-api.amplitude.com/v1/userprofile?user_id=testUser&comp_id=testCompId`
{% endraw %}
#### Beispielhafte Antwort
```json
{
  "userData": {
    "recommendations": null,
    "user_id": "testUser",
    "device_id": "ffff-ffff-ffff-ffff",
    "amp_props": {
      "computed-prop-2": "3"
    },
    "cohort_ids": null
  }
}
```

### Alle Berechnungen abrufen

#### Endpunkt
{% raw %}
`https://profile-api.amplitude.com/v1/userprofile?user_id=testUser&get_computations=true`
{% endraw %}
#### Beispielhafte Antwort
```json
{
  "userData": {
    "recommendations": null,
    "user_id": "testUser",
    "device_id": "ffff-ffff-ffff-ffff",
    "amp_props": {
      "computed-prop-1": "5000000.0",
      "computed-prop-2": "3"
    },
    "cohort_ids": null
  }
}
```

