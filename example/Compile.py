import sys, numpy, csv

if __name__ == "__main__":
    
    
    file = csv.reader(open("../data/capes.csv", "rb"), delimiter=",")
    matrix = list(file)
    
    data_generate = []
        
    # Qualis          A1 ,A2  ,B1 ,B2  ,B3 ,B4 ,B5  ,C   ,NC
    weight_qualis   =[0.9,0.75,0.6,0.45,0.3,0.25,0.1,0.07,0.01]
    # year base
    base_year       = 2016
    cut_year        = 2013 # year that has become interesting analyze the brazil's productions 
    num_error_di_ti = 0
    file_out = open('training.csv', 'w')
    file_out.write("row, course, years_open, diss_doce_year, tese_doce_year, peri_doce_year, weight_a1, weight_a2, weight_b1, weight_b2, weight_b3, weight_b4, weight_b5, weight_c, weight_nc, qual_doce_year, conf_doce_year, livr_doce_year, capi_doce_year,arti_doce_year,has_phd,is_academic,level")
    file_out.write('\n')
    
    
        
    for i in range(len(matrix)):
        if i != 0:
            years_open      = -1
            diss            = 0
            doce            = 0
            tese            = 0
            peri            = 0
            qual            = 0
            conf            = 0
            livr            = 0
            capi            = 0
            arti            = 0
            weight_a1       = 0
            weight_a2       = 0
            weight_b1       = 0
            weight_b2       = 0
            weight_b3       = 0
            weight_b4       = 0
            weight_b5       = 0
            weight_c        = 0
            weight_nc       = 0
            diss_doce_year  = 0
            tese_doce_year  = 0
            peri_doce_year  = 0
            conf_doce_year  = 0
            qual_doce_year  = 0
            livr_doce_year  = 0
            capi_doce_year  = 0
            has_phd         = False
            is_academic     = True
            level           = -1
            area            = "?"
            
            num_diss_tese_prop  = 0
            num_years_old   = 0
            
            # try to count the years open
            #   if not has masters information use the PhD
            #   else not use the curse to create the tree
            #
            if matrix[i][4] != "" and matrix[i][4] != None:
                years_open = float(base_year - int(float(matrix[i][4])))
            else:
                if matrix[i][3] != "" and matrix[i][3] != None:
                    years_open = float(base_year - int(float(matrix[i][3])))
            if years_open != -1:
                num_years_old += years_open
                
                # try to set 20 year the ceiling
                if years_open > float(base_year - cut_year):
                    years_open = float(base_year - cut_year)
                    
                print 'row ',i, ' years old ',years_open 
                
                try:
                    diss = int(float(matrix[i][6]))
                except:
                    print 'error num diss at row',i
                try:
                    doce = int(float(matrix[i][5]))
                except:
                    print 'error num doce at row',i
                try:
                    tese = int(float(matrix[i][7]))
                except:
                    print 'error num tese at row',i
                try:
                    peri = int(float(matrix[i][9]))
                except:
                    print 'error num peri at row',i
                try:
                    peri = int(float(matrix[i][10]))
                except:
                    print 'error num qual at row',i
                try:
                    conf = int(float(matrix[i][20]))
                except:
                    print 'error num conf at row',i
                try:
                    livr = int(float(matrix[i][11]))
                except:
                    print 'error num livr at row',i
                try:
                    capi = int(float(matrix[i][12]))
                except:
                    print 'error num capi at row',i
                try:
                    arti = int(float(matrix[i][14]))
                except:
                    print 'error num arti at row',i
                try:
                    weight_a1 = int(float(matrix[i][11]))*weight_qualis[0]
                except:
                    print 'error num A1   at row',i
                try:
                    weight_a2 = int(float(matrix[i][12]))*weight_qualis[1]
                except:
                    print 'error num A2   at row',i
                try:
                    weight_b1 = int(float(matrix[i][13]))*weight_qualis[2]
                except:
                    print 'error num B1   at row',i
                try:
                    weight_b2 = int(float(matrix[i][14]))*weight_qualis[3]
                except:
                    print 'error num B2   at row',i
                try:
                    weight_b3 = int(float(matrix[i][15]))*weight_qualis[4]
                except:
                    print 'error num B3   at row',i
                try:
                    weight_b4 = int(float(matrix[i][16]))*weight_qualis[5]
                except:
                    print 'error num B4   at row',i
                try:
                    weight_b5 = int(float(matrix[i][17]))*weight_qualis[6]
                except:
                    print 'error num B5   at row',i
                try:
                    weight_c  = int(float(matrix[i][18]))*weight_qualis[7]
                except:
                    print 'error num C    at row',i
                try:
                    weight_nc = int(float(matrix[i][19]))*weight_qualis[8]
                except:
                    print 'error num NC   at row',i
                try:
                    diss_tese_prop = float(matrix[i][8])
                except:
                    print 'error di/ti pr.at row',i
                    num_diss_tese_prop+=1
                    
                if matrix[i][3] != None and matrix[i][3] != "":
                    has_phd = True
                if matrix[i][2] == "Acad":
                    is_academic = True
                    
                diss_doce_year = (diss/doce)/years_open
                tese_doce_year = (tese/doce)/years_open
                peri_doce_year = (peri/doce)/years_open
                qual_doce_year = (qual/doce)/years_open
                livr_doce_year = (livr/doce)/years_open
                conf_doce_year = (conf/doce)/years_open
                capi_doce_year = (capi/doce)/years_open
                arti_doce_year = (arti/doce)/years_open
                level          = matrix[i][26]
                area           = matrix[i][0]
                #file_out.write("row,course, years_open, diss_doce_year, tese_doce_year, peri_doce_year, weight_a1, weight_a2, weight_b1, weight_b2, weight_b3, weight_b4, weight_b5, weight_c, weight_nc, qual_doce_year, conf_doce_year, livr_doce_year, capi_doce_year, arti_doce_year, has_phd, is_academic, level")
                
                row_inf = str(i)+"," +str(area)+"," +str(years_open)+"," +str(diss_doce_year)+"," +str(tese_doce_year)+"," +str(peri_doce_year)+"," +str(weight_a1)+"," +str(weight_a2)+"," +str(weight_b1)+"," +str(weight_b2)+"," +str(weight_b3)+"," +str(weight_b4)+"," +str(weight_b5)+"," +str(weight_c)+"," +str(weight_nc)+"," +str(qual_doce_year)+"," +str(conf_doce_year)+"," +str(livr_doce_year)+"," +str(capi_doce_year)+"," +str(arti_doce_year)+"," +str(has_phd)+"," +str(is_academic)+"," +str(level)
                row_inf = row_inf.lower()
                file_out.write(row_inf)
                file_out.write('\n')
            else:
                print 'row ',i, ' can\'t computed'
                
    print 'Di/Ti prop. error',num_diss_tese_prop/len(matrix)
    print 'year old meddly  ',num_years_old/len(matrix)
    file_out.close()