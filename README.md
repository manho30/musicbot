# Self-Deploy YouTube Music API

🎵 This is a YouTube Music API endpoint that allows you to search for songs, get song information, and get song thumbnails.
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

## Usage

The  API Endpoint provides three endpoints:
- `/api/search`: Searches for a song.
- `/api/info`: Gets the info of a song.
- `/api/thumbnail`: Gets the thumbnail of a song.
- `/api/download`: Downloads a song.

### Search

Searches for a song.

`GET /api/search`

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `query` | `string` | **Required**. The search query. |
| `limit` | `integer` | The number of results to return. Default is 10. Maximum is 25. |
| `page` | `integer` | The page number of the results. Default is 1. |
### Info

Gets the info of a song.

`GET /api/info`

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `id` | `string` | **Required**. The ID of the song. |


### Thumbnail

Gets the thumbnail of a song.


`GET /api/thumbnail`

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `id` | `string` | **Required**. The ID of the song. |


### Download

Downloads a song.

`GET /api/download`

#### Parameters

| Name | Type | Description |
| --- | --- | --- |
| `id` | `string` | **Required**. The ID of the song. |

## Make you own

To get started with the  Endpoint, you will need to have Python 3 installed on your machine. You can download Python 3 from the official website.

Once you have Python 3 installed, you can clone the API Endpoint repository from GitHub:

```
git clone https://github.com/manho30/musicbot.git
```

After cloning the repository, you can install the required dependencies by running the following command:

```
pip install -r requirements.txt
```

To start the API Endpoint, run the following command:

```
python api/index.py
```

The DouYin API Endpoint will now be running on `http://localhost:5000`.

## Deployment

To deploy your own API Endpoint, you can use a cloud hosting service such as Heroku or AWS. You will need to create an account with the cloud hosting service and follow their instructions for deploying a Python application.

## Technologies Used

The YouTube Music API Endpoint is built using the following technologies:

- Python 3
- Flask
- Flask-CORS
- Requests
- Ytdl-core

Thank you for using the API Endpoint! If you have any questions or feedback, please feel free to contact us.
