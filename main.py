from flask import Flask, render_template, request

app = Flask(__name__)
wallArea = float(0)
gallonsNeeded = float(0)
quartsNeeded = float(0)
cansNeeded = 0.0
sqftPerGallon = float(350.0)
gallonsPerCan = 1.0

@app.route('/')
def main():
  return render_template('index.html')

@app.route('/estimate', methods=['POST'])
def estimate(wallArea=wallArea, gallonsNeeded=gallonsNeeded, quartsNeeded=quartsNeeded):
    if request.method == 'POST':

      wallHeight = request.form['wallHeight']
      wallWidth = request.form['wallWidth']

      wallArea = float(wallHeight) * float(wallWidth)
      gallonsNeeded = round(wallArea / sqftPerGallon, 2)
      quartsNeeded = round(wallArea / (sqftPerGallon / 4), 2)
      return render_template('index.html', wallArea=wallArea, gallonsNeeded=gallonsNeeded, quartsNeeded=quartsNeeded)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)