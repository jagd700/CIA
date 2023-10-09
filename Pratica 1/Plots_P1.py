# %% [markdown]
# # Plot NMOS and PMOS comparison

# %% [markdown]
# Import libs

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# %% [markdown]
# ### Fazer dois graficos para NMOS e para PMOS  
# Y = gm / gds   
# X = gm / Id    
# 
# Y =( gm / cgs ) / ( 2pi )   
# X = gm / Id  

# %% [markdown]
# #### NMOS

# %%
# length sizes of the transistors
Lsizes = [120, 200, 300, 400, 600, 800, 1000, 1500, 2000]
df_NMOS = []

# read the csv files and store the data in a list of dataframes
for i in range(0, len(Lsizes)):
        df_CSV_nmos = pd.read_csv('Resultados/NMOS_W5u_L' + str(Lsizes[i]) + 'n_Vds200m.csv')
        df_aux = pd.DataFrame()
        df_aux["gm_over_id"] = df_CSV_nmos["NM0:gm Y"]/df_CSV_nmos["NM0:id Y"]
        df_aux["gm_over_gds"] = df_CSV_nmos["NM0:gm Y"]/df_CSV_nmos["NM0:gds Y"]
        df_aux["gm_over_cgs_rad"] = df_CSV_nmos["NM0:gm Y"]/abs(df_CSV_nmos["NM0:cgs Y"])
        df_NMOS.append(df_aux)

# Plot gm/gds vs gm/id of the NMOS transistors
plt.figure(1)
plt.title("NMOS Gain gm/gds")
plt.ylabel("gm/gds")
plt.xlabel("gm/id")
for i in range(0, len(Lsizes)):
        plt.plot(df_NMOS[i]["gm_over_id"],df_NMOS[i]["gm_over_gds"], label="L=" + str(Lsizes[i]) + "nm")
plt.legend()

# Plot gm/cgs rad vs gm/id of the NMOS transistors
plt.figure(2)
plt.title("NMOS GBW")
plt.yscale('log')
plt.ylabel("gm/cgs rad")
plt.xlabel("gm/id")
for i in range(0, len(Lsizes)):
        plt.plot(df_NMOS[i]["gm_over_id"],df_NMOS[i]["gm_over_cgs_rad"], label="L=" + str(Lsizes[i]) + "nm")
plt.legend()


# %% [markdown]
# NMOS:  
# L= 600 nm   
# gm/id = 25      
# 
# 8GHz    
# 60dB   

# %%
L_nmos_index = 4
gm_over_id_nmos = 25
gm_nmos=690e-6
Id_nmos = gm_nmos/gm_over_id_nmos

# %% [markdown]
# ### PMOS

# %%
df_PMOS = []

# read the csv files and store the data in a list of dataframes
for i in range(0, len(Lsizes)):
        df_CSV_pmos = pd.read_csv('Resultados/PMOS_W5u_L' + str(Lsizes[i]) + 'n_Vds200m.csv')
        df_aux = pd.DataFrame()
        df_aux["gm_over_id"] = abs(df_CSV_pmos["PM0:gm Y"]/df_CSV_pmos["PM0:id Y"])
        df_aux["gm_over_gds"] = df_CSV_pmos["PM0:gm Y"]/df_CSV_pmos["PM0:gds Y"]
        df_aux["gm_over_cgs_rad"] = df_CSV_pmos["PM0:gm Y"]/abs(df_CSV_pmos["PM0:cgs Y"])
        df_aux["Kgm"] = abs(gm_nmos/df_CSV_pmos["PM0:gm Y"]) # TESTE Kgm
        df_aux["Ki"] = abs(Id_nmos/df_CSV_pmos["PM0:id Y"]) # TESTE Ki
        df_PMOS.append(df_aux)

# Plot the gm/gds vs gm/id of the PMOS transistors
plt.figure(1)
plt.title("PMOS Gain gm/gds")
plt.ylabel("gm/gds")
plt.xlabel("gm/id")
for i in range(0, len(Lsizes)):
        plt.plot(df_PMOS[i]["gm_over_id"],df_PMOS[i]["gm_over_gds"], label="L=" + str(Lsizes[i]) + "nm")
plt.legend()


# Plot the gm/cgs rad vs gm/id of the PMOS transistors
plt.figure(2)
plt.title("PMOS GBW")
plt.yscale('log')
plt.ylabel("gm/cgs rad")
plt.xlabel("gm/id")
for i in range(0, len(Lsizes)):
        plt.plot(df_PMOS[i]["gm_over_id"],df_PMOS[i]["gm_over_cgs_rad"], label="L=" + str(Lsizes[i]) + "nm")
plt.legend()


# Plot the Kgm vs gm/id of the PMOS transistors
plt.figure(3)
plt.title("PMOS Kgm")
plt.yscale('log')
plt.ylabel("Kgm")
plt.xlabel("gm/id")
for i in range(0, len(Lsizes)):
        plt.plot(df_PMOS[i]["gm_over_id"],df_PMOS[i]["Kgm"], label="L=" + str(Lsizes[i]) + "nm")
        # plt.plot(df_CSV_pmos[i]["PM0:id Y"],gm_nmos/df_CSV_pmos[i]["PM0:gm Y"], label="L=" + str(Lsizes[i]) + "nm")
plt.legend()


# Plot the Ki vs gm/id of the PMOS transistors
plt.figure(5)
plt.title("PMOS Ki")
plt.yscale('log')
plt.ylabel("Ki")
plt.xlabel("gm/id")
for i in range(0, len(Lsizes)):
        plt.plot(df_PMOS[i]["gm_over_id"],df_PMOS[i]["Ki"], label="L=" + str(Lsizes[i]) + "nm")
plt.legend()



# %% [markdown]
# 

# %%
# # read the csv files and store the data in a list of dataframes
# for i in range(0, len(Lsizes)):
#         df_aux["KI"] = gm_nmos/df_CSV_pmos["PM0:gm Y"]
#         # df_aux["Kgm"] = df_CSV_pmos["PM0:gm Y"]/df_CSV_pmos["PM0:gds Y"]
#         # df_aux["gm_over_cgs_rad"] = df_CSV_pmos["PM0:gm Y"]/abs(df_CSV_pmos["PM0:cgs Y"])
#         df_PMOS.append(df_aux)

df_CSV_pmos


