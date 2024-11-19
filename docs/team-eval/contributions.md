---
title: Contributions
parent: Team Evaluation
nav_order: 4
---

{: .label }
[65Coders]

{: .no_toc }
# Summary of individual contributions

<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>

## [Lamine Touré]

Contributions
: **Backend-Entwicklung mit Flask**
  - Integration von Firebase-Diensten (Firestore, Auth, Storage) in die Flask-App.
  - Entwicklung der **Session-Verwaltung** für Event-Ersteller:
    - Einrichtung eines Login-Systems mit Session-Tracking für Event-Ersteller.
    - Sicherstellen, dass nur angemeldete Nutzer Zugriff auf die Event-Erstellungsseite haben.
  - Aufbau der **RESTful APIs** für:
    - Registrierung und Login von Event-Erstellern.
    - Erstellung von Events (inklusive Speichern der Daten und Hochladen von Bildern).
    - RSVP-Funktion für Nutzer (Zähler für Teilnahme).
  - Implementierung von Sicherheitsmaßnahmen in der Firebase-Konfiguration:
    - Zugriffsbeschränkungen für das Schreiben und Lesen von Daten.
    - Schutz der Eventbilder in Firebase Storage.
  - Unit-Tests und Debugging:
    - Validierung der APIs.
    - Sicherstellen der korrekten Session- und Fehlerbehandlung.
  - Deployment des Backends auf einer Plattform (z. B. Heroku).

: **Kenntnis-Verbesserung**
  - Erweiterung der Fähigkeiten in **Datenbankintegration** (Firestore) und **Session-Management** mit Flask.

---

## [Veysel Sam]

Contributions
: **Frontend-Design und Benutzeroberfläche**
  - Aufbau der **Projektstruktur für das Frontend**:
    - Organisation von HTML-Dateien in `templates/` und statischen Dateien in `static/`.
  - Gestaltung des Layouts:
    - Erstellung einer Basisvorlage (`base.html`) mit Navigation und Footer.
    - Dynamisches Anzeigen des Session-Status für Event-Ersteller.
  - Entwicklung der Benutzeroberfläche:
    - **Startseite** mit Veranstaltungsübersicht (Karten- oder Listenansicht).
    - **Such- und Filterleiste** für Veranstaltungen nach Thema oder Datum.
    - **Event-Detailseite** mit Titel, Beschreibung, Ort, Datum, Thema und Bild.
    - Integration des RSVP-Buttons mit visuellem Feedback.
  - Styling und Branding:
    - Einheitliches Design mit einer konsistenten Farbpalette, Schriftarten und responsivem Layout (Bootstrap).
    - Sicherstellen, dass die Benutzeroberfläche mobilfreundlich ist.
  - Entwicklung der **Login- und Registrierungsseiten** für Event-Ersteller:
    - Formulare für Anmeldung und Registrierung mit Firebase Auth.
    - Session-Statusanzeige basierend auf dem Login-Zustand.
  - **Event-Erstellungsseite**:
    - Gestaltung eines benutzerfreundlichen Formulars für die Eingabe von Eventdetails.
    - Bild-Upload-Funktion mit Integration in Firebase Storage.
  - Testing und Deployment:
    - Cross-Browser-Tests und Usability-Tests.
    - Deployment des Frontends auf einer Plattform (z. B. Netlify oder Vercel).

: **Kenntnis-Verbesserung**
  - Erweiterung der Fähigkeiten in **UI/UX-Design**, responsivem Webdesign und Frontend-Interaktion mit Firebase SDK.
