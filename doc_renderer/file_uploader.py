from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload


class FileUploader:
    service = None

    def create(self, credentials: Credentials):
        self.service = build('drive', 'v3', credentials=credentials)

    def upload(self, title: str, path: str):
        file_metadata = {'name': title}
        media = MediaFileUpload(path, mimetype='image/png')

        # pylint: disable=maybe-no-member
        file = self.service.files().create(body=file_metadata, media_body=media, fields='webContentLink').execute()
        print(F'File webContentLink: {file.get("webContentLink")}')
