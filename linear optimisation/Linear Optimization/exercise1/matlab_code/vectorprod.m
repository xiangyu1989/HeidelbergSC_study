function c = vectorprod(a, b)
% This fuction calculates the vector product of two vectors 
% The two inputs vector a and b should be both 3 * 1 vector 
% The output vector c should also be a 3 * 1 vector 
% 
% c = a (*) b = (a2 * b3 - a3 * b2,
%                a3 * b1 - a1 * b3, 
%                a1 * b2 - a2 * b1); 
% 
% Author: Yu Xiang 2017-10-21 
%% 

% Notice, the input of a and b must be a dimension of 3 * 1 vector
a1 = a(1); 
a2 = a(2); 
a3 = a(3); 

b1 = b(1); 
b2 = b(2); 
b3 = b(3); 

c  = [a2 * b3 - a3 * b2; a3 * b1 - a1 * b3; a1 * b2 - a2 * b1]; 

end