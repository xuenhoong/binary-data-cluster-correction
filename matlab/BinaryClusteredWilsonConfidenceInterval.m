function [CCM,LCI,UCI] = BinaryClusteredWilsonConfidenceInterval(T,alpha)
%BINARYCLUSTEREDWILSONCONFIDENCEINTERVAL Summary of this function goes here
%   Detailed explanation goes here

z = abs(norminv(alpha ./ 2));

n_dot  = sum(T.num_sub_unit);
x_dot = sum(T.outcome);

pi_hat = x_dot ./ n_dot;

phi_hat = intraclusterCorrelation(T);

xi_hat = (1 ./ n_dot) .* ...
    sum(T.num_sub_unit .* (1 + ((T.num_sub_unit - 1) .* phi_hat)));

n_dot_tilde = n_dot + (xi_hat .* z.^2);

CCM = (n_dot .* pi_hat + (0.5 * xi_hat * z.^2)) ...
    ./ (n_dot + (xi_hat .* z.^2)) ;

CI = (z ./ n_dot_tilde) ...
    .* sqrt( (n_dot .* pi_hat .* (1 - pi_hat) .* xi_hat) + (xi_hat.^2 * z.^2 ./ 4));

LCI = CCM - CI;
UCI = CCM + CI;

end



