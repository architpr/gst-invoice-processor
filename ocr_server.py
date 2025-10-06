from flask import Flask, request, jsonify
import pytesseract
import cv2
import re
import base64
import numpy as np
from io import BytesIO
from PIL import Image
import os

app = Flask(__name__)

# Set tesseract path for Windows
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

print("✅ GST OCR Server Starting...")
print("📁 Working directory:", os.getcwd())

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "active", "message": "GST OCR Server is running"})

@app.route('/process-invoice', methods=['POST'])
def process_invoice():
    try:
        # Get JSON data from n8n
        data = request.get_json()
        if not data:
            return jsonify({"success": False, "error": "No JSON data received"})
            
        image_data = data.get('image', '')
        
        print("📨 Received image data for processing")
        
        if not image_data:
            return jsonify({"success": False, "error": "No image data received"})
        
        # Remove base64 prefix if present
        if 'base64,' in image_data:
            image_data = image_data.split('base64,')[1]
        
        # Decode base64 image
        image_bytes = base64.b64decode(image_data)
        image = Image.open(BytesIO(image_bytes))
        
        # Convert to OpenCV format
        img = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        print("🔍 Running OCR...")
        # OCR processing
        text = pytesseract.image_to_string(gray)
        print("✅ OCR Completed")
        
        # Extract GST number
        gst_pattern = r'[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z]{1}[1-9A-Z]{1}[Z]{1}[0-9A-Z]{1}'
        gst_match = re.search(gst_pattern, text)
        gst_number = gst_match.group(0) if gst_match else "Not Found"
        
        # Extract invoice number
        invoice_pattern = r'Invoice No[:\\s]*([A-Za-z0-9-\\/]+)'
        invoice_match = re.search(invoice_pattern, text, re.IGNORECASE)
        invoice_number = invoice_match.group(1) if invoice_match else "Not Found"
        
        # Extract date
        date_pattern = r'\\d{1,2}/\\d{1,2}/\\d{4}'
        date_match = re.search(date_pattern, text)
        invoice_date = date_match.group(0) if date_match else "Not Found"
        
        # Extract amount
        amount_pattern = r'Total[:\\s]*[₹]?\\s*(\\d+(?:\\.\\d{2})?)'
        amount_match = re.search(amount_pattern, text, re.IGNORECASE)
        total_amount = amount_match.group(1) if amount_match else "Not Found"
        
        result = {
            "success": True,
            "gst_number": gst_number,
            "invoice_number": invoice_number,
            "invoice_date": invoice_date,
            "total_amount": total_amount,
            "raw_text": text[:300] + "..." if len(text) > 300 else text,
            "status": "processed"
        }
        
        print("🎉 Extraction successful")
        print(f"   GST: {gst_number}, Invoice: {invoice_number}, Amount: {total_amount}")
        return jsonify(result)
        
    except Exception as e:
        error_msg = f"OCR processing failed: {str(e)}"
        print("❌ Error:", error_msg)
        return jsonify({"success": False, "error": error_msg})

if __name__ == '__main__':
    print("🚀 Server running on http://localhost:5000")
    print("📝 Endpoints:")
    print("   GET  http://localhost:5000/health")
    print("   POST http://localhost:5000/process-invoice")
    print("Press Ctrl+C to stop the server")
    app.run(host='localhost', port=5001, debug=False)