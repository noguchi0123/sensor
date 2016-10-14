def heat_trans_coef(*,a_out,thick,heat_trans,a_in,c=False):
    if c is False:
        coef = 1/((1/a_out)+(thick/heat_trans)+(1/a_in))
    else:
        coef = 1/((1/a_out)+(thick/heat_trans)+(1/c)+(1/a_in))
    return coef
