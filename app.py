#!/usr/bin/env python3
import os
import json
import uuid
from flask import Flask, request, jsonify, send_from_directory, send_file
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Serve static files
@app.route('/')
def serve_index():
    return send_file('index.html')

@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory('.', filename)

@app.route('/api/generate-image', methods=['POST'])
def generate_image():
    try:
        data = request.get_json()
        
        if not data or 'prompt' not in data:
            return jsonify({'error': 'Missing prompt in request'}), 400
            
        prompt = data['prompt']
        aspect_ratio = data.get('aspect_ratio', '3:4')
        one_line_summary = data.get('one_line_summary', 'Wordle results image')
        
        # Here we would call the image generation tool
        # For now, we'll simulate this with a placeholder
        # In a real implementation, you would integrate with the actual image generation service
        
        # Generate a unique filename
        image_id = str(uuid.uuid4())
        image_filename = f'wordle-result-{image_id}.png'
        image_path = f'generated_images/{image_filename}'
        
        # Create directory if it doesn't exist
        os.makedirs('generated_images', exist_ok=True)
        
        # TODO: Replace this with actual image generation
        # For now, return a mock response
        return jsonify({
            'success': True,
            'image_url': f'/generated_images/{image_filename}',
            'image_path': image_path,
            'message': 'Image generation endpoint created - needs actual image generation implementation'
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Serve generated images
@app.route('/generated_images/<filename>')
def serve_generated_image(filename):
    return send_from_directory('generated_images', filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)