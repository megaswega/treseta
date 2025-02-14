from flask import Flask, request, jsonify, render_template
from game_logic import TresetteGame

app = Flask(__name__)

# Initialize your game logic
game = TresetteGame()

@app.route('/')
def home():
    # Render a basic homepage
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play_card():
    data = request.get_json()
    player = data.get('player')
    card = data.get('card')
    
    # Process the move using your game logic
    result = game.play_card(player, card)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)