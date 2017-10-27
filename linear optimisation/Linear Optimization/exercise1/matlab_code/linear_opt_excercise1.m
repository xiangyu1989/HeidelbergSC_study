% This script is for the linear optimisation exerciese 1 

% Author: Yu Xiang, student number: 897864

%% M1 
% Input: 
A = [1, 2; 3, 0]; 
b = [1, 3]'; 
B = [4, 6, 8; 11, 2, 12; 3, 5, 16]; 
u = [4, 6, 8]; 

% Output: 
% M1 a)
c = u * B; 
% M1 b)
d = B * u'; 
% M1 c)
e = c * d;
% M1 d)
F = d * c;
% M1 e)
G = (c'*d')'; 

% % The following code is to show the result 
c, 
d, 
e, 
F, 
G
%% M2 
% lookfor function is used to find the inverse function for matrix
% inversion calcuation
% In Matlab 2017a, with command: lookfor 'inversion', the following result
% is returned on the prompt: 
%     cond                           - Condition number with respect to inversion.
%     ssinv                          - State-space inversion.
% with the help function: help cond, the function inv is found, and this
% function could be used for calculating the invesion of a square matrix 
A = [2, 4, -2; 4, 9, -3; -2, -3, 7]; 
y = [2, 8, 10]'; 
x = inv(A) * y;

% while calling function inv for the matrix inversion calculation, 
% warning message appears on the screen as follows, and another way to
% calculate inversion is suggested. I.e. : Replace inv(A)*b with A\b
% 
% Explanation 
% Code Analyzer has detected a call to inv in a multiplication operation.
% For solving a system of linear equations, the inverse of a matrix is primarily of theoretical value. Never use the inverse of a matrix to solve a linear system Ax=b with x=inv(A)*b, because it is slow and inaccurate.
%  Suggested Action 
% Instead of multiplying by the inverse, use matrix right division (/) or matrix left division (\). That is:
% Replace inv(A)*b with A\b
% Replace b*inv(A) with b/A
% In longer expressions, parentheses might be necessary to preserve the order of operations. For example, replace A*inv(B)*C with A*(B\C).
% Frequently, an application needs to solve a series of related linear systems Ax=b, where A does not change, but b does. In this case, use lu, chol, or qr instead of inv, depending on the matrix type.
% 

% here we test another way of calculating inversion of matrix
x2 = A \ y
% x and x2 have identical result

%% M3 
% a1 = 2, a2 = 4, a3 = -6 
 
coefficients = [2, 4, -6]; 
r = roots(coefficients); 

% according to a1, a2, a3 
% p = a2 / a1, q = a3 / a1, i.e.  p = 2,q = -3
p = 2; 
q = -3;
r1 = - p/2 - sqrt(p^2 / 4 - q); 
r2 = - p/2 + sqrt(p^2 / 4 - q); 

% % compare the result 
% r, 
% r1, 
% r2

%% M4
% M4 a)
e = 1; % initilize the e value with 1 (corresponding to n == 0)
i_minus_prod = 1; 
for i = 1: 5  
    e = e + 1/(i_minus_prod * i); 
    i_minus_prod = i_minus_prod * i; 
end

% M4 b)
eMat = exp(1); 
nRel = abs((e - eMat) / eMat) * 100; 

% M4 c)
e = 1;  
nRel = 1; 
Tol = 10e-6;
i_minus_prod = 1; 
i = 1; 
eMat = exp(1); 
while nRel > Tol    
    e = e + 1 / (i_minus_prod * i); 
   
    i_minus_prod = i_minus_prod * i;  
    i = i + 1; 
    nRel = abs((e - eMat) / eMat) * 100; 
end

% M4 d) 
e = 1; % initilize the e value with 1 (corresponding to n == 0)
i_minus_prod = 1; 
for i = 1: 5  
    e = e + 1/(i_minus_prod * i); 
    i_minus_prod = i_minus_prod * i; 
end

%% M5
% test cases, please refer to function nullst for the detailed explanation 

case1 = [1, 2, -3]; 
case2 = [0, 2, 4]; 
case3 = [1, 2, 1]; 
case4 = [1, 2, 8]; 

[x1_c1, x2_c1] = nullst(case1);
[x1_c2, x2_c2] = nullst(case2);
[x1_c3, x2_c3] = nullst(case3);
[x1_c4, x2_c4] = nullst(case4);


% % % the following part is kept in case the user want to test the result. 
% [x1_c1, x2_c1] = nullst(case1),
% [x1_c2, x2_c2] = nullst(case2),
% [x1_c3, x2_c3] = nullst(case3),
% [x1_c4, x2_c4] = nullst(case4),

%% M6
a = [4; 1; 0]; 
b = [-2; -2; 0]; 
c = vectorprod(a, b); 

% % % if the result is wanted to be shown on the prompt, 
% c = vectorprod(a, b), 

%% M7    

B = [11 2; 3 5]; 
u = [4; 6; 8]; 
v = [8; 12; 16]; 

A = u'; 
A(2:3,1:2) = B; 
A(:, 3) = v; 
% A = [4 6 8; 11 2 12; 3 4 16]; 

%% M8 

% M8 a) 
fx = @(x) x.^2 + 2 .* x - 3; 
df = @(x) 2 .* x + 2; 

x0 = 0; 
x1 = x0 - fx(x0) / df(x0); 
x2 = x1 - fx(x1) / df(x1); 
x3 = x2 - fx(x2) / df(x2); 


x0 = 0; 
NMAX = 20;
tic 
TOL  = 10e-9; 
x_test1 = newton (fx, df, x0, TOL, NMAX);
toc 

tic 
TOL  = 10e-3; 
x_test2 = newton (fx, df, x0, TOL, NMAX);
toc 

Intervals = x_test1 - 5 : 0.1: x_test1 + 5; 
plot(Intervals, fx(Intervals))

%% M9 
% this part will be skipped, the user could test the command directly


