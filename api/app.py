from flask import Flask, request, jsonify
from cache_classic import ClassicCache
from cache_replicated import ReplicatedCache
from cache_partitioned import PartitionedCache

app = Flask(__name__)

classic_cache = ClassicCache()
replicated_cache = ReplicatedCache()
partitioned_cache = PartitionedCache()

@app.route('/cache/classic', methods=['GET', 'POST'])
def classic_cache_handler():
    if request.method == 'GET':
        key = request.args.get('key')
        value = classic_cache.get(key)
        if value:
            return jsonify({key: value}), 200
        else:
            return jsonify({"error": "Key not found"}), 404
    elif request.method == 'POST':
        data = request.json
        key = data.get('key')
        value = data.get('value')
        if key and value:
            classic_cache.set(key, value)
            return jsonify({"message": "Value added to cache"}), 201
        else:
            return jsonify({"error": "Invalid data"}), 400

@app.route('/cache/replicated', methods=['GET', 'POST'])
def replicated_cache_handler():
    if request.method == 'GET':
        key = request.args.get('key')
        value = replicated_cache.get(key)
        if value:
            return jsonify({key: value}), 200
        else:
            return jsonify({"error": "Key not found"}), 404
    elif request.method == 'POST':
        data = request.json
        key = data.get('key')
        value = data.get('value')
        if key and value:
            replicated_cache.set(key, value)
            return jsonify({"message": "Value added to cache"}), 201
        else:
            return jsonify({"error": "Invalid data"}), 400

@app.route('/cache/partitioned', methods=['GET', 'POST'])
def partitioned_cache_handler():
    if request.method == 'GET':
        key = request.args.get('key')
        value = partitioned_cache.get(key)
        if value:
            return jsonify({key: value}), 200
        else:
            return jsonify({"error": "Key not found"}), 404
    elif request.method == 'POST':
        data = request.json
        key = data.get('key')
        value = data.get('value')
        if key and value:
            partitioned_cache.set(key, value)
            return jsonify({"message": "Value added to cache"}), 201
        else:
            return jsonify({"error": "Invalid data"}), 400

if __name__ == '__main__':
    app.run(debug=True)
