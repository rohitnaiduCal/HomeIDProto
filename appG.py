import base64
import requests
import json
import streamlit as st
from PIL import Image
from io import BytesIO

# Predefined API keys
GEOCODE_API_KEY = "AIz"
STREET_VIEW_API_KEY = "AIz"
STATIC_MAP_API_KEY = "AIz"
GEMINI_API_KEY = "AIz"

def analyze_images_with_gemini(street_view_image, satellite_view_image, api_key):
    """
    Send images to the Gemini API for comprehensive property analysis.

    :param street_view_image: Street view image content
    :param satellite_view_image: Satellite view image content
    :param api_key: Your Google AI API key
    :return: The analysis response from the API
    """
    # API endpoint for Gemini 1.5 Flash model
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key={api_key}"

    # Encode the images
    base64_street = base64.b64encode(street_view_image).decode('utf-8')
    base64_satellite = base64.b64encode(satellite_view_image).decode('utf-8')

    # Prepare the request payload
    payload = {
        "contents": [{
            "parts": [
                {
                    "text": (
                        "Analyze the architectural style of the house in detail. "
                        "Provide a breakdown for each feature (e.g., windows, roof, pillars, porch, exterior). "
                        "Use one concise term for the style of each feature, and provide a final concise overall style."
                        "Give a key final verdict at the top in one concise term what the architectural style is"
                    )
                },
                {
                    "text": (
                        "PLEASE FILL OUT every single thing below with either a score or detailed answer"
                        "Based on the provided images, here's an evaluation of the property's condition. Note that this is a visual assessment based on limited photographic evidence and may not encompass all aspects of the property's condition. A physical inspection would be necessary for a definitive assessment.\n\n"
                        "**Exterior Condition Scoring (Front of House)**\n\n"
                        "| Feature                     | Condition Description                                     | Score (1-5) |\n"
                        "|------------------------------|---------------------------------------------------------|-------------|\n"
                        "| Siding Quality              | Evaluate siding quality (e.g., cracks, wear).            | Score: [1-5]|\n"
                        "| Windows & Doors             | Evaluate functionality and appearance.                   | Score: [1-5]|\n"
                        "| Foundation/Porch Condition | Assess cracks, stability, and maintenance level.         | Score: [1-5]|\n"
                        "| Landscaping & Driveway      | Examine overgrowth, driveway condition, and cleanliness. | Score: [1-5]|\n\n"
                        "**Roof Condition Scoring**\n\n"
                        "| Feature              | Condition Description                                         | Score (1-5) |\n"
                        "|-----------------------|-------------------------------------------------------------|-------------|\n"
                        "| Shingle/Tiling       | Assess gaps, warping, or missing shingles.                   | Score: [1-5]|\n"
                        "| Flashing and Gutters | Examine for rust, blockages, or proper drainage.             | Score: [1-5]|\n"
                        "| Structural Integrity | Evaluate overall roof structure soundness.                   | Score: [1-5]|\n\n"
                        "**Overall Property Condition Assessment**\n\n"
                        "To calculate the overall score, average the exterior and roof scores.\n"
                        "- Exterior Average: Sum of scores divided by 4.\n"
                        "- Roof Average: Sum of scores divided by 3.\n"
                        "- Overall Average: Average of exterior and roof averages.\n"
                        "Assign a condition category (C1 to C6) based on overall average.\n\n"
                        "**Backyard Features Table**\n\n"
                        "| Feature                    | Details                                                                                     |\n"
                        "|----------------------------|---------------------------------------------------------------------------------------------|\n"
                        "| Grass Coverage            | Estimate percentage of backyard area covered with grass.                                     |\n"
                        "| Big Trees                 | Number of large trees and their condition.                                                  |\n"
                        "| Small Trees               | Number of small trees and their condition.                                                  |\n"
                        "| Shrubs                   | Number of shrubs and their condition.                                                       |\n"
                        "| Flower Beds              | Number and general condition of flower beds.                                                 |\n"
                        "| Patio                    | Condition and coverage area of patio (if present).                                           |\n"
                        "| Fences                   | Condition of fences (e.g., wooden, chain-link).                                              |\n"
                        "| Outdoor Features         | Presence and condition of outdoor elements like firepits or grills.                          |\n"
                        "| Drainage                 | Issues related to water pooling or erosion.                                                  |\n\n"
                        "**Front Lawn Features Table**\n\n"
                        "| Feature                    | Details                                                                                     |\n"
                        "|----------------------------|---------------------------------------------------------------------------------------------|\n"
                        "| Lawn Coverage            | Approximate percentage of front yard area covered with grass.                                |\n"
                        "| Grass Condition          | General health of the grass (e.g., green and lush, patchy).                                  |\n"
                        "| Flower Beds              | Number and general condition of flower beds.                                                 |\n"
                        "| Walkways                 | Condition and material of walkways.                                                          |\n"
                        "| Big Trees                | Number of large trees and their condition.                                                  |\n"
                        "| Small Trees              | Number of small ornamental trees and their condition.                                        |\n"
                        "| Shrubs                   | Number of shrubs and their condition.                                                       |\n"
                        "| Driveway                 | Condition and material of driveway.                                                          |\n"
                        "| Outdoor Features         | Presence and condition of decorative elements (e.g., fountains, lights).                    |\n"
                        "| Fencing                  | Describe any fencing present in the front yard.                                              |\n\n"
                        "Ensure that all data is returned in a clean table format for easy reading and analysis."
                    )
                },
                {
                    "inlineData": {
                        "mimeType": "image/jpeg",
                        "data": base64_street
                    }
                },
                {
                    "inlineData": {
                        "mimeType": "image/jpeg",
                        "data": base64_satellite
                    }
                }
            ]
        }]
    }

    # Headers for the request
    headers = {
        "Content-Type": "application/json"
    }

    try:
        # Send POST request to the API
        response = requests.post(url,
                                 headers=headers,
                                 data=json.dumps(payload))

        # Check if the request was successful
        response.raise_for_status()

        # Parse and return the response
        response_json = response.json()

        # Extract the generated text
        generated_text = response_json['candidates'][0]['content']['parts'][0]['text']

        return generated_text

    except requests.RequestException as e:
        print(f"Error making API request: {e}")
        return None
    except (KeyError, IndexError) as e:
        print(f"Error parsing API response: {e}")
        return None

# Function to reverse geocode an address to latitude and longitude
def get_lat_lon(address):
    geocode_url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {"address": address, "key": GEOCODE_API_KEY}

    try:
        response = requests.get(geocode_url, params=params)
        response.raise_for_status()
        data = response.json()

        if data["status"] == "OK":
            location = data["results"][0]["geometry"]["location"]
            return location["lat"], location["lng"], None
        else:
            return None, None, f"Geocoding failed: {data['status']} - {data.get('error_message', 'No additional details.')}"
    except Exception as e:
        return None, None, f"Error during geocoding: {e}"

# Function to get a Street View image using latitude and longitude
def get_street_view_image(lat, lon):
    street_view_url = "https://maps.googleapis.com/maps/api/streetview"
    params = {
        "size": "600x400",  # Image dimensions
        "location": f"{lat},{lon}",
        "key": STREET_VIEW_API_KEY,
        "fov": 90,  # Field of view
        "pitch": 10  # Angle of the camera
    }

    try:
        response = requests.get(street_view_url, params=params)
        response.raise_for_status()
        return response.content, None
    except Exception as e:
        return None, f"Error fetching Street View image: {e}"

# Function to fetch hybrid satellite map
def fetch_hybrid_map(lat, lon, zoom=20, width=600, height=400):
    static_map_url = (
        f"https://maps.googleapis.com/maps/api/staticmap?"
        f"center={lat},{lon}&zoom={zoom}&size={width}x{height}&maptype=hybrid&key={STATIC_MAP_API_KEY}"
    )

    try:
        response = requests.get(static_map_url)
        response.raise_for_status()
        return response.content, None
    except requests.exceptions.RequestException as e:
        return None, f"Error fetching hybrid map: {e}"

# Streamlit App
def main():
    st.set_page_config(page_title="Comprehensive Property Analyzer", page_icon="🏠")

    st.title("🏠 Comprehensive Property Analyzer")

    # Address input
    address = st.text_input("Enter the address to analyze:", placeholder="e.g., 1600 Amphitheatre Parkway, Mountain View, CA")

    if st.button("Analyze Property"):
        if not address:
            st.warning("Please enter an address.")
            return

        # Step 1: Geocoding
        with st.spinner("Geocoding the address..."):
            lat, lon, geo_error = get_lat_lon(address)

        if geo_error:
            st.error(geo_error)
            return

        st.success(f"Geocoded Location: Latitude {lat}, Longitude {lon}")

        # Step 2: Fetch Street View Image
        with st.spinner("Fetching front view (Street View)..."):
            street_view_content, street_view_error = get_street_view_image(lat, lon)

        if street_view_error:
            st.error(street_view_error)
            return

        st.image(street_view_content, caption="Front View (Street View)", use_container_width=True)

        # Step 3: Fetch Satellite View Image
        with st.spinner("Fetching satellite view..."):
            satellite_map_content, satellite_map_error = fetch_hybrid_map(lat, lon, zoom=20)

        if satellite_map_error:
            st.error(satellite_map_error)
            return

        st.image(satellite_map_content, caption="Satellite View (Hybrid)", use_container_width=True)

        # Step 4: Comprehensive Property Analysis
        with st.spinner("Conducting comprehensive property analysis..."):
            comprehensive_analysis = analyze_images_with_gemini(
                street_view_content,
                satellite_map_content,
                GEMINI_API_KEY
            )

        if comprehensive_analysis:
            st.subheader("Comprehensive Property Analysis")
            st.write(comprehensive_analysis)
        else:
            st.error("Unable to complete property analysis.")

if __name__ == "__main__":
    main()
