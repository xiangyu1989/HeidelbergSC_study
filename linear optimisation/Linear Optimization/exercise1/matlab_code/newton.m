function x = newton (f, df, x0, TOL, NMAX)
%  This function uses Netwon method to calculates the soultion for the zero
%  point of a function, i.e. to find the x such as f(x) = 0
%  
%  The Newton method is implemented with iterations combined with original function 
%  and the differential function 
%     x(n + 1) = x(n) - f(x(n)) / df (xn);  where df is the first order
%     differential equation of f. 
%   
%  The solution is find when the difference between x(n+1) and x(n) is smaller
%  than a tolerance level or the maximum iteration number is reached. 
% 
%   Author: Yu Xiang 2017-10-21 
%%   

if nargin == 3 
    TOL = 10e-6; 
    NMAX = 20; 
elseif nargin == 4
    NMAX = 20; 
elseif nargin < 3
    error('There is not enough input!')    
end
    
xn = x0;
xn1 = xn - f(xn) / df(xn);
NrIt = 1;

while abs(xn1 - xn) > TOL || NrIt < NMAX    
    xn1 = xn - f(xn) / df(xn);
    NrIt = NrIt + 1;
    xn = xn1;
end

x = xn1;

end