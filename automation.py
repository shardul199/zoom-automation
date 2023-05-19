import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Define the scope and credentials for accessing Google Sheets API
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('zoom.json', scope)

# Authenticate and access the Google Sheets API
client = gspread.authorize(credentials)

# Open the Google Sheet by its title
sheet = client.open('Zoom_Automation').sheet1

# Define the JSON data
data = {
    "account_name": "account_01",
    "archive_files": [
        {
            "download_url": "https://example.com/recording/download/Qg75t7xZBtEbAkjdlgbfdngBBBB",
            "file_extension": "JSON",
            "file_path": "/9090876528/path01/demo.mp4",
            "file_size": 165743,
            "file_type": "CHAT",
            "id": "a2f19f96-9294-4f51-8134-6f0eea108eb2",
            "individual": True,
            "participant_email": "jchill@example.com",
            "participant_join_time": "2021-03-12T02:07:27Z",
            "participant_leave_time": "2021-03-12T02:12:27Z",
            "recording_type": "chat_message",
            "status": "completed",
            "encryption_fingerprint": "abf85f0fe6a4db3cdd8c37e505e1dd18a34d9696170a14b5bc6395677472cf43",
            "number_of_messages": 150
        }
    ],
    "complete_time": "2021-03-12T02:12:27Z",
    "duration": 1,
    "duration_in_second": 1800,
    "host_id": "Dhjdfgdkg8w",
    "id": 553068284,
    "is_breakout_room": False,
    "meeting_type": "internal",
    "parent_meeting_id": "atsXxhSEQWit9t+U02HXNQ==",
    "recording_count": 2,
    "start_time": "2021-04-26T05:23:18Z",
    "timezone": "Asia/Shanghai",
    "topic": "My Personal Meeting Room",
    "total_size": 364463,
    "type": 1,
    "uuid": "yO3dfhh3t467UkQ==",
    "status": "completed"
}

# Flatten the nested JSON structure into a single level dictionary
def flatten_dict(d, parent_key='', sep='_'):
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

flattened_data = flatten_dict(data)

# Write the data to the Google Sheet
row = list(flattened_data.keys())
values = list(flattened_data.values())

sheet.append_row(row)
sheet.append_row(values)
