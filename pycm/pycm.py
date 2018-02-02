# -*- coding: utf-8 -*-

from .functions import *
import os
class pycmError(Exception):
    pass
class ConfusionMatrix():
    '''
    Main Class Of ConfusionMatrix
    '''
    def __init__(self,actual_vector,predict_vector):
        if not isinstance(actual_vector,list) or not isinstance(predict_vector,list):
            raise pycmError("Input Vectors Must Be List")
        if len(actual_vector)!=len(predict_vector):
            raise pycmError("Input Vectors Must Be The Same Length")
        matrix_param=matrix_params_calc(actual_vector,predict_vector)
        self.actual_vector=actual_vector
        self.predict_vector=predict_vector
        self.classes=matrix_param[0]
        self.table=matrix_param[1]
        self.TP=matrix_param[2]
        self.TN=matrix_param[3]
        self.FP=matrix_param[4]
        self.FN=matrix_param[5]
        statistic_result=class_statistics(TP=matrix_param[2],TN=matrix_param[3],FP=matrix_param[4],
                                         FN=matrix_param[5])
        self.class_stat=statistic_result
        self.overall_stat=overall_statistics(statistic_result["ACC"],statistic_result["RACC"])
        self.TPR=statistic_result["TPR"]
        self.TNR=statistic_result["TNR"]
        self.PPV = statistic_result["PPV"]
        self.NPV = statistic_result["NPV"]
        self.FNR = statistic_result["FNR"]
        self.FPR = statistic_result["FPR"]
        self.FDR = statistic_result["FDR"]
        self.FOR = statistic_result["FOR"]
        self.ACC = statistic_result["ACC"]
        self.F1 = statistic_result["F1"]
        self.MCC = statistic_result["MCC"]
        self.BM = statistic_result["BM"]
        self.MK = statistic_result["MK"]
        self.DOR=statistic_result["DOR"]
        self.PLR=statistic_result["LR+"]
        self.NLR=statistic_result["LR-"]
        self.POP=statistic_result["POP"]
        self.P=statistic_result["P"]
        self.N=statistic_result["N"]
        self.TOP=statistic_result["TOP"]
        self.TON=statistic_result["TON"]
        self.PRE=statistic_result["PRE"]
        self.G=statistic_result["G"]
        self.K=statistic_result["K"]
        self.RACC=statistic_result["RACC"]
        self.SOA=statistic_result["SOA"]
        self.F2=statistic_result["F2"]
        self.F05=statistic_result["F0.5"]
    def matrix(self):
        '''
        This method print confusion matrix
        :return:
        '''
        print(table_print(self.classes,self.table))
    def normalized_matrix(self):
        '''
        This method print normalized confusion matrix
        :return:
        '''
        print(normalized_table_print(self.classes,self.table))
    def stat(self):
        '''
        This method print statistical measures table
        :return: None
        '''
        print(stat_print(self.classes,self.class_stat,self.overall_stat))
    def __str__(self):
        '''
        ConfusionMatrix object string representation method
        :return: representation as str (matrix + params)
        '''
        result=table_print(self.classes,self.table)
        result+="\n"*4
        result+=stat_print(self.classes,self.class_stat,self.overall_stat)
        return result
    def save_stat(self,name):
        try:
            file = open(name + ".pycm", "w")
            stat=stat_print(self.classes,self.class_stat,self.overall_stat)
            file.write(stat)
            file.close()
            return {"Status":True,"Message":os.path.join(os.getcwd(),name+".pycm")}
        except Exception as e:
            if file.closed==False:
                file.close()
            return {"Status":False,"Message":str(e)}
    def F_score(self,Beta):
        F_Dict = {}
        for i in self.TP.keys():
            F_Dict[i]=F_calc(TP=self.TP[i],FP=self.FP[i],FN=self.FN[i],Beta=Beta)
        return F_Dict

    def __repr__(self):
        '''
        ConfusionMatrix object representation method
        :return: representation as str
        '''
        return "pycm.ConfusionMatrix(classes: "+str(self.classes)+")"



