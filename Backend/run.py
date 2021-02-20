import json
from datetime import datetime

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

from main import app

app.run(debug=True, host='0.0.0.0', port=5000)
