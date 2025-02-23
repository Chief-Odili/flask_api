from flask import Flask, jsonify, request

app = Flask(__name__)

# @app.route('/')
# def home():
#     return "Flask is running!"

tasks = []  # In-memory data storage


# create task
@app.route("/tasks",methods=["POST"])
def create_task():
    data = request.get_json()
    task = {
        "id": len(tasks) + 1,
        "title": data.get("title"),
        "description": data.get("description"),
        "done": False
    }
    tasks.append(task)
    return jsonify({
        "message": "Task created Successfully",
        "task": task
    }),201

#get all task
@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify({
        "message": "All task retrieved Successfully",
        "Task": tasks
    })


# get single task
@app.route("/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        return jsonify({"error": "Task not found"}), 404
    return jsonify({
        "message": "Requested task retrieved Successfully",
        "Task": task
    })

# update a task
@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    task = next((task for task in tasks if task["id"] == task_id), None)
    if task is None:
        return jsonify({"error": "Task not found"}), 404
    
    data = request.get_json()
    task["title"] = data.get("title", task["title"])
    task["description"] = data.get("description", task["description"])
    task["done"] = data.get("done", task["done"])
    return jsonify({
        "message": "Task Updated Successfully",
        "Task": task
    })

# delete a task
@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    task = next((task for task in tasks if task["id"] == task_id), None)
    if task is None:
        return jsonify({"error": "Task not found"}), 404

    tasks.remove(task)
    return jsonify({"message": "Task deleted"})
    


if __name__ == '__main__':
    app.run(debug=True)