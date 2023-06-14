from flask import Flask, render_template, request

app = Flask(__name__, static_folder='static')


# Gestion de la redirection
@app.route('/', methods=['GET', 'POST'])
def main():
    print(request.form)
    if request.method == 'GET':  # qlq lit les informations HTML
        print("quelqu'un à ouvert les pages")
        return render_template('/Connexion.html')
    else:
        print("quelqu'un à envoyé des informations")  # Le serveur recoit des informations
        name = request.form['username']
        mdp = request.form['password']
        print(name)
        print(mdp)
        return render_template('/Success.html')


if __name__ == '__main__':
    app.run()

print("test")
