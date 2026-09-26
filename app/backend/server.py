from flask import Flask, jsonify
from flask_cors import CORS
import time
import os

app = Flask(__name__)
CORS(app)

start_time = time.time()

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({
        "status": "HEALTHY",
        "service": "EasyWork-Backend-API",
        "uptime_seconds": round(time.time() - start_time, 2),
        "cluster_node": os.getenv("HOSTNAME", "k8s-pod")
    }), 200

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    tasks = [
        {"id": "TASK-101", "name": "Sync EKS Pod Replicas", "status": "COMPLETED", "priority": "HIGH"},
        {"id": "TASK-102", "name": "Validate Ingress Traffic Routing", "status": "IN_PROGRESS", "priority": "CRITICAL"},
        {"id": "TASK-103", "name": "Terraform State Consistency Check", "status": "COMPLETED", "priority": "MEDIUM"},
        {"id": "TASK-104", "name": "GitHub Actions CI/CD Image Scan", "status": "COMPLETED", "priority": "HIGH"}
    ]
    return jsonify({
        "total_tasks": len(tasks),
        "tasks": tasks,
        "engine": "Easy-work Enterprise Microservices Engine"
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)