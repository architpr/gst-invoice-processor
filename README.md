markdown
# 🧾 GST Invoice Processor

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/Flask-2.3.3-green)
![n8n](https://img.shields.io/badge/n8n-Workflow_Automation-orange)
![OCR](https://img.shields.io/badge/OCR-Tesseract-lightgrey)

*Automated GST invoice processing with AI-powered OCR and workflow automation*

</div>

## 🚀 Features

- 🖼️ **Image Upload** - Simple web interface for invoice image upload
- 🔍 **OCR Processing** - Automatic text extraction using Tesseract OCR
- 🏷️ **GST Number Extraction** - Smart pattern recognition for GSTIN
- ✅ **Validation** - Real-time GST number format validation
- 📊 **Workflow Automation** - Seamless n8n integration
- ⚡ **Fast Processing** - Quick results with minimal setup

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| **Backend** | Python, Flask |
| **OCR Engine** | Tesseract |
| **Workflow** | n8n |
| **Frontend** | HTML, CSS, JavaScript |
| **Image Processing** | OpenCV, Pillow |

## 📁 Project Structure
gst-invoice-processor/

├── ocr_server.py # Flask OCR server

├── requirements.txt # Python dependencies

├── test_gst.html # Web interface

├── n8n_workflow.json # Automation workflow

├── .gitignore # Git ignore rules

└── README.md # Project documentation 


## 🎯 Quick Start

### Prerequisites
- Python 3.8+
- Tesseract OCR
- n8n (local installation)



## Use the Application

Open test_gst.html in browser

Upload invoice image

View extracted GST details! 🎉


## 🖥️ Usage Demo

Web Interface
https://via.placeholder.com/600x400/007bff/ffffff?text=GST+Invoice+Processor


## Sample Output
json
{
  "success": true,
  
  "gst_number": "07ABCDE1234F1Z5",
  
  "invoice_number": "INV-2024-001",
  
  "invoice_date": "15/12/2024",
  
  "total_amount": "2500.00",
  
  "validation": {
    "isValid": true,
    "reason": "Valid GST number format"
  },
  
  "final_status": "VALID"

}



## 🎨 n8n Workflow
The automation workflow includes:
Webhook Trigger - Receives image data

HTTP Request - Calls Python OCR server

Data Processing - Extracts and validates GST information

Response Handler - Returns formatted results
