from flask import Flask,render_template,request
import pickle
import numpy as np

model = pickle.load(open("model.pkl","rb"))
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods = ["POST"])
def predict_thyroid():
    age = int(request.form.get('age'))
    on_thyroine = request.form.get('on_thyroine')
    on_antithyroid_meds = request.form.get('on_antithyroid_meds')
    pregnant = request.form.get('pregnant')
    thyroid_surgery = request.form.get('thyroid_surgery')
    I131_treatment = request.form.get('I131_treatment')
    lithium = request.form.get('lithium')
    goitre = request.form.get('goitre')
    TSH_measured = request.form.get('TSH_measured')
    TSH = float(request.form.get('TSH'))
    TT4_measured = request.form.get('TT4_measured')
    TT4 = float(request.form.get('TT4'))
    T4U_measured = request.form.get('T4U_measured')
    T4U = float(request.form.get('T4U'))
    FTI_measured = request.form.get('FTI_measured')
    FTI = float(request.form.get('FTI'))
    patient_id = int(request.form.get('patient_id'))
    sex_F = request.form.get('sex_F')
    sex_M = request.form.get('sex_M')

    #prediction
    result = model.predict(np.array([age,on_thyroine,on_antithyroid_meds,pregnant,thyroid_surgery,I131_treatment,lithium,goitre,TSH_measured,TSH,TT4_measured,TT4,T4U_measured,T4U,FTI_measured,FTI,patient_id,sex_M,sex_F]).reshape(1,19))
    if result[0] == 0:
        result = "Thyroid zhala nahiye boss, so chill"
    elif result[0] == 1:
        result = "hyperthyroid"
    elif result[0] == 2:
        result = "T3 toxic"
    elif result[0] == 3:
        result = "consistent with toxic goitre, but more likely increased binding protein"
    elif result[0] == 4:
        result = "hypothyroid"
    elif result[0] == 5:
        result = "primary hypothyroid"
    elif result[0] == 6:
        result = "compensated hypothyroid"
    elif result[0] == 7:
        result = "consistent with compensated hypothyroid, but more likely increased binding protein"
    elif result[0] == 8:
        result = "consistent with compensated hypothyroid, but more likely concurrent non-thyroidal illness"
    elif result[0] == 9:
        result = "consistent with secondary hypothyroid, but more likely concurrent non-thyroidal illness"
    elif result[0] == 10:
        result = "increased binding protein"
    elif result[0] == 11:
        result = "decreased binding protein"
    elif result[0] == 12:
        result = "concurrent non-thyroidal illness"
    elif result[0] == 13:
        result = "consistent with concurrent non-thyroidal illness, but more likely decreased binding protein"
    elif result[0] == 14:
        result = "consistent with replacement theory"
    elif result[0] == 15:
        result = "unreplaced"
    elif result[0] == 16:
        result = "consistent with unreplaced, but more likely concurrent non-thyroidal illness"
    elif result[0] == 17:
        result = "overreplaced"
    elif result[0] == 18:
        result = "antithyroid drugs"
    elif result[0] == 19:
        result = "Surgery"
    elif result[0] == 20:
        result = "discordant assay results"
    elif result[0] == 21:
        result = "elevated TBG"
    else:
        result = "none"

    return result




if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)
