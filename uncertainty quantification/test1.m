% 
% close all
% f = @ (x)  x.* sin(x)./(1 - cos(x)); 
% sinx = @ (x) sin(x); 
% one_consx = @ (x) 1- cos(x); 
% xsinx = @ (x) x.* sin(x); 
% 
% t = 2* pi -1;
% k = 100; 
% x = (pi /2 + 2 * k * pi : 0.01: 1.5 * pi + 2 * k * pi)'; 
% ysinx = sinx(x); 
% yxsinx = xsinx(x); 
% yone_consx = one_consx(x);
% 
% y = f(x); 
%  
% figure
%  plot (x, y,'b-', x, ysinx, 'r:', x, yxsinx,'k--', x, yone_consx, 'go', x, cos(x), 'c*'); 
% % plot (x, y,'b-')
% xL = xlim;
% yL = ylim;
% line([0 0], yL);  %x-axis
% line(xL, [0 0]);  %y-axis
%  legend('y', 'sinx', 'xsinx', 'one_consx', 'cosx','Location', 'southeast')
% 
% f(pi * 3 /2) 
% 
% 

a = 2 ; 
b = 1; 
x1 = zeros(100,1);

for i = 1: 100 
   a = a/ 10;    
   b = b /10; 
   
  x1(i) = ceil((1+ a)/(1+b)), 
end


% 