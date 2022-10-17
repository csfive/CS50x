import os
from datetime import datetime

from cs50 import SQL
from flask import Flask, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
    orders = db.execute(
        "SELECT symbol, name, sum(shares) as sumshares, price FROM orders WHERE user_id = ? GROUP BY symbol",
        session["user_id"],
    )
    account = cash[0]["cash"]
    for order in orders:
        name = order["name"]
        total = order["sumshares"] * order["price"]
        order["name"] = name
        order["total"] = total
        order["price"] = order["price"]
        account += total
    return render_template(
        "index.html", orders=orders, cash=cash[0]["cash"], account=account
    )


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "GET":
        return render_template("buy.html")
    else:
        symbol = request.form.get("symbol")
        if not symbol:
            return apology("Missing Symbol")

        quote = lookup(symbol)
        if not quote:
            return apology("Invalid Symbol")

        try:
            shares = float(request.form.get("shares"))
            if not shares or not float.is_integer(shares) or shares <= 0:
                raise ValueError
        except ValueError:
            return apology("Invalid number")

        row = db.execute("SELECT cash FROM users where id = ?", session["user_id"])
        cash = row[0]["cash"]
        balance = cash - shares * quote["price"]
        if balance < 0:
            return apology("insufficient balance")

        db.execute(
            "UPDATE users SET cash = ? WHERE id = ?", balance, session["user_id"]
        )
        db.execute(
            "INSERT INTO orders (user_id, symbol, shares, name, price, timestamp) VALUES (?, ?, ?, ?, ?, ?)",
            session["user_id"],
            symbol.upper(),
            shares,
            quote["name"],
            quote["price"],
            datetime.now(),
        )
        return redirect("/")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    orders = db.execute(
        "SELECT symbol, name, shares, price, timestamp FROM orders WHERE user_id = ?",
        session["user_id"],
    )
    if not orders:
        return apology("No history", 403)
    else:
        for order in orders:
            if order["shares"] > 0:
                order["status"] = "Bought"
            else:
                order["status"] = "Sold"
        return render_template("history.html", orders=orders)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "GET":
        return render_template("quote.html")
    else:
        symbol = request.form.get("symbol")
        quote = lookup(symbol)
        if not symbol:
            return apology("missing symbol")
        if not quote:
            return apology("invalid symbol")
        return render_template("quoted.html", quote=quote)


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "GET":
        return render_template("register.html")
    else:
        name = request.form.get("username")
        ps1 = request.form.get("password")
        ps2 = request.form.get("confirmation")
        if not name or not ps1 or not ps1:
            return apology("please provide username and password!")
        if ps1 != ps2:
            return apology("password and confirmation don't match")
        if db.execute("SELECT * FROM users WHERE username = ?", name):
            return apology("user already exist!")

        db.execute(
            "INSERT INTO users (username, hash) VALUES (?, ?)",
            name,
            generate_password_hash(ps1),
        )
        return redirect("/")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "GET":
        symbols = db.execute(
            "SELECT symbol FROM orders WHERE user_id = ? GROUP BY symbol",
            session["user_id"],
        )
        return render_template("sell.html", symbol=symbols)
    else:
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")

        if not shares:
            return apology("Invalid shares")
        shares = int(shares)
        if shares <= 0:
            return apology("Invalid symbol or shares")

        sumshares = db.execute(
            "SELECT symbol, price, name, SUM(shares) as sumshares FROM orders WHERE user_id = ? AND symbol = ?",
            session["user_id"],
            symbol,
        )

        if shares > sumshares[0]["sumshares"]:
            return apology("You don't have so many shares")

        db.execute(
            "INSERT INTO orders (user_id, symbol, shares, name, price, timestamp) VALUES (?, ?, ?, ?, ?, ?)",
            session["user_id"],
            symbol,
            -shares,
            sumshares[0]["name"],
            sumshares[0]["price"],
            datetime.now(),
        )
        sold = shares * sumshares[0]["price"]

        cash = db.execute("select cash FROM users WHERE id = ?", session["user_id"])[0]["cash"]
        db.execute(
            "UPDATE users SET cash = ? WHERE id = ?", cash + sold, session["user_id"]
        )
        return redirect("/")
