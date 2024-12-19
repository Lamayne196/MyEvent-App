---
title: Daily Progress - Lamine Touré
nav_order: 1
---

{: .label }
[65Coders - Backend]

{: .no_toc }
# Daily Progress - Lamine Touré

<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>

## Daily Log

### 22-Nov-2024

**Task, an dem gearbeitet wird:**  
Einrichtung eines Firebase-Projekts und Verbindung mit unserer App.  

**Tasks completed**:  
-  
  - Firebase-Account und neues Projekt erstellt.  
  - Firestore-Datenbank und Storage im Firebase-Projekt aktiviert.  
  - Eine `fireBase_config.py` Datei erstellt, um die Datenbank und den Storage zu initialisieren.  
---
---
### 01-Dez-2024

**Task, an dem gearbeitet wird:**  
Erstellung von Authentifizierungsrouten (Login, Registrierung und Logout) für die Anwendung und deren Registrierung in einer neuen `app.py`-Datei.

**Tasks completed**:  
- Eine neue Datei `authRoute.py` wurde erstellt, die die Authentifizierungsrouten verwaltet.  
  - **Login**: Nutzer können sich mit ihrer E-Mail und Passwort anmelden. Erfolgreiche Anmeldungen führen zum Dashboard, bei Fehlern wird eine Fehlermeldung angezeigt.  
  - **Registrierung**: Neue Nutzer können sich mit einer E-Mail und einem Passwort registrieren. Es wird sichergestellt, dass die Passwörter übereinstimmen und die E-Mail-Adresse noch nicht vergeben ist.  
  - **Logout**: Nutzer können sich abmelden, wodurch die Session gelöscht wird und eine Bestätigung angezeigt wird.  

- Die Routen wurden in einer neuen `app.py`-Datei mit Blueprints registriert, um die Struktur der Anwendung zu verbessern.  
- Flask-Sessions wurden in der `app.py`-Datei initialisiert, um Benutzersitzungen zu verwalten. Dadurch können sich Nutzer anmelden und ihre Sitzung während der Nutzung der Anwendung aufrechterhalten.  
- Die Benutzerdaten werden in Firebase (Firestore) gespeichert und verwaltet.

**Challenges**:  
- Sicherstellen, dass die Passwörter korrekt validiert und verarbeitet werden.
- Fehlerbehandlung bei ungültigen Anmeldeversuchen oder bereits vorhandenen E-Mails.

**Next steps**:  
- Erstellung von Event-Routen zur Verwaltung von Veranstaltungen in der Anwendung.  
---
---


### 07-Dez-2024

**Task, an dem gearbeitet wird:**  
Implementierung von Event-Management-Routen in der Datei `eventRoute.py`.  

**Tasks completed**:  
- **Event Details anzeigen:**  
  - Route: `/event/<event_id>` (GET, POST)  
  - Zeigt Details eines spezifischen Events an.  
  - Teilnehmerstatus (RSVP) wird basierend auf der Nutzer-E-Mail überprüft. Nutzer können Event-Daten bearbeiten oder das Event löschen, wenn sie der Ersteller sind.  
  - Gäste sehen eine andere Ansicht mit beschränkten Bearbeitungsrechten.

- **Event-Erstellung:**  
  - Route: `/event/create` (GET, POST)  
  - Ermöglicht es authentifizierten Nutzern, ein neues Event zu erstellen.  
  - Upload von Bildern für das Event mit Speicherung im Firebase-Storage.  
  - Event-Daten werden in Firestore sowohl in der öffentlichen Sammlung `public_events` als auch in der Nutzersammlung gespeichert.

- **Teilnahme an Events (RSVP):**  
  - Route: `/event/<event_id>/rsvp` (POST)  
  - Nutzer können sich für ein Event anmelden oder ihre Anmeldung stornieren.  
  - Die Anzahl der Teilnehmer wird dynamisch in Firestore aktualisiert.  

- **Teilnehmerliste anzeigen:**  
  - Route: `/event/<event_id>/participants` (GET)  
  - Authentifizierte Nutzer können die Teilnehmer eines Events anzeigen.  
  - Liste enthält Vorname, Nachname und E-Mail der Teilnehmer.

- **Event-Löschung:**  
  - Route: `/event/<event_id>/delete` (POST)  
  - Löscht ein Event aus der Nutzersammlung und der öffentlichen Sammlung.  
  - Authentifizierung erforderlich, um sicherzustellen, dass nur der Ersteller ein Event löschen kann.

**Challenges:**  
- Synchronisierung der Teilnehmerdaten zwischen der Nutzersammlung und der öffentlichen Sammlung.  
- Validierung von Eingaben wie Teilnehmeranzahl und Kategorie des Events.

**Next steps:**  
- Verfeinerung der Teilnehmerlistenanzeige (z.B. Hinzufügen von Paginierung).  
- Erstellen von zusätzlichen Event-Management-Funktionen, wie z.B. das Verschieben eines Events.  

---
---
### 10-Dez-2024

**Task, an dem gearbeitet wird:**  
Verwaltung des Dashboards für authentifizierte Benutzer, einschließlich der Anzeige und Löschung von Events.  

**Tasks completed**:  
- **Dashboard anzeigen:**  
  - **Route:** `/dashboard/`  
  - Authentifizierte Benutzer können sich anmelden und eine Liste ihrer eigenen Events anzeigen.  
  - Die Events werden aus der persönlichen Sammlung (`events`) des Nutzers in Firestore abgerufen.  
  - Jedes Event enthält Details wie Titel, Beschreibung und Datum. Die automatisch generierte Event-ID wird ebenfalls bereitgestellt, um Aktionen wie Bearbeitung oder Löschung zu ermöglichen.  

- **Löschen von Events:**  
  - **Route:** `/dashboard/delete_event/<event_id>`  
  - Authentifizierte Benutzer können Events löschen.  
  - Das Event wird sowohl aus der Nutzersammlung des Benutzers als auch aus der zentralen Sammlung `public_events` entfernt.  
  - Dies stellt sicher, dass die Datenbank synchron bleibt.  

**Challenges:**  
- Umgang mit fehlerhaften oder nicht existierenden Benutzerprofilen in Firebase.  
- Sicherstellen, dass die Löschaktionen ordnungsgemäß synchronisiert werden, um redundante Daten zu vermeiden.  

**Next steps:**  
- Hinzufügen der Möglichkeit, Events direkt im Dashboard zu bearbeiten.  
- Implementierung eines visuellen Layouts für das Dashboard zur besseren Nutzererfahrung.  
- Integration von Benachrichtigungen für erfolgreiche Aktionen wie das Hinzufügen, Bearbeiten oder Löschen eines Events.  

---
---
### 14-Dez-2024

**Task, an dem gearbeitet wird:**  
Implementierung der Homepage zur Anzeige aller öffentlichen Events.  

**Tasks completed**:  
- **Homepage anzeigen:**  
  - **Route:** `/`  
  - Eine neue Route wurde erstellt, um alle öffentlichen Events aus der Firebase-Sammlung `public_events` anzuzeigen.  
  - Die Events werden mithilfe von Firestore's `stream()`-Funktion abgerufen und in eine Liste konvertiert.  
  - Jedes Event enthält Details wie Titel, Beschreibung, Datum, Kategorie und die Event-ID. Die Event-ID wird hinzugefügt, um Links zur Event-Detailseite zu erstellen.  
  - Die Event-Daten werden an das Template `home.html` weitergeleitet, das die Events benutzerfreundlich anzeigt.  

**Challenges:**  
- Optimierung der Datenabfrage, um eine effiziente Anzeige bei einer großen Anzahl von Events sicherzustellen.  
- Sicherstellen, dass fehlende oder fehlerhafte Event-Daten korrekt behandelt werden, um das Nutzererlebnis nicht zu beeinträchtigen.  

**Next steps:**  
- Verbesserung des Layouts der Homepage, um die Event-Anzeige visuell ansprechender zu gestalten.  
- Hinzufügen von Filtern und Suchoptionen für Events basierend auf Kategorien oder Datum.  
- Integration eines Links zu den Event-Details für weitere Informationen.  
---
---
### 15-Dez-2024

**Task, an dem gearbeitet wird:**  
Initialisierung der Flask-Anwendung und Integration von Blueprints.  

**Tasks completed**:  
- **Grundstruktur der App:**  
  - Eine zentrale Flask-Anwendung wurde erstellt, um die verschiedenen Module der Anwendung zu integrieren.  
  - Konfiguration der Flask-Session mit dem Typ `filesystem`, um Benutzersitzungen zu verwalten.  

- **Blueprint-Integration:**  
  - Die folgenden Blueprints wurden registriert, um die Anwendung modular und übersichtlich zu gestalten:  
    - `auth` (Authentifizierungsrouten) mit Präfix `/auth`  
    - `dashboard` (Benutzer-Dashboard) mit Präfix `/dashboard`  
    - `event` (Event-Management-Routen) mit Präfix `/event`  
    - `home` (Homepage für öffentliche Events ohne Präfix)  
  - Diese Struktur ermöglicht eine klare Trennung der verschiedenen Routen und Funktionen.  

- **Startseite:**  
  - Die Route `/` wurde definiert, um eine Begrüßungsnachricht ("Willkommen auf der Event-Seite!") anzuzeigen.  

- **Lokaler Entwicklungsserver:**  
  - Der Entwicklungsmodus wurde aktiviert (`debug=True`), um eine schnelle Iteration und Fehlerverfolgung während der Entwicklung zu ermöglichen.  

**Challenges:**  
- Sicherstellen, dass alle Blueprints korrekt registriert und mit ihren jeweiligen Präfixen funktional sind.  
- Verwaltung der Session-Daten effizient und sicher.  

**Next steps:**  
- Verbinden der Startseite mit der `home`-Route, um die öffentlichen Events direkt anzuzeigen.  
- Optimierung der Fehlerbehandlung und Implementierung einer globalen Fehlerseite.  
- Deployment der Anwendung in einer Produktionsumgebung.  


