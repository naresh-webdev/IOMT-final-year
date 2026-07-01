from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'medical_gateway_secret'
socketio = SocketIO(app, cors_allowed_origins="*", allow_unsafe_werkzeug=True)

@app.route('/')
def index():
    return render_template('index.html')

# NEW ROUTE: Listens for the ESP32 data packages over the local network
@app.route('/telemetry', methods=['POST'])
def receive_telemetry():
    data = request.get_json()
    print(f"Wireless Stream Received: {data}")
    
    # Instantly forward the data package to the frontend web browser via WebSockets
    socketio.emit('update_dashboard', data)
    
    return jsonify({"status": "success", "message": "Telemetry received"}), 200

if __name__ == '__main__':
    # host='0.0.0.0' allows devices on your Wi-Fi (like the ESP32) to connect
    socketio.run(app, host='0.0.0.0', port=5002, debug=True)