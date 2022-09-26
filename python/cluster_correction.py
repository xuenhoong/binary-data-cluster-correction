import numpy as np
from scipy.stats import norm

def wilson_confidence_intervals(T: list = None, alpha: float = 0.05):
    """Calculates Wilson confidence interval corrected for binary clustered data.
    Described in Section 3.2 of:
    Saha, K., Miller, D. & Wang, S. (2016). A Comparison of Some Approximate C-
    onfidence Intervals for a Single Proportion for Clustered Binary Outcome D-
    ata. The International Journal of Biostatistics, 12(2), 20150024.
    https://doi.org/10.1515/ijb-2015-0024
    """
    T = np.array(T)

    z = round(abs(norm.ppf(alpha/2)),2)

    n_dot = sum(i[0] for i in T) # number of observations/samples
    x_dot = sum(i[1] for i in T) # number of desired outcomes 
    
    pi_hat = x_dot / n_dot

    phi_hat = _intraclass_correlation(T)


    # xi (ξ) 
    xi_hat = (1 / n_dot) * sum(T[:,0] * (1 + ((T[:,0] - 1) * phi_hat)))

    n_dot_tilde = n_dot + (xi_hat * z**2)

    # pi_tilde (π^~) is also the cluster corrected metric
    ccm = (n_dot * pi_hat + (0.5 * xi_hat * (z**2))) \
        / (n_dot + (xi_hat * (z**2)))

    ci = (z / n_dot_tilde) * \
        np.sqrt( (n_dot * pi_hat * (1 - pi_hat) * xi_hat) \
            + ((xi_hat**2) * (z**2) / 4) )

    lci = ccm - ci
    uci = ccm + ci

    return (ccm, lci, uci)

def _intraclass_correlation(T: np.array) -> float:
    """Calculate the intraclass correlation.
    The intraclass correlation for a single proportion is calculated according 
    to pp. 441 to 444 of the following work:
    J. L. Fleiss, B. Levin and M. C. Paik, Statistical Methods for Rates and P-
    roportions, Hoboken, NJ, USA::Wiley, 2003
    """

    n = sum(i[0] for i in T) # number of observations/samples
    x = sum(i[1] for i in T) # number of desired outcomes 

    p = x / n # Overall proportion

    # rho (ρ) - is the intracluster correlation
    rho_numer = (T[:,1] * (T[:,1] - 1)) \
                - (2 * p * (T[:,0] - 1) * T[:,1]) \
                + (T[:,0] * (T[:,0] - 1) * (p**2))
    
    rho_denom = T[:,0] * (T[:,0] - 1) * p * (1 - p)

    # To do: check if ρ_hat is correct when there is no correlation between cluster (usually nan)
    if sum(rho_numer)==0 and sum(rho_denom)==0:
        rho_hat = 0
    else:
        rho_hat = sum(rho_numer) / sum(rho_denom)

    return rho_hat

def main():
    T = [[12,12], [11,11], [10,10], [9,9], [11,10], [10,9], [10,9], [9,8], [9,8], [5,4], [9,7], [7,4], [10,5], [6,3], [10,3], [7,0]]
    
    alpha = 0.05
    
    ccm, lci, uci = wilson_confidence_intervals(T, alpha)

    print(f'The cluster-corrected metric is {round(ccm*100, 2)}% ({int((1-alpha) * 100)}% CI: {round(lci*100, 2)} - {round(uci*100, 2)})')

if __name__ == "__main__":
    main()
