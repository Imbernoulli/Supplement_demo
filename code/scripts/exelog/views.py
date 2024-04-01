import hashlib
import json
import os
import subprocess
import time

from django.http import JsonResponse
from django.shortcuts import render


# find log in local folder
def find_first_match_with_string(root_folder, string):
    for root, dirs, files in os.walk(root_folder):
        for dirname in dirs:
            if string in dirname:
                return os.path.join(root, dirname)
        for filename in files:
            if string in filename:
                return os.path.join(root, filename)
    return None


# start task
def start_task(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            query = data.get("query")
            q_time = data.get("start_time")
            config = json.load(open("./config.json"))
            subprocess.Popen(
                [
                    "python",
                    "./scripts/main.py",
                    "--query",
                    str(query),
                    "--name",
                    str(q_time),
                    "--gpt_version",
                    str(config["Model"]),
                    "--temperature",
                    str(config["Temperature"]),
                ]
            )
            return JsonResponse({"code": 200, "message": "Task started successfully"})
        except:
            return JsonResponse({"code": 500, "error": "Internal Server Error"})
    else:
        return JsonResponse({"code": 405, "error": "Invalid request method"})


# get logs
def get_logs(request):
    if request.method == "GET":
        try:
            query = request.GET.get("query")
            q_time = request.GET.get("start_time")
            print(query)
            print(q_time)
            query_hash = hashlib.sha256(query.encode()).hexdigest()[:8]
            log_path = find_first_match_with_string(f"logs/{str(q_time)}/", query_hash)
            log = json.load(open(log_path))
            return JsonResponse({"code": 200, "log": log})
        except:
            return JsonResponse({"code": 500, "error": "Internal Server Error"})
    else:
        return JsonResponse({"code": 405, "error": "Invalid request method"})


if __name__ == "__main__":
    query = "Please use ChemFormula(https://github.com/molshape/ChemFormula) to fulfill this task: Create a 'ChemFormula' object for benzene and output its HTML representation."
    q_time = time.time()
    config = json.load(open("./config.json"))
    subprocess.Popen(
        [
            "python",
            "./scripts/main.py",
            "--query",
            str(query),
            "--name",
            str(q_time),
            "--gpt_version",
            str(config["Model"]),
            "--temperature",
            str(config["Temperature"]),
        ]
    )
    time.sleep(1)
    import pdb

    pdb.set_trace()
    query_hash = hashlib.sha256(query.encode()).hexdigest()[:8]
    log_path = find_first_match_with_string(f"logs/{str(q_time)}/", query_hash)
    print(log_path)
