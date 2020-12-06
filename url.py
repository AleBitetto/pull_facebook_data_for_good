def format_urls(dataset_name: str, dataset_id: str, download_dates: list):
    """Function to format urls with the appropriate format"""

    # Define base urls for each supported dataset
    # Move this into a config in the future
    base_urls = {
        "TileMovement": "https://www.facebook.com/geoinsights-portal/downloads/vector/?id={}&ds={}"
    }

    # Define date formats for download urls of each dataset
    date_formats = {"TileMovement": "%Y-%m-%d+%H%M"}

    # Define the appropriate base_url
    base_url = base_urls[dataset_name]

    # Define the appropriate date_format
    date_format = date_formats[dataset_name]

    # List of download urls
    urls = []

    # For each download date, format a download url and record dataset date
    for date in download_dates:

        urls.append(
            {
                "url": base_url.format(dataset_id, date.strftime(date_format)),
                "date": date,
            }
        )

    # Return a list of url, date pair dictionaries
    return urls
