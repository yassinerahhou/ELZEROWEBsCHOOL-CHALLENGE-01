from flask import Flask, render_template
ajitkhdm1 = Flask(__name__)


@ajitkhdm1.route("/")
def homepage():
    return render_template("HOME_PAGE.html", )


@ajitkhdm1.route("/login")
def login():
    return render_template("login.html")


@ajitkhdm1.route("/contact")
def contact():
    return render_template("contact.html")


@ajitkhdm1.route("/prive")
def sctr_prv():
    return render_template("sctr_prv.html", pp="PRIVé")


@ajitkhdm1.route("/public")
def sctr_pblc():
    return render_template("sctr_pblc.html", pp="public")


@ajitkhdm1.route("/councours")
def councours():
    return render_template('modls_councours.html',  pp="councours")


@ajitkhdm1.route("/stages")
def stages():
    return render_template('stages.html', pp=" stages")


@ajitkhdm1.route("/orientation")
def orientation():
    return render_template("orientation.html", pp="oriontations")


@ajitkhdm1.route("/faq")
def faq():
    return render_template("faq_page.html", pp="faq")


@ajitkhdm1.route("/404")
def notf():
    return ("THIS PAGE NOT FOUND")


@ajitkhdm1.route("/test")
def onlytest():
    return render_template("sctr_pblc.html", pp="public")


if __name__ == "__main__":
    ajitkhdm1.run(debug=True, port=9000)
