import os
import xlrd
import sqlite3
import sys
import importlib

importlib.reload(sys)

def creat_table(item_name):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('create table '+item_name+'(id int(10) primary key,\
                                     case_id varchar,\
                                     req_id text,\
                                     verification_method text,\
                                     description text,\
                                     detail_steps text,\
                                     expect_result text,\
                                     function_allocation text,\
                                     test_type text,\
                                     verification_procedure_id text,\
                                     verification_case_approval_status text,\
                                     verification_site text,\
                                     verification_status text,\
                                     coverage_analysis text)')
    conn.commit()
    conn.close()

def delete_table(item_name):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('drop table '+item_name)

def db_import(tc_path, tc_name,item_name):
    path = os.path.join(tc_path,tc_name)
    data = xlrd.open_workbook(path)
    table = data.sheet_by_name('Test Case')
    ncols = table.ncols
    case_id_list = table.col_values(0)[1:]
    req_id_list = table.col_values(2)[1:]
    description_list = table.col_values(1)[1:]
    verification_method_list = table.col_values(3)[1:]
    detail_steps_list = table.col_values(4)[1:]
    expect_result_list = table.col_values(5)[1:]
    function_allocation_list = table.col_values(6)[1:]
    test_type_list = table.col_values(7)[1:]
    verification_procedure_id_list = table.col_values(8)[1:]
    verification_case_approval_status_list = table.col_values(9)[1:]
    verification_site_list = table.col_values(10)[1:]
    verification_status_list = table.col_values(11)[1:]
    coverage_analysis_list = table.col_values(12)[1:]
    data_list = zip(case_id_list,req_id_list,description_list,verification_method_list,detail_steps_list,expect_result_list,\
        function_allocation_list,test_type_list,verification_procedure_id_list,verification_case_approval_status_list,\
        verification_site_list,verification_status_list,coverage_analysis_list)
    i = 1
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    for case_id,req_id,description,verification_method,detail_steps,expect_result,\
        function_allocation,test_type,verification_procedure_id,verification_case_approval_status,\
        verification_site,verification_status,coverage_analysis in data_list:
        if (case_id != 'N/A') and (case_id != ""):
            description = description.replace("\"","\'")
            detail_steps = detail_steps.replace("\"","\'")
            expect_result = expect_result.replace("\"","\'")
            cursor.execute('insert into '+item_name+'(id,\
                    case_id,\
                    req_id,\
                    description,\
                    verification_method,\
                    detail_steps,\
                    expect_result,\
                    function_allocation,\
                    test_type,\
                    verification_procedure_id,\
                    verification_case_approval_status,\
                    verification_site,\
                    verification_status,\
                    coverage_analysis)values("{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}")'.format(i,\
                        case_id,req_id,description,verification_method,\
                        detail_steps,expect_result,function_allocation,\
                        test_type,verification_procedure_id,verification_case_approval_status,\
                        verification_site,verification_status,coverage_analysis))
            i=i+1
    cursor.close()
    conn.commit()
    conn.close()

#creat_table('test')
#db_import('D:\\workspace\\tools_platform\\viewbook\\data\\DMI','C919-TC-DMI.xlsx','test')