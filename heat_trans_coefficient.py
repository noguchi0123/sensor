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


