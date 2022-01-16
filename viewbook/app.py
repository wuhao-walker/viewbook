from flask import Flask,render_template,redirect,url_for,send_from_directory,abort,flash,session
from flask_sqlalchemy import SQLAlchemy
from form import PageForm,NewTCForm,EditTCForm,DeleteTCForm,DeleteMakeSureForm
from import_data import db_import,creat_table,delete_table
import sqlite3
import os
import click
import xlrd

app = Flask(__name__)
app.secret_key = '123'

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL','sqlite:///'
    +os.path.join(app.root_path,'data.db'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_PATH'] = os.path.join(app.root_path,'data')

db = SQLAlchemy(app)

class DMI(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    case_id = db.Column(db.String)
    req_id = db.Column(db.String)
    description = db.Column(db.Text)
    verification_method = db.Column(db.Text)
    detail_steps = db.Column(db.Text)
    expect_result = db.Column(db.Text)
    function_allocation = db.Column(db.Text)
    test_type = db.Column(db.Text)
    verification_procedure_id = db.Column(db.Text)
    verification_case_approval_status = db.Column(db.Text)
    verification_site = db.Column(db.Text)
    verification_status = db.Column(db.Text)
    coverage_analysis = db.Column(db.Text)

class DMH(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    case_id = db.Column(db.String)
    req_id = db.Column(db.String)
    description = db.Column(db.Text)
    verification_method = db.Column(db.Text)
    detail_steps = db.Column(db.Text)
    expect_result = db.Column(db.Text)
    function_allocation = db.Column(db.Text)
    test_type = db.Column(db.Text)
    verification_procedure_id = db.Column(db.Text)
    verification_case_approval_status = db.Column(db.Text)
    verification_site = db.Column(db.Text)
    verification_status = db.Column(db.Text)
    coverage_analysis = db.Column(db.Text)
    
@app.cli.command()
def initdb():
    db.create_all()
    click.echo('Initialized database')

@app.cli.command()
def importdb():
    db_import('D:\\workspace\\tools_platform\\viewbook\\data\\DMI','C919-CASE-DMI-Part2-revision.xlsx')

@app.route('/')
def home():
    return render_template('home_page.html')

@app.route('/dmi page/<string:item>',methods = ['GET','POST'])
def DMI_Page(item):
    global filename
    try:
        creat_table(item)
    except:
        print('table exits now')
    form1 = PageForm()
    if item == 'DMI':
        notes = DMI.query.all()
    elif item == 'DMH':
        notes = DMH.query.all()
    if form1.validate_on_submit():
        if form1.excel.data:
            f = form1.excel.data
            filename = f.filename
            session['filename'] = filename
            f.save(os.path.join(app.config['UPLOAD_PATH'],item+'\\'+filename))
            flash('Upload success.')
        if form1.import_data.data:
            try:
                print(filename)
                db_import('D:\\workspace\\tools_platform\\viewbook\\data\\'+item,filename,item)
            except:
                print('db exits now')
        if form1.delete_db.data:
            delete_table(item)
    return render_template('dmi_page.html',form1 = form1,form2 = DeleteTCForm(),notes = notes,item = item)

@app.route('/new/<string:item>',methods = ['GET','POST'])
def new_tc(item):
    form = NewTCForm()
    if form.validate_on_submit():
        case_id = form.Case_ID.data
        req_id = form.Requirement_ID.data
        description = form.Description.data
        verification_method = form.Verification_Method.data
        detail_steps = form.Detail_Steps.data
        expect_result = form.Expected_Result.data
        function_allocation = form.Function_Allocation.data
        test_type = form.Test_Type.data
        verification_procedure_id = form.Verification_Procedure_ID.data
        verification_case_approval_status = form.Verification_Case_Approval_Status.data
        verification_site = form.Verification_Site.data
        verification_status = form.Verification_Status.data
        coverage_analysis = form.Coverage_Analysis.data
        if item == 'DMI':
            i = DMI.query.count()
            tc = DMI(id = i+1,case_id = case_id,req_id = req_id,description = description,verification_method = verification_method,\
        detail_steps = detail_steps,expect_result = expect_result,function_allocation = function_allocation,test_type = test_type,\
        verification_procedure_id = verification_procedure_id,verification_case_approval_status = verification_case_approval_status,\
        verification_site = verification_site,verification_status = verification_status,coverage_analysis = coverage_analysis)
        elif item == 'DMH':
            i = DMI.query.count()
            tc = DMH(id = i+1,case_id = case_id,req_id = req_id,description = description,verification_method = verification_method,\
        detail_steps = detail_steps,expect_result = expect_result,function_allocation = function_allocation,test_type = test_type,\
        verification_procedure_id = verification_procedure_id,verification_case_approval_status = verification_case_approval_status,\
        verification_site = verification_site,verification_status = verification_status,coverage_analysis = coverage_analysis)
        db.session.add(tc)
        db.session.commit()
        flash('Your tc is saved.')
        return redirect(url_for('DMI_Page',item = item))
    return render_template('new_tc.html',form = form, item = item)

@app.route('/edit/<string:item>/<int:tc_id>',methods = ['GET','POST'])
def edit_tc(item,tc_id):
    form = EditTCForm()
    if item == 'DMI':
        tc = DMI.query.get(tc_id)
    elif item == 'DMH':
        tc = DMH.query.get(tc_id)
    print(form.validate_on_submit())
    if form.validate_on_submit():
        tc.case_id = form.Case_ID.data
        tc.req_id = form.Requirement_ID.data
        tc.description = form.Description.data
        tc.verification_method = form.Verification_Method.data
        tc.detail_steps = form.Detail_Steps.data
        tc.expect_result = form.Expected_Result.data
        tc.function_allocation = form.Function_Allocation.data
        tc.test_type = form.Test_Type.data
        tc.verification_procedure_id = form.Verification_Procedure_ID.data
        tc.verification_case_approval_status = form.Verification_Case_Approval_Status.data
        tc.verification_site = form.Verification_Site.data
        tc.verification_status = form.Verification_Status.data
        tc.coverage_analysis = form.Coverage_Analysis.data
        db.session.commit()
        flash('Your tc is updated')
        print('wwwwwwwwwwws')
        return redirect(url_for('DMI_Page',item = item))
    form.Case_ID.data = tc.case_id
    form.Requirement_ID.data = tc.req_id
    form.Description.data = tc.description
    form.Verification_Method.data = tc.verification_method
    form.Detail_Steps.data = tc.detail_steps
    form.Expected_Result.data = tc.expect_result
    form.Function_Allocation.data = tc.function_allocation
    form.Test_Type.data = tc.test_type
    form.Verification_Procedure_ID.data = tc.verification_procedure_id
    form.Verification_Case_Approval_Status.data = tc.verification_case_approval_status
    form.Verification_Site.data = tc.verification_site
    form.Verification_Status.data = tc.verification_status
    form.Coverage_Analysis.data = tc.coverage_analysis
    print('000000')
    return render_template('edit_tc.html',form =form,item = item,tc_id = tc_id)

@app.route('/delete/<string:item>/<int:tc_id>',methods = ['GET','POST'])
def delete_tc(tc_id,item):
    form = DeleteTCForm()
    #i = 1
    if form.validate_on_submit():
        '''if item == 'DMI':
            tc_delete = DMI.query.get(tc_id)
        if item == 'DMH':
            tc_delete = DMH.query.get(tc_id)
        db.session.delete(tc_delete)
        if item == 'DMI':
            tcs = DMI.query.all()
        if item == 'DMH':
            tcs = DMH.query.all()
        for tc in tcs:
            tc.id = i
            i = i+1
        db.session.commit()
        flash('Your tc is deleted.')
        return redirect(url_for('DMI_Page',item = item))'''
        return redirect(url_for('del_make_sure',item = item,tc_id = tc_id))
    return redirect(url_for('DMI_Page',item = item))

@app.route('/del_make_sure/<string:item>/<int:tc_id>',methods = ['GET','POST'])
def del_make_sure(tc_id,item):
    form = DeleteMakeSureForm()
    i = 1
    if form.validate_on_submit():
        if form.yes.data:
            if item == 'DMI':
                tc_delete = DMI.query.get(tc_id)
            if item == 'DMH':
                tc_delete = DMH.query.get(tc_id)
            db.session.delete(tc_delete)
            if item == 'DMI':
                tcs = DMI.query.all()
            if item == 'DMH':
                tcs = DMH.query.all()
            for tc in tcs:
                tc.id = i
                i = i+1
            db.session.commit()
            flash('Your tc is deleted.')
            return redirect(url_for('DMI_Page',item = item))
        elif form.no.data:
            return redirect(url_for('DMI_Page',item = item))
        else:
            abort(400)
    return render_template('del_make_sure.html',form = form,item = item,tc_id = tc_id)