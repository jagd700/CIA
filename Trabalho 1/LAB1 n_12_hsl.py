# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

#----- Variables ------------------------------------------------------------------------------

l_sizes = [340, 400, 500, 600, 700, 800, 1000, 1500, 2000]
df_nmos = []
df_pmos = []
df_nmos_hg = []
gmd_nmos = 3.2e-3
idd_pmos = 5.57e-06
l_pmos = 800
cdb_pmos = 4.1540e-15
cd = 1e-12
cdac = 0.5e-12


#----- Read Files and Create Dataframes -------------------------------------------------------

def df_nmos_results(l_sizes, df_nmos):
        for i in range(0, len(l_sizes)):
                df_nmos_csv = pd.read_csv(r'Resultados\Results n_12_hsl130\NMOS_W10u_L' + str(l_sizes[i]) + 'n_Vds200m.csv')
                df_aux = pd.DataFrame()
                df_aux["id"] = df_nmos_csv["NM0:id Y"]
                df_aux["gm"] = df_nmos_csv["NM0:gm Y"]
                df_aux["gds"] = df_nmos_csv["NM0:gds Y"]
                df_aux["cgs"] = abs(df_nmos_csv["NM0:cgs Y"])
                df_aux["cdb"] = abs(df_nmos_csv["NM0:cdb Y"])
                df_aux["gm_over_id"] = df_aux["gm"]/df_aux["id"]
                df_aux["gm_over_gds"] = df_aux["gm"]/df_aux["gds"]
                
                # for j in range(len(df_aux["gm_over_gds"])):
                
                #         df_aux["gain"][j] = 20*math.log(10, df_aux["gm_over_gds"][j])
                        
                df_aux["gm_over_cgs_rad"] = df_aux["gm"]/df_aux["cgs"]

                df_aux["kgm"] = gmd_nmos/df_aux["gm"]
                df_aux["P2"] = (df_aux["kgm"] * df_aux["gm"]) / (cd + df_aux["kgm"]*df_aux["cgs"] + cdac)
                df_aux["kid"] = df_aux["id"] / idd_pmos

                df_aux["gbw"] = ((df_aux["gm"]*df_aux["kgm"])/(1e-12+df_aux["cdb"]*df_aux["kgm"]+cdb_pmos*df_aux["kgm"]*df_aux["kid"]))/(2*np.pi)
                df_nmos.append(df_aux)

def df_pmos_results(l_sizes, df_pmos):
        for i in range(0, len(l_sizes)):
                df_pmos_csv = pd.read_csv(r'Resultados\Results n_12_hsl130\PMOS_W10u_L' + str(l_sizes[i]) + 'n_Vds200m.csv')
                # print(df_pmos_csv)
                df_aux = pd.DataFrame()
                df_aux["id"] = df_pmos_csv["PM0:id Y"]
                df_aux["gm"] = df_pmos_csv["PM0:gm Y"]
                df_aux["gds"] = df_pmos_csv["PM0:gds Y"]
                df_aux["cgs"] = df_pmos_csv["PM0:cgs Y"]
                df_aux["gm_over_id"] = abs(df_pmos_csv["PM0:gm Y"]/df_pmos_csv["PM0:id Y"])
                df_aux["gm_over_gds"] = df_pmos_csv["PM0:gm Y"]/df_pmos_csv["PM0:gds Y"]
                df_aux["gm_over_cgs_rad"] = df_pmos_csv["PM0:gm Y"]/abs(df_pmos_csv["PM0:cgs Y"])
                df_pmos.append(df_aux)


#----- Plot Graphs ----------------------------------------------------------------------------

def nmos_gain_plot(l_sizes):
        plt.figure(1)
        plt.title("NMOS Gain - 1 (HSL W=10u)")
        plt.ylabel("gm/gds")
        plt.xlabel("gm/id")
        for i in range(0, len(l_sizes)):
                plt.plot(df_nmos[i]["gm_over_id"].values, df_nmos[i]["gm_over_gds"].values, label="L=" + str(l_sizes[i]) + "nm")
        plt.legend()
        plt.show()
        
def nmos_gain_plot_2(l_sizes):
        plt.figure(1)
        plt.title("NMOS Gain - 1")
        plt.ylabel("gm/gds dB")
        plt.xlabel("gm/id")
        for i in range(0, len(l_sizes)):
                plt.plot(df_nmos[i]["gm_over_id"].values, df_nmos[i]["gain"].values, label="L=" + str(l_sizes[i]) + "nm")
        plt.legend()
        plt.show()

def nmos_gbw_plot(l_sizes):
        plt.figure(2)
        plt.title("NMOS GBW")
        plt.yscale('log')
        plt.ylabel("gm/cgs rad")
        plt.xlabel("gm/id")
        for i in range(0, len(l_sizes)):
                plt.plot(df_nmos[i]["gm_over_id"].values, df_nmos[i]["gm_over_cgs_rad"].values, label="L=" + str(l_sizes[i]) + "nm")
        plt.legend()
        plt.show()

def nmos_kgm_plot(l_sizes):
        plt.figure(3)
        plt.title("NMOS kgm")
        plt.yscale('log')
        plt.ylabel("kgm")
        plt.xlabel("gm/id")
        for i in range(0, len(l_sizes)):
                plt.plot(df_nmos[i]["gm_over_id"].values, df_nmos[i]["kgm"].values, label="L=" + str(l_sizes[i]) + "nm")
        plt.legend()
        plt.show()

def nmos_kid_plot(l_sizes):
        plt.figure(4)
        plt.title("NMOS kid")
        plt.yscale('log')
        plt.ylabel("kid")
        plt.xlabel("gm/id")
        for i in range(0, len(l_sizes)):
                plt.plot(df_nmos[i]["gm_over_id"].values, df_nmos[i]["kid"].values, label="L=" + str(l_sizes[i]) + "nm")
        plt.legend()
        plt.show()

def gbw_plot(l_sizes):
        plt.figure(7)
        plt.title("AMP GBW (HSL W=10u)")
        plt.ylabel("Hz")
        plt.xlabel("gm/id")
        for i in range(0, len(l_sizes)):
                plt.plot(df_nmos[i]["gm_over_id"].values, df_nmos[i]["gbw"].values, label="L=" + str(l_sizes[i]) + "nm")
        plt.legend()
        plt.show()
        
def ki_plot(l_sizes):
        plt.figure(8)
        plt.title("KI")
        plt.ylabel("KI")
        plt.xlabel("gm/id")
        for i in range(0, len(l_sizes)):
                plt.plot(df_pmos[i]["gm_over_id"].values, df_pmos[i]["ki"].values, label="L=" + str(l_sizes[i]) + "nm")
        plt.legend()
        plt.show()

def kgm_plot(l_sizes):
        plt.figure(9)
        plt.title("KGM")
        plt.ylabel("KGM")
        plt.xlabel("gm/id")
        plt.yscale('log')
        for i in range(0, len(l_sizes)):
                plt.plot(df_nmos[i]["gm_over_id"].values, df_nmos[i]["kgm"].values, label="L=" + str(l_sizes[i]) + "nm")
        plt.legend()
        plt.show()

def P2_plot(l_sizes):
        plt.figure(10)
        plt.title("P2")
        plt.ylabel("P2")
        plt.xlabel("gm/id")
        for i in range(0, len(l_sizes)):
                plt.plot(df_nmos[i]["gm_over_id"].values, df_nmos[i]["P2"].values, label="L=" + str(l_sizes[i]) + "nm")
        plt.legend()
        plt.show()


#----------------------------------------------------------------------------------------------

df_nmos_results(l_sizes, df_nmos)

df_pmos_results(l_sizes, df_pmos)

#df_nmos[5].to_csv('L800NMOS.csv', index=False)

gbw_plot(l_sizes)

nmos_gain_plot(l_sizes)
# pmos_gain_plot(l_sizes)
kgm_plot(l_sizes)
P2_plot(l_sizes)















# plt.figure(5)
# plt.title("PMOS Gain")
# plt.ylabel("gm/gds")
# plt.xlabel("gm/id")
# for i in range(0, len(l_sizes)):
#         plt.plot(df_pmos[i]["gm_over_id"].values, df_pmos[i]["gm_over_gds"].values, label="L=" + str(l_sizes[i]) + "nm")
# plt.legend()

# plt.figure(6)
# plt.title("PMOS GBW")
# plt.yscale('log')
# plt.ylabel("gm/cgs rad")
# plt.xlabel("gm/id")
# for i in range(0, len(l_sizes)):
#         plt.plot(df_pmos[i]["gm_over_id"].values, df_pmos[i]["gm_over_cgs_rad"].values, label="L=" + str(l_sizes[i]) + "nm")
# plt.legend()



# %%
