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


