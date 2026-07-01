import os
import urllib.request

# Automatically create the static folder if it doesn't exist
os.makedirs('static', exist_ok=True)

assets = {
    'socket.io.js': 'https://cdnjs.cloudflare.com/ajax/libs/socket.io/4.7.2/socket.io.js',
    'chart.js': 'https://cdn.jsdelivr.net/npm/chart.js'
}

print("--- Starting Local Asset Download ---")
for filename, url in assets.items():
    target_path = os.path.join('static', filename)
    try:
        print(f"Downloading {filename}...")
        # Bypasses browser restrictions by downloading via standard network streams
        urllib.request.urlretrieve(url, target_path)
        print(f"✓ Saved successfully to: {target_path}")
    except Exception as e:
        print(f"✗ Failed to download {filename}: {e}")
print("---------------------------------------")