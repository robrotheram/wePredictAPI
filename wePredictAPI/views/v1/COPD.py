__author__ = 'robert'
from flask import jsonify , g
from flask import request
from flask import Response
import simplejson

from wePredictAPI.app import app

@app.route('/v1/getcopd')
def getcopd():
    limit = request.args.get('limit')
    if limit is None:
        return jsonify(data= g.db.getResult("SELECT * from COPD"))
    else:
        return jsonify(data=g.db.getResult("SELECT * from COPD LIMIT " + limit))


@app.route('/v1/getcopdaverage')
def getcopdaverage():
    data = g.db.getResult("SELECT Avg(Value_09)as v09, Avg(Value_10)as v10, Avg(Value_11)as v11, Avg(Value_12)as v12, Avg(Value_13)as v13 FROM COPD")
    js_data = []
    for obj in data:
        objjst = {"y": "2009", "value_y": obj['v09']}
        js_data.append(objjst)
        objjst = {"y": "2010", "value_y": obj['v10']}
        js_data.append(objjst)
        objjst = {"y": "2011", "value_y": obj['v11']}
        js_data.append(objjst)
        objjst = {"y": "2012", "value_y": obj['v12']}
        js_data.append(objjst)
        objjst = {"y": "2013", "value_y": obj['v13']}
        js_data.append(objjst)


    return Response(simplejson.dumps(js_data), mimetype='application/json')


@app.route('/v1/get_copd_ASTHMA_average')
def getcopdasthmaaverage():
    data = g.db.getResult("SELECT Avg(COPD.Value_09) as v09, Avg(COPD.Value_10)as v10, Avg(COPD.Value_11)as v11, Avg(COPD.Value_12) as v12, "
                   "Avg(COPD.Value_13) as v13, Avg(ASTHMA_QOF.Value_09) as Q09, Avg(ASTHMA_QOF.Value_10) as Q10, Avg(ASTHMA_QOF.Value_11)as Q11, "
                   "Avg(ASTHMA_QOF.Value_12)as Q12, Avg(ASTHMA_QOF.Value_13) as Q13 FROM COPD "
                   "Join ASTHMA_QOF  on COPD.Practice_Code = ASTHMA_QOF.Practice_Code")
    js_data = []
    for obj in data:
        objjst = {"y": "2009", "value_COPD": obj['v09'], "value_ASMTHA": obj['Q09']}
        js_data.append(objjst)
        objjst = {"y": "2010", "value_COPD": obj['v10'], "value_ASMTHA": obj['Q10']}
        js_data.append(objjst)
        objjst = {"y": "2011", "value_COPD": obj['v11'], "value_ASMTHA": obj['Q11']}
        js_data.append(objjst)
        objjst = {"y": "2012", "value_COPD": obj['v12'], "value_ASMTHA": obj['Q12']}
        js_data.append(objjst)
        objjst = {"y": "2013", "value_COPD": obj['v13'], "value_ASMTHA": obj['Q13']}
        js_data.append(objjst)

    return Response(simplejson.dumps(js_data), mimetype='application/json')

