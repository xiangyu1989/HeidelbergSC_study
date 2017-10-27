function [x1, x2] = nullst(a)
% This function solve a quadratic equation and returns the root
% The input is a vector of the three quadratic function
% The output is the solution, i.e. the root 
% 
%  Input: a, 3*1 or 1*3 vector 
%         a1 = a(1), a2 = a(2), a3 = a(3)
%         a1, a2, a3 are the coefficient of each term from higher order to
%         the lower order
%  Output: solution of the qudrative equation: the root
% 
% Author: Yu Xiang 2017-10-21
%%

a1 = a(1); 
a2 = a(2); 
a3 = a(3); 
if a1 == 0 
    if a2 == 0 
        disp('No real solution when both a1 and a2 are zero!')
        x1 = []; 
        x2 = []; 
    else
        disp('Only one solution when a1 is equal to zero and a2 is non-zero!')
        x1 = - a3 / a2; 
        x2 = []; 
    end
    
else  % a1 ~= 0 
    p = a2 / a1; 
    q = a3 / a1; 
    D = p ^ 2 / 4 - q; 
    if D < 0 
        disp('No real solution/root!')
        x1 = []; 
        x2 = []; 
    elseif D == 0 
        disp('Only one real solution/root!')
        x1 = - p / 2 - sqrt(D); 
        % x2 = - p / 2 + sqrt(D); 
        x2 = []; 
    else 
        disp('Two real solution/root!')
        x1 = - p / 2 - sqrt(D); 
        x2 = - p / 2 + sqrt(D); 
    end   
end   

% end of function
end