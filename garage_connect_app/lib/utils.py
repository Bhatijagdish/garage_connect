from datetime import datetime


def transform_response(data):
    """
    rdw API data transform as per the need so it can be used within ajax request
    """
    data = data[0]

    # merk and handelsbenaming as it is
    merk = data["merk"]
    handelsbenaming = data["handelsbenaming"]

    # only extracting year from datum_eerste_toelating
    manufacture_date = data["datum_eerste_toelating"][:4]

    # converting the date into readable format
    original_date = datetime.strptime(data["datum_tenaamstelling"], "%Y%m%d")
    apk_date = original_date.strftime("%d-%m-%Y")

    new_data = {
        "merk": merk,
        "model": handelsbenaming,
        "bouwjaar": manufacture_date,
        "apk_vervaldatum": apk_date
    }

    return new_data