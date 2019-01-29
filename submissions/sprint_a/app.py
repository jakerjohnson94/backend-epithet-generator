from sprint_a import app
import json
@app.route('/')
def epithets():
  return json.dumps({"epithets": []})
@app.route('/vocabulary')
def vocabulary():
  return json.dumps({"vocabulary": {}})

