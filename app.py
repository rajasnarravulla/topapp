from flask import Flask, render_template, request, flash
import openai
import html

app = Flask(__name__)
app.secret_key = "rajaraja"
openai.api_key = "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"

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/", methods=['POST','GET'])
def fetch():
	number = request.form['number']
	place = request.form['place']
	location = request.form['location']
	modelengine = "text-davinci-003"
	question = "Best of or Top "+str(request.form['number'])+" " + str(request.form['place']) + " in " + str(request.form['location']) + " with full details and description."
	completion = openai.Completion.create(
		model = modelengine,
		prompt = question,
		max_tokens = 2500,
		temperature = 0,
		n=2
		)
	answer = completion.choices[0].text
	return render_template('index.html', result=answer, number=number, place=place, location=location)

if __name__ == '__main__':
	app.run(debug=True, port=3001)



