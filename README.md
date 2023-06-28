# AstroFetch

This project allows you to download NASA's Astronomy Picture of the Day (APOD) images for a specific date range. It utilizes the NASA APOD API to fetch the image data and saves the images locally.

## Prerequisites

- Python 3.0 or higher
- `requests` library (can be installed via `pip install requests`)

## Usage

1. Obtain an API key from the NASA API website by registering at https://api.nasa.gov/.
2. Modify the file `params.json` in the project directory with the required parameters:
   - "start_date": The start date of the range in the format "yyyy-mm-dd".
   - "end_date": The end date of the range in the format "yyyy-mm-dd".
   - "api_key": Your API key obtained from NASA.
   - "thumbs": Keep `true` in order to avoid errors.
3. Run the `main.py` script to initiate the image download process:
   The script will fetch the APOD image data for each date within the specified range and save the images in the `images` directory. If an image already exists with the same title, it will skip the download for that particular image.
4. The downloaded images can be found in the `images` directory.

## Deleting Images

To delete all the images stored in the `images` directory, you can run the `deleteImages.py` script inside the `assets` folder.

This will remove all the files inside the `images` directory.

## License

This project is licensed under the MIT License.

Feel free to modify and enhance the code according to your requirements.

**Note:** Ensure that you comply with NASA's usage guidelines and terms when using their APOD API.

For further details, refer to the official NASA APOD API documentation at https://api.nasa.gov/.
