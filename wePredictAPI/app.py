from flask import Flask
from wePredictAPI.database.db import DB

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True

databaseConnection = DB()


import wePredictAPI.views.v1
import wePredictAPI.views.v1.Asmtha
import wePredictAPI.views.v1.COPD
import wePredictAPI.views.v1.flu
import wePredictAPI.views.v1.MedicalCenters
import wePredictAPI.views.v1.Pollution
import wePredictAPI.views.v1.smoking

if __name__ == '__main__':
    app.run()