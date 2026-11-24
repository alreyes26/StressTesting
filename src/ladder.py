import numpy as np

def interpolate_net_yields(
years : np.ndarray,
y5: float,
y7: float,
y10: float,
y20: float,
fund_fee: float,
fee_max_years: float = 10.0,
) -> np.ndarray:
    knots_x = np.array([5.0, 7.0, 10.0, 20.0])
    knotx_y = np.array([y5, y7, y10, y20])
    gross_yields = np.interp(years, knots_x, knotx_y)
    net_yields = gross_yields - fund_fee
    return net_yields
