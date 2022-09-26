function [ rho_hat ] = intraclusterCorrelation(T)
%INTRACLUSTERCORRELATION Calculation of the intracluster correlation
%   Based on X, from Y.
%   Detailed explanation goes here

n = sum(T.num_sub_unit);
x = sum(T.outcome);

p = x ./ n; % Overall proportion

rho_numer = (T.outcome .* (T.outcome - 1)) ...
    - (2 .* p .* (T.num_sub_unit - 1) .* T.outcome) ...
    + (T.num_sub_unit .* (T.num_sub_unit - 1) .* p.^2); % Numerator

rho_denom = T.num_sub_unit .* (T.num_sub_unit - 1) .* p .* (1 - p); % Denominator

rho_hat = sum(rho_numer) ./ sum(rho_denom);

if isnan(rho_hat) % Check if no correlation between clusters
    if sum(rho_numer)==0 && sum(rho_denom)==0
        rho_hat = 0;
    else
        assert(false,"Check intracluster correlation calculations!!");
    end
end

end

