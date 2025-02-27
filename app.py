from flask import Flask, render_template
from datetime import datetime, timedelta

app = Flask(__name__)

developers_info = {
    "Kaue Campos": {
        "position": "Desenvolvedor Fullstack",
        "email": "kaue.campos@surf.com.br",
        "phone": "(11) 91122-7411"
    },
    "Haron Moreira": {
        "position": "Desenvolvedor Fullstack",
        "email": "haron.moreira@surf.com.br",
        "phone": "(11) 95852-6269"
    },
    "Kevin Souza": {
        "position": "Desenvolvedor Fullstack e Sustentação",
        "email": "kevin.souza@surf.com.br",
        "phone": "(11) 95299-4427"
    },
    "Daniel Roberto": {
        "position": "Desenvolvedor Fullstack e Mobile",
        "email": "daniel.pereira@surf.com.br",
        "phone": "(11) 98381-5740"
    }
}

developers_schedule = ["Haron Moreira", "Kaue Campos", "Daniel Roberto", "Kevin Souza"]

def get_on_call_developer():
    today = datetime.now()
    start_date = datetime(2025, 2, 3)

    # Calcula o número de semanas desde o início do sobreaviso
    weeks_passed = (today - start_date).days // 7
    developer_index = weeks_passed % len(developers_schedule)

    developer_on_call = developers_schedule[developer_index]

    # Calcula o período do sobreaviso
    week_start = start_date + timedelta(weeks=weeks_passed)
    on_call_start = week_start.strftime('%d/%m/%Y')
    on_call_end = (week_start + timedelta(days=6)).strftime('%d/%m/%Y')
    on_call_period = f"{on_call_start} até {on_call_end}"

    return developer_on_call, on_call_period

@app.route('/')
def index():
    developer_on_call, on_call_period = get_on_call_developer()
    developer_info = developers_info[developer_on_call]
    return render_template('index.html', 
                           developer_on_call=developer_on_call,
                           developer_info=developer_info,
                           on_call_period=on_call_period)

if __name__ == "__main__":
    app.run(debug=True)
