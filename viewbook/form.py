from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField
from flask_wtf.file import FileField,FileRequired,FileAllowed
from wtforms.validators import DataRequired,Length

class PageForm(FlaskForm):
    excel = FileField('Upload Excel')
    upload = SubmitField('upload')
    import_data = SubmitField('import')
    delete_db = SubmitField('delete')


class NewTCForm(FlaskForm):
    Case_ID = TextAreaField('Case_ID',validators = [DataRequired()])
    Requirement_ID = TextAreaField('Requirement_ID',validators = [DataRequired()])
    Description = TextAreaField('Description',validators = [DataRequired()])
    Verification_Method = TextAreaField('Verification_Method',validators = [DataRequired()])
    Detail_Steps = TextAreaField('Detail_Steps',validators = [DataRequired()])
    Expected_Result = TextAreaField('Expected_Result',validators = [DataRequired()])
    Function_Allocation = TextAreaField('Function_Allocation',validators = [DataRequired()])
    Test_Type = TextAreaField('Test_Type',validators = [DataRequired()])
    Verification_Procedure_ID = TextAreaField('Verification_Procedure_ID',validators = [DataRequired()])
    Verification_Case_Approval_Status = TextAreaField('Verification_Case_Approval_Status',validators = [DataRequired()])
    Verification_Site = TextAreaField('Verification_Site',validators = [DataRequired()])
    Verification_Status = TextAreaField('Verification_Status',validators = [DataRequired()])
    Coverage_Analysis = TextAreaField('Coverage_Analysis',validators = [DataRequired()])
    submit = SubmitField('save')

class EditTCForm(FlaskForm):
    Case_ID = TextAreaField('Case_ID',validators = [DataRequired()])
    Requirement_ID = TextAreaField('Requirement_ID',validators = [DataRequired()])
    Description = TextAreaField('Description',validators = [DataRequired()])
    Verification_Method = TextAreaField('Verification_Method',validators = [DataRequired()])
    Detail_Steps = TextAreaField('Detail_Steps',validators = [DataRequired()])
    Expected_Result = TextAreaField('Expected_Result',validators = [DataRequired()])
    Function_Allocation = TextAreaField('Function_Allocation',validators = [DataRequired()])
    Test_Type = TextAreaField('Test_Type',validators = [DataRequired()])
    Verification_Procedure_ID = TextAreaField('Verification_Procedure_ID',validators = [DataRequired()])
    Verification_Case_Approval_Status = TextAreaField('Verification_Case_Approval_Status',validators = [DataRequired()])
    Verification_Site = TextAreaField('Verification_Site',validators = [DataRequired()])
    Verification_Status = TextAreaField('Verification_Status',validators = [DataRequired()])
    Coverage_Analysis = TextAreaField('Coverage_Analysis',validators = [DataRequired()])
    submit = SubmitField('Update')

class DeleteTCForm(FlaskForm):
    submit = SubmitField('Delete')

class DeleteMakeSureForm(FlaskForm):
    yes = SubmitField('Yes')
    no = SubmitField('No')