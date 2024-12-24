---
title: Daily Progress - Veysel Sam
nav_order: 1
---

{: .label }
[65Coders - Backend]

{: .no_toc }
# Daily Progress - Veysel Sam

<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>

## Daily Log

### 16-Dez-2024

**Task, an dem gearbeitet wird:**  
Erstellung der grundlegenden Frontend-Struktur mit Templates und Stylesheets.  

**Tasks completed:**  

- **Ordnerstruktur:**  
  - Ein `templates`-Ordner wurde erstellt, um die HTML-Dateien der Anwendung zu speichern.  
  - Ein `static`-Ordner wurde hinzugefügt, um die benutzerdefinierten CSS-Dateien und andere statische Ressourcen zu speichern.  
  - Eine erste CSS-Datei (`style.css`) wurde im `static`-Ordner erstellt.  

- **Basisvorlage (`base.html`):**  
  - Die Datei `base.html` dient als Grundgerüst für alle Seiten der Anwendung.  
  - Sie enthält folgende Elemente:  
    - **Doctype und Grundstruktur:** Die Datei ist als HTML5-Dokument definiert und nutzt UTF-8-Codierung.  
    - **Bootstrap-Integration:** Bootstrap 5.3.0 wurde über ein CDN eingebunden, um die Entwicklung zu erleichtern.  
    - **Benutzerdefiniertes Stylesheet:** Die Datei `style.css` wird eingebunden, um benutzerdefinierte Designs zu ermöglichen.  

- **Navigation:**  
  - Eine responsive Navigationsleiste mit den folgenden Elementen wurde implementiert:  
    - **Logo:** Ein Link zur Startseite mit dem Titel "MyEvent".  
    - **Links:** Ein Link zum Dashboard und ein Platzhalter-Link für die "Über uns"-Seite.  
    - **Session-abhängige Links:**  
      - Wenn ein Nutzer angemeldet ist: Logout-Button.  
      - Wenn kein Nutzer angemeldet ist: Links für Login und Registrierung.  

- **Flash-Nachrichten:**  
  - Ein Bereich wurde integriert, um Flash-Nachrichten anzuzeigen, die dynamisch eingebunden und bei Bedarf vom Nutzer geschlossen werden können.  

- **Hauptinhalt:**  
  - Ein `block`-Element für den Inhalt (`{% block content %}`), um Seiten-spezifischen Inhalt einzufügen, während die Basisstruktur erhalten bleibt.  

- **Footer:**  
  - Ein einfacher Footer mit dem Jahr 2024, Impressum und Datenschutz-Links wurde hinzugefügt.  

- **JavaScript:**  
  - Das Bootstrap-Bundle-Script wurde eingebunden, um interaktive Komponenten (z. B. Dropdowns, Modals) zu ermöglichen.  

**Challenges:**  
- Sicherstellen, dass die Flash-Nachrichten und session-basierten Elemente korrekt funktionieren und nahtlos in die Anwendung integriert sind.  
- Aufbau eines responsiven Designs, das sowohl auf mobilen als auch auf Desktop-Geräten gut funktioniert.  

**Next steps:**  
- Erstellung der `login.html`-Datei basierend auf der neuen Template-Struktur.  
- Anbindung der Login-Logik im Backend, um die Formularverarbeitung (Authentifizierung) zu implementieren.  
- Erweiterung der `style.css`, um spezifische Designs für die Login-Seite zu unterstützen.  

---

### 17-Dez-2024

**Task, an dem gearbeitet wird:**  
Erstellung der Login-Template-Datei (`login.html`) und Backend-Anbindung zur Verarbeitung der Login-Daten.  

**Tasks completed:**  

- **Login-Template (`login.html`):**  
  - Die Datei `login.html` basiert auf der `base.html` und implementiert den `block content`.  
  - Der Titelblock (`{% block title %}`) wurde für die Login-Seite auf "Login | MyEvent" gesetzt.  
  - **Layout und Struktur:**  
    - Das Login-Formular ist in einer zentrierten `login-container`-Box integriert.  
    - Der Header zeigt eine Überschrift mit dem Titel "Login".  

  - **Formular:**  
    - Es enthält zwei Eingabefelder:  
      - **E-Mail:** Ein Eingabefeld vom Typ `email`, das für die Eingabe der Nutzer-E-Mail konfiguriert ist.  
      - **Passwort:** Ein Eingabefeld vom Typ `password`, das eine sichere Eingabe des Nutzerpassworts ermöglicht.  
    - Beide Eingabefelder sind mit der Klasse `form-control` versehen, um Bootstrap-Styling zu nutzen.  
    - **Buttons und Links:**  
      - Ein Login-Button mit der Klasse `btn-gradient`, die den benutzerdefinierten Farbverlauf-Stil anwendet.  
      - Ein Link mit der Klasse `text-gradient`, der auf die Registrierungsseite verweist.  

  - **Styling:**  
    - Das Template nutzt vorhandene Styles aus der `style.css`, um ein ansprechendes Layout zu gewährleisten:  
      - **`login-container`:** Der Container zentriert das Login-Formular auf der Seite.  
      - **`btn-gradient`:** Der Login-Button hat einen linearen Farbverlauf für einen modernen Look.  
      - **`form-control`:** Eingabefelder sind transparent und passend zum Farbschema gestaltet.  

- **Backend-Anbindung:**  
  - Das Formular verwendet `method="POST"`, um die Eingabedaten an das Backend zu senden.  
  - Die Login-Daten werden im Backend mit einer bestehenden Authentifizierungsroute (`auth.login`) verarbeitet.  
  - Session-Handling wurde eingebunden, um die Nutzer-Session nach erfolgreichem Login zu verwalten.  

**Challenges:**  
- Sicherstellen, dass die Login-Authentifizierung sicher und effizient funktioniert.  
- Validierung der Nutzereingaben sowohl clientseitig (HTML5-Validierung) als auch serverseitig (im Backend).  

**Next steps:**  
- Implementierung einer Registrierungsseite (`register.html`), basierend auf ähnlichem Design und Layout.  
- Testen der Login-Funktionalität und Sicherstellung, dass Flash-Nachrichten korrekt angezeigt werden (z. B. bei fehlerhaften Anmeldungen).  
- Erweiterung des Dashboards für eingeloggte Nutzer mit dynamischen Inhalten. 
---
---

### 18-Dez-2024

**Task, an dem gearbeitet wird:**  
Erstellung der Registrierungsseite (`register.html`) und Implementierung der Backend-Logik für die Benutzerregistrierung.  

**Tasks completed:**  

- **Registrierungs-Template (`register.html`):**  
  - Die Datei `register.html` basiert auf der `base.html` und implementiert den `block content`.  
  - Der Titelblock (`{% block title %}`) wurde für die Registrierungsseite auf "Registrierung | MyEvent" gesetzt.  
  - **Layout und Struktur:**  
    - Das Registrierungsformular ist in einer zentrierten `register-container`-Box integriert.  
    - Der Header zeigt eine Überschrift mit dem Titel "Registrierung".  

  - **Formular:**  
    - Es enthält vier Eingabefelder:  
      - **Benutzername:** Ein Eingabefeld vom Typ `text` für den Nutzernamen.  
      - **E-Mail:** Ein Eingabefeld vom Typ `email`, das für die Eingabe der Nutzer-E-Mail konfiguriert ist.  
      - **Passwort:** Ein Eingabefeld vom Typ `password` für die Passwort-Eingabe.  
      - **Passwort bestätigen:** Ein weiteres Eingabefeld vom Typ `password` für die Bestätigung des Passworts.  
    - Alle Eingabefelder sind mit der Klasse `form-control` versehen, um Bootstrap-Styling zu nutzen.  
    - **Buttons und Links:**  
      - Ein Registrierungsbutton mit der Klasse `btn-gradient`, die den benutzerdefinierten Farbverlauf-Stil anwendet.  
      - Ein Link mit der Klasse `text-gradient`, der auf die Login-Seite verweist.  

  - **Styling:**  
    - Das Template nutzt vorhandene Styles aus der `style.css`, um ein einheitliches Design sicherzustellen:  
      - **`register-container`:** Der Container zentriert das Formular auf der Seite.  
      - **`btn-gradient`:** Der Button hat einen modernen Farbverlauf.  
      - **`form-control`:** Eingabefelder sind transparent und passen zum Farbschema.  

- **Backend-Logik zur Registrierung neuer Nutzer:**  
  - Eine neue Route wurde für die Benutzerregistrierung implementiert (`@auth.route('/register', methods=['GET', 'POST'])`).  
  - **Funktionsweise:**  
    - Beim Aufruf der Seite mit `GET` wird das `register.html`-Template gerendert.  
    - Bei `POST` wird die Formulareingabe verarbeitet und geprüft:  
      - Überprüfung, ob der Benutzername oder die E-Mail-Adresse bereits existieren.  
      - Validierung der Passwort- und Bestätigungspasswort-Felder (müssen übereinstimmen).  
      - Sicherstellen, dass alle Eingaben die erforderlichen Kriterien erfüllen (z. B. gültige E-Mail, Passwortlänge).  
    - Bei erfolgreicher Registrierung wird das Passwort mit einer sicheren Hashing-Methode (`werkzeug.security.generate_password_hash`) verschlüsselt.  
    - Ein neuer Benutzer wird in die Datenbank eingefügt und eine Success-Nachricht angezeigt.  

  - **Fehlerbehandlung:**  
    - Falls die Eingaben nicht korrekt sind oder der Benutzer existiert, werden entsprechende Flash-Nachrichten angezeigt (z. B. "E-Mail-Adresse ist bereits registriert").  
    - Sicherheitsmaßnahmen wie die Verwendung von prepared statements verhindern SQL-Injections.  

  - **Datenbank-Modell:**  
    - Die Benutzer werden in einer `User`-Tabelle gespeichert, die mindestens folgende Felder enthält:  
      - `id`: Primärschlüssel.  
      - `username`: Benutzername (eindeutig).  
      - `email`: E-Mail-Adresse (eindeutig).  
      - `password`: Gehashter Passwort-String.  

- **Flash-Nachrichten:**  
  - Erfolgreiche und fehlerhafte Registrierungsversuche werden durch Flash-Nachrichten angezeigt, die in der `base.html` dynamisch eingebunden sind.  

**Challenges:**  
- Sicherstellen, dass alle Sicherheitsmaßnahmen (z. B. Passwort-Hashing, Validierungen) korrekt implementiert sind.  
- Ausbalancieren der Client-seitigen Validierung (HTML5) mit der Server-seitigen, um robuste Sicherheits- und UX-Standards zu gewährleisten.  

**Next steps:**  
- Testen des kompletten Registrierungs-Workflows:  
  - Eingabe-Validierung.  
  - Flash-Nachrichten.  
  - Datenbankeinträge.  
- Integration von Unit-Tests für die Backend-Registrierungslogik.  
- Aufbau einer Login-Authentifizierung mit Session-Management und Zugriffsbeschränkungen.  
---
---



## Daily Log

### 19-Dez-2024

**Task, an dem gearbeitet wird:**  
Erstellung der Event-Erstellungsseite (`createEvent.html`) und Backend-Integration zur Verarbeitung von Event-Daten.

**Tasks completed:**  

- **Event-Erstellungsseite (`createEvent.html`):**  
  - Die Datei ermöglicht es Nutzern, neue Events über ein Formular zu erstellen.  
  - Sie basiert auf der `base.html` und erweitert diese mit einem spezifischen Inhalt (`{% block content %}`).  
  - Der Titel der Seite ist `Event erstellen | MyEvent`.  

  - **Formular-Elemente:**  
    - **Name:** Eingabefeld für den Namen des Events (`type="text"`, erforderlich).  
    - **Beschreibung:** Textbereich für eine Beschreibung des Events (`textarea`, erforderlich).  
    - **Datum:** Eingabefeld für das Datum des Events (`type="date"`, erforderlich).  
    - **Ort:** Eingabefeld für die Eingabe des Veranstaltungsortes (`type="text"`, erforderlich).  
      - Dynamische Fehlermeldungen werden angezeigt, falls die Eingabe des Orts nicht den Anforderungen entspricht.  
    - **Eventbild:** Dateiupload-Feld für ein Eventbild (`type="file"`, nur Bildformate).  
    - **Format:** Dropdown-Menü mit den Optionen `Online` und `Präsenz`.  
    - **Gerät/Plattform:** Dropdown-Menü mit den Optionen `Konsole`, `PC`, `Handy` und `Alle`.  
    - **Kategorie:** Dropdown-Menü mit verschiedenen Kategorien wie `Action`, `Abenteuer`, `Rollenspiele (RPGs)` etc. (erforderlich).  
    - **Tags:** Eingabefeld für Schlagwörter, die durch Kommata getrennt eingegeben werden können.  
    - **Maximale Teilnehmerzahl:** Eingabefeld für die maximale Teilnehmeranzahl (`type="number"`, Mindestwert 1, erforderlich).  
    - **Submit-Button:** Ein Button mit der Klasse `btn-gradient`, der das Formular absendet.  

  - **Styling:**  
    - `create-event-container`: Der Hauptcontainer sorgt für eine zentrierte und aufgeräumte Darstellung des Formulars.  
    - Bootstrap-Klassen wie `form-control`, `form-select` und `btn-gradient` werden genutzt, um ein einheitliches und modernes Design zu gewährleisten.  

- **Backend-Integration zur Verarbeitung der Event-Daten:**  
  - Eine neue Route wurde für die Event-Erstellung implementiert (`@event.route('/create', methods=['GET', 'POST'])`).  
  - **Funktionsweise:**  
    - Beim Aufruf mit `GET` wird die Seite `createEvent.html` gerendert.  
    - Bei `POST` werden die Formulardaten ausgelesen und validiert:  
      - **Validierung:**  
        - Sicherstellen, dass alle Pflichtfelder ausgefüllt sind.  
        - Prüfen, ob das hochgeladene Bild den Anforderungen entspricht (Dateityp und Größe).  
      - **Speicherung:**  
        - Die Event-Daten werden in der Datenbank gespeichert, einschließlich der Metadaten des hochgeladenen Bilds.  
        - Die Datei wird im entsprechenden Ordner auf dem Server abgelegt.  
      - **Flash-Nachrichten:**  
        - Erfolgreiche Erstellung eines Events: Nachricht wie "Event erfolgreich erstellt."  
        - Fehlerhafte Eingaben: Dynamische Flash-Nachrichten, die dem Nutzer Hinweise zur Korrektur geben.  

  - **Datenbank-Modell:**  
    - Die `Event`-Tabelle speichert:  
      - `id`: Primärschlüssel.  
      - `title`: Name des Events.  
      - `description`: Beschreibungstext.  
      - `date`: Datum des Events.  
      - `location`: Veranstaltungsort.  
      - `image`: Dateiname des hochgeladenen Bildes.  
      - `format`: Event-Format (`Online` oder `Präsenz`).  
      - `platform`: Zielplattform (`Konsole`, `PC`, `Handy`, `Alle`).  
      - `category`: Kategorie des Events.  
      - `tags`: Liste von Schlagwörtern, getrennt durch Kommata.  
      - `max_participants`: Maximale Anzahl der Teilnehmer.  

**Challenges:**  
- Sicherstellen, dass hochgeladene Bilder korrekt validiert und gespeichert werden.  
- Dynamische Validierung von Eingabefeldern wie `location` und `tags`.  
- Aufbau einer robusten Fehlerbehandlung für Benutzer-Feedback.  

**Next steps:**  
- Testen der Event-Erstellung mit unterschiedlichen Eingabewerten (z. B. leere Felder, ungültige Bildformate).  
- Implementierung der Anzeige aller erstellten Events auf einer separaten Seite (`events.html`).  
- Einbindung eines Features zur Bearbeitung und Löschung von Events.
---
---

### 20-Dez-2024

**Task, an dem gearbeitet wird:**  
Erstellung und Implementierung von Event-Detailseiten für angemeldete (`eventInfo.html`) und nicht angemeldete Nutzer (`eventInfoGuest.html`).  

---

### Event-Detailseite (`eventInfo.html`)

- **Funktionalität:**  
  - Zeigt die Details eines ausgewählten Events für angemeldete Nutzer an.  
  - Ermöglicht es Nutzern, Events zu bearbeiten, zu löschen oder die Teilnehmerliste einzusehen.  

- **Aufbau der Seite:**  
  - **Event-Darstellung:**  
    - Event-Bild: Dynamisch aus der Datenbank geladen, Standardbild bei fehlendem Event-Bild.  
    - Event-Details: Titel, Datum, Ort, Kategorie, Format, Plattform, Tags und Teilnehmeranzahl.  
  - **Bearbeitungsbereich:**  
    - Eingabefelder und Dropdown-Menüs zur Bearbeitung von Event-Daten (z. B. Titel, Datum, Kategorie).  
    - Neue Felder für **Format** (Online/Präsenz) und **Plattform** (Konsole, PC, Handy).  
    - Formular für das Löschen von Events.  
  - **Teilnehmerliste:**  
    - Link zur Seite mit einer vollständigen Liste der Event-Teilnehmer.  

- **Backend-Integration:**  
  - Route: `@event.route('/info/<event_id>', methods=['GET', 'POST'])`  
    - **GET:** Lädt die Event-Daten und rendert die `eventInfo.html`.  
    - **POST:**  
      - Aktualisiert die Event-Daten in der Datenbank, wenn das Bearbeitungsformular gesendet wird.  
      - Löscht das Event bei Absendung des Löschformulars.  
  - Datenvalidierung: Sicherstellung, dass alle Pflichtfelder korrekt ausgefüllt sind.  
  - Teilnehmerzählung: Anzeige der aktuellen Teilnehmerzahl im Vergleich zum Maximum.  

---

### Event-Detailseite für Gäste (`eventInfoGuest.html`)

- **Funktionalität:**  
  - Zeigt Event-Details an, ohne Bearbeitungs- oder Löschoptionen.  
  - Bietet Gästen die Möglichkeit, sich über ein RSVP-Formular für das Event anzumelden.  

- **Aufbau der Seite:**  
  - **Event-Darstellung:**  
    - Ähnlich wie bei `eventInfo.html`, jedoch ohne Bearbeitungs- und Löschfunktionen.  
  - **RSVP-Bereich:**  
    - Formular zur Anmeldung: Erfordert Vorname, Nachname und E-Mail-Adresse.  
    - Dynamische Anzeige:  
      - Bei vollem Teilnehmerlimit wird eine Warnung angezeigt.  
      - Wenn der Nutzer bereits zugesagt hat, erscheint eine Bestätigungsmeldung mit der Option, abzusagen.  

- **Backend-Integration:**  
  - Route: `@event.route('/guest/<event_id>', methods=['GET', 'POST'])`  
    - **GET:** Lädt die Event-Daten und rendert `eventInfoGuest.html`.  
    - **POST:**  
      - Fügt die RSVP-Daten in der Datenbank hinzu, wenn das Formular gesendet wird.  
      - Löscht die RSVP-Daten, falls die Absageoption gewählt wird.  
  - Validierung: Überprüfung von Feldern wie E-Mail-Adresse und Doppelanmeldungen.  
  - Teilnehmerzählung: Dynamische Anpassung der Anzeige basierend auf der aktuellen Teilnehmerzahl.  

---

### Unterschiede zwischen `eventInfo.html` und `eventInfoGuest.html`

| **Feature**                  | **eventInfo.html**                    | **eventInfoGuest.html**             |
|-------------------------------|---------------------------------------|-------------------------------------|
| Event-Details anzeigen       | ✅                                    | ✅                                  |
| Event bearbeiten/löschen     | ✅                                    | ❌                                  |
| Teilnehmerliste anzeigen     | ✅                                    | ❌                                  |
| RSVP-Bereich                 | ❌                                    | ✅                                  |
| Anzeige für nicht angemeldet | ❌                                    | ✅                                  |

---

**Challenges:**  
- Verwaltung von zwei getrennten Ansichten mit ähnlichen Datenquellen.  
- Sicherstellen, dass nicht angemeldete Nutzer keine Bearbeitungsrechte erhalten.  
- Dynamische Validierung für die RSVP-Funktion bei `eventInfoGuest.html`.  

**Next steps:**  
- Integration von Testfällen für beide Seiten.  
- Optimierung der Ladezeit durch bessere Bildkomprimierung.  
- Styling-Feinschliff für beide Seiten, um eine einheitliche Nutzererfahrung zu gewährleisten.
---
---

### 20-Dez-2024

**Task:**  
Erstellung eines nutzerspezifischen Dashboards zur Verwaltung eigener Events.

---

### Dashboard (`dashboard.html`)

- **Funktionalität:**  
  - Bietet Nutzern eine Übersicht über alle von ihnen erstellten Events.  
  - Ermöglicht die Verwaltung von Events:  
    - Details eines Events anzeigen.  
    - Events löschen.  
  - Bietet eine Schaltfläche zur Erstellung neuer Events.

- **Aufbau der Seite:**  
  - **Header:**  
    - Begrüßung des Nutzers mit personalisierter Ansprache (`{{ user }}`).  
    - Schaltfläche "Event erstellen", die zur `createEvent`-Seite führt.  
  - **Eventliste:**  
    - Anzeige aller erstellten Events in einer dynamischen Kartenansicht.  
    - Pro Event:  
      - Titel, Datum und Ort in der Kartenansicht.  
      - Schaltflächen:  
        - "Mehr erfahren": Führt zur Detailseite (`eventInfo.html`).  
        - "Löschen": Sendet eine POST-Anfrage, um das Event aus der Datenbank zu entfernen.  
  - **Fehlermeldung:**  
    - Hinweis, wenn der Nutzer keine Events erstellt hat.

---

### Backend-Integration:

- **Route:** `@dashboard.route('/dashboard', methods=['GET'])`  
  - Lädt alle Events des angemeldeten Nutzers aus der Datenbank und übergibt diese an das Dashboard-Template.  
  - Datenmodell:  
    - `user`: Name oder Benutzerkennung des eingeloggten Nutzers.  
    - `events`: Liste aller Events, die mit dem Nutzer verknüpft sind.

- **Event-Löschung:**  
  - Route: `@event.route('/delete/<event_id>', methods=['POST'])`  
  - Überprüfung:  
    - Nutzerberechtigung: Nur der Ersteller des Events darf dieses löschen.  
    - Erfolgreiche Löschung führt zu einem Reload des Dashboards.

---

### Key Features im Dashboard

| **Feature**            | **Beschreibung**                                                                 |
|-------------------------|----------------------------------------------------------------------------------|
| Begrüßung              | Zeigt den Namen des angemeldeten Nutzers an.                                     |
| Event erstellen        | Weiterleitung zu einem Formular zur Erstellung eines neuen Events.               |
| Eventliste             | Dynamische Darstellung aller Events des Nutzers.                                 |
| Eventdetails           | Verlinkung zu detaillierten Informationen und Bearbeitungsmöglichkeiten.         |
| Event löschen          | Direkte Option, ein Event über eine Schaltfläche zu entfernen.                   |
| Leerer Zustand         | Benutzerfreundliche Nachricht bei Abwesenheit von Events im Dashboard.           |

---

### Herausforderungen:

- **Dynamische Kartenansicht:**  
  Optimierung der Darstellung für verschiedene Bildschirmgrößen (Responsivität mit Bootstrap).  
- **Löschfunktion:**  
  Vermeidung von ungewolltem Löschen durch zusätzliche Bestätigungsdialoge (noch zu implementieren).  
- **Fehlermeldungen:**  
  Sicherstellen, dass Fehler (z. B. unberechtigter Zugriff) klar an den Nutzer kommuniziert werden.

---

### Nächste Schritte:

- **Optimierungen:**  
  - Implementierung eines Bestätigungsdialogs vor dem Löschen eines Events.  
  - Hinzufügen einer "Bearbeiten"-Option direkt im Dashboard.  
  - Styling-Verbesserungen, um die Eventkarten visuell hervorzuheben.  
- **Testing:**  
  - Sicherstellen, dass die Lösch- und Detailansicht-Links korrekt funktionieren.  
  - Testen auf verschiedenen Geräten und Browsern.
  ---
  ---

 

### 21-Dez-2024

**Task:**  
Erstellung der Teilnehmerliste für ein Event (`participantList.html`).

---

### Teilnehmerliste (`participantList.html`)

- **Funktionalität:**  
  - Bietet eine übersichtliche Darstellung aller Teilnehmer eines Events.  
  - Ermöglicht Veranstaltern, Teilnehmern per Klick abzusagen.  
  - Leitet bei Bedarf zurück zur Eventseite.

- **Aufbau der Seite:**  
  - **Header:**  
    - Titel der Seite: "Teilnehmerliste".  
    - Button: "Zurück zum Event".  
  - **Teilnehmertabelle:**  
    - Strukturierte Auflistung von Teilnehmerdaten (Vorname, Nachname, E-Mail).  
    - Schaltfläche, um eine RSVP (Teilnahmebestätigung) zu stornieren.  
  - **Leerer Zustand:**  
    - Hinweis, wenn es noch keine Teilnehmer gibt.

- **Besonderheiten:**  
  - Dynamische Datenübertragung über die Variable `participants`.  
  - Formulargestütztes Entfernen von Teilnehmern (`cancel_rsvp`), das eine POST-Anfrage an die entsprechende Route im Backend sendet.

---

### Backend-Integration:

- **Route:** `@event.route('/participants/<event_id>', methods=['GET'])`  
  - Lädt alle Teilnehmer eines spezifischen Events aus der Datenbank und übergibt diese an das Template.  
  - Datenmodell:  
    - `participants`: Liste der Teilnehmer (Vorname, Nachname, E-Mail).  
    - `event_id`: ID des aktuellen Events.

- **Absagefunktion:**  
  - Route: `@event.route('/rsvp/<event_id>', methods=['POST'])`  
  - Überprüfung:  
    - Nur der Veranstalter kann eine Teilnahme stornieren.  
    - Erfolgreiche Absage führt zu einem Reload der Teilnehmerliste.

---

### Herausforderungen:

- **Absage-Funktion:**  
  Integration einer Bestätigung (Modal oder Dialog), um versehentliche Löschungen zu vermeiden (geplant).  
- **Responsivität:**  
  Sicherstellen, dass die Tabelle auch auf mobilen Geräten gut lesbar bleibt.

---

### 22-Dez-2024

**Task:**  
Erstellung der Startseite mit einer Übersicht aller Events und Filteroptionen (`home.html`).

---

### Startseite (`home.html`)

- **Funktionalität:**  
  - Zeigt alle verfügbaren Events an, inklusive relevanter Details (Titel, Datum, Ort, Teilnehmerzahl).  
  - Ermöglicht eine detaillierte Suche durch Filter wie Kategorie, Plattform und Format.  
  - Zeigt aktive Filter und Tags an.

- **Aufbau der Seite:**  
  - **Titel:** "Alle Events".  
  - **Suchformular:**  
    - Eingabefeld für eine Stichwortsuche.  
    - Dropdown-Menüs für Filteroptionen: Kategorie, Plattform, Format.  
    - Such-Button.  
  - **Aktive Filter:**  
    - Anzeige der angewandten Filter mit der Möglichkeit, diese zurückzusetzen.  
  - **Liste aller Tags:**  
    - Anklickbare Tags, um die Suche schnell einzugrenzen.  
  - **Eventkarten:**  
    - Darstellung der Events in einer dynamischen Kartenansicht mit Informationen wie Titel, Datum, Ort, Kategorie, Format und RSVP-Status.  

---

### Backend-Integration:

- **Route:** `@home.route('/', methods=['GET'])`  
  - Lädt alle verfügbaren Events aus der Datenbank und übergibt diese an das Template.  
  - Datenmodell:  
    - `events`: Liste der Events mit Details (Titel, Datum, Ort, Kategorie, Plattform, Format, Tags, Teilnehmerzahl, Maximalanzahl).  
    - `all_tags`: Liste aller verfügbaren Tags.  

---

### Key Features in beiden Seiten

| **Seite**          | **Feature**                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| Teilnehmerliste     | Teilnehmer anzeigen, Teilnahme absagen, Zurück zum Event.                  |
| Startseite          | Suchfilter, dynamische Tags, Eventkarten mit RSVP-Status und Filteroptionen.|

---

### Herausforderungen und Lösungen:

- **Filterlogik:**  
  Implementierung einer komplexen Filterung basierend auf mehreren Kriterien (Backend + Frontend).  
- **Benutzererfahrung:**  
  Sicherstellen, dass die Filter und Tags intuitiv und leicht zugänglich sind.  
- **Design:**  
  Optimierung der Kartenansicht für verschiedene Bildschirmgrößen (Bootstrap).  

---

### Nächste Schritte:

- **Teilnehmerliste:**  
  - Hinzufügen eines Modals zur Bestätigung der Absage.  
  - Anzeige der Gesamtzahl der Teilnehmer.  
- **Startseite:**  
  - Verbesserung der Tag-Auswahl durch multiselektive Filterung.  
  - Hinzufügen einer Pagination für lange Eventlisten.  
  - Anzeige eines Loaders während der Filterung.


