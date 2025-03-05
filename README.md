# 🏠 Comprehensive Property Analyzer

## Overview
The **Comprehensive Property Analyzer** is a tool that provides an in-depth assessment of a given residential property based on geocoded location data, architectural style, exterior condition scoring, and additional property features. This tool is particularly useful for real estate investors, homebuyers, and property analysts who need a structured evaluation of a property.

## Features
- **Geolocation Analysis:** Converts a given address into latitude and longitude for mapping purposes.
- **Architectural Style Breakdown:** Identifies and classifies key architectural features of the property.
- **Exterior Condition Assessment:** Scores critical exterior features, including siding, windows, foundation, and landscaping.
- **Roof Condition Evaluation:** Provides an estimated score for roofing features based on available images.
- **Overall Property Condition Rating:** Aggregates exterior and roof condition scores into an overall rating.
- **Front & Backyard Features Analysis:** Summarizes the condition and presence of various landscaping and structural elements.

## Example Analysis
**Address:** 5598 Creekview Dr, Dublin, CA 94568  
**Geocoded Location:** Latitude 37.7170234, Longitude -121.8747405  

### **Architectural Style**
- **Overall Style:** Contemporary Craftsman
- **Roof:** Gable with solar panels
- **Windows:** Double-hung, modern
- **Columns:** Tuscan/Simplified
- **Porch:** Covered with railings
- **Exterior:** Craftsman elements blended with contemporary design

### **Exterior Condition Scoring**
| Feature               | Condition Description                               | Score (1-5) |
|-----------------------|---------------------------------------------------|-------------|
| Siding Quality       | Appears in good condition; no visible damage      | 4           |
| Windows & Doors      | Well-maintained, clean                            | 4           |
| Foundation/Porch     | Appears stable and in good condition              | 4           |
| Landscaping & Driveway | Well-kept, clean                                 | 4           |

**Exterior Condition Average Score:** 4.00

### **Roof Condition Scoring**
| Feature              | Condition Description                              | Score (1-5) |
|----------------------|---------------------------------------------------|-------------|
| Shingle/Tiling      | Appears intact but not fully visible              | 4           |
| Flashing and Gutters | Limited visibility; assumed functional           | 3           |
| Structural Integrity | Appears sound                                    | 4           |

**Roof Condition Average Score:** 3.67

### **Overall Property Condition Assessment**
**Final Condition Score:** 3.83 (C1 - Excellent)

### **Front Yard Features**
- **Lawn:** Well-maintained, green
- **Trees:** Large and small trees present
- **Shrubs & Flower Beds:** Healthy and well-maintained
- **Walkways & Driveway:** Concrete, in good condition
- **Fencing:** No visible fencing

### **Backyard Features** *(Cannot be determined from images provided.)*

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/comprehensive-property-analyzer.git
   ```
2. Navigate to the project folder:
   ```sh
   cd comprehensive-property-analyzer
   ```
3. Install dependencies (if applicable):
   ```sh
   npm install  # or pip install -r requirements.txt (depending on language)
   ```
4. Run the project:
   ```sh
   npm start  # or python main.py
   ```

## Usage
1. Enter a property address to analyze.
2. The tool retrieves geolocation data and fetches images for analysis.
3. It evaluates architectural style, exterior and roof conditions, and landscaping features.
4. The system generates a final condition rating and property report.

## Contributing
We welcome contributions! Please follow these steps:
1. Fork the repository.
2. Create a new feature branch (`git checkout -b feature-branch`).
3. Commit changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License
This project is licensed under the MIT License.

## Contact
For questions or feedback, reach out to **Apollo** or submit an issue on GitHub.

---

*Disclaimer: This analysis is based on image recognition and geolocation data. A full property assessment requires an in-person inspection.*
