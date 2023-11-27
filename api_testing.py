import requests
import json

BASE_URL = "http://localhost:8000/versicherung/api/mitarbeiter/"  # Ändern Sie dies zu Ihrer Basis-URL


def list_mitarbeiter():
    response = requests.get(BASE_URL)
    print("Liste der Mitarbeiter:")
    print(response.json())


def create_mitarbeiter(data):
    response = requests.post(
        BASE_URL + "create/",
        data=json.dumps(data),
        headers={"Content-Type": "application/json"},
    )
    print("Erstellen eines Mitarbeiters:")
    print(response.json())


def retrieve_mitarbeiter(pk):
    response = requests.get(BASE_URL + f"{pk}/")
    print(f"Abrufen von Mitarbeiter {pk}:")
    print(response.json())


def update_mitarbeiter(pk, data):
    response = requests.put(
        BASE_URL + f"{pk}/update/",
        data=json.dumps(data),
        headers={"Content-Type": "application/json"},
    )
    print(f"Aktualisieren von Mitarbeiter {pk}:")
    print(response.json())


def delete_mitarbeiter(pk):
    response = requests.delete(BASE_URL + f"{pk}/delete/")
    print(f"Löschen von Mitarbeiter {pk}:")
    print(response.status_code)


# Testen der Funktionen
list_mitarbeiter()

# Daten für einen neuen Mitarbeiter - Ändern Sie diese entsprechend
new_mitarbeiter = {
    "user": 3,  # Hier eine gültige Benutzer-ID einfügen
    "position": "agent",
    "geburtsdatum": "1990-01-01",
    "einstellungsdatum": "2023-01-01",
    "telefonnummer": "1233245617890",
}
# create_mitarbeiter(new_mitarbeiter)

# Mitarbeiter abrufen - Setzen Sie eine gültige ID ein
# retrieve_mitarbeiter(25)

# Mitarbeiter aktualisieren - Setzen Sie eine gültige ID ein und ändern Sie die Daten
# update_mitarbeiter(25, {"position": "manager"})
# retrieve_mitarbeiter(25)


# Mitarbeiter löschen - Setzen Sie eine gültige ID ein
# delete_mitarbeiter(25)

# retrieve_mitarbeiter(25)
