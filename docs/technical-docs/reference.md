---
title: Reference
parent: Technical Docs
nav_order: 3
---

{: .label }
[Jane Dane]

{: .no_toc }
# Reference documentation

{: .attention }
> This page collects internal functions, routes with their functions, and APIs (if any).
> 
> See [Uber](https://developer.uber.com/docs/drivers/references/api) or [PayPal](https://developer.paypal.com/api/rest/) for exemplary high-quality API reference documentation.
>
> You may delete this `attention` box.

<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>

## Auth Routes

### `Funktion: login()`

**Route:** `/login`

**Methods:** `GET` `POST`

**Purpose:**  
Verarbeitet die Login-Anfrage eines Nutzers. Überprüft, ob die eingegebene E-Mail und das Passwort mit den in der Firebase-Datenbank gespeicherten Nutzerdaten übereinstimmen. Bei erfolgreicher Anmeldung wird der Nutzer auf das Dashboard weitergeleitet, bei Fehlern wird eine Fehlermeldung angezeigt.

**Sample output:**  
- Erfolgreiche Anmeldung: Weiterleitung zum Dashboard.  
- Fehlermeldung: `Ungültige Anmeldeinformationen.`  

---

### `Funktion: register()`

**Route:** `/register`

**Methods:** `GET` `POST`

**Purpose:**  
Verarbeitet die Registrierung eines neuen Nutzers. Überprüft, ob die eingegebenen Passwörter übereinstimmen und ob die E-Mail-Adresse bereits vergeben ist. Bei erfolgreicher Registrierung wird der Nutzer in Firebase gespeichert und zur Login-Seite weitergeleitet.

**Sample output:**  
- Erfolgreiche Registrierung: `Benutzer erfolgreich registriert.`  
- Fehlermeldung: `Passwörter stimmen nicht überein.` oder `Benutzername bereits vergeben.`

---

### `Funktion: logout()`

**Route:** `/logout`

**Methods:** `GET`

**Purpose:**  
Verarbeitet die Abmeldung eines Nutzers. Entfernt den Nutzer aus der Sitzung (Session) und leitet ihn zurück zur Home-Seite.

**Sample output:**  
- Erfolgreiche Abmeldung: `Du hast dich erfolgreich abgemeldet.`  

---

## Additional Notes

- Die Auth-Routen sind in einer separaten `authRoute.py`-Datei definiert und in der Hauptapplikation (`app.py`) über Blueprints registriert.
- **Flask Sessions** werden verwendet, um die Benutzersitzung zu verwalten und die Anmeldeinformationen während der Sitzung zu speichern.
- **Firebase Firestore** wird verwendet, um Nutzerdaten (E-Mail und Passwort) zu speichern und zu validieren.

---
---
## Event Routes

### `Funktion: event_info(event_id)`

**Route:** `/<event_id>`

**Methods:** `GET` `POST`

**Purpose:**  
Zeigt Informationen zu einem Event an und ermöglicht es dem Event-Ersteller, Details zu aktualisieren oder das Event zu löschen. Gäste können Informationen einsehen und RSVP (Zu- oder Absage) vornehmen.

**Sample output:**  
- Anzeige der Event-Details.  
- Erfolgreiche Event-Updates oder -Löschung.  
- Fehlermeldung: `Event nicht gefunden`, wenn die Event-ID ungültig ist.

---

### `Funktion: create_event()`

**Route:** `/create`

**Methods:** `GET` `POST`

**Purpose:**  
Ermöglicht registrierten Nutzern, neue Events zu erstellen. Die Details (z. B. Titel, Beschreibung, Bild) werden in Firebase Firestore gespeichert. Event-Bilder werden im Firebase Storage hochgeladen und öffentlich zugänglich gemacht.

**Sample output:**  
- Erfolgreiche Erstellung: `Event erfolgreich erstellt.`  
- Fehlermeldung: `Benutzer nicht gefunden`, wenn der Benutzer in der Firebase-Datenbank nicht existiert.

---

### `rsvp(event_id)`

**Route:** `/<event_id>/rsvp`

**Methods:** `POST`

**Purpose:**  
Ermöglicht Nutzern, sich für ein Event an- oder abzumelden. Berücksichtigt dabei das Teilnehmerlimit und überprüft, ob der Nutzer bereits zugesagt hat.

**Sample output:**  
- Erfolgreiche Anmeldung: `Du hast dich erfolgreich für das Event angemeldet.`  
- Absage: `Du hast das Event erfolgreich abgesagt.`  
- Fehlermeldung: `Teilnehmerlimit erreicht.` oder `Du hast bereits zugesagt.`

---

### `participant_list(event_id)`

**Route:** `/<event_id>/participants`

**Methods:** `GET`

**Purpose:**  
Zeigt eine Liste aller Teilnehmer eines Events an. Diese Funktion ist nur für eingeloggte Nutzer verfügbar.

**Sample output:**  
- Anzeige der Teilnehmerliste mit Namen und E-Mails.  

---

### `delete_event_from_info(event_id)`

**Route:** `/<event_id>/delete`

**Methods:** `POST`

**Purpose:**  
Ermöglicht dem Event-Ersteller, ein Event vollständig zu löschen, einschließlich aller Teilnehmerdaten.

**Sample output:**  
- Erfolgreiche Löschung: Rückleitung zum Dashboard.  
- Fehlermeldung: `Benutzer nicht gefunden`, wenn der Benutzer in der Datenbank nicht existiert.

---

### `update_event_info(event_id)`

**Route:** `/<event_id>/update`

**Methods:** `POST`

**Purpose:**  
Erlaubt dem Event-Ersteller, die Details eines Events zu bearbeiten (z. B. Titel, Datum, Beschreibung).

**Sample output:**  
- Erfolgreiches Update: Weiterleitung zur Event-Info-Seite.  
- Fehlermeldung: `Event nicht gefunden`, wenn die Event-ID ungültig ist.

---

## Additional Notes

- **Firebase Firestore** wird für die Speicherung von Event-Daten und die Verwaltung von RSVP-Informationen verwendet.  
- **Firebase Storage** wird genutzt, um Event-Bilder hochzuladen und zu speichern.  
- **Flask Sessions** werden verwendet, um den aktuellen Benutzer zu identifizieren und Berechtigungen zu überprüfen.  
- Die Event-Routen sind in der Datei `eventRoute.py` definiert und in der Hauptanwendung (`app.py`) über Blueprints registriert. 

---
---
## Home Routes

### `home_view()`

**Route:** `/`

**Methods:** `GET`

**Purpose:**  
Zeigt alle öffentlichen Events auf der Homepage an, indem sie aus der Firebase Firestore-Sammlung `public_events` abgerufen werden. Jedes Event enthält seine ID, um Links zur Detailansicht zu erstellen.

**Sample output:**  
- Eine HTML-Seite mit einer Liste von Events und den entsprechenden Details.  

---

## Dashboard Routes

### `dashboard_view()`

**Route:** `/`

**Methods:** `GET`

**Purpose:**  
Zeigt die persönliche Event-Übersicht für den aktuell angemeldeten Benutzer an. Events werden aus der Firebase-Datenbank basierend auf der Benutzersitzung geladen.

**Sample output:**  
- Eine HTML-Seite mit der Event-Liste des Benutzers.  
- Fehlermeldung: `Benutzer nicht gefunden`, wenn der Nutzer nicht in der Datenbank existiert.  

---

### `delete_event(event_id)`

**Route:** `/delete_event/<event_id>`

**Methods:** `POST`

**Purpose:**  
Löscht ein Event aus der Firebase-Datenbank. Es wird sowohl aus der Benutzer-Unter-Sammlung als auch aus der zentralen Sammlung `public_events` entfernt.

**Sample output:**  
- Erfolgreiche Löschung: Rückleitung zur Dashboard-Seite.  
- Fehlermeldung: `Benutzer nicht gefunden`, wenn der Nutzer nicht existiert.  

---

### `login_required(f)`

**Purpose:**  
Ein Decorator, der sicherstellt, dass die jeweilige Funktion nur von authentifizierten Benutzern aufgerufen werden kann. Wenn kein Benutzer angemeldet ist, wird der Nutzer zur Login-Seite umgeleitet.

---

## Firebase Configuration

### Firestore Initialization

**File:** `fireBase_config.py`

**Purpose:**  
Initialisiert Firebase Firestore und Storage. Ermöglicht den Zugriff auf die Datenbank und die Speicherung von Dateien.

**Configuration Steps:**
1. Der Pfad zur Firebase-Dienstkonto-Datei (`MyEventDbKey.json`) wird automatisch basierend auf dem Skriptverzeichnis gefunden.
2. Der Firebase Admin SDK wird mit den Zertifikaten initialisiert.
3. Firestore und Storage werden mit den Firebase-Diensten verbunden.

**Storage Details:**  
- Der Bucket-Name lautet `mydataevent.firebasestorage.app`.  

---

### Database Connection

**Purpose:**  
Erstellt die globale Datenbankverbindung (`db`) und den Bucket (`bucket`) für die Anwendung.

---

## Additional Notes

- **Firebase Firestore**: Wird zur Speicherung von Benutzerdaten, Events und deren Details verwendet.  
- **Firebase Storage**: Speichert Event-Bilder und macht sie öffentlich zugänglich.  
- **Blueprints**: Die Routen für Homepage und Dashboard werden über die Blueprints `home` und `dashboard` registriert.  
- **Session Management**: Die Nutzer-Authentifizierung basiert auf Flask-Sessions, die in den Routen überprüft werden.
