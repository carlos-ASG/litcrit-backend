from flask import jsonify


def create_item(data):
    # Logic to create an item
    return jsonify({"message": "Item created", "data": data}), 201

def get_item(item_id):
    # Logic to get an item
    return jsonify({"message": f"Get item {item_id}"}), 200

def update_item(item_id, data):
    # Logic to update an item
    return jsonify({"message": f"Update item {item_id}", "data": data}), 200

def delete_item(item_id):
    # Logic to delete an item
    return jsonify({"message": f"Delete item {item_id}"}), 200