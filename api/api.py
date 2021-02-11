from flask  import Flask, request, jsonify
from youtube import Download

app = Flask(__name__)
        
@app.route('/')
def home():
    return jsonify({"Home":"Bem Vindo!"})

@app.route('/download', methods=["POST"])
def downloadVideo():
    data = request.get_json()
    
    download = Download(data.get('url'))
    download.downloadVideo()

    return jsonify({"Mensagem":"Vídeo Baixado com Sucesso!"})    


app.run(debug=True)

