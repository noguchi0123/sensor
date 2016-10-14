##caluculate heat transmit coefficent 
def heat_trans_coef(*,a_out,thick,heat_trans,a_in,c=False):
    if c is False:
        coef = 1/((1/a_out)+(thick/heat_trans)+(1/a_in))
    else:
        coef = 1/((1/a_out)+(thick/heat_trans)+(1/c)+(1/a_in))
    return coef

##surface area
def surface_area(*,width=0.150,height=0.075,depth=0.150):
    return 2*(width*height+height*depth+depth*width)

##volumetric flow rate
def volmetric_flow_rate(*,v_wind,hole_area):
    return v_wind*hole_area

def get_air_parameter(temp,para=None):
    import pandas as pd
    df_para = pd.DataFrame()
    df_para = pd.read_csv('../2_data/air_parameter.csv')
    if temp<20:
        temperature=10
        if para is None:
            return df_para[df_para.temperature==temperature]
        elif para=='hc':
            return df_para.heat_conductivity[df_para.temperature==temperature]
        elif para=='d':
            return df_para.density[df_para.temperature==temperature]
        elif para=='sh':
            return df_para.specific_heat[df_para.temperature==temperature]
        else:
            return ('Input MUST be hc/d/sh.')
    elif temp<40:
        temperature=30
        if para is None:
            return df_para[df_para.temperature==temperature]
        elif para=='hc':
            return df_para.heat_conductivity[df_para.temperature==temperature]
        elif para=='d':
            return df_para.density[df_para.temperature==temperature]
        elif para=='sh':
            return df_para.specific_heat[df_para.temperature==temperature]
        else:
            return ('Input MUST be hc/d/sh.')
    elif temp<60:
        temperature=50
        if para is None:
            return df_para[df_para.temperature==temperature]
        elif para=='hc':
            return df_para.heat_conductivity[df_para.temperature==temperature]
        elif para=='d':
            return df_para.density[df_para.temperature==temperature]
        elif para=='sh':
            return df_para.specific_heat[df_para.temperature==temperature]
        else:
            return ('Input MUST be hc/d/sh.')
    elif temp<80:
        temperature=70
        if para is None:
            return df_para[df_para.temperature==temperature]
        elif para=='hc':
            return df_para.heat_conductivity[df_para.temperature==temperature]
        elif para=='d':
            return df_para.density[df_para.temperature==temperature]
        elif para=='sh':
            return df_para.specific_heat[df_para.temperature==temperature]
        else:
            return ('Input MUST be hc/d/sh.')
    else:
        temperature=90
        if para is None:
            return df_para[df_para.temperature==temperature]
        elif para=='hc':
            return df_para.heat_conductivity[df_para.temperature==temperature]
        elif para=='d':
            return df_para.density[df_para.temperature==temperature]
        elif para=='sh':
            return df_para.specific_heat[df_para.temperature==temperature]
        else:
            return ('Input MUST be hc/d/sh.')

