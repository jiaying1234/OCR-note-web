from flask import Flask, render_template, request, jsonify, redirect, url_for
from PIL import Image
import pytesseract
from textblob import TextBlob
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

notes = {}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/create_note', methods=['GET', 'POST'])
def create_note():
    if request.method == 'POST':
        exam_name = request.form['exam_name']
        note_content = request.form['note_content']
        
        if exam_name:
            notes[exam_name] = note_content
            return redirect(url_for('create_note'))
    
    return render_template('create_note.html')

@app.route('/upload_image', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({'success': False, 'message': 'No image part'})
    
    image = request.files['image']
    if image and allowed_file(image.filename):
        filename = image.filename
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        image.save(image_path)
        
        # 進行 OCR 和 NLP
        text = pytesseract.image_to_string(Image.open(image_path))
        blob = TextBlob(text)
        extracted_text = "\n".join([str(sentence) for sentence in blob.sentences])
        
        return jsonify({'success': True, 'text': extracted_text})
    
    return jsonify({'success': False, 'message': 'Invalid file'})

@app.route('/view_note', methods=['GET', 'POST'])
def view_note():
    if request.method == 'POST':
        action = request.form.get('action')
        note_name = request.form.get('note_name')
        note_content = request.form.get('note_content_' + note_name)

        if action == 'update':
            notes[note_name] = note_content
        elif action == 'delete':
            notes.pop(note_name, None)

    return render_template('view_note.html', notes=notes)

if __name__ == '__main__':
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    app.run(debug=True)
