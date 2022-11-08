from google.oauth2 import service_account
from googleapiclient.discovery import build


def get_all_tips_from_google_sheets():
    scopes = ["https://www.googleapis.com/auth/spreadsheets"]
    service_account_file = "credentials.json"

    creds = service_account.Credentials.from_service_account_file(
        service_account_file, scopes=scopes
    )

    spreadsheet_id = "1yHSTmSJpLCh_2Vf_tUeuRbjAstHE8nricPExhO6I3_o"
    range_name = "TIPS!C2:AY150"
    service = build("sheets", "v4", credentials=creds)

    # Call the Sheets API
    request = (
        service.spreadsheets()
        .values()
        .get(spreadsheetId=spreadsheet_id, range=range_name)
    )
    response = request.execute()
    data = response.get("values", {})

    all_tips = []

    # iterate over every player tip
    for tips in data:
        player_tips = []
        # iterate over every tip in single player tips
        for tip in tips[:-1]:
            player_tips.append((tips[-1], tip))
        all_tips.append(player_tips)

    return list(zip(*all_tips))
