from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import bleach
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)
db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'created_at': self.created_at.isoformat()
        }

with app.app_context():
    db.create_all()

def sanitize_input(data):
    data['title'] = bleach.clean(data.get('title', ''), strip=True)
    data['content'] = bleach.clean(data.get('content', ''), strip=True)
    return data

@app.route('/api/posts', methods=['POST'])
def create_post():
    try:
        data = request.get_json()
        data = sanitize_input(data)
        
        if not data.get('title') or not data.get('content'):
            return jsonify({'error': 'Title and content are required'}), 400
            
        if len(data['title']) > 100:
            return jsonify({'error': 'Title must be less than 100 characters'}), 400
            
        post = Post(title=data['title'], content=data['content'])
        db.session.add(post)
        db.session.commit()
        return jsonify(post.to_dict()), 201
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/posts', methods=['GET'])
def get_posts():
    try:
        posts = Post.query.order_by(Post.created_at.desc()).all()
        return jsonify([post.to_dict() for post in posts])
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/posts/<int:id>', methods=['GET'])
def get_post(id):
    try:
        post = Post.query.get_or_404(id)
        return jsonify(post.to_dict())
    except Exception as e:
        return jsonify({'error': str(e)}), 404

@app.route('/api/posts/<int:id>', methods=['PUT'])
def update_post(id):
    try:
        post = Post.query.get_or_404(id)
        data = request.get_json()
        data = sanitize_input(data)
        
        if not data.get('title') or not data.get('content'):
            return jsonify({'error': 'Title and content are required'}), 400
            
        if len(data['title']) > 100:
            return jsonify({'error': 'Title must be less than 100 characters'}), 400
            
        post.title = data['title']
        post.content = data['content']
        db.session.commit()
        return jsonify(post.to_dict())
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/posts/<int:id>', methods=['DELETE'])
def delete_post(id):
    try:
        post = Post.query.get_or_404(id)
        db.session.delete(post)
        db.session.commit()
        return jsonify({'message': 'Post deleted successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)